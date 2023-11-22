from dependencies import *

# Calculate Model Split
def models_split(od_matrix, models_df):
    '''Split OD matrix into different OD matrices for different vehicle types.
    Input: OD matrix (pandas DataFrame), models (pandas DataFrame)
    Output: OD matrices for different vehicle types (list of pandas DataFrames)
    '''
    # initialize OD matrices for different vehicle types
    od_matrices = []
    sum_of_models = sum(models_df.iloc[:, 1])
    for i in range(len(models_df)):
        od_matrices.append(pd.DataFrame(np.zeros((len(od_matrix), len(od_matrix.columns)))))
    
    # split OD matrix into different OD matrices for different vehicle types
    models = {}
    for i in range(len(models_df)):
        for j in range(len(od_matrix)):
            for k in range(len(od_matrix.columns)):
                od_matrices[i].iloc[j, k] = od_matrix.iloc[j, k] * models_df.iloc[i, 1] / sum_of_models
        models[models_df.iloc[i, 0]] = od_matrices[i]
    return models