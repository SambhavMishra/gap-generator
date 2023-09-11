import streamlit as st 
from stageOne import StageOne
from stageTwo import StageTwo
from stageThree import StageThree
import pandas as pd
import ast
from preview import Preview


# "st.session_state object:", st.session_state  
st.session_state.keys_selected = []

if 'page' not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1


def page_three():
    result = ''
    gap_list = []
    this_words = st.session_state.words
    for i in range(len(st.session_state.words)):
        if f'{i}' in st.session_state and st.session_state[f'{i}']:
            result += ' ' + "_"*10
            gap_list.append(this_words[i])
        else:
            result += " " + this_words[i]

    df = pd.read_csv("gaps.csv") 
    row = {
        'result': result,
        'gap': gap_list
    }   
    df.loc[df.index.max() + 1] = row
    df.to_csv("gaps.csv")
    st.session_state.page += 1


def prev_page():
    st.session_state.page -= 1


if st.session_state.page == 0:
    stage1 = StageOne()
    stage1.render()
    title = st.text_input("title")
    text = st.text_area("text")
    st.session_state.title = title 
    st.session_state.text = text 
    st.button("Next", on_click=next_page)


elif st.session_state['page'] == 1: 

    st.session_state.words = st.session_state['text'].split(" ")

    title = st.session_state['title']
    stage2 = StageTwo()
    stage2.render()

    words = st.session_state.words
    wordKeys = {}
    for i in range(len(words)):
        wordKeys[words[i]+f"{i}"] = i

    words = st.session_state['text'].split(" ")


    c = 0
    col1, col2, col3, col4, col5 = st.columns(5)

    for i in range(len(words)):
        word = words[i]

        if c % 5 == 0:
            with col1:
                st.checkbox(word, key=wordKeys[word+f"{i}"])
                st.session_state.keys_selected.append(i)
        elif c % 5 == 1:
            with col2:
                st.checkbox(word, key= wordKeys[word+f"{i}"])
                st.session_state.keys_selected.append(i)
        elif c % 5 == 2:
            with col3:
                st.checkbox(word, key=wordKeys[word+f"{i}"]) 
                st.session_state.keys_selected.append(i)
        elif c % 5 == 3:
            with col4:
                st.checkbox(word, key = wordKeys[word+f"{i}"])
                st.session_state.keys_selected.append(i)
        else:
            with col5:
                st.checkbox(word, key= wordKeys[word+f"{i}"])
                st.session_state.keys_selected.append(i)

        c += 1


    st.button("previous", on_click=prev_page)
    st.button("next", on_click=page_three)



elif st.session_state['page'] == 2:

    df = pd.read_csv("gaps.csv").tail(1)
    content = df['result'].iloc[0]
    gap_list = ast.literal_eval(df['gap'].iloc[0])

    result = ''

    
    gaps = ' '.join(gap_list)

    stage3 = StageThree()
    stage3.render()
    options = st.selectbox(label='select', options=['Show words', "Don't show words", "Show only first letter", "Show only spaces", "Show spaces along with first letter", "No vowels", "No consonents", "Anagrams (Show random letters)", "Inline"])

    st.write("Settings and preview")

    gapper = []
    if options == 'Show words':
        result = content + "&NewLine;"
        gapper = gaps 
    
    if options == "Don't show words":
        result = content
        gapper = []

    if options == "Show only first letter":
        idx = 0 
        res = ''
        for i in content.split(" "):
            if i == "_"*10:
                res += ' '+ gap_list[idx][0] + "_"*9 + ' '
                idx += 1
            else:
                res += " " + i 
        result = res

    if options == "Show only spaces":
        res = ''
        for i in content.split(" "):
            if i == "_"*10:
                res +=  " _"*5
            else:
                res += " " + i 
        result = res
        gapper = []


    if options == "Show spaces along with first letter":
        idx = 0 
        res = ''
        for i in content.split(" "):
            if i == "_"*10:
                res += ' '+ gap_list[idx][0] + "_ "*4 + ' '
                idx += 1
            else:
                res += " " + i 
        result = res 
        gapper = []


    if options == "No vowels":
        def no_vowel(string):
            res = '_'
            for i in string:
                if i in 'aeiou':
                    res += '_'
                else:
                    res += i 
            res += "_"
            return res 
        
        idx = 0 
        res = ''
        for i in content.split(" "):
            if i == "_"*10:
                res += ' '+ no_vowel(gap_list[idx]) + ' '
                idx += 1
            else:
                res += " " + i 
        result = res 
        gapper = []


    if options == "No consonents":
        def no_consonents(string):
            res = ''
            for j in string:
                if j not in 'aeiou':
                    res += "&lowbar;"
                else:
                    res += j
            return res 
        
        idx = 0 
        res = ''
        for i in content.split(" "):
            if i == "_"*10:
                res += ' '+ no_consonents(gap_list[idx]) + ' '
                idx += 1
            else:
                res += " " + i 
        result = res 
        gapper = []


    if options == "Anagrams (Show random letters)":
        def anagram(string):
            res = ''
            for i in range(0,len(string),2): 
                res += string[i] + "_"
            if len(string) % 2 == 0:
                return res
            else:
                return res[:-1]
        idx = 0 
        res = ''
        for i in content.split(" "):
            if i == "_"*10:
                res += ' '+ anagram(gap_list[idx]) + ' '
                idx += 1
            else:
                res += " " + i 
        result = res 
        gapper = []


    if options == 'Inline':
        res = ''
        idx = 0
        for i in content.split(" "):
            if i == "_"*10:
                res += "&nbsp;" +"&lowbar;"*10 + f"&nbsp;[{gap_list[idx]}]" + '&nbsp;'
                idx += 1
            else:
                res += " " + i 
        result = res 
        gapper = []



    title = st.session_state.title
    st.markdown(gaps)
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



