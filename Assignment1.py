# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 23:33:22 2021

@author: JMada
"""
import streamlit as st
from random import randint
from sklearn.linear_model import LinearRegression

st.title('Simple Streamlit App for linear Regression')
st.markdown("This model was trained on data that fit the equation: x1 + 2*x2 + 3*x3.")
st.markdown("However, we want to see if the model can learn from this pattern and predict the correct outcome.")
#comment test

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)
    
    


predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

st.text('Type any three whole numbers in the boxes below')
n1 = st.number_input('Number 1', step=1)
n2 = st.number_input('Number 2', step=1)
n3 = st.number_input('Number 3', step=1)

X_TEST = [[n1, n2, n3]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

st.write('Outcome : {}'.format(outcome))