import streamlit as st 
from stageOne import StageOne
from stageTwo import StageTwo
from stageThree import StageThree
from fillTypes import fillTypes
from preview import Preview
import pandas as pd
import ast


def createCheckbox(c, word, wordKeys,i):
    if c % 5 == 0:
        with col1:
            st.checkbox(word, key=wordKeys[f"{i}"])
            st.session_state.keys_selected.append(i)
    elif c % 5 == 1:
        with col2:
            st.checkbox(word, key=wordKeys[f"{i}"])
            st.session_state.keys_selected.append(i)
    elif c % 5 == 2:
        with col3:
            st.checkbox(word, key=wordKeys[f"{i}"])
            st.session_state.keys_selected.append(i)
    elif c % 5 == 3:
        with col4:
            st.checkbox(word, key=wordKeys[f"{i}"])
            st.session_state.keys_selected.append(i)
    else:
        with col5:
            st.checkbox(word, key=wordKeys[f"{i}"])
            st.session_state.keys_selected.append(i)

st.set_page_config(layout='wide')

# "st.session_state object:", st.session_state  


st.session_state.keys_selected = []

if 'page' not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1


def page_three():
    result = ''
    gap_list = []
    this_words = st.session_state.words
    counter = 0
    nextIdx = 0
    for i in range(len(st.session_state.words)):
        if f'{i}' in st.session_state and st.session_state[f'{i}']:
            result += ' ' + "_"*10
            gap_list.append(this_words[i])
        else:
            result += " " + this_words[i]
        if counter == st.session_state.newLines[nextIdx]-1:
            result += "\n"
            nextIdx += 1
            counter = 0
        else:
            counter += 1  

    df = pd.read_csv("gaps.csv") 
    row = {
        'result': result,
        'gap': gap_list
    }   
    df.loc[0] = row
    df.to_csv("gaps.csv")
    st.session_state.page += 1



if st.session_state.page == 0:
    stage1 = StageOne()
    stage1.render()
    title = st.text_input("title")
    text = st.text_area("text")
    st.session_state.title = title 
    st.session_state.text = text 
    st.button("Next", on_click=next_page)


elif st.session_state['page'] == 1:     

    title = st.session_state['title']
    stage2 = StageTwo()
    stage2.render()


    words = []
    for i in st.session_state['text'].split(" "):
        words.extend(i.split("\n"))

    st.session_state.words = words

    words = st.session_state.words
    wordKeys = {}
    for i in range(len(words)):
        wordKeys[f"{i}"] = i

    paras = st.session_state['text'].split("\n")
    newLines = [len(i.split(" ")) for i in paras]
    st.session_state.newLines = newLines


    c = 0
    counter = 0
    newLineIdx = 0
    col1, col2, col3, col4, col5 = st.columns(5)

    for i in range(len(words)):
        word = words[i]
        counter += 1 
        if counter == newLines[newLineIdx]:
            st.write("&NewLine;", unsafe_allow_html=True)
            newLineIdx += 1
            counter = 0 
            createCheckbox(c, word, wordKeys, i)
            c = 0
            container = st.container()  
            col1, col2, col3, col4, col5 = container.columns(5)
            
        else:
            createCheckbox(c, word, wordKeys, i)

            c += 1


    st.button("previous", on_click=prev_page)
    st.button("next", on_click=page_three)



elif st.session_state['page'] == 2:

    df = pd.read_csv("gaps.csv").tail(1)
    content = df['result'].iloc[0]
    content = " <br/>".join(content.split("\n"))

    gap_list = ast.literal_eval(df['gap'].iloc[0])


    result = ''

    
    gaps = ' '.join(gap_list)

    stage3 = StageThree()
    stage3.render()
    options = st.selectbox(label='select', options=['Show words', "Don't show words", "Show only first letter", "Show only spaces", "Show spaces along with first letter", "No vowels", "No consonents", "Anagrams (Show random letters)", "Inline", "Box and Bounded"])

    st.write("Settings and preview")

    ft = fillTypes()
    result, gapper = ft.fill(options, content, gap_list, gaps)

    




    title = st.session_state.title
    if len(gapper) > 0:
        st.markdown(gapper)
    st.markdown(result, unsafe_allow_html=True)
    

    st.session_state.report_text = result
    st.session_state.report_gaps = gapper
    st.button("Previous", on_click=prev_page)
    st.button("Preview", on_click=next_page)

if st.session_state['page'] == 3:
    preview = Preview()
    Preview.render(st.session_state.title, st.session_state.report_text, st.session_state.report_gaps)
    st.write("&NewLine; &NewLine; &NewLine;", unsafe_allow_html=True)
    st.button("Previous", on_click=prev_page)