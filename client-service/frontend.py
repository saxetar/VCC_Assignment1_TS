from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    url = "http://192.168.56.101:5000/balance"
    
    try:
        r = requests.get(url)
        return f"Data from Backend: {r.text}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)