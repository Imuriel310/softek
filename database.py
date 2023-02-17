import sqlite3

# Crear una conexión a la base de datos y un cursor para ejecutar comandos
conn = sqlite3.connect('softtek.db')
cursor = conn.cursor()

# Crear la tabla customer_ord_lines
cursor.execute('''CREATE TABLE customer_ord_lines
                (order_number text, item_name text, status text)''')

# Insertar datos en la tabla customer_ord_lines
ord_lines_data = [
    ('ORD_1567', 'LAPTOP', 'SHIPPED'),
    ('ORD_1567', 'MOUSE', 'SHIPPED'),
    ('ORD_1567', 'KEYBOARD', 'PENDING'),
    ('ORD_1234', 'GAME', 'SHIPPED'),
    ('ORD_1234', 'BOOK', 'CANCELLED'),
    ('ORD_1234', 'BOOK', 'CANCELLED'),
    ('ORD_9834', 'SHIRT', 'SHIPPED'),
    ('ORD_9834', 'PANTS', 'CANCELLED'),
    ('ORD_7654', 'TV', 'CANCELLED'),
    ('ORD_7654', 'DVD', 'CANCELLED')
]
cursor.executemany("INSERT INTO customer_ord_lines VALUES (?,?,?)", ord_lines_data)

# Crear la tabla customer_orders
cursor.execute('''CREATE TABLE customer_orders
                (ord_id text, ord_dt text, qt_ordd integer)''')

# Insertar datos en la tabla customer_orders
orders_data = [
    ('113-8909896-6940269', '9/23/19', 1),
    ('114-0291773-7262677', '1/1/20', 1),
    ('114-0291773-7262697', '12/5/19', 1),
    ('114-9900513-7761000', '9/24/20', 1),
    ('112-5230502-8173028', '1/30/20', 1),
    ('112-7714081-3300254', '5/2/20', 1),
    ('114-5384551-1465853', '4/2/20', 1),
    ('114-7232801-4607440', '10/9/20', 1)
]
cursor.executemany("INSERT INTO customer_orders VALUES (?,?,?)", orders_data)

# Crear la tabla weather
cursor.execute('''CREATE TABLE weather
                (date text, was_rainy integer)''')

# Insertar datos en la tabla weather
weather_data = [
    ('1/1/20', 0),
    ('1/2/20', 1),
    ('1/3/20', 1),
    ('1/4/20', 0),
    ('1/5/20', 0),
    ('1/6/20', 1),
    ('1/7/20', 0),
    ('1/8/20', 1),
    ('1/9/20', 1),
    ('1/10/20', 1)
]
cursor.executemany("INSERT INTO weather VALUES (?,?)", weather_data)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
