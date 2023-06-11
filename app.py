from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        color = os.getenv('COLOR', 'red')
        return render_template_string('<body style="background-color:{}">Welcome to DevOps Clinics Flasks App!</body>'.format(color))
    except Exception as e:
        print(e)
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

~                                          