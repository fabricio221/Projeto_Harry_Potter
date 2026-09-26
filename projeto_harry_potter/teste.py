import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"
st.set_page_config(layout='wide')
# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()
print(dados[0]['name'])
# Pega apenas os nomes dos personagens , a partir de uma lista vazia
nomes = []
for personagem in dados:
     nomes.append(personagem['name'])


  # ordena os nomes em ordem alfabetica
nomes.sort()

   # Título do app
st.title('busca bruxo - o lugar onde encontrara todas as informaçoesdos bruxos')

# Sidebar com a lista de nomes
nome_escolhido = st.selectbox('escolha um bruxo,nomes')

# Procura o personagem escolhido na lista de dados
for p in dados:
    if p['name'] == nome_escolhido:
       persoangem = p
    break    

# Mostra o nome do personagem
st.header(f'nome de {personagem['name']}')

# ===== IMAGEM EM DESTAQUE =====
# Verifica se o personagem tem imagem


# Linha divisória

 