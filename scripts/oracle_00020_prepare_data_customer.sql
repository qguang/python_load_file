delete from customer;

insert into customer ( customer_id, first_name, last_name, gender, dob ) values('C000001', 'Marty',   'McFly',    'M',  date '1970-01-01' );
insert into customer ( customer_id, first_name, last_name, gender, dob ) values('C000002', 'Aurora',  'Lane',     'F',  date '1970-01-02' );
insert into customer ( customer_id, first_name, last_name, gender, dob ) values('C000003', 'Rita',    'Vrataski', 'F',  date '1970-01-03' );
insert into customer ( customer_id, first_name, last_name, gender, dob ) values('C000004', 'William', 'Cage',     'M',  date '1970-01-04' );
insert into customer ( customer_id, first_name, last_name, gender, dob ) values('C000005', 'Stanley', 'Ipkiss',   'M',  date '1970-01-05' );
insert into customer ( customer_id, first_name, last_name, gender, dob ) values('C000006', 'Tina',    'Carlyle',  'F',  date '1970-01-06' );

insert into customer ( customer_id, first_name, last_name, gender, dob )
with level_vw as (
    select level l
    from dual
    connect by level < 1001
)
select 'C'||lpad(l, 6, '0')  as customer_id, 
       'First '||lpad(l, 6, '0') as first_name, 
       'Last '||lpad(l, 6, '0') as last_name, 
       case when mod(l, 2) = 0 then 'F' else 'M' end as gender,
       date '1970-01-01' + l as dob
from  level_vw
where l > 6;





cd $GIT_REPO/python_load_file/data_load/incoming/

sql ocean_studio_iii/oracle@//127.0.0.1:1521/ORCL
SET sqlformat csv
set feedback off
set linesize 1000
set pagesize 50000
-- remove extra space at each line due to large line size
set trimout on    
set trimspool on  
set termout off
set tab off
set echo off
set verify off
alter session set NLS_DATE_FORMAT='YYYY-MM-DD HH24:mi:ss';
alter session set NLS_TIMESTAMP_FORMAT='YYYY-MM-DD HH24:mi:ss.ff6';
spool customer.csv replace;
select * from customer order by customer_id;
spool off


--select * from customer;

--insert into customer ( customer_id, first_name, last_name, gender, dob ) values();
