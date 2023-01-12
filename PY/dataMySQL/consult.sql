show databases;
USE for_education;
CREATE TABLE products(
	id INT NOT NULL auto_increment,
    NAME varchar(50) not null,
    created_by int not null,
    marca varchar(50),
    primary key(id),
    foreign key(created_by) references collaborators(id)
);

rename table products to article; -- Cambiar el nombre de la tabla

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

select c.id,c.name, a.name from collaborators c left join article a on c.id = a.created_by;
select c.id, c.name, a.name from collaborators c right join article a on c.id = a.created_by;
select c.id, c.name, a.name from collaborators c inner join article a on c.id = a.created_by;
select c.id, c.name, a.id, a.name from collaborators c cross join article a;
select count(id_article), marca from article group by marca;
select count(a.id_article), c.name from article a left join collaborators c on c.id = a.created_by group by a.created_by;

mysqldump -u [root] -p [] for_education > for_education.sql;