import streamlit as st
import tempfile
import pandas as pd
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
st.subheader("This is a web app to run the transportation planning models for city of Kota. We generate the following matrices: Distance Matrix, Time Travel Matrix, Trip Distribution Matrix, and Mode Split Matrices.")

# Load data (take csv files as input)
zonal_location_file = st.file_uploader("Zonal Location", type=["csv"])
od_matrix_file = st.file_uploader("Production Attraction Matrix", type=["csv"])
models_file = st.file_uploader("Vehicles for Model Split", type=["csv"])

if zonal_location_file is None or od_matrix_file is None or models_file is None:
    st.warning("Please upload the files to continue")
    st.stop()
else:
    st.success("Files uploaded successfully")
    zonal_tmp = tempfile.NamedTemporaryFile(delete=False)
    zonal_tmp.write(zonal_location_file.getvalue())
    zonal_tmp.seek(0)

    od_tmp = tempfile.NamedTemporaryFile(delete=False)
    od_tmp.write(od_matrix_file.getvalue())
    od_tmp.seek(0)
    
    models_tmp = tempfile.NamedTemporaryFile(delete=False)
    models_tmp.write(models_file.getvalue())
    models_tmp.seek(0)

# Load data
try:
    with open(zonal_tmp.name, "rb") as f:
        result = chardet.detect(f.read())
    # Result will contain the encoding
    enc = result["encoding"]
    data = pd.read_csv(zonal_tmp.name, encoding=enc)
    od_org = pd.read_csv(od_tmp.name)
    od_org = od_org.iloc[1:, 2:]
    st.header("Production Attraction Matrix")
    st.write(od_org)
    od_matrix = copy.deepcopy(od_org)
    dist_matrix = calculate_distance_matrix(data)
    dist_df = pd.DataFrame(dist_matrix)
    dist_df.to_csv("output/distance_matrix.csv")
    st.header("Distance Matrix")
    st.write(dist_df)
    time_matrix = calculate_time_matrix(dist_df)
    time_df = pd.DataFrame(time_matrix)
    time_df.to_csv("output/time_matrix.csv")
    # show time matrix
    st.header("Time Travel Matrix")
    st.write(time_df)
    new_od = calculate_T(od_matrix, dist_df)
    new_od_df = pd.DataFrame(new_od)
    new_od_df.to_csv("output/new_od.csv")
    st.header("Trip Distribution Matrix")
    st.write(new_od_df)
    models_df = pd.read_csv(models_tmp.name)
    od_matrices = models_split(od_matrix, models_df)
    # convert these matrices to dataframes with key as title
    od_matrices_df = {}
    for key in od_matrices:
        od_matrices_df[key] = pd.DataFrame(od_matrices[key])
    # show od matrices
    st.header("Mode Split Matrices")
    for key in od_matrices_df:
        st.write(key)
        st.write(od_matrices_df[key])
finally:
    zonal_tmp.close()
    od_tmp.close()
    models_tmp.close()
