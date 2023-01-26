/* Write your T-SQL query statement below */
Select player_id,  MIN(event_date) first_login 
from Activity 
group by
player_id;
