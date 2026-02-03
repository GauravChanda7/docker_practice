import os
import psycopg2
import time

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST'),
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
    )
    return conn

def init_db():
    retries = 5
    while retries > 0:
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
            return
        
        except Exception as e:
            print(f"DB not ready yet, retrying ... ({e})")
            retries -= 1
            time.sleep(5)

    print("Coundn't connect to DB after 5 retries") 
