from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="flaskdb",
            user="flaskuser",
            password=os.getenv("POSTGRES_PASSWORD"),
            host="postgres",
            port="5432"
        )
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database Connection Failed: {conn}"
    return "Connected to PostgreSQL successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
