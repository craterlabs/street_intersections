create database intersections;

create table yvr_data (
    id bigserial primary key,
    coordinate1 float not null,
    coordinate2 float not null,
    intersection_name varchar(255) not null,
    latitude float,
    longitude float
);