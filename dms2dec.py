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


def convert_coordinates(latitude, longitude):
    decimal_latitude = latitude_dms_to_decimal(latitude)
    decimal_longitude = longitude_dms_to_decimal(longitude)

    return decimal_latitude, decimal_longitude


lat1 = "484727N"
long1 = "0165333E"

decimal_latitude, decimal_longitude = convert_coordinates(lat1, long1)

print("Latitude (Decimal):", decimal_latitude)
print("Longitude (Decimal):", decimal_longitude)

lat2 = "500359.08N"
long2 = "0122446.35E"

decimal_latitude, decimal_longitude = convert_coordinates(lat2, long2)

print("Latitude (Decimal):", decimal_latitude)
print("Longitude (Decimal):", decimal_longitude)
