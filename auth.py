from flask import Blueprint
from utils import get_db_connection, init_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signin")
def signin():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors(page_name) VALUES ('signin')")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visitors WHERE page_name = 'signin'")
        count_signin_visitor = cursor.fetchone()[0]

        return f"""
            <div>
                <h1>You are signed in</h1>
                <h2>You are visitor {count_signin_visitor} at Signin Page</h2>
            </div>
        """
    
    except Exception as e:
        return f"""
            <div>
                <h1>Errors</h1>
                <p>{e}</p>
            </div>
        """


@auth_bp.route("/login")
def login():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors(page_name) VALUES ('login')")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visitors WHERE page_name = 'login'")
        count_login_visitor = cursor.fetchone()[0]

        return f"""
            <div>
                <h1>You are logged in</h1>
                <h2>You are visitor {count_login_visitor} at Login Page</h2>
            </div>
        """
    except Exception as e:
        return f"""
            <div>
                <h1>Errors</h1>
                <p>{e}</p>
            </div>
        """