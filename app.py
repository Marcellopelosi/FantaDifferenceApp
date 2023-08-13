import streamlit as st
import pandas as pd

# Define the Streamlit app
def main():
    st.title("DataFrame Difference Viewer")

    # Upload the CSV files
    st.sidebar.header("Upload DataFrames")
    uploaded_file1 = st.sidebar.file_uploader("Upload CSV file for DataFrame 1", type=["csv"])
    uploaded_file2 = st.sidebar.file_uploader("Upload CSV file for DataFrame 2", type=["csv"])

    if uploaded_file1 and uploaded_file2:
        # Load DataFrames from uploaded files
        df1 = pd.read_csv(uploaded_file1)
        df2 = pd.read_csv(uploaded_file2)

        # Calculate the difference between DataFrames
        df_diff = df1.merge(df2, how='outer', indicator=True).loc[lambda x: x['_merge'] != 'both']

        # Display the original DataFrames
        st.subheader("DataFrame 1:")
        st.write(df1)

        st.subheader("DataFrame 2:")
        st.write(df2)

        # Display the differences
        st.subheader("Differences:")
        st.write(df_diff)

if __name__ == '__main__':
    main()
