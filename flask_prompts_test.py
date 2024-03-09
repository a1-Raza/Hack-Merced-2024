
from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('prompts_test.html')

if __name__ == '__main__':
    app.run(debug=True)
