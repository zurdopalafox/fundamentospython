1. Encontrar el salario medio de los analistas, mostrando el número de los empleados con oficio analista.

select AVG(SALARIO) as MEDIA, COUNT(*) AS PERSONAS, OFICIO 
from EMP 
where OFICIO='ANALISTA'
group by OFICIO;



2. Encontrar el salario más alto, mas bajo y la diferencia entre ambos de todos los empleados con oficio EMPLEADO.

select  oficio, max(salario) as SALARIOMAXIMO
, min(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA 
from emp group by oficio having oficio = 'EMPLEADO';

3. Visualizar los salarios mayores para cada oficio.
select oficio, max(salario) as SALARIOMAXIMO
from emp group by oficio;

4. Visualizar el número de personas que realizan cada oficio en cada departamento.

select dept_no, 
count(*) as PERSONAS, oficio
from emp group by dept_no, oficio
order by 1;

5. Buscar aquellos departamentos con cuatro o más personas trabajando.
select dept_no, count(*) as PERSONAS 
from emp group by dept_no having count(*) >= 4;

6. Mostrar el número de directores que existen por departamento.
select count(*) as NUMEROEMPLEADOS, dept_no 
from emp
where oficio = 'DIRECTOR'
group by dept_no;

7. Visualizar el número de enfermeros, enfermeras e interinos que hay en la plantilla, ordenados por la función.
select FUNCION, count(*) as NUMEROEMPLEADOS
from PLANTILLA
where FUNCION in ('ENFERMERO','ENFERMERA','INTERINO')
group by FUNCION
order by FUNCION;

8. Visualizar departamentos, oficios y número de personas, para aquellos departamentos que tengan dos o más personas trabajando en el mismo oficio.
select dept_no, oficio, count(*) as NUMEROEMPLEADOS
from emp
group by dept_no, oficio
having count(*) >= 2
order by dept_no, oficio;


9. Calcular el salario medio, Diferencia, Máximo y Mínimo de cada oficio. Indicando el oficio y el número de empleados de cada oficio.

select oficio, count(*) as EMPLEADOS
, min(salario) as SALARIOMAXIMO
, max(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA
, avg(salario) as MEDIA
 from emp 
 group by  oficio;

10. Calcular el valor medio de las camas que existen para cada nombre de sala. Indicar el nombre de cada sala y el número de cada una de ellas.
select COUNT(*) as NUMEROSALAS
,  avg(NUM_CAMA) as MEDIACAMAS
, NOMBRE
from SALA
group by NOMBRE;

11. Calcular el salario medio de la plantilla de la sala 6, según la función que realizan. Indicar la función y el número de empleados.
select funcion, sala_cod, avg(salario) as SALARIOMEDIO 
from plantilla
where sala_cod = 6
group by FUNCION, sala_cod;


12. Averiguar los últimos empleados que se dieron de alta en la empresa en cada uno de los oficios, ordenados por la fecha.
select max(fecha_alt) as FECHAMAXIMA, oficio
from emp
group by oficio
order by FECHAMAXIMA desc;


13. Mostrar el número de hombres y el número de mujeres que hay entre los enfermos.

select COUNT(*) as PERSONAS
, SEXO
from ENFERMO
group by SEXO;

14. Mostrar la suma total del salario que cobran los empleados de la plantilla para cada función y turno.

select SUM(SALARIO) as SUMASALARIAL
, FUNCION, TURNO
from PLANTILLA
group by FUNCION, TURNO;


15. Calcular el número de salas que existen en cada hospital.

select count(*) as NUMEROSALAS
, hospital_cod from sala
group by hospital_cod;

16.Mostrar el número de enfermeras que existan por cada sala.
select count(*) as NUMEROENFERMERAS
, sala_cod from plantilla
where funcion = 'ENFERMERA'
group by sala_cod;