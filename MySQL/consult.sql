show databases;
USE employees;
show tables;
select * from article;
CREATE TABLE products(
	id INT NOT NULL auto_increment,
    NAME varchar(50) not null,
    created_by int not null,
    marca varchar(50),
    primary key(id),
    foreign key(created_by) references employees_2023(id)
);

alter table article change NAME name varchar(255);
alter table article change id id_article int;

insert into article(NAME, created_by, marca)
values
	("laptop", 6, "Asus"),
    ("laptop", 6, "Dell"),
    ("Tablet", 2, "Microsoft"),
    ("Smart TV", 4, "Tecnomaster"),
    ("laptop", 6, "HP"),
    ("laptop", 6, "HP"),
    ("SmartPhone", 5, "Apple"),
    ("SmartWatch", 4, "Samsung"),
    ("Macbook", 1, "Apple");



select article.name, employees_2023.name from employees_2023 left join article on employees_2023.id = article.created_by;
select c.id, c.name, a.name from collaborators c right join article a on c.id = a.created_by;
select c.id, c.name, a.name from collaborators c inner join article a on c.id = a.created_by;
select c.id, c.name, a.id, a.name from collaborators c cross join article a;
select count(id_article), marca from article group by marca;
select count(a.id_article), c.name from article a left join collaborators c on c.id = a.created_by group by a.created_by;

select id, after_name from employees_2023
where id in(
	select art.created_by from article art
);

select created_by, count(*) as count from article group by created_by HAVING COUNT(*) > 1; --

