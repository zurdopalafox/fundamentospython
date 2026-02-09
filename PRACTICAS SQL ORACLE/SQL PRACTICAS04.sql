1. Mostrar el número de empleado, el apellido y la fecha de alta del empleado más antiguo de la empresa.
select emp_no, apellido, fecha_alt 
from EMP
where fecha_alt = (select max(fecha_alt) from emp);

2. Mostrar el número de empleado, el apellido y la fecha de alta del empleado más moderno de la empresa.
select emp_no, apellido, fecha_alt 
from EMP
where fecha_alt = (select min(fecha_alt) from emp);

3. Visualizar el apellido y el salario de los empleados con el mismo oficio que Jiménez.

select apellido, salario
from emp
where salario = (select salario from emp where apellido='jimenez');

4. Queremos saber el apellido, oficio, salario y número de departamento de los empleados
   con salario mayor que el mejor salario del departamento 30.

select apellido, oficio,salario, dept_no
from emp
where salario > (select max(salario) from emp where dept_no = 30);

5. Mostrar el apellido, la función u oficio, sala o departamento 
   de todos los empleados que trabajen en Empresa o Plantilla.
select apellido, oficio, dept_no 
from emp
union 
select apellido, funcion, sala_cod
from plantilla;

6. Mostrar apellidos y oficio de los empleados del departamento 20 
   cuyo trabajo sea el mismo que el de cualquier empleado de ventas.

select apellido, oficio
from emp
where dept_no = 20 and oficio in (select oficio from emp where DEPT_NO = (select dept_no from dept where dnombre = 'VENTAS'));


7. Mostrar los empleados que tienen mejor salario que la media de los directores, no incluyendo al presidente.

select *
from emp
where salario > (select avg(salario) from emp where oficio = 'DIRECTOR') and oficio <> 'PRESIDENTE';


8. Mostrar el apellido, función, salario y código de hospital de los empleados de la plantilla que siendo 
   enfermeros o enfermeras pertenecen al hospital SAN CARLOS.

select plantilla.apellido, plantilla.funcion, plantilla.salario, plantilla.hospital_cod, hospital.nombre as NOMBRE_HOSPITAL
from plantilla
right join hospital
on plantilla.hospital_cod = hospital.hospital_cod
where funcion in ('ENFERMERO', 'ENFERMERA') and (hospital.hospital_cod = (select hospital_cod from hospital where nombre = 'san carlos'));

9.	Averiguar el salario de TODAS las personas de la bbdd, 
   de forma que se aprecien las diferencias salariales entre ellos.

select APELLIDO, OFICIO, SALARIO as SUELDO from EMP
union
select APELLIDO, ESPECIALIDAD, SALARIO from DOCTOR
union
select APELLIDO, FUNCION, SALARIO from PLANTILLA
order by SUELDO desc;

10. Realizar la misma consulta anterior, 
    pero solamente mostraremos las personas que cuyo oficio termine en O.

select *
from (
select APELLIDO, OFICIO as CARGO, SALARIO as SUELDO, 'EMP' as TABLA_ORIGEN from EMP 
union
select APELLIDO, ESPECIALIDAD, SALARIO, 'DOCTOR' as TABLA_ORIGEN from DOCTOR
union
select APELLIDO, FUNCION, SALARIO,'PLANTILLA' as TABLA_ORIGEN from PLANTILLA
)
where upper(CARGO) like '%O'
order by SUELDO desc;

11.	Visualizar los datos de los hospitales que tienen personal (Doctores) de cardiología.

select distinct * 
from hospital
where hospital_cod in (select hospital_cod from doctor where upper(especialidad) = 'CARDIOLOGIA')
order by hospital.hospital_cod;  


12.	Visualizar el apellido y el salario anual de los empleados de la plantilla del Hospital Provincial y General.

select apellido, salario 
from plantilla
where hospital_cod = (select hospital_cod from hospital where upper(nombre) = ('PROVINCIAL'));

13	Necesitamos un informe para evaluar cómo van las cuentas generales de la empresa.  
Para ello, necesitamos saber lo que cobra cada persona por cada oficio de manera detallada.  
Necesitamos el máximo salario y el mínimo más la media salarial,
 el total de sueldos y el número de trabajadores que hay en cada puesto de toda la base de datos.

select CARGO, count(*) as TOTALEMPLEADOS, MAX(SALARIO) as MAXSALARIO,
MIN(SALARIO) as MINSALARIO, avg(SALARIO) as PROMSALARIO, sum(SALARIO) as SUMASALARIOS 
from (
   select OFICIO as CARGO, salario from EMP
   union all
   select FUNCION, SALARIO from plantilla
   )
group by CARGO;

select * from hospital;
select * from doctor;
select * from emp;
select * from plantilla order by hospital_cod;


-- XXXXXX AGREGO ESTA LINEA DESDE LAP ASUS EN CASA
-- XXXXXX AGREGO ESTA LINEA DESDE LAP ASUS EN CASA

xxxxxx
xxxxxx

