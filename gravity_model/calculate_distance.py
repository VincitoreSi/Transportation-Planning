from dependencies import *

# Convert DMS to DD
def dms_to_dd(full_coordinate):
    """Converts a coordinate in degrees, minutes, seconds to decimal degrees.
    Input: a coordinate in degrees, minutes, seconds (string)
    Output: a coordinate in decimal degrees (float)
    """
    degrees_minutes_seconds = full_coordinate.split('"')[0]
    degrees, minutes_seconds = degrees_minutes_seconds.split("°")
    minutes, seconds = minutes_seconds.split("'")
    dd = int(degrees) + int(minutes) / 60 + float(seconds) / 3600
    dd = dd * -1 if full_coordinate[-1] in ("W", "S") else dd
    return dd

# Calculate distance between two points
def calculate_distance(row1, row2):
    """Calculate distance between two points using Haversine formula.
    Input: two rows of data (pandas Series)
    Output: distance between the two points (float)
    """
    lat1 = dms_to_dd(row1["Lat"])
    lon1 = dms_to_dd(row1["Long"])
    lat2 = dms_to_dd(row2["Lat"])
    lon2 = dms_to_dd(row2["Long"])
    ans = hs.haversine(
        (lat1, lon1), (lat2, lon2), unit=hs.Unit.KILOMETERS
    )  # return distance in kilometers
    return round(ans, 3)  # round to 3 decimal places


# Calculate distance matrix
def calculate_distance_matrix(data):
    """Calculate distance matrix for a given dataset.
    Input: dataset (pandas DataFrame)
    Output: distance matrix (numpy array)
    """
    distance_matrix = np.zeros((len(data), len(data)))
    for i in range(len(data)):
        for j in range(len(data)):
            distance_matrix[i][j] = calculate_distance(data.iloc[i, :], data.iloc[j, :])
    return distance_matrix
