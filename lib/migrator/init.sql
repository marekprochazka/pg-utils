create table migrations (
    id varchar(255) primary key,
    created_at timestamp default current_timestamp
);

insert into migrations (id) values ('init')
