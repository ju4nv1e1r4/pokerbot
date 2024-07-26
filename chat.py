from openai import OpenAI
import pandas as pd
import streamlit as st
from config import info

client = OpenAI(api_key=info.api_key)

system_message = '''
Seu nome é André e você é um jogador de poker profissional que leciona poker para pessoas que nunca jogaram antes.

Nota :
O seu método de ensino é baseado em passo a passo, cuidadosamente explicado e ensina com uma excelente didática,
dando exemplos quando possível, praticando jogadas e ensinando também o que não fazer em uma mesa de poker.

Obs: Comportamentos ofensivos, racistas, homofóbicos e afins serão proibidos.
'''

def get_response(client, model, system_message, user_message, max_tokens=1000, temperature=0.8, seed=1):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': user_message}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        seed=seed
    )
    return response.choices[0].message.content

st.markdown('### :blue[Olá, me chamo André estou aqui para te ensinar a jogar poker. Vamos começar?] :black_joker:')

with st.form('my_form'):
    text = st.text_area('Digite aqui: ')
    submitted = st.form_submit_button('Enter')
    if submitted:
        user_message = text
        response_text = get_response(client, 'gpt-3.5-turbo', system_message, user_message)
        st.write(response_text)

    

