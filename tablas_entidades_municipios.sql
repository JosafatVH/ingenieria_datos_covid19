/*
truncate table estados.aguascalientes;
truncate table estados.baja_california;
truncate table estados.baja_california_sur;
truncate table estados.campeche;
truncate table estados.chiapas;
truncate table estados.chihuahua;
truncate table estados.ciudad_de_mexico;
truncate table estados.coahuila;
truncate table estados.colima;
truncate table estados.durango;
truncate table estados.eum;
truncate table estados.guanajuato;
truncate table estados.guerrero;
truncate table estados.hidalgo;
truncate table estados.jalisco;
truncate table estados.mexico;
truncate table estados.michoacan;
truncate table estados.morelos;
truncate table estados.nayarit;
truncate table estados.nuevo_leon;
truncate table estados.oaxaca;
truncate table estados.puebla;
truncate table estados.queretaro;
truncate table estados.quintana_roo;
truncate table estados.san_luis_potosi;
truncate table estados.sinaloa;
truncate table estados.sonora;
truncate table estados.tabasco;
truncate table estados.tamaulipas;
truncate table estados.tlaxcala;
truncate table estados.veracruz;
truncate table estados.yucatan;
truncate table estados.zacatecas;
truncate table estados.entidades;

-- creamos las tablas en el estado.
create table estados.aguascalientes(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.baja_california(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.baja_california_sur(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.campeche(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.coahuila(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.colima(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.chiapas(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.chihuahua(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.ciudad_de_mexico(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.durango(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.guanajuato(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.guerrero(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.hidalgo(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.jalisco(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.mexico(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.michoacan(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.morelos(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.nayarit(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.nuevo_leon(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.oaxaca(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.puebla(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.queretaro(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.quintana_roo(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.san_luis_potosi(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.sinaloa(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.sonora(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.tabasco(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.tamaulipas(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.tlaxcala(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.veracruz(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.yucatan(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.zacatecas(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.eum(
	clave_municipio int unique,
	municipio varchar(100),
	clave_entidad varchar(100)
)

create table estados.entidades(
	clave_entidad int unique,
	entidad_federativa varchar(100),
	abreviatura varchar(100)
)

*/

-- creamos las tablas en el estado.
select * from estados.aguascalientes;
select * from estados.baja_california;
select * from estados.baja_california_sur;
select * from estados.campeche;
select * from estados.chiapas;
select * from estados.chihuahua;
select * from estados.ciudad_de_mexico;
select * from estados.coahuila;
select * from estados.colima;
select * from estados.durango;
select * from estados.eum;
select * from estados.guanajuato;
select * from estados.guerrero;
select * from estados.hidalgo;
select * from estados.jalisco;
select * from estados.mexico;
select * from estados.michoacan;
select * from estados.morelos;
select * from estados.nayarit;
select * from estados.nuevo_leon;
select * from estados.oaxaca;
select * from estados.puebla;
select * from estados.queretaro;
select * from estados.quintana_roo;
select * from estados.san_luis_potosi;
select * from estados.sinaloa;
select * from estados.sonora;
select * from estados.tabasco;
select * from estados.tamaulipas;
select * from estados.tlaxcala;
select * from estados.veracruz;
select * from estados.yucatan;
select * from estados.zacatecas;
select * from estados.entidades;



