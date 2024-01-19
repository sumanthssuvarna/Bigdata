 -- Complex SQL Query 1 | Derive Points table for ICC tournament
 -- https://www.youtube.com/watch?v=qyAgWL066Vo&list=PLBTZqjSKn0IeKBQDjLmzisazhqQy4iGkb

 
 create table encouraging-key-348500.abc123.encouraging-key-348500.abc123.icc_world_cup
(
Team_1 string(20),
Team_2 string(20),
Winner string(20)
);
INSERT INTO encouraging-key-348500.abc123.icc_world_cup values('India','SL','India');
INSERT INTO encouraging-key-348500.abc123.icc_world_cup values('SL','Aus','Aus');
INSERT INTO encouraging-key-348500.abc123.icc_world_cup values('SA','Eng','Eng');
INSERT INTO encouraging-key-348500.abc123.icc_world_cup values('Eng','NZ','NZ');
INSERT INTO encouraging-key-348500.abc123.icc_world_cup values('Aus','India','India');

select 
team, 
count(1) as total_matches,
sum(result) as win ,
count(1) - sum(result) as loose

from
(
    select team_1 as team, (case when winner=team_1 then 1 else 0 end) as result from icc_world_cup
    union all 
    select team_2 as team, (case when winner=team_2 then 1 else 0 end) as result  from icc_world_cup
) A

group by team
order by total_matches desc