USE mydatabase;

create table users (
    id int auto_increment primary key,
    city varchar(255) not null,
    temperature float not null
);