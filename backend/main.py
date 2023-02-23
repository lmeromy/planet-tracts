from flask import Flask
import geopandas as gpd
import fiona
import sqlite3


app = Flask(__name__)


@app.route("/tracts")
def list_tracts():

    # gpkg =  './test.geojson'
    file = gpd.read_file('geojson_tracts.geojson')
    # with fiona.open('tracts.gpkg') as layer:
    #     for feature in layer:
    #         print(feature['geometry'])
    # filtered = file.loc[file['NAMELSAD']]

    return {
       "tracts": file.to_json(),
        
    }


@app.route("/tracts/<int:pk>")
def get_tract(pk):

    geodataframe = gpd.read_file('geojson_tracts.geojson')

    selected_tract =  geodataframe.loc[geodataframe['fid'] == pk, ["NAMELSAD", "GEOID", "geometry"]]
    print(selected_tract.to_json())
    return {
        "selected_tract":  selected_tract.to_json()
    }
