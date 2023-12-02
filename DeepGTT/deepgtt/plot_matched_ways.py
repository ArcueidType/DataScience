import h5py
import psycopg2
import geopandas as gpd
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

host = "localhost"
port = 5432
database = "harbin"
user = "osmuser"
password = "pass"

con = psycopg2.connect(
    host=host, port=port, database=database, user=user, password=password)
con.set_client_encoding("UTF8")

bfmap_ways = gpd.read_postgis("select gid, osm_id, source, target, reverse, priority, geom from bfmap_ways;", con)
ways = pd.read_sql_query("select id as osm_id, tags, nodes from ways;", con)
roads = bfmap_ways.merge(ways, on='osm_id')
bfm_plt = bfmap_ways.plot(figsize=(12, 8), color='navajowhite')
m = bfmap_ways.explore(color='navajowhite', style_kwds={'opacity': 0})
con.close()

road_color = [x[0] for x in list(colors.cnames.items())[20:]]
paths = []
with h5py.File('./data/trainpath/150104.h5', 'r') as file_ways:
    with h5py.File('./data/h5path/trips_150104.h5') as file_trips:
        i = 0
        for key in file_ways.keys():
            if i == 1:
                break
            for key2 in file_ways[key]['trip'].keys():
                paths.append(file_ways[key]['trip'][key2])
            i += 1

        i = 0
        lat = []
        lon = []
        for key in file_trips['trip'].keys():
            if i != 10:
                i += 1
                continue
            for x in range(file_trips['trip'][key]['lon'].shape[0]):
                lon.append(file_trips['trip'][key]['lon'][x])
                lat.append(file_trips['trip'][key]['lat'][x])
            i += 1
            gps_point = {'lon': lon, 'lat': lat}
            df_gps = pd.DataFrame(gps_point)
            gdf_gps = gpd.GeoDataFrame(df_gps, geometry=gpd.points_from_xy(df_gps.lon, df_gps.lat))
            # match_map = gdf_gps.explore(m=m)
            # gdf_gps.plot(axes=bfm_plt)
            print(gdf_gps)
            for key2 in file_trips['trip'][key]:
                print(file_trips['trip'][key][key2])

        count_path = 0
        for path in paths[200:201]:
            road = roads[roads.gid.isin(path)]
            print(road)
            # road.plot(axes=bfm_plt, color="red")
            match_map = road.explore(m=m) # color=road_color[count_path % len(road_color)]
            count_path += 1

        file_name = 'match_map.html'
        file_path = 'file:///Users/arcueid/DeepGTT/deepgtt/' + file_name
        match_map.save(file_name)
        webbrowser.open_new_tab(file_path)
        # plt.title('Ways After Matching')
        # plt.axis('off')
        # plt.show()

