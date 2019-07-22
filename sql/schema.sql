-- SPO SNEAK PEEK OSINT
-- Author: Victor de Queiroz

-- create a user for SPO
create user 'japonesdafederal'@'localhost' identified by 'aytegs&7s7gj';

-- set permissions
grant ALL privileges on * . * to 'japonesdafederal'@'localhost';

-- create a tablespace
create database SPO;

-- select spo database
use SPO;

-- create tables
-- table for user on SPO
CREATE TABLE user_spo(
id_user integer not null AUTO_INCREMENT,
login varchar(100) not null,
password varchar(300) not null,
constraint user_pk primary key(id_user)
);
-- table for api keys or passwords and users for social media
CREATE TABLE key_api(
id_key integer not null AUTO_INCREMENT,
id_user integer not null,
user_key varchar(300),
key_value varchar(600) not null,
name_key varchar(100),
constraint key_pk primary key(id_key),
constraint key_fk foreign key(id_user)
references user_spo (id_user)

);
-- table for new projects
CREATE TABLE project(
id_project integer not null AUTO_INCREMENT,
id_user integer not null,
name_project varchar(100) not null,
scope_project varchar(600) not null,
constraint project_pk primary key(id_project),
constraint project_fk foreign key(id_user)
references user_spo (id_user)
);
-- table for personal stalking
CREATE TABLE personal_trace(
id_person integer not null AUTO_INCREMENT,
id_project integer not null,
name_person varchar(100),
date_of_birth date,
email varchar(100),
telephone varchar(100),
CPF varchar(100),
renavam varchar(100),
RG varchar(1000),
address varchar(1000),
facebook varchar(1000),
instagram varchar(1000),
twitter varchar(1000),
domain varchar(100),
business blob(10000),
vehicle blob(10000),
vehicle_plate blob(100),
proceedings blob(60000),
constraint personal_trace_pk primary key(id_person),
constraint personal_trace_fk foreign key(id_project)
references project (id_project)
);
-- table for photo references, in the dir
-- insert the local of picture example "/home/japonesdafederal/lula/pictures/lulaAndAtibaiaSitio.png"
CREATE TABLE photo(
id_photo integer not null AUTO_INCREMENT,
id_project integer not null,
dir_photo varchar(100) not null,
constraint photo_pk primary key(id_photo),
constraint photo_fk foreign key(id_project)
references project (id_project)
);
-- table for servers data as service banner
-- or ip address
CREATE TABLE servers(
id_server integer not null AUTO_INCREMENT,
id_project integer not null,
address varchar(100),
ports_open varchar(1000),
ports_filtred varchar(1000),
describe varchar(1000),
ip_address varchar(100),
constraint servers_pk primary key(id_server),
constraint servers_fk foreign key(id_project)
references project (id_project)
);
-- table for domain information as owner name for example
CREATE TABLE domain(
id_domain integer primary key AUTO_INCREMENT,
id_project integer not null,
owner_name varchar(100),
owner_document varchar(100),
owner_email varchar(100),
domain varchar(100),
data_creation date,
data_expiration date,
host_address varchar(100),
constraint domain_pk primary key(id_domain),
constraint domain_fk foreign key(id_project)
references project (id_project)
);
-- table for service for example "Apache"
CREATE TABLE service(
id_service integer not null AUTO_INCREMENT,
id_project integer not null,
type_service varchar(100),
describe_service blob(10000),
banner_service varchar(1000),
version_service varchar(100),
constraint service_pk primary key(id_service),
constraint service_fk foreign key(id_project)
references project (id_project)

);
-- tables for others informations
CREATE TABLE other_information(
id_other integer not null AUTO_INCREMENT,
id_project integer not null,
other_information blob(100000),
constraint other_pk primary key(id_other),
constraint other_fk foreign key(id_project)
references project (id_project)
);

