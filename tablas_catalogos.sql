/*
create schema estados;
create schema raw

truncate table raw_data.cat_origen;
truncate table raw_data.cat_sector;
truncate table raw_data.sexo;
truncate table raw_data.tipo_paciente;
truncate table raw_data.si_no;
truncate table raw_data.nacionalidad;
truncate table raw_data.resultado_lab;
truncate table raw_data.resultado_antigeno;
truncate table raw_data.clasificacion_final;
truncate table raw_data.casos_covid;

create table raw_data.cat_origen(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.cat_sector(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.sexo(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.tipo_paciente(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.si_no(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.nacionalidad(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.resultado_lab(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.resultado_antigeno(
	clave int unique,
	descripcion varchar(100)
)

create table raw_data.clasificacion_final(
	clave int unique,
	clasificacion varchar(70),
	descripcion varchar(490)
)

select * from raw_data.cat_origen;
select * from raw_data.cat_sector;
select * from raw_data.sexo;
select * from raw_data.tipo_paciente;
select * from raw_data.si_no;
select * from raw_data.nacionalidad;
select * from raw_data.resultado_lab;
select * from raw_data.resultado_antigeno;
select * from raw_data.clasificacion_final;


create table raw_data.casos_covid(
	fecha_actualizacion date, id_registro varchar(50) unique,
	origen int, sector int, entidad_um int,sexo int,
	entidad_nac int, entidad_res int, municipio_res int,
	tipo_paciente int, fecha_ingreso date, fecha_sintomas date,
	fecha_def varchar(50), intubado int, neumonia int, edad int,
	nacionalidad int, embarazo int, habla_lengua_indig int,
	indigena int, diabetes int, epoc int,asma int,inmusupr int,
	hipertension int,otra_com int,cardiovascular int,obesidad int,
	renal_cronica int,tabaquismo int,otro_caso int,
	toma_muestra_lab int,resultado_lab int,
	toma_muestra_antigeno int,resultado_antigeno int,
	clasificacion_final int,migrante int,
	pais_nacionalidad varchar(100),
	pais_origen varchar(210),uci int
)

*/

select count(*) from raw_data.casos_covid limit 10;
