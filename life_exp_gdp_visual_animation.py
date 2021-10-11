#import modules
import plotly.express as px
import streamlit as st

#import the data available in plotly.express
gapminder_df = px.data.gapminder()

animation_title = '<p style="font-family:Arial Bold; color:royalblue; font-size: 30px;"> Animated Data Visualization</p>'
sub_title1 = '<p style="font-family:Arial Bold Italic; color:royalblue; font-size: 20px;">This animation shows world life expectancy and wealth (GDP per capita) evolution from 1952 to 2007</p>'
sub_title2 = '<p style="font-family:Arial Bold Italic; color:royalblue; font-size: 15px;">Source: https://www.gapminder.org/data/</p>'
sub_title3 = '<p style="font-family:Arial Bold Italic; color:royalblue; font-size: 10px;">Author: Reda Merzouki, https://www.linkedin.com/in/reda-merzouki-02843b/</p>' 
st.set_page_config(layout='wide')
st.markdown(animation_title, unsafe_allow_html=True)
st.markdown(sub_title1, unsafe_allow_html=True)
st.markdown(sub_title2, unsafe_allow_html=True)
st.markdown(sub_title3, unsafe_allow_html=True)

# Animation year by year basis

animation = px.scatter(data_frame=gapminder_df,
          x= 'gdpPercap',
          y = 'lifeExp',
          size= 'pop',
          color = 'continent',
          title = 'World Life Expectancy and Wealth 1952 - 2007',
          labels = {'gdpPercap': 'Wealth', 
                   'lifeExp' : 'Life expectancy'},
          log_x = True,
          range_y = [20,95],
          hover_name = 'country',
          animation_frame='year',
          height=650,          
          size_max=100)

st.plotly_chart(animation, use_container_width=True)
