from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask import jsonify
from db.data_access import getInfoOfYearData
from flask import request
from flask import json

app = Flask(__name__, template_folder="templates")

# API_KEY: AIzaSyDBT3WjjGrEgU-0JL7BjV_KwTQq6b88uyU

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDBT3WjjGrEgU-0JL7BjV_KwTQq6b88uyU"

GoogleMaps(
    app,
    key="AIzaSyDBT3WjjGrEgU-0JL7BjV_KwTQq6b88uyU"
)


@app.route('/')
def fullmap():
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:1;"
        ),
        lat=37.811024, 
        lng=-98.906707,
        markers=[],
        maptype = "TERRAIN",
        zoom="5"
    )
    return render_template(
        'map.html',
        fullmap=fullmap,
        GOOGLEMAPS_KEY=request.args.get('apikey')
    )

@app.route('/getInfoOfYear', methods=['POST'])
def getInfoOfYear():
    data = request.json
    year = data['year']
    getInfoOfYearData(year)

if __name__ == '__main__':
    # Add obtain information
    app.run(port=5000, debug=True)
