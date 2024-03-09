
from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # new coordinates for the map's center
    map_location = [37.350567, -120.427406]
    map_zoom_start = 8

    # make the map object with the new center
    mymap = folium.Map(location=map_location, zoom_start=map_zoom_start)

    # make a map as HTML string
    map_html = mymap._repr_html_()

    # Pass the map HTML to the template
    return render_template('map.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
