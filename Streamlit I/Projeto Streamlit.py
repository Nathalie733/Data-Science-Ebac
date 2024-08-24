import pandas as pd
import streamlit as st
from streamlit_player import st_player
import numpy as np

st.set_page_config(page_title = 'Vencedores do Oscar',
                    page_icon='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkH-mOOTeLMRJCVt26I-_6YP5IgtUebS47ODBbPr76pA&s',
                    layout='wide')

st.title(':red[Vencedores do Oscar]')
st.header('Vamos ver os vencedores do oscar de acordo com ano, filme e categoria!')
st.subheader('Fique atento ao seus artistas favoritos!', divider='rainbow')
st.subheader('Apenas os :blue[melhores] :sunglasses:')

oscar = pd.read_csv(r'C:\Users\natha\Downloads\Streamlit I\the_oscar_award.csv')

df = pd.DataFrame(oscar)

st.dataframe(df)

st.write("Quer saber mais sobre a premiação do ano passado? Assista o vídeo abaixo:")
st_player('https://www.youtube.com/watch?v=wkk22Dq88ME')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Meryl Streep")
   st.image("https://i.pinimg.com/474x/e6/e4/61/e6e4618271bad7621ded01c46b064069.jpg")
   st.write("A atriz mais indicada ao Oscar de Melhor Atriz.")
with col2:
   st.header("Steven Spielberg")
   st.image("https://static01.nyt.com/images/2022/03/23/arts/20director-history2/merlin_204015957_8bdebc27-d40b-4051-954e-ecaf9eb9c605-articleLarge.jpg?quality=75&auto=webp&disable=upscale")
   st.write("Um dos diretores mais respeitados do cinema.")
with col3:
   st.header("Viola Davis")
   st.image("https://people.com/thmb/ZyfOtoBjwJmOOsPFcCVSt3kgiuk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(818x0:820x2)/viola-davis17-ac741a954765417390a8d5f3516a1ec8.jpg")
   st.write("Uma das poucas atrizes negras a ganhar o Oscar de Melhor Atriz Coadjuvante.")


genre = st.radio(
    "Qual é o seu gênero favorito?",
    [":rainbow[Comédia]", "***Drama***", "Documentário :movie_camera:", "Comédia Romântica"],
    captions = ['"Segura Meu Poodle!"', '"Stellaaaa!"', '"⁠A tecnologia deixou de ter o papel de ferramenta para se tornar um vício e um meio de manipulação."', '"Não se esqueça. Eu sou apenas uma garota, parada na frente de um rapaz pedindo a ele que a ame!"'])

if genre == ':rainbow[Comédia]':
    st.write('Nada melhor do que algo que te faz rir.')
elif genre == '***Drama***':
    st.write("Já pega os lenços!")
elif genre == 'Comédia Romântica':
    st.write("Para deixar o coração quentinho...")
else:
    st.write("Ótima escolha!")

option = st.selectbox(
   'Quer receber mais atualizações ou fazer sugestões? Como gostaria de ser contactado?',
   ('Email', 'SMS', 'Celular'))

st.write('Você selecionou:', option)

st.subheader('**:yellow[Obrigada por acompanhar meu projeto!]** :coffee:')