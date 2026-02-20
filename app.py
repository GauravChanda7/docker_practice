import os
from flask import Flask
from auth import auth_bp
from heavy_load import heavy_load_bp
from utils import get_db_connection, init_db

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(heavy_load_bp, url_prefix="/heavy")

with app.app_context():
    init_db()

@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors(page_name) VALUES ('home')")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visitors WHERE page_name = 'home'")
        count_home_visitor = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        greeting = os.environ.get('APP_GREETING', 'Hello')
        return f"""
            <div>
                <h1>{greeting}</h1>
                <h2>You are visitor {count_home_visitor} at Home Page</h2>
            </div>
        """
    except Exception as e:
        return f"""
            <div>
                <h1>Errors</h1>
                <p>{e}</p>
            </div>
        """




if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')


