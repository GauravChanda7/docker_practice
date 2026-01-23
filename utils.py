import os
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
    )
    return conn

def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS visitors (
                       id SERIAL PRIMARY KEY,
                       visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       page_name VARCHAR(20)
                    );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Database init successfully")
    
    except Exception as e:
        print("Error init DB")