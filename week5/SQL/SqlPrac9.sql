SELECT `name` FROM `user` WHERE

user.id IN
(SELECT userid FROM score WHERE
teamid = (SELECT id from team WHERE teamName = 'ECNU')
)
AND age < 20
