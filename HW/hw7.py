import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Создание таблицы products
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()


# 1. CREATE — добавление товара
def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()
    print("Товар добавлен")


# 2. READ — получение всех товаров
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    if products:
        print("Список товаров:")
        for product in products:
            print(product)
    else:
        print("Товаров пока нет")


# 3. UPDATE — обновление цены товара по id
def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    conn.commit()
    print("Цена товара обновлена")


# 4. DELETE — удаление товара по id
def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    conn.commit()
    print("Товар удален")


# Пример работы
create_product("Apple", 120.5, 10)
create_product("Milk", 80, 5)

read_products()

update_product(1, 150)

read_products()

delete_product(2)

read_products()

# Закрытие соединения
conn.close()