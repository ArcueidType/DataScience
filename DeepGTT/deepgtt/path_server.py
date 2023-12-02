import os
import socket
import threading
import geopandas
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
con.close()

paths = []

def handle_request(port, client):
    while True:
        recv_data = client.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('ascii')
            path_id = int(recv_content)
            path = paths[path_id]
            road = roads[roads.gid.isin(path)]
            m = bfmap_ways.explore(color='navajowhite', style_kwds={'opacity': 0})
            match_map = road.explore(m=m, color='red')
            file_name = '../VisualServer/match_map.html'
            match_map.save(file_name)
            print('save complete')
            # file_path = 'file:///Users/arcueid/DeepGTT/VisualServer/match_map.html'
            # webbrowser.open_new_tab(file_path)
            send_content = 'got it'
            send_data = send_content.encode('ascii')
            client.send(send_data)
        else:
            break


if __name__ == '__main__':
    with h5py.File('./data/trainpath/150104.h5', 'r') as file_ways:
        i = 0
        for key in file_ways.keys():
            if i == 1:
                break
            for key2 in file_ways[key]['trip'].keys():
                paths.append(file_ways[key]['trip'][key2])
            i += 1

        with open('../paths_count.txt', 'w') as fp:
            fp.write(str(len(paths)))
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        
        server_socket.bind(('127.0.0.1', 10001))
        
        server_socket.listen(128)

        print('path server start')
        while True:
            client, port = server_socket.accept()
            sub_thread = threading.Thread(target=handle_request, args=(port, client), daemon=True)
            
            sub_thread.start()
        
    server_socket.close()
    