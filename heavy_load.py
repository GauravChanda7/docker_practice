from flask import Blueprint
import time

heavy_load_bp = Blueprint("heavy", __name__)

@heavy_load_bp.route("/")
def heavy():
    start = time.time()
    while time.time() - start < 0.5:
        _ = [x**2 for x in range(10000)]
    return f"""
        <div>
            <h1>Heavy Load</h1>
            <p>This page simulates a heavy load by performing a CPU-intensive task for 0.5 seconds.</p>
        </div>
    """
