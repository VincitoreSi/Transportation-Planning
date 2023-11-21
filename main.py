from gravity_model.F import calculate_F
from gravity_model.K import calculate_K
from gravity_model.T import calculate_T
from gravity_model.distance import calculate_distance_matrix
from gravity_model.time import calculate_time_matrix
from constants import CONSTANTS
from dependencies import *

def main():
    # Load data
    with open('data/zonal location.csv', 'rb') as f:
        result = chardet.detect(f.read()) 

    # Result will contain the encoding
    enc = result['encoding']
    data = pd.read_csv('data/zonal location.csv', encoding=enc)
    od_org = pd.read_csv('data/production attraction matrix.csv')
    od_org = od_org.iloc[1:, 2:]
    od_matrix = copy.deepcopy(od_org)
    dist_matrix = calculate_distance_matrix(data)
    dist_df = pd.DataFrame(dist_matrix)
    dist_df.to_csv('output/distance_matrix.csv')
    
    time_matrix = calculate_time_matrix(dist_df)
    time_df = pd.DataFrame(time_matrix)
    time_df.to_csv('output/time_matrix.csv')
    print(len(od_matrix), len(od_matrix.columns))
    print(len(dist_df), len(dist_df.columns))
    print(len(time_df), len(time_df.columns))
    
    new_od = calculate_T(od_matrix, dist_df)
    new_od_df = pd.DataFrame(new_od)
    new_od_df.to_csv('output/new_od.csv')

if __name__ == '__main__':
    main()