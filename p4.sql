delimiter $$
drop procedure if exists p4$$
create procedure p4()
begin
select * from prof join bmi on bmi.id=prof.pid and profession='Doctor';
end$$
delimiter ;
