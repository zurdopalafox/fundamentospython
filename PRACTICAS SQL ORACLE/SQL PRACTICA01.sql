select * from dept;
select * from enfermo;
select * from doctor;
select * from emp;
select * from hospital;
1. Mostrar todos los datos de los empleados de nuestra tabla emp.
select * from emp;
2. Mostrar el apellido, oficio, salario anual, con las dos extras para aquellos empleados con comisión mayor de 100000.
select apellido,oficio, salario * 14 as salario_anual from emp where comision > 100000;
3. Idem del anterior, pero para aquellos empleados que su salario anual con extras supere las 750.000 ptas.
select apellido,oficio, salario * 14 + comision as salarioanualycomision_total from emp where salario * 14 > 750000;
4. Idem del anterior, pero para aquellos empleados que sumen entre salario anual con extras y comisión el 1.000.000. 
select apellido,oficio, salario * 14 + comision as salarioanualycomision_total from emp where salario * 14 + comision > 1000000;
5. Mostrar todos los datos de empleados ordenados por departamento y dentro de este por oficio para tener una visión jerárquica.(order by)
select * from emp order by dept_no,oficio;
6. Mostrar todos los enfermos nacidos antes del 1/1/70.
select * from enfermo where fecha_nac < '1/1/1970';
7. Igual que el anterior, para los nacidos antes del 1/1/1970 ordenados por número de inscripción.
select * from enfermo where fecha_nac < '1/1/1970' order by inscripcion;
8. Listar todos los datos de la plantilla del hospital del turno de mañana
select * from plantilla where turno = 'M';
9. Idem del turno de noche.
select * from plantilla where turno = 'N';
10. Listar los doctores que su salario anual supere 3.000.000 ptas.
select * from emp;
select EMP_NO, APELLIDO, OFICIO, SALARIO, salario * 12 as SALARIOANUAL from emp where (salario * 12 > 3000000);
11. Visualizar los empleados de la plantilla del turno de mañana que tengan un salario entre 2.000.000 y 2.250.000.
select * from plantilla where turno = 'M' and ((salario * 14) between 2000000 and 2300000);
12. Visualizar los empleados de la tabla emp que no se dieron de alta entre el 01/01/80 y el 12/12/82.
select * from emp where fecha_alt between '01/01/80' and '12/12/95';
13. Mostrar los nombres de los departamentos situados en Madrid o en Barcelona.
select * from dept where LOC in ('MADRID','BARCELONA');
14. Mostrar todos los enfermos nacidos antes de 1970.
select * from enfermo where extract(year from fecha_nac) < 1970;
15. Igual que el anterior, para los nacidos antes de 1970 ordenados por número de inscripción descendente
select * from enfermo where extract(year from fecha_nac) < 1970 order by inscripcion desc;
16. Mostrar todos los datos de empleados ordenados por departamento y dentro de este por oficio para tener una visión jerárquica.
select * from emp order by dept_no asc, oficio desc;
