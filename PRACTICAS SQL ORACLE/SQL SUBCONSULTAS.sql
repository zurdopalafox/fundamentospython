--Necesito ver los datos el empleado que más cobra en la empresa.
--1) Necesitamos el máximo salario de la tabla empleados
select max(SALARIO) from EMP;
--650000
--2) Realizamos la consulta para mostrar los datos del 
--empleado que más cobra en la empresa.
select * from EMP where SALARIO=
(select max(SALARIO) from EMP);
select * from EMP;
--alonso y sala
--Mostrar todos los empleados que tengan el mismo oficio que 
--ALONSO
select OFICIO from EMP where APELLIDO='alonso';
select * from EMP where OFICIO=
(select OFICIO from EMP where APELLIDO='alonso');
--Mostrar todos los empleados que tengan el mismo oficio que 
--ALONSO y que cobren más que SALA
select OFICIO from EMP where APELLIDO='alonso'; --EMPLEADO
select SALARIO from EMP where APELLIDO='sala'; --162500
select * from EMP where OFICIO=
(select OFICIO from EMP where APELLIDO='alonso') 
and SALARIO > (select SALARIO from EMP where APELLIDO='sala');
--Mostrar los empleados que tengan 
--el mismo oficio que JIMENEZ y ALONSO
select OFICIO from EMP where APELLIDO='jimenez' 
or APELLIDO='alonso';
select * from EMP where OFICIO in 
(select OFICIO from EMP where APELLIDO='jimenez' 
or APELLIDO='alonso');

--el promedio de los 4 sueldos superiores ignorando al presi
--avg(SALARIO)
--OFICIO <> 'PRESIDENTE'
--SALARIO > ??
--LOS 4 SALARIOS

--MEDIA SALARIAL DE LOS EMPLEADOS SIN EL PRESIDENTE
select avg(SALARIO) as MEDIASALARIAL from EMP
where OFICIO <> 'PRESIDENTE';
select * from EMP where OFICIO <> 'PRESIDENTE' 
order by SALARIO desc;
--los 4 primeros salarios 
select APELLIDO, SALARIO from EMP 
where OFICIO <> 'PRESIDENTE'
order by SALARIO DESC;
select * from EMP where rownum <= 4;
--CONSULTAS UNION: EMP, DOCTOR, PLANTILLA
select APELLIDO, OFICIO, SALARIO as SUELDO from EMP
where SALARIO > 250000
union
select APELLIDO, ESPECIALIDAD, SALARIO from DOCTOR
where SALARIO > 250000
union
select APELLIDO, FUNCION, SALARIO from PLANTILLA
where SALARIO > 250000;

select APELLIDO, OFICIO, SALARIO from EMP
union all
select APELLIDO, OFICIO, SALARIO from EMP;
--order by
select APELLIDO, OFICIO, SALARIO as SUELDO from EMP
union
select APELLIDO, ESPECIALIDAD, SALARIO from DOCTOR
union
select APELLIDO, FUNCION, SALARIO from PLANTILLA
order by SUELDO;
--SELECT TO SELECT
--QUEREMOS FILTRAR SOBRE EL SUELDO DE TODA LA CONSULTA
select * from 
(select APELLIDO, OFICIO, SALARIO as SUELDO from EMP
union
select APELLIDO, ESPECIALIDAD, SALARIO from DOCTOR
union
select APELLIDO, FUNCION, SALARIO from PLANTILLA) consulta
where consulta.SUELDO >= 250000;
--CAMPOS CALCULADOS
--Mostrar el Apellido, Oficio, Salario Anual de los empleados 
--cuyo salario anual sea mayor a 1500000
select * from
(select APELLIDO, OFICIO, (SALARIO * 12) as SALARIOANUAL
from EMP) miconsulta
where miconsulta.SALARIOANUAL >= 1500000;

select * from
(select APELLIDO, SALARIO from EMP 
where OFICIO <> 'PRESIDENTE'
order by SALARIO DESC) query
where ROWNUM <= 4;
--Tenemos el turno en plantilla
select APELLIDO, FUNCION, 
case TURNO 
    when 'T' then 'Tarde'
    when 'M' then 'Mañana'
    else 'Noche'
end as TURNOBONITO, TURNO
from PLANTILLA;

select APELLIDO, FUNCION, 
case  
    when SALARIO > 250000 then 'Mucho'
    when SALARIO < 150000 then 'Poquito'
    else 'Normal'
end as TURNOBONITO, TURNO
from PLANTILLA;