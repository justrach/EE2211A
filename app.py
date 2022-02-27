import ast
import streamlit as st
import numpy as np

from streamlit_tags import st_tags
# Create an Invertible Matrix Checker
st.header("Streamlit Application for EE2211")

st.subheader("Matrix Rank Calculator")

matrix_rank_value = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=[[1]],
    suggestions=['five', 'six', 'seven', 
                 'eight', 'nine', 'three', 
                 'eleven', 'ten', 'four'],
    maxtags = 10,
    key='1')
st.write(matrix_rank_value)
st.write(type(matrix_rank_value))

new_list = []
for x in range(0,len(matrix_rank_value)):
    matrix_rank_value[x].strip(" ")
    _list = ast.literal_eval(matrix_rank_value[x])
    # print(_list)
    # drag_list.extend(_list)
    # print(drag_list)
    new_list.append(_list)
st.write(new_list)
st.write(np.linalg.matrix_rank(new_list))