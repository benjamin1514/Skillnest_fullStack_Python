/*drop database sistema_gimnasio;*/
create database sistema_gimnasio;
use sistema_gimnasio;

create table tipo_usuarios (
id_tipo_usuario int primary key unique not null auto_increment,
nombre_tipo_usuario varchar(100) not null,
descripcion_tipo_usuario varchar(100) not null,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0
);

create table tipo_plan_entrenamientos (
id_tipo_plan_entrenamiento int primary key unique not null auto_increment,
nombre_tipo_plan varchar(100) not null,
decripcion_tipo_plan varchar(150) not null,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0
);

create table clientes (
id_cliente int primary key unique not null auto_increment,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0
);

create table entrenadores (
id_entrenador int primary key unique not null auto_increment,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0
);

create table personas (
id_persona int primary key unique not null auto_increment,
nombre varchar(20) not null,
apellido varchar(20) not null,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0,
id_cliente INT,
foreign key (id_cliente)
references clientes (id_cliente),
id_entrenador INT,
foreign key (id_entrenador)
references entrenadores (id_entrenador)
);

create table usuarios (
id_usuario int primary key unique not null auto_increment,
username varchar(100) not null unique,
email varchar(150) not null unique,
telefono varchar(15) not null unique,
password_hash varchar(50) not null,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0,
id_persona INT,
foreign key (id_persona)
references personas (id_persona),
id_tipo_usuario INT,
foreign key (id_tipo_usuario)
references tipo_usuarios (id_tipo_usuario)
);



create table plan_entrenamientos (
id_plan_entrenamiento int primary key unique not null auto_increment,
duracion_semana date not null,
created_at datetime default current_timestamp,
update_at  datetime default current_timestamp on update current_timestamp,
created_by int null,
deleted tinyint(1) default 0,
id_tipo_plan_entrenamiento INT,
FOREIGN KEY (id_tipo_plan_entrenamiento) 
REFERENCES tipo_plan_entrenamientos (id_tipo_plan_entrenamiento),
id_entrenador INT,
FOREIGN KEY (id_entrenador) 
REFERENCES entrenadores (id_entrenador),
id_cliente INT,                         
FOREIGN KEY (id_cliente) 
REFERENCES clientes (id_cliente)
);
