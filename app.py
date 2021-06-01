# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:41:51 2021

@author: Saurav
"""
import streamlit as st
import pickle
model = pickle.load(open('rf_crop_prediction.pkl', 'rb'))
st.markdown('<style>body{text-align:center;background-color:#66FF99;align-items:center;display:flex;flex-direction:column;}</style>', unsafe_allow_html=True)
st.title("Crop preidction")
st.sidebar.title("Crop preidction")
st.sidebar.image("ezgif.com-gif-maker (1).gif")
st.sidebar.markdown("made by souravsing 💖")
N = st.text_input("nitrogen level")
P = st.text_input("Phosphoorous")
K = st.text_input("potassium")
temperature = st.text_input("temprature")
humidity = st.text_input("humidity")
ph = st.text_input("ph")
rainfall = st.text_input("rainfall")
if st.button("predict"):
    prediction=model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
    prediction=int(prediction)
    if prediction==1:
        prediction="rice"
    elif prediction==2:
        prediction="maize"
    elif prediction==3:
        prediction="chickpea"
    elif prediction==4:
        prediction="kidneybeans"
    elif prediction==5:
        prediction="pigeonpeas"
    elif prediction==6:
        prediction="mothbeans"
    elif prediction==7:
        prediction="mungbean"
    elif prediction==8:
        prediction="blackgram"
    elif prediction==9:
        prediction="lentil"
    elif prediction==10:
        prediction="pomegranate"
    elif prediction==11:
        prediction="banana"
    elif prediction==12:
        prediction="mango"
    elif prediction==13:
        prediction="grapes"
    elif prediction==14:
        prediction="watermelon"
    elif prediction==15:
        prediction="apple"
    elif prediction==16:
        prediction="papaya  "
    elif prediction==17:
        prediction="coconut"
    elif prediction==18:
        prediction="cotton"
    elif prediction==19:
        prediction="maize"
    elif prediction==20:
        prediction="jute"
    elif prediction==21:
        prediction="coffee"
    elif prediction==22:
        prediction="muskmelon"
    st.success("you should take {} crop".format(prediction))
