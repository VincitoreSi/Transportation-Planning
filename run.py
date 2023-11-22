import streamlit as st
from gravity_model.F import calculate_F
from gravity_model.K import calculate_K
from gravity_model.T import calculate_T
from gravity_model.distance import calculate_distance_matrix
from gravity_model.time import calculate_time_matrix
from constants import CONSTANTS
from dependencies import *
from model_split.models import *

# Title
st.title("Transportation Planning Models for city of Kota")

# Load data (take csv files as input)
zonal_location_file = st.file_uploader("Zonal Location", type=["csv"])
od_matrix_file = st.file_uploader("Production Attraction Matrix", type=["csv"])
models_file = st.file_uploader("Vehicles for Model Split", type=["csv"])


# Load data
with open(zonal_location_file, "rb") as f:
    result = chardet.detect(f.read())
# Result will contain the encoding
enc = result["encoding"]
data = pd.read_csv(zonal_location_file, encoding=enc)
od_org = pd.read_csv(od_matrix_file)
od_org = od_org.iloc[1:, 2:]
od_matrix = copy.deepcopy(od_org)
dist_matrix = calculate_distance_matrix(data)
dist_df = pd.DataFrame(dist_matrix)
dist_df.to_csv("output/distance_matrix.csv")
st.write(dist_df)
time_matrix = calculate_time_matrix(dist_df)
time_df = pd.DataFrame(time_matrix)
time_df.to_csv("output/time_matrix.csv")
# show time matrix
st.write(time_df)
new_od = calculate_T(od_matrix, dist_df)
new_od_df = pd.DataFrame(new_od)
new_od_df.to_csv("output/new_od.csv")
st.write(new_od_df)
models_df = pd.read_csv(models_file)
od_matrices = models_split(od_matrix, models_df)
st.write(od_matrices)