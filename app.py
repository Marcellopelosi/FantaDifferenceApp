import streamlit as st
import pandas as pd

# Load your DataFrames here (replace with actual file paths or data loading methods)
df1 = pd.read_csv('path_to_df1.csv')
df2 = pd.read_csv('path_to_df2.csv')

# Calculate the difference between DataFrames
df_diff = df1.merge(df2, how='outer', indicator=True).loc[lambda x : x['_merge']!='both']

# Define the Streamlit app
def main():
    st.title("Fanta app: differenza tra listoni")
    
    # Display the original DataFrames
    st.subheader("listone vecchio:")
    st.write(df1)

    st.subheader("listone nuovo:")
    st.write(df2)

    # Display the differences
    st.subheader("Differenze:")
    st.write(df_diff)

if __name__ == '__main__':
    main()
