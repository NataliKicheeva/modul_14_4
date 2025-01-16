import sqlite3


# Функция для создания таблицы Products
def initiate_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS Products")
    # Создание таблицы, если она не существует
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products


def insert_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    for i in range(1, 5):
        cursor.execute(
            "INSERT INTO Products(id, title, description, price, image) VALUES (?,?,?,?, ?)",
                       (i, f"Продукт {i}", f"Описание {i}", i * 100, f"{i}.jpg")
        )

    conn.commit()
    conn.close()


# Инициализация базы данных и вставка данных
if __name__ == "__main__":
    initiate_db()
    insert_products()
