import streamlit as st

# streamlit ui
st.title('power calculator')
st.write('enter the number that u want to calculate its square,cube,and fifth power')

# get user input
n=st.number_input('enter an integer',value=1,step=1)

# calulator result
square= n**2
cube=n**3
fifth_power=n**5

#display the result 
st.write(f'the square of {n} is :{square}')
st.write(f'the cube of {n} is : {cube}')
st.write(f'The fifth power of {n} is :{fifth_power}')



