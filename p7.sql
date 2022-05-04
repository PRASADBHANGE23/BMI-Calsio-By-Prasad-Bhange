delimiter $$
drop procedure if exists p7$$
create procedure p7()
begin
select * from prof join bmi on bmi.id=prof.pid and profession='Teacher';
end$$
delimiter ;