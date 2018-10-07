# Examen Práctico de Programación Python

Se desea realizar ajuste sobre un sistema que permite realizar órdenes de productos para clientes.

## Parte 1

En una base de datos con las siguientes entidades:

![alt text](https://raw.githubusercontent.com/josdavidmo/beitech_test/develop/doc/initial_rem.png)

Se desea hacer las siguientes adiciones:

1. Los clientes ahora solo tendrán un conjunto de productos disponibles, es decir, para cada cliente debe ser posible escoger qué productos puede comprar.

Ejemplo:

| Customer | Available Products |
| ------------- | ------------- |
| Manny Bharma | Product A, Product B, Product C |
| Alan Briggs | Product B |
| Mike Simm | Product A, Product D |

2. Se debe poder establecer el precio de cada producto.

Agregue al diagrama las columnas y entidades que considere necesarias y cree la base de datos.

### ajustes realizados sobre el modelo

![alt text](https://raw.githubusercontent.com/josdavidmo/beitech_test/develop/doc/mer.png)

Se realizaron las siguientes modificaciones sobre las entidades:

1. Se elimino la columnas price y product_description de la tabla order_detail.
2. Se agrego la columnas price y product_description a la tabla product.
3. Se agrego la columna date en la tabla order.
4. Se agrego la columnas quantity y product_id a la tabla order_detail.
5. Se creo la entidad availableproduct y se agregaron las columnas customer_id y product_id.
6. Se completaron las llaves foraneas a todas las entidades.

El diagrama de clases es el siguiente:

![alt text](https://raw.githubusercontent.com/josdavidmo/beitech_test/develop/doc/models.png)

Es posible apreciar que corresponde de forma fidedigna al diagrama relacional de la aplicación. El diagrama fue generado usando el siguiente comando:

```
python manage.py graph\_models invoice -o doc/models.png
```

***Nota:***

Asegurese de tener instalado el siguiente paquete:

```
sudo apt-get install graphviz
```

## Parte 2 - Crear un servicio web REST

Utilizando Python 3, implemente un servicio web REST que permita realizar las siguientes operaciones:

1. ***Crear una órden*** para un cliente con hasta máximo 5 productos. Tenga en cuenta que sólo algunos productos están permitidos por cliente.
2. ***Listar las órdenes*** de un cliente por un rango de fechas.

### creación de servicios web REST

Para el desarrollo de los servicios se utilizó Django2.1.2 usando la libreria djangorestframework3.8.2. Los servicios se encuentran documentados usando Swagger y es posible visualizar la información sobre el servicio usando el siguiente link [/doc/](/doc/).

1. ***Crear una orden***. Para crear una órden se debe consumir el servicio [/invoice/order/](/invoice/order/) usando el método POST. Los datos para consumir este servicio se deben presentar de la siguiente estructura:
```
{
  "customer": 1,
  "delivery_address": "Diagonal 86a # 101 - 40",
  "date": "2018-10-06",
  "order_details": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 2,
      "quantity": 1
    },
    {
      "product_id": 3,
      "quantity": 41
    },
    {
      "product_id": 4,
      "quantity": 54
    }
  ]
}
```

El servicio validara que el usuario tenga disponibles los productos asociados y que el order_details no supere más de 5 productos.

2. ***Listar las órdenes***. Para crear una órden se debe consumir el servicio [/invoice/order/](/invoice/order/) usando el método GET. Si ingresa usando el navegador visualizara la siguiente imagen:

![alt text](https://raw.githubusercontent.com/josdavidmo/beitech_test/develop/doc/orderget.png)

Los datos retornados por este servicio presentan la siguiente estructura:
```
[
    {
        "customer": 1,
        "id": 1,
        "delivery_address": "Calle 26c #13-97",
        "date": "2018-10-01",
        "total": 42271,
        "products": "Arroz,Azúcar,Consomate"
    },
    {
        "customer": 1,
        "id": 2,
        "delivery_address": "Calle 26c #13-97",
        "date": "2018-10-01",
        "total": 31396,
        "products": "Sopa,Consomate"
    }
]
```

## Parte 3

Cree una página html que permita seleccionar un cliente y presente las órdenes del
último mes usando el método listar órdenes del servicio web.

| Creation Date | Order ID | Total $ | Delivery Address | Products |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 01 - 05 - 2017 | 84564 | $ 30.56 | 15 | Queens Park Road\, W32 YYY, UK | 2 x Product A\, 1 x Product B |
| 02 - 05 - 2017 | 84566 | $ 11.00 | 12001 | White Oak Avenue\, 12332. USA | 1 x Product C |

***Notas***

- Los datos de prueba para las tablas clientes, productos y productos permitidos se deben insertar directamente en la base de datos.
- Los datos de prueba para las cualquier tabla adicional que haya creado también se pueden agregar directamente en la base de datos.
- Las únicas tablas que no deben tener datos son ‘order’ y ‘order_detail’ en estas sólo se deben agregar registros a través del servicio web.
- No es necesario implementar un CRUD para cada tabla en la base de datos, los endpoints indispensables para la prueba son: Creación de órden y Listar órdenes por rango de fechas.


***Entregables***

- El Diagrama Entidad Relación en formato imagen.
- Los scripts SQL para la creación de la base de datos y los datos de prueba.
- La documentación de los métodos del API REST
- Diagrama de clases u otros diagramas que considere necesarios para ilustrar la solución.
- El código fuente de la aplicación. Este código preferiblemente debe estar en un repositorio git.


***Tecnologías***

- Backend: La aplicación debe realizarse preferiblemente utilizando el framework Falcon, Flask o Django
- Base de datos: Puede utilizar cualquier base de datos relacional.
