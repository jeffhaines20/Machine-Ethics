from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch 
import pandas as pd
import numpy as np
import streamlit as st
from transformers import pipeline
from transformers_interpret import SequenceClassificationExplainer
from transformers import AutoModelForSequenceClassification, AutoTokenizer

st.title('Ethics Classifier')
st.write('This app uses a pre-trained Distilbert model fine-tuned on the Commonsense Ethics dataset from the Aligning AI With Shared Human Values project (https://github.com/hendrycks/ethics). It judges whether a given action of scenario is wrong or not wrong and shows how the words in the scenario affected the judgment.')

loaded_model = DistilBertForSequenceClassification.from_pretrained('commonsense_ethics')
model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
cls_explainer = SequenceClassificationExplainer(loaded_model, tokenizer)

clf = pipeline("text-classification", model = loaded_model, tokenizer = tokenizer)

text = st.text_input('Enter a scenario or action.')

if text:
    answer = clf(text)
    label = 'wrong' if answer[0]['label'] == 'LABEL_1' else 'not wrong'
    st.write(f'This action is {label} (confidence level {answer[0]["score"]*100:.2f}%).')
    attributions = cls_explainer(text)
    df = pd.DataFrame(attributions[1:-1])
    df.rename(columns = {0: 'Token', 1: 'Contribution'}, inplace = True)
    st.write(df.style.hide(axis = 'index'))
    st.write(cls_explainer.visualize())
