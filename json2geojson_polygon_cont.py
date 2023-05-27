import json


def latitude_dms_to_decimal(coordinate):
    degrees = int(coordinate["Geo_lat"][:2])
    minutes = int(coordinate["Geo_lat"][2:4])
    seconds = float(coordinate["Geo_lat"][4:-1])
    direction = coordinate["Geo_lat"][-1]

    decimal = degrees + (minutes / 60) + (seconds / 3600)

    if direction in ['S', 'W']:
        decimal = -decimal

    return decimal


def longitude_dms_to_decimal(coordinate):
    degrees = int(coordinate["Geo_long"][:3])
    minutes = int(coordinate["Geo_long"][3:5])
    seconds = float(coordinate["Geo_long"][5:-1])
    direction = coordinate["Geo_long"][-1]

    decimal = degrees + (minutes / 60) + (seconds / 3600)

    if direction in ['S', 'W']:
        decimal = -decimal

    return decimal


def convert_json_to_geojson(json_data):

    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for item in json_data[0]['Data']['Object']:
        polygon_coords = item["Polygon_continuing_coord"]
        coordinates = []

        for coord in polygon_coords:
            if "Geo_lat" in coord and "Geo_long" in coord:
                print(coord)
                latitude = latitude_dms_to_decimal(coord)
                print(latitude)
                longitude = longitude_dms_to_decimal(coord)
                print(longitude)
                coordinates.append([longitude, latitude])

        feature = {
            "type": "Feature",
            "properties": {
                "Identification": item["Identification"],
                "Name": item["Name"],
                "Lower_limit": item["Lower_limit"],
                "Upper_limit": item["Upper_limit"]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [coordinates]
            }
        }

        geojson_data["features"].append(feature)

    return geojson_data


# Load the JSON file
with open("input.json", "r") as file:
    json_data = json.load(file)


# Convert JSON to GeoJSON
geojson_data = convert_json_to_geojson(json_data)


# Save the GeoJSON file
with open("output.geojson", "w") as file:
    json.dump(geojson_data, file, indent=2)
