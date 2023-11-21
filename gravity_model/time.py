from dependencies import *
from constants import CONSTANTS

# convert given distance df to time df by dividing by speed
def calculate_time_matrix(dist_df, speed=CONSTANTS._SPEED):
    '''Calculate time matrix by dividing distance matrix by speed.
    Input: distance matrix (pandas DataFrame), speed (float)
    Output: time matrix (pandas DataFrame)
    '''
    return dist_df / speed