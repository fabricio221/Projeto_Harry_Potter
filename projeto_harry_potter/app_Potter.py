import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"

# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()

# Pega apenas os nomes dos personagens , a partir de uma lista vazia
nomes = []
for personagem in dados:
     nomes.append(personagem['name'])

    
# Ordena os nomes em ordem alfabética
nomes.sort()

# Título do app
st.title('busca bruxo - o lugar onde encontrara todas as informaçoesdos bruxos')

# Sidebar com a lista de nomes
nome_escolhido = st.selectbox('escolha um bruxo',nomes)

# Procura o personagem escolhido na lista de dados
for p in dados:
    if p['name'] == nome_escolhido:
       persoangem = p
    break    

# Mostra o nome do personagem
st.header(f'nome de {personagem['name']}')

# ===== IMAGEM EM DESTAQUE =====
# Verifica se o personagem tem imagem
if persoangem['imagem'] and persoangem !="":
    st.image(personagem,['image'], width=300)
else:
    st.write("este personagem nao possui imagm")

# Linha divisória
st.divider()

# Informações principais
st.write(f"**Casa:**{personagem['house']}")
st.write(f"**Especie:**{personagem['house']}")
st.write(f"**genero**{personagem}[gender] :")
st.write(f"**data de nascimento:**{personagem['date0fbirth']}")
st.write(f"**data de nascimento:**{persoangem[year0fbirth]}")

# Informações da varinha
st.write("**Varinha:**")
st.write(f"- Madeira: {personagem['wand']['wood']}")
st.write(f"- Núcleo: {personagem['wand']['core']}")
st.write(f"- Tamanho: {personagem['wand']['length']} polegadas")


st.write(f"**Patrono:** {personagem['patronus']}")
st.write(f"**Ator/Atriz:** {personagem['actor']}")




# Mostra se está vivo
