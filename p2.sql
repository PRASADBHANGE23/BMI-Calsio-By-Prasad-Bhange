delimiter $$
drop procedure if exists p2$$
create procedure p2()
begin
select 'id','name','age','phone','gender','height','weight' 
union 
select * into OUTFILE "D:\\project related\\MySQL project\\data4.csv" 
fields terminated by "," 
from bmi;
end$$
delimiter ;
