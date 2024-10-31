import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',
                  page_title = 'dashboard')

tab1, tab2, tab3 = st.tabs(['descriptive statistics', 'numerical charts', 'categorical chart'])

df = pd.read_csv(r"C:\Users\A80843\OneDrive - Arrow Electronics, Inc\Documents\Local_Disk_D\PythonProjects\Scrapping_propertyfinder\apartments_updated.csv")
box = st.sidebar.checkbox('show data', False ,key =1)
num = df.describe()
cat = df.describe(include="O")



if box:
    st.header('sample data')
    st.dataframe(df.head(10))

with tab1:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader('categorical descriptive statistics')
        st.dataframe(cat)
        
    with col3:
        st.subheader('numerical descriptive statistics')
        st.dataframe(num)
with tab2:
    area = st.sidebar.selectbox('select area',df['area'].unique())
    price = st.sidebar.selectbox('select address',df['Price'].unique())
    col1,col2,col3 = st.columns(3)
    with col1:
        new_df = df[df['area'] == area]
        fig = px.histogram(new_df, x ='Price', color = 'bedrooms', title = f'price for {area} area'.title())
        st.plotly_chart(fig,use_container_width=True)
        fig = px.histogram(new_df, x ='bedrooms', color = 'area', title = f'bedrooms for {area} area'.title())
        st.plotly_chart(fig,use_container_width=True)
        new_df1 = df[df['Price'] == price]
        fig = px.scatter(new_df1, x= 'bedrooms', y='area', color = 'Price', title = f'correlation between bedrooms and area {price}'.title())
        st.plotly_chart(fig,use_container_width=True)
        
with tab3:
    address = st.sidebar.selectbox('select address',df['address'].unique())
    bedrooms = st.sidebar.selectbox('select number of bedrooms',df['bedrooms'].unique())
    col1,col2,col3 = st.columns(3)
    with col1:
        df_new2 = df[df['address'] == address]
        fig = px.box(df_new2, x= 'address', y= 'Price',color='advantage', title = f'box plot for each {address} with advantage'.title())
        st.plotly_chart(fig,use_container_width=True)
        df_new3 = df[df['bedrooms'] == bedrooms]
    with col3:
        fig = px.bar(df_new3, x = 'Price', y = 'area', color = 'bedrooms', barmode = 'group', title = f'price and area for {bedrooms}bedrooms'.title())
        st.plotly_chart(fig,use_container_width = True)
