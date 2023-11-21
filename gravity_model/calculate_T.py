from dependencies import *
from . import calculate_F, calculate_K

# Calculate T[i,j] for a pair of locations
def calculate_Tij(od_matrix, dist_df, i, j):
    '''Calculate T[i,j] for a pair of locations for gravity model.
    Input: OD matrix (pandas DataFrame), distance matrix (pandas DataFrame), row index (int), column index (int)
    Output: T[i,j] value (float)
    '''
    od_matrix = od_matrix.iloc[:, 1:]
    Aj = sum(od_matrix.iloc[:, j])
    Pi = sum(od_matrix.iloc[i, :])
    denominator = [sum(od_matrix.iloc[:, k]) * calculate_F(dist_df, i, k) * calculate_K(i, k) for k in range(0, len(od_matrix.columns))]
    return round(Aj * calculate_F(i, j) * Pi / sum(denominator))  # round to 3 decimal places

# Calculate T matrix using T[i,j] values
def calculate_T(od_matrix, dist_df):
    '''Calculate T matrix using T[i,j] values.
    Input: OD matrix (pandas DataFrame), distance matrix (pandas DataFrame)
    Output: T matrix (pandas DataFrame)
    '''
    T = np.zeros((len(od_matrix), len(od_matrix.columns)-1))
    for i in range(len(od_matrix)):
        for j in range(len(od_matrix.columns)-1):
            T[i][j] = calculate_Tij(od_matrix, dist_df, i, j)
    return pd.DataFrame(T)  # return DataFrame