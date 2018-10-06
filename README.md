# Examen Práctico de Programación Python

Se desea realizar ajuste sobre un sistema que permite realizar órdenes de productos para clientes.

## Parte 1

En una base de datos con las siguientes entidades:

Se desea hacer las siguientes adiciones:

1. Los clientes ahora solo tendrán un conjunto de productos disponibles, es decir,
    para cada cliente debe ser posible escoger qué productos puede comprar.

Ejemplo:

```
Customer Available Products
```
```
Manny Bharma Product A, Product B, Product C
```
```
Alan Briggs Product B
```
```
Mike Simm Product A, Product D
```
2. Se debe poder establecer el precio de cada producto.

Agregue al diagrama las columnas y entidades que considere necesarias y cree la
base de datos.

## Parte 2 - Crear un servicio web REST

```
Utilizando Python 3, implemente un servicio web REST que permita realizar las
siguientes operaciones:
```
1. Crear una órden para un cliente con hasta máximo 5 productos. Tenga en cuenta
    que sólo algunos productos están permitidos por cliente.
2. Listar las órdenes de un cliente por un rango de fechas.

## Parte 3

Cree una página html que permita seleccionar un cliente y presente las órdenes del
último mes usando el método listar órdenes del servicio web.

```
Creation
Date
```
```
Order ID Total $ Delivery Address Products
```
```
01 - 05 - 2017 84564 $ 30.56 15 Queens Park Road,
W32 YYY, UK
```
```
2 x Product A
1 x Product B
```
```
02 - 05 - 2017 84566 $ 11.00 12001 White Oak
Avenue, 12332. USA
```
```
1 x Product C
```
Notas

- Los datos de prueba para las tablas clientes, productos y productos permitidos se deben insertar directamente en la base de datos.
- Los datos de prueba para las cualquier tabla adicional que haya creado también se pueden agregar directamente en la base de datos.
- Las únicas tablas que no deben tener datos son ‘order’ y ‘order_detail’ en estas sólo se deben agregar registros a través del servicio web.
- No es necesario implementar un CRUD para cada tabla en la base de datos, los endpoints indispensables para la prueba son: Creación de órden y Listar órdenes por rango de fechas.


Entregables

- El Diagrama Entidad Relación en formato imagen.
- Los scripts SQL para la creación de la base de datos y los datos de prueba.
- La documentación de los métodos del API REST
- Diagrama de clases u otros diagramas que considere necesarios para ilustrar la solución.
- El código fuente de la aplicación. Este código preferiblemente debe estar en un repositorio git.

```
Tecnologías
```
- Backend: La aplicación debe realizarse preferiblemente utilizando el framework Falcon, Flask o Django
- Base de datos: Puede utilizar cualquier base de datos relacional.
