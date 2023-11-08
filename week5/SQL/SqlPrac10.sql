SELECT SUM(score) as 'TotalScore' FROM score WHERE
teamid =
(SELECT id FROM team WHERE teamName = 'ECNU')