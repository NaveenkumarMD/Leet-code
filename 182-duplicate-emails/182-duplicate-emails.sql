# Write your MySQL query statement below
select Email from (select Email,count(email) as countx from Person group by Email)as stat where countx>1