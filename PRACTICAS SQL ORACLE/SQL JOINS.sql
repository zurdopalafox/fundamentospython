select doctor.apellido, doctor.especialidad, hospital.nombre as NOMBRE_HOSPITAL, hospital.direccion as DIRECCION_HOSPITAL
from doctor
inner join hospital 
on doctor.hospital_cod = hospital.hospital_cod;

INSERT INTO "SYSTEM"."EMP" 
(EMP_NO, APELLIDO, OFICIO, DIR, FECHA_ALT, SALARIO, COMISION, DEPT_NO) 
VALUES (1111, 'SOLEDAD', 'AVIADOR', 7839, TO_DATE('2026-02-05 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), 100000, 30000, 50);

# EJEMPLO INNER JOIN
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from EMP
inner join DEPT
on EMP.DEPT_NO = dept.DEPT_NO;

# Muestra todos los empleados, incluyendo aquellos que su departamento no existe en la tabla de Departamentos
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from EMP
left join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;

# Muestra todos los registros que tienene departamento y el departamento que no (GRANADA) 
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from EMP
right join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;

# Muestra todos los registros de ambas tablas coincidan o no
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from EMP
full join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;

# Muestra el Producto cartesiano de las dos tablas 
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from EMP
cross join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;

select hospital.nombre as NOMBREHOSPITAL, sum(plantilla.salario) as TOTALSALARIOS 
from plantilla
left join hospital
on plantilla.hospital_cod = hospital.hospital_cod
group by hospital.nombre; 

select emp.DEPT_NO, DEPT.LOC, count(emp.apellido) as NOEMPLEADOS
from DEPT
full join EMP
on DEPT.DEPT_NO = EMP.DEPT_NO
group by emp.dept_no, DEPT.LOC;
# Seleccionar apellido, funcion, nombre, dirección del hospital y nombre de la sala de toda la plantilla
select plantilla.apellido, plantilla.funcion, hospital.nombre, hospital.direccion, sala.nombre
from PLANTILLA
left join hospital
on plantilla.hospital_cod = hospital.hospital_cod
left join sala
on plantilla.hospital_cod = sala.hospital_cod
and plantilla.sala_cod = sala.sala_cod;

select * from plantilla;