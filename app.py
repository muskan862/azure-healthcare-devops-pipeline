import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Clinical Early-Warning Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; color: #333; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #0056b3; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .status-box { background-color: #d4edda; color: #155724; padding: 15px; border-radius: 5px; margin: 20px 0; font-weight: bold; }
        .metric { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏥 Clinical Early-Warning Analytics Engine</h1>
        <div class="status-box">✓ System Status: Operational (Live on AKS)</div>
        <h3>Real-time Patient Metrics</h3>
        <div class="metric"><span>Vitals Processing Pipeline:</span> <strong>Active</strong></div>
        <div class="metric"><span>ML Analytics Model Status:</span> <strong>Loaded</strong></div>
        <div class="metric"><span>Inference Latency:</span> <strong>12ms</strong></div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(DASHBOARD_TEMPLATE)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "engine": "operational"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)