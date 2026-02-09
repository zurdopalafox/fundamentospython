1. Seleccionar el apellido, oficio, salario, numero de departamento 
y su nombre de todos los empleados cuyo salario sea mayor de 300000

select emp.apellido, emp.oficio, emp.salario, emp.DEPT_NO, dept.DNOMBRE 
from EMP
left join DEPT
on emp.dept_no = dept.dept_no;

2. Mostrar todos los nombres de Hospital con sus nombres de salas correspondientes.

select hospital.nombre, sala.nombre
from HOSPITAL 
left join SALA 
on hospital.hospital_cod = sala.hospital_cod;

3. Calcular cuántos trabajadores de la empresa hay en cada ciudad.

select dept.loc, count(emp.apellido) as TRABAJADORES 
from EMP
left join dept
on emp.dept_no = dept.dept_no
group by dept.loc;

4. Visualizar cuantas personas realizan cada oficio en cada departamento mostrando el nombre del departamento.
select dept.dnombre, emp.oficio, count(emp.apellido) as TRABAJADORES 
from EMP
left join dept
on emp.dept_no = dept.dept_no
group by  emp.oficio, dept.dnombre;

5. Contar cuantas salas hay en cada hospital, mostrando el nombre de las salas y el nombre del hospital.

select hospital.nombre, sala.nombre, count(sala.sala_cod) as NUMERODESALAS
from HOSPITAL
left join sala
on hospital.hospital_cod = sala.hospital_cod
group by hospital.nombre, sala.nombre;

6. Queremos saber cuántos trabajadores se dieron de alta entre el año 1997 y 1998 y en qué departamento.

select dept.dnombre, count(emp.apellido) as NUMERODETRABAJADORES
from EMP
left join DEPT
on EMP.DEPT_NO = dept.dept_no
where extract(year from EMP.fecha_alt) between '1997' and '1998'
group by dept.dnombre;

7. Buscar aquellas ciudades con cuatro o más personas trabajando.

select dept.loc, count(emp.apellido) as TRABAJADORES 
from EMP
left join dept
on emp.dept_no = dept.dept_no
group by dept.loc
having count(emp.apellido) >= 4;

8. Calcular la media salarial por ciudad.  Mostrar solamente la media para Madrid y Elche.

select dept.loc, avg(emp.salario)
from EMP
left join dept
on emp.dept_no = dept.dept_no
where dept.loc in ('MADRID','ELCHE')
group by dept.loc;

9. Mostrar los doctores junto con el nombre de hospital en el que ejercen, la dirección y el teléfono del mismo.

select doctor.apellido, hospital.nombre as NOMBRE_HOSPITAL, hospital.direccion as DIRECCION_HOSPITAL, hospital.telefono as TELEFONO_HOSPITAL
from doctor
left join hospital
on doctor.hospital_cod = hospital.hospital_cod;

10. Mostrar los nombres de los hospitales junto con el mejor salario de los empleados de la plantilla de cada hospital.

select hospital.nombre, max(plantilla.salario)
from HOSPITAL
left join plantilla
on hospital.hospital_cod = plantilla.hospital_cod
group by hospital.nombre;
select * from plantilla;

11. Visualizar el Apellido, función y turno de los empleados de la plantilla 
    junto con el nombre de la sala y el nombre del hospital con el teléfono.
select plantilla.apellido, plantilla.funcion, plantilla.turno, hospital.nombre as NOMBREHOSPITAL, sala.nombre as NOMBRESALA , hospital.direccion, hospital.telefono
from PLANTILLA
left join hospital
on plantilla.hospital_cod = hospital.hospital_cod
left join sala
on plantilla.hospital_cod = sala.hospital_cod
and plantilla.sala_cod = sala.sala_cod;

12. Visualizar el máximo salario, mínimo salario de los Directores dependiendo de la ciudad en la que trabajen. 
    Indicar el número total de directores por ciudad.

select dept.loc, emp.oficio = 'DIRECTOR', max(emp.salario), min(emp.salario), count(*)
from EMP
left join DEPT
on emp.dept_no = dept.dept_no
where upper(emp.oficio) = 'DIRECTOR'
group by emp.oficio, dept.loc;

13.	Averiguar la combinación de que salas podría haber por cada uno de los hospitales.

select hospital.nombre, sala.nombre, count(*) as NUMERO_DE_SALAS
from hospital
right join sala
on hospital.hospital_cod = sala.hospital_cod
group by hospital.nombre, sala.nombre
union all
select 'Total', NULL, count(*) as NUMERO_DE_SALAS
from hospital
right join sala
on hospital.hospital_cod = sala.hospital_cod;


select * from emp where oficio = 'DIRECTOR';
select * from sala;

-- XXXXXX AGREGO ESTA LINEA DESDE LAP ASUS EN CASA
-- XXXXXX AGREGO ESTA LINEA DESDE LAP ASUS EN CASA
