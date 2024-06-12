create database myDB;
create table Manager(
	idManager int
    ,passwordManager varchar(50)
    ,nameManager varchar(50)
);
alter table manager modify column idManager char(4);
create table staff(
	idStaff char (4)
    ,nameStaff varchar (50)
    ,passwordStaff varchar (50)
    ,addressStaff varchar (100)
    ,starDate date
    ,workDay int
);
create table tableB (
	dateTable date
    ,nameTable varchar(10)
    ,checkIn time
    ,checkOut time
    ,incomeDay float
    ,idStaff varchar(5)
);
alter table tableb alter DateTable set default CURRENT_DATE();
drop table tableb;
alter table tableb alter checkIn set default CURRENT_TIMESTAMP;

select * from Manager;
insert into manager values ("QL01","1234","Phạm Minh Niên");
select * from staff;
insert into staff value ("NV01","Nguyễn Văn Đại","1234","199 Lê Quang Định phường 7 quận Bình Thạnh","2023-08-28", 25);
select * from tableb;
insert into tableb values ("Ban01","10:0:0","12:0:0",1000000,15000000);
set AUTOCOMMIT = off;
commit;
delete from manager;
/*
update tablename 
set columnupdate 
where primarykey 
delete from table 
where primarykey
func CURRENT_DATE CURRENT_TIME
*/
ALTER TABLE manager
ADD CONSTRAINT
unique (idManager);
alter table staff
add constraint unique (idStaff);
alter table manager
modify passwordManager varchar(50)  not null;
alter table staff
modify passwordStaff varchar(50) not null;
alter table staff drop constraint ck_workday;
alter table staff add constraint ck_workday check (workDay >0 );
select * from tableb;
insert into tableb (nameTable,checkIn,checkOut,IncomeDay) values('nameTable','10:0:0','12:0:0',100000);


alter table manager add constraint primary key(idManager);
alter table staff add constraint primary key (idstaff);
alter table staff add idManager char(4);
alter table staff 
add constraint fk_manager
foreign key (idManager) references manager(idManager);
alter table staff drop foreign key fk_manager;
alter table staff drop column idManager;
alter table tableb add idStaff char(4);

add constraint fk_staff
foreign key (idStaff) references staff(idStaff);
alter table tableb drop primary key;
drop table tableb;
alter table tableb  add constraint primary key (CheckIn);

CREATE TABLE customer (
  `phone` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `dob` DATE NULL,
  PRIMARY KEY (`phone`)
  );
alter table customer
modify column phone varchar(11);
select * from customer;
delete from  customer where phone = '123456789';
insert into customer (phone,name,dob) values( '012345671E','Nguyen Van G',"1987/09/27");
select * from customer;
delete from  customer where phone = '01234567167';
insert into customer (phone,name,dob) values( '01234567167','Nguyen Tran Thao',date_format(str_to_date('30-07-2000','%d-%m-%Y'),'%Y-%m-%d'));
update customer
set name = 'Nguyen Thi Be' 
where phone like '0123456713';

delete from customer where phone='0123456712';
update customer
                set name = 'Tran Van C' 
                where phone like '0123456714';
select phone from customer where phone ='0111111110';
alter table staff drop column starDate;
select * from staff;
alter table staff add column Luong float;
update staff
set Luong = ( select workDay from staff where idStaff ='NV01')* 200000
where idStaff = 'NV01';
drop table tableb;
select * from tableb;
delete from tableb where nameTable = 'Ban09';
insert into tableb (nameTable,idstaff,checkIn) values ('Ban03','NV03',now());
alter table tableb alter column incomeDay set default 0;
update tableb set checkOut= now() where dateTable = current_date() and nameTable ='Ban03'; 
update tableb set checkIn= 0 where dateTable = current_date() and nameTable ='Ban03'; 
update tableb set checkOut= 0 where dateTable = current_date() and nameTable ='Ban03'; 
select checkOut from tableb where nameTable = 'ban03' and idStaff ='nv03' and checkIn ='16:21:54';
alter table tableb modify checkIn time=0;

update tableb set incomeDay = 1000 where nameTable ='Ban03';
delete from tableb where nameTable ='ban05';
select incomeDay from tableb where nameTable ='Ban03' and dateTable =current_date();
update tableb set  checkOut = now() where nameTable='ban03' and idstaff = 'nv04' and checkIn = (select max(checkIn) from tableb where  idStaff='nv04'and nameTable='ban03');
select checkOut from tableb wher nameTable ='ban05' and idstaff='nv01' and checkIn = (select max(checkIn) from tableb where nameTable like 'ban05' and idStaff like'nv01');
select round(sum(incomeDay),2) from tableb where month(dateTable) = month(curdate()) ;
select dateTable, round(sum(incomeDay),2)
                    from tableb
                    group by dateTable;
select * from staff;
select round(sum(Luong),1) from staff;

                            