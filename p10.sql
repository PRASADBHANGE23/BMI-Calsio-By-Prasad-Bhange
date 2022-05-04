delimiter $$
drop procedure if exists p10$$
create procedure p10()
begin
select * from prof join bmi on bmi.id=prof.pid and profession='INDIANarmy';
end$$
delimiter ;