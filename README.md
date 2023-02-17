# Prueba tecnica softek
Este es un proyecto de ejemplo que utiliza Python, SQLite y Flask para resolver tres problemas en cocreto el primero permite determinar el estado de unas ordenes,  el segundo la estación del año en que se crearon otras ordenes y los días en que se produjo un cambio de clima dado un conjunto finito de dias. Los usuarios pueden utilizar los endpoints para obtener esta información.

# Requisitos
Para utilizar este proyecto, necesitarás tener instalado lo siguiente:

- Python (versión 3.6 o superior)
- SQLite 
- Flask

## Instalación
    - Clona este repositorio en tu máquina local.
    - Crea un entorno virtual en Python e instala los requisitos
```sh
$ python3 -m venv venv
$ venv\Scripts\activate
$(venv) pip install -r requirements.txt
```
- Ejecuta la aplicación:
 ```sh
    $ flask run
```
la base de datos se creará automaticamente

## Endpoints
/order_status: este endpoint muestra el estado actual de las ordenes existentes en la base de datos

/season: este endpoint permite a los usuarios determinar la estación del año en que se creó una orden.

/weather_change: este endpoint permite a los usuarios determinar los días en que se produjo un cambio de clima en relación a una orden.

# Estructura del proyecto
.
 * dao
    * [customer_ord_line.py](./dao/customer_ord_line.py)
    * [customer_orders.py](./dao/customer_orders.py)
    * [weather.py](./dao/weather.py)
 * database
    * config.py(.database/config.py)
    * database.py(.database/database.py)
 * entity
    * [customer_ord_line.py](./entity/customer_ord_line.py)
    * [customer_orders.py](./entity/customer_orders.py)
    * [weather.py](./entity/weather.py)
 * models
    * [customer_ord_line.py](./models/customer_ord_line.py)
    * [customer_orders.py](./models/customer_orders.py)
    * [weather.py](./models/customer_orders.py)
* service
    * [customer_ord_line.py](./services/customer_ord_line.py)
    * [customer_orders.py](./services/customer_orders.py)
    * [weather.py](./services/weather.py)
 * [README.md](./README.md)
 * [app.py](./app.py)
 * [.gitingore](./gitignore)
 * [softtek.db](./softek.db)
 * [requirements.txt](./requierements.txt)
 
dao: contiene los controladores de la base de datos, aqui podemos encontrar las consultas sql
database: contiene la estructura y los datos de la base de datos, asi como la conexion de sqlalchemy
entity: contiene las entidades de la base de datos (modelos sqlalchemy)
models: contiene las clase modelo de las respuestas esperadas
service: contiene los archivos donde se consulta la informacion y se trata con ella, esta es la cabeza del proyecto


