delimiter $$
drop procedure if exists p5$$
create procedure p5()
begin
select * from prof join bmi on bmi.id=prof.pid and profession='Engineer';
end$$
delimiter ;