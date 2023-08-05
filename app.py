import streamlit as st
import pandas as pd
from helper_functions import find_common_elements_in_row
def main():
    st.title("Row Compare")

    uploaded_file = st.file_uploader("Choose a Excel file", type=["xlsx", "xls"])
    if uploaded_file is not None:
        st.subheader("Rows Loaded")
        data =  pd.read_excel(uploaded_file, header=None)
        st.dataframe(data)
        table = data.values.tolist()
        data_to_render = find_common_elements_in_row(table)
        st.divider()
        st.subheader("Results")
        st.json(data_to_render)

    st.divider()
    st.markdown("""
    Made with :heart: by Niranjan Shah \n
    Repo: https://github.com/niranjanblank/MovieRecommenderSystem
    """)

if __name__ == "__main__":
    main()
#%%
