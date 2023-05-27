import json


def latitude_dms_to_decimal(coordinate):
    degrees = int(coordinate[:2])
    minutes = int(coordinate[2:4])
    seconds = float(coordinate[4:-1])
    direction = coordinate[-1]

    decimal = degrees + (minutes / 60) + (seconds / 3600)

    if direction in ['S', 'W']:
        decimal = -decimal

    return decimal


def longitude_dms_to_decimal(coordinate):
    degrees = int(coordinate[:3])
    minutes = int(coordinate[3:5])
    seconds = float(coordinate[5:-1])
    direction = coordinate[-1]

    decimal = degrees + (minutes / 60) + (seconds / 3600)

    if direction in ['S', 'W']:
        decimal = -decimal

    return decimal


def convert_json_to_geojson(json_data):

    features = []
    properties2 = {}
    geo_lat_cen = "000000.00N"
    geo_long_cen = "0000000.00E"

    for item in json_data:
        if "Data" in item:
            for obj in item["Data"]["Object"]:
                properties = {
                    "Identification": obj["Identification"],
                    "Name": obj["Name"],
                    "Lower_limit": obj["Lower_limit"],
                    "Upper_limit": obj["Upper_limit"]
                }
                for detail in obj['Circle_coord']:
                    properties2 = {
                        "Radius_unit": detail['Radius_unit'],
                        "Radius_value": detail['Radius_value']
                    }
                    geo_lat_cen = detail['Geo_lat_cen']
                    geo_long_cen = detail['Geo_long_cen']
                    print(geo_lat_cen)
                    print(geo_long_cen)
                properties.update(properties2)
                latitude = latitude_dms_to_decimal(geo_lat_cen)
                longitude = longitude_dms_to_decimal(geo_long_cen)
                print(str(latitude) + " - " + str(longitude))
                geometry = {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                }
                feature = {
                    "type": "Feature",
                    "geometry": geometry,
                    "properties": properties
                }
                features.append(feature)
                geo_lat_cen = "000000.00N"
                geo_long_cen = "0000000.00E"

    geojson_data = {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": features
    }

    return geojson_data


# Read JSON file
with open('input.json') as json_file:
    json_data = json.load(json_file)


# Convert JSON to GeoJSON
geojson_data = convert_json_to_geojson(json_data)


# Write GeoJSON to file
with open('output.geojson', 'w') as geojson_file:
    json.dump(geojson_data, geojson_file, indent=4)
