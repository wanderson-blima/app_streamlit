import streamlit as st
import pandas as pd
from pycaret.regression import predict_model, load_model
from pycaret.classification import predict_model, load_model

paginas = ['Home', 'Widgets Streamlit', 'Modelo Custos', 'Modelo Fumante', 'Modelo Churn']

pagina = st.sidebar.radio('Navegue por aqui', paginas)


if pagina == 'Home':
    st.title('Meus Modelos em Produção :gem:')
    st.write('Navegue pelo meno na barra lateral para escolher entre os modelos disponíveis nessa aplicação WEB')

if pagina == 'Widgets Streamlit':
    st.title('Principais Widgets Interativos do Streamlit')

    st.markdown('## Botões')

    st.code("st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali')")
    botao = st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali')

    if botao:
        st.write('Você apertou o botão. Parabéns')

    st.markdown('## Caixa de Seleção')
    st.code("check = st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')")
    check = st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')

    if check:
        st.write('Você apertou o botão. Parabéns!')
    else:
        st.write('Você vai partar o botão acima? ')

    st.markdown('## Botões de Rádio')
    st.code("st.radio('Botões de Rádio', options = [100, 'Python', print, [1, 2, 3]], index = 1, help = 'Ajuda')")

    radio = st.radio('Botões de Rádio', options = [100, 'Python', print, [1, 2, 3]], index = 1, help = 'Ajuda')

    st.markdown('## Caixas de Seleção Múltipla')
    st.code("st.multiselect('Selecione quantas opções desejar', options = ['A', 'B', 'C', 'D', 'E'])")

    selecao = st.multiselect('Selecione quantas opções desejar', options = ['A', 'B', 'C', 'D', 'E'])

    st.markdown('## Slider')
    st.code("st.slider('Entrada numérica', min_value = 1, max_value = 25, value = 7, step = 2)")

    numero_slider = st.slider('Entrada numérica', min_value = 1, max_value = 100, value = 15, step = 1)

    st.title(f'O quadrado de {numero_slider} é {numero_slider**2}')

    st.markdown('## Inputs')

    st.write('Input de texto')
    st.code("st.text_input('Digite um texto aqui!')")
    input_text = st.text_input('Digite um texto aqui!')

    if input_text != '':
        st.write(f'**{input_text}**')

    st.write('Input de Data')
    st.code("st.date_input('Selecione uma data')")
    input_date = st.date_input('Selecione uma data')

    if input_date != '':
        st.write(f'**Data selecionada: {input_date}**')

    st.write('Input numérico')
    st.code("st.number_input('Selecione um número')")
    input_numero = st.number_input('Selecione um número')

    if input_numero != '':
        st.write(f'**Número selecionado: {input_numero}**')


if pagina == 'Modelo Custos':
    st.title('Modelo para Previsão de Custos de Seguro')

    idade = st.number_input('Idade', 18, 65, 30)
    imc = st.number_input('Índice de Massa Corporal', 15, 54, 24)
    fumante = st.selectbox('É fumante?', ['Sim', 'Não'])
    regiao = st.selectbox('Em que região mora?', ['southeast', 'southwest', 'northeast', 'northwest'])
    sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    criancas = st.selectbox('Quantidade de dependentes', [0, 1, 2, 3, 4, 5])

    sexo_modelo = 'male' if sexo == 'Masculino' else 'famale'

    dados0 = {'age': [idade], 'sex': [sexo_modelo], 'bmi': [imc], 'children': [criancas], 'smoker': [fumante], 'region': [regiao]}
    dados = pd.DataFrame(dados0)

    st.markdown('---')

    modelo = load_model('modelo_regressao_insurance_charges')

    if st.button('Executar Modelo'):
        pred = float(predict_model(modelo, data = dados)['Label'].round(2))
        saida = f'O previsto para o Custo de Seguro é de $ {pred}'
        st.subheader(saida)


if pagina == 'Modelo Fumante':
    st.title('Modelos para Previsão de Possíveis Fraudadores')

    idade = st.number_input('Idade', 18, 65, 30)
    imc = st.number_input('Índice de Massa Corporal', 15, 54, 24)
    custos = st.slider('Informe o Custo do Seguro', 1000, 50000, 10000, 1000)
    regiao = st.selectbox('Em que região mora?', ['southeast', 'southwest', 'northeast', 'northwest'])
    sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    criancas = st.selectbox('Quantidade de dependentes', [0, 1, 2, 3, 4, 5])

    sexo_modelo = 'male' if sexo == 'Masculino' else 'famale'

    dados0 = {'age': [idade], 'sex': [sexo_modelo], 'bmi': [imc], 'children': [criancas], 'charges': [custos], 'region': [regiao]}
    dados = pd.DataFrame(dados0)

    st.markdown('---')

    modelo = load_model('modelo_classificacao_insurance_smoker')

    if st.button('Executar Modelo'):
        pred = predict_model(modelo, data = dados)['Label'][0]
        saida = 'Ele não é fumante' if pred == 'no' else 'É um possível fumante'
        st.write(saida)


if pagina == 'Modelo Churn':
    st.title('Modelos de Churn Bancário')