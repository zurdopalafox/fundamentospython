1) Insertar un nuevo empleado de la plantilla, Mr. Cabrales, sala4,  
   turno N y trabajara en el hospital 'El carmen' y el ID será el maximo disponible.

insert into PLANTILLA (EMPLEADO_NO, APELLIDO, SALA_COD, TURNO, HOSPITAL_COD)
values ((select max(EMPLEADO_NO) + 1 from PLANTILLA),'Mr. CABRALES','4','N',
(select hospital_cod from hospital where upper(nombre) = 'EL CARMEN'));

-- INSERTAMOS UNOS REGISTROS CON UN CODIGO HOSPITAL 55 QUE NO EXISTE
insert into PLANTILLA (EMPLEADO_NO, APELLIDO, SALA_COD, TURNO, HOSPITAL_COD)
values ((select max(EMPLEADO_NO) + 1 from PLANTILLA),'Mr. CABRALES','4','N',
55);


2) Eliminar de la plantilla a las personas que no tienen un hospital asignado.

delete from PLANTILLA where hospital_cod is null or ((hospital_cod not in (select hospital_cod from hospital)));

rollback;
select * from plantilla;
select * from hospital;


1. Dar de alta con fecha actual al empleado José Escriche Barrera como programador perteneciente al departamento de producción.  
   Tendrá un salario base de 70000 pts/mes y no cobrará comisión. 

insert into emp (EMP_NO, APELLIDO, OFICIO, DEPT_NO,SALARIO, fecha_alt)
values ((select max(emp_NO)+1 from emp),'JOSE ESCRICHE','PROGRAMADOR', (select DEPT_NO from dept where upper(dnombre) = 'PRODUCCIÓN'), 70000, TO_CHAR(SYSDATE, 'DD/MM/YY'));

rollback;
select * from emp;
select * from dept;


2. Se quiere dar de alta un departamento de informática situado en Fuenlabrada (Madrid).

insert into dept (DEPT_NO, DNOMBRE, LOC)
values(50,'FUENLABRADA','MADRID');

rollback;
select * from emp;
select * from dept;


3. El departamento de ventas, por motivos peseteros, se traslada a Teruel, realizar dicha modificación.

UPDATE DEPT 
SET LOC = 'TERUEL' 
where DNOMBRE='VENTAS';

rollback;
select * from emp;
select * from dept;

4. En el departamento anterior (ventas), se dan de alta dos empleados: Julián Romeral y Luis Alonso.  
   Su salario base es el menor que cobre un empleado, y cobrarán una comisión del 15% de dicho salario.

insert into emp (EMP_NO, APELLIDO, OFICIO, DEPT_NO,SALARIO, COMISION, fecha_alt)
values ((select max(emp_NO)+1 from emp),'Julian Romeral','VENDEDOR', (select DEPT_NO from dept where upper(dnombre) = 'VENTAS'), 
         (select min(SALARIO) from emp), 15, TO_CHAR(SYSDATE, 'DD/MM/YY'));

insert into emp (EMP_NO, APELLIDO, OFICIO, DEPT_NO,SALARIO, COMISION, fecha_alt)
values ((select max(emp_NO)+1 from emp),'Luis Alonso','VENDEDOR', (select DEPT_NO from dept where upper(dnombre) = 'VENTAS'), 
         (select min(SALARIO) from emp), 15, TO_CHAR(SYSDATE, 'DD/MM/YY'));
         commit;

rollback;
select * from emp;
select * from dept;

5. Modificar la comisión de los empleados de la empresa, de forma que todos tengan un incremento del 10% del salario.

update emp set COMISION = COMISION + (salario * .1);
rollback;
select * from emp;
select * from dept;


6. Incrementar un 5% el salario de los interinos de la plantilla que trabajen en el turno de noche.

update plantilla 
set salario = (salario * 1.05) 
where upper(funcion) = 'INTERINO' and TURNO='N';

select * from plantilla;


7. Incrementar en 5000 Pts. el salario de los empleados del departamento de ventas y del presidente, 
   tomando en cuenta los que se dieron de alta antes que el presidente de la empresa.

update emp 
set salario = (salario + 5000)
where (dept_no = ((select DEPT_NO from dept where upper(dnombre) = 'VENTAS') or OFICIO ='PRESIDENTE') and (fecha_alt < (select FECHA_ALT from emp where OFICIO='PRESIDENTE')));
rollback;
select * from emp;

8. El empleado Sancha ha pasado por la derecha a un compañero.  
   Debe cobrar de comisión 12.000 ptas más que el empleado Arroyo y su sueldo se ha incrementado un 10% respecto a su compañero.
update emp
set comision = (select comision from emp where upper(apellido)='ARROYO') + 12000, salario = (select salario from emp where upper(apellido)='ARROYO') * 1.1
where upper(apellido) ='SANCHEZ';

select * from emp;


Se tienen que desplazar cien camas del Hospital SAN CARLOS para un Hospital de Venezuela.  Actualizar el número de camas del Hospital SAN CARLOS.

Subir el salario y la comisión en 100000 pesetas y veinticinco mil pesetas respectivamente a los empleados que se dieron de alta en este año.

Ha llegado un nuevo doctor a la Paz.  Su apellido es House y su especialidad es Diagnostico.   Introducir el siguiente número de doctor disponible.

Borrar todos los empleados dados de alta entre las fechas 01/01/80 y 31/12/82.

Modificar el salario de los empleados trabajen en la paz y estén destinados a Psiquiatría.  Subirles el sueldo 20000 Ptas. más que al señor Amigo R.

Insertar un empleado con valores null (por ejemplo la comisión o el oficio), y después borrarlo buscando como valor dicho valor null creado.

Borrar los empleados cuyo nombre de departamento sea producción.

Borrar todos los registros de la tabla Emp sin delete.

Volver a ejecutar los SCRIPTS de BBDD para dejar la base de datos intacta para el siguiente módulo.

