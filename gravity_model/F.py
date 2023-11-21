from dependencies import *
from constants import CONSTANTS

# Calculate F value for a pair of locations
def calculate_F(dist_df, i, j, a=CONSTANTS._A, b=CONSTANTS._B, c=CONSTANTS._C):
    '''Calculate F value for a pair of locations for gravity model.
    Input: distance matrix (pandas DataFrame), row index (int), column index (int), constants (floats)
    Output: F value (float)
    '''
    return a * (dist_df.iloc[i, j] ** b) * math.exp(c * dist_df.iloc[i, j])
