from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

# Koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"]
)

# Fungsi untuk membuat tabel tugas
def create_task_table():
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            description TEXT
        );
    """)
    conn.commit()
    cursor.close()

# Fungsi untuk mendapatkan semua tugas
def get_all_tasks():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks;")
    rows = cursor.fetchall()
    cursor.close()
    return rows

@app.route("/")
def index():
    tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    create_task_table()
    app.run(host="0.0.0.0")
