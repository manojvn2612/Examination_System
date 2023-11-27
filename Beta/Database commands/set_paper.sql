use examination;
show tables;
desc question_paper;
-- insert into question_paper values(100,123,"Manoj",current_timestamp(),"2023-11-23","2023-12-24");
delimiter $$

delimiter ;
-- SHOW TRIGGERS LIKE 'q_create';
insert into question_paper values(101,123,"Manoj",current_timestamp(),"2023-11-23","2023-12-24");
select * from question_paper;