from gravity_model.calculate_F import calculate_F
from gravity_model.calculate_K import calculate_K
from gravity_model.calculate_T import calculate_T
from gravity_model.calculate_distance import calculate_distance_matrix
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
    od_matrix = copy.deepcopy(od_org)
    dist_matrix = calculate_distance_matrix(data)
    dist_df = pd.DataFrame(dist_matrix)
    dist_df.to_csv('output/distance_matrix.csv')

if __name__ == '__main__':
    main()