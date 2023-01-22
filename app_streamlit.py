# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
from pycaret.regression import predict_model, load_model
from pycaret.classification import predict_model, load_model

# Este código cria uma lista de páginas disponíveis para navegação em uma aplicação WEB criada com o framework Streamlit. 
# Ele também cria um widget de seleção de página no sidebar, permitindo que o usuário navegue entre as páginas.

# Iniciando a lista de páginas disponíveis
paginas = ['Home', 'Widgets Streamlit', 'Modelo Custos', 'Modelo Fumante', 'Modelo Churn']

# Criando um widget para seleção de página no sidebar
pagina = st.sidebar.radio('Navegue por aqui', paginas)

# Quando a página "Home" é selecionada, um título é exibido na página e uma instrução para navegação no sidebar é exibida.

# Verifica se a página acessada é "Home"
if pagina == 'Home':
    # Exibindo título na página
    st.title('Meus Modelos em Produção :gem:')
    # Exibindo instrução para navegação no sidebar
    st.write('Navegue pelo meno na barra lateral para escolher entre os modelos disponíveis nessa aplicação WEB')


# O código abaixo apresenta os principais widgets interativos do Streamlit. 
# Cada widget é criado com rótulos e textos de ajuda específicos e possui verificações 
# para que possa ser exibida uma mensagem ou realizada uma ação quando o usuário interagir com eles.

# Verifica se a página acessada é "Widgets Streamlit"
if pagina == 'Widgets Streamlit':
    # Título da página
    st.title('Principais Widgets Interativos do Streamlit')

    # Cabeçalho "Botões"
    st.markdown('## Botões')

    # Exibe código para criação de botão
    st.code("st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali')")

    # Cria um botão com o rótulo "-> Clique aqui! <-" e texto de ajuda "É só clicar ali"
    botao = st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali')

    # Verifica se o botão foi pressionado
    if botao:
        # Exibe mensagem "Você apertou o botão. Parabéns"
        st.write('Você apertou o botão. Parabéns')

    # Cabeçalho "Caixa de Seleção"
    st.markdown('## Caixa de Seleção')

    # Exibe código para criação de caixa de seleção
    st.code("check = st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')")

    # Cria uma caixa de seleção com o rótulo "Clique para me selecionar" e texto de ajuda "Clique e desclique quando quiser"
    check = st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')

    # Verifica se a caixa de seleção foi selecionada
    if check:
        # Exibe mensagem "Você apertou o botão. Parabéns!"
        st.write('Você apertou o botão. Parabéns!')
    else:
        # Exibe mensagem "Você vai partar o botão acima? "
        st.write('Você vai partar o botão acima? ')

    # Cabeçalho "Botões de Rádio"
    st.markdown('## Botões de Rádio')

    # Exibe código para criação de botões de rádio
    st.code("st.radio('Botões de Rádio', options = [100, 'Python', print, [1, 2, 3]], index = 1, help = 'Ajuda')")

    # Cria botões de rádio com o rótulo "Botões de Rádio", opções [100, 'Python',print, [1, 2, 3]], seleção inicial no índice 1 e texto de ajuda "Ajuda"
    radio = st.radio('Botões de Rádio', options = [100, 'Python', print, [1, 2, 3]], index = 1, help = 'Ajuda')

    # Cabeçalho "Caixas de Seleção Múltipla"
    st.markdown('## Caixas de Seleção Múltipla')

    # Exibe código para criação de caixas de seleção múltipla
    st.code("st.multiselect('Selecione quantas opções desejar', options = ['A', 'B', 'C', 'D', 'E'])")

    # Cria caixas de seleção múltipla com o rótulo "Selecione quantas opções desejar" e opções ['A', 'B', 'C', 'D', 'E']
    selecao = st.multiselect('Selecione quantas opções desejar', options = ['A', 'B', 'C', 'D', 'E'])

    # Cabeçalho "Slider"
    st.markdown('## Slider')

    # Exibe código para criação de slider
    st.code("st.slider('Entrada numérica', min_value = 1, max_value = 25, value = 7, step = 2)")

    # Cria um slider com o rótulo "Entrada numérica", valor mínimo 1, valor máximo 100, valor inicial 15 e passo 1
    numero_slider = st.slider('Entrada numérica', min_value = 1, max_value = 100, value = 15, step = 1)

    # Exibe o título com o resultado do quadrado do número selecionado no slider
    st.title(f'O quadrado de {numero_slider} é {numero_slider**2}')

    # Cabeçalho "Inputs"
    st.markdown('## Inputs')

    # Exibe mensagem "Input de texto"
    st.write('Input de texto')

    # Exibe código para criação de input de texto
    st.code("st.text_input('Digite um texto aqui!')")

    # Cria um input de texto com o rótulo "Digite um texto aqui!"
    input_text = st.text_input('Digite um texto aqui!')

    # Verifica se o input de texto não está vazio
    if input_text != '':
        # Exibe o texto digitado com formatação em negrito
        st.write(f'**{input_text}**')

    # Exibe mensagem "Input de Data"
    st.write('Input de Data')

    # Exibe código para criação de input de data
    st.code("st.date_input('Selecione uma data')")

    # Cria um input de data com o rótulo "Selecione uma data"
    input_date = st.date_input('Selecione uma data')

    # Verifica se o input de data não está vazio
    if input_date != '':
        # Exibe a data selecionada com formatação em negrito
        st.write(f'**Data selecionada: {input_date}**')

    # Exibe mensagem "Input numérico"
    st.write('Input numérico')

    # Exibe código para criação de input numérico
    st.code("st.number_input('Selecione um número')")

    # Cria um input numérico com o rótulo "Selecione um número"
    input_numero = st.number_input('Selecione um número')

    # Verifica se o input numérico não está vazio
    if input_numero != '':
        # Exibe o número selecionado com formatação em negrito
        st.write(f'**Número selecionado: {input_numero}**')


# Este código cria uma página para a previsão de custos de seguro usando um modelo de regressão. 
# Ele cria campos de entrada para os usuários inserirem informações relevantes, 
# como idade, índice de massa corporal, se é fumante, região, sexo e número de dependentes. 
# Esses dados são então convertidos em um dicionário de dados e passados para o modelo, que é carregado a partir de um arquivo salvo. 
# O usuário pode então clicar em um botão para executar o modelo e exibir a previsão de custo do seguro.

# Verifica se a página acessada é "Modelo Custos"
if pagina == 'Modelo Custos':
    # Exibindo título da página
    st.title('Modelo para Previsão de Custos de Seguro')
    
    # Criando campos de entrada para idade, índice de massa corporal, fumante, região, sexo e número de dependentes
    idade = st.number_input('Idade', 18, 65, 30)
    imc = st.number_input('Índice de Massa Corporal', 15, 54, 24)
    fumante = st.selectbox('É fumante?', ['Sim', 'Não'])
    regiao = st.selectbox('Em que região mora?', ['southeast', 'southwest', 'northeast', 'northwest'])
    sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    criancas = st.selectbox('Quantidade de dependentes', [0, 1, 2, 3, 4, 5])

    # Alterando o sexo para o formato aceito pelo modelo
    sexo_modelo = 'male' if sexo == 'Masculino' else 'famale'

    # Criando um dicionário de dados a partir das entradas do usuário
    dados0 = {'age': [idade], 'sex': [sexo_modelo], 'bmi': [imc], 'children': [criancas], 'smoker': [fumante], 'region': [regiao]}
    dados = pd.DataFrame(dados0)

    # Adicionando uma linha horizontal na página
    st.markdown('---')

    # Carregando o modelo salvo
    modelo = load_model('modelo_regressao_insurance_charges')

    # Criando um botão para executar o modelo
    if st.button('Executar Modelo'):
        # Utilizando o modelo para prever o custo de seguro
        pred = float(predict_model(modelo, data = dados)['Label'].round(2))
        saida = f'O previsto para o Custo de Seguro é de $ {pred}'
        # Exibindo a previsão na página
        st.subheader(saida)


# Este código cria uma página para a previsão de possíveis fraudadores, usando um modelo de classificação. 
# Ele cria campos de entrada para os usuários inserirem informações relevantes, 
# como idade, índice de massa corporal, custo do seguro, região, sexo e número de dependentes. 
# Esses dados são então convertidos em um dicionário de dados e passados para o modelo, que é carregado a partir de um arquivo salvo.
# O usuário pode então clicar em um botão para executar o modelo e exibir a previsão de possível fraude.

# Verifica se a página acessada é "Modelo Fumante"
if pagina == 'Modelo Fumante':
    # Exibindo título da página
    st.title('Modelos para Previsão de Possíveis Fraudadores')

    # Criando campos de entrada para idade, índice de massa corporal, custo do seguro, região, sexo e número de dependentes
    idade = st.number_input('Idade', 18, 65, 30)
    imc = st.number_input('Índice de Massa Corporal', 15, 54, 24)
    custos = st.slider('Informe o Custo do Seguro', 1000, 50000, 10000, 1000)
    regiao = st.selectbox('Em que região mora?', ['southeast', 'southwest', 'northeast', 'northwest'])
    sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    criancas = st.selectbox('Quantidade de dependentes', [0, 1, 2, 3, 4, 5])

    # Alterando o sexo para o formato aceito pelo modelo
    sexo_modelo = 'male' if sexo == 'Masculino' else 'famale'

    # Criando um dicionário de dados a partir das entradas do usuário
    dados0 = {'age': [idade], 'sex': [sexo_modelo], 'bmi': [imc], 'children': [criancas], 'charges': [custos], 'region': [regiao]}
    dados = pd.DataFrame(dados0)

    # Adicionando uma linha horizontal na página
    st.markdown('---')

    # Carregando o modelo salvo
    modelo = load_model('modelo_classificacao_insurance_smoker')

    # Criando um botão para executar o modelo
    if st.button('Executar Modelo'):
        # Utilizando o modelo para prever se é fumante
        pred = predict_model(modelo, data = dados)['Label'][0]
        # Verificando se é fumante
        saida = 'Ele não é fumante' if pred == 'no' else 'É um possível fumante'
        # Exibindo a previsão na página
        st.write(saida)


# Verifica se a página acessada é "Modelo Churn"
if pagina == 'Modelo Churn':
    # Exibindo título da página
    st.title('Modelos de Churn Bancário')