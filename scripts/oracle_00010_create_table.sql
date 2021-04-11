drop table account_holder purge;
drop table transaction purge;
drop table account purge;
drop table customer_address purge;
drop table customer purge;

create table customer
(
    customer_id varchar2(20) not null,
    first_name  varchar2(100) not null,
    last_name   varchar2(100) not null,
    gender      varchar2(5)   not null,
    dob         date not null,
    constraint customer_pk primary key (customer_id)
);


create table customer_address
(
    customer_id varchar2(20) not null,
    address_type varchar2(10) not null,
    address varchar2(100) not null,
    constraint customer_address_pk primary key (customer_id, address_type),
    constraint customer_address_fk1 foreign key (customer_id) references customer(customer_id)
);


create table account
(
    account_number varchar2(20) not null,
    account_type varchar2(20) not null,
    closing_balance number(25,2),
    constraint account_pk primary key (account_number)
);

create table account_holder
(
    customer_id varchar2(20) not null,
    account_number varchar2(20) not null,
    account_role varchar2(50) not null,
    constraint account_holder_pk primary key (customer_id, account_number, account_role),
    constraint account_holder_fk1 foreign key (customer_id) references customer(customer_id),
    constraint account_holder_fk2 foreign key (account_number) references account(account_number)
);

create table transaction
(
    account_number varchar2(20) not null,
    transaction_datetime timestamp not null,
    amount number(25,2),
    transaction_desc varchar2(100),
    constraint transaction_pk primary key (account_number, transaction_datetime),
    constraint transaction_fk1 foreign key (account_number) references account(account_number)
);



