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
where dept_no = 20 and oficio in (select oficio from emp where DEPT_NO = 30);

7. Mostrar los empleados que tienen mejor salario que la media de los directores, no incluyendo al presidente.

select *
from emp
where salario > (select avg(salario) from emp where oficio = 'DIRECTOR') and oficio <> 'PRESIDENTE';


8. Mostrar el apellido, función, salario y código de hospital de los empleados de la plantilla que siendo 
   enfermeros o enfermeras pertenecen al hospital SAN CARLOS.

select apellido, funcion, salario, hospital_cod
form plantilla 
where funcion in ('ENFERMERO', 'ENFERMERA') and hospital_cod = 19;

select * from plantilla;


-- YYYYYYY modificacion desde el CRN
-- YYYYYYY modificacion desde el CRN
