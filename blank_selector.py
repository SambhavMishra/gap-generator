import streamlit as st 
from stageTwo import StageTwo

class blank_selector():

    def selector():
        def createCheckbox(c, word, wordKeys,i):
            with col1 if i % 5 == 0 else col2 if i % 5 == 1 else col3 if i % 5 == 2 else col4 if i % 5 == 3 else col5:
                if st.checkbox(word, key=wordKeys[f"{i}"]):
                    st.session_state.blanks[wordKeys[f"{i}"]] = True 
                else:
                    st.session_state.blanks[wordKeys[f"{i}"]] = False 



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

        st.session_state.blanks = {wordKeys[f"{i}"]:False for i in range(len(words))}


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


        st.write("Tip: you only need to enter more options if you want to create omr sheet.") 
        st.write("Tip: You need to enter 4 options for each selections.")
        mcq_questions = [(st.session_state.words[i], st.session_state.blanks[i]) for i in range(len(st.session_state.blanks))]
        mcqs = {}
        for i in mcq_questions:
            if i[1]:
                choices = st.text_input(f"Enter more options for {i[0]} (seperated by comma)", key=f"mcq_{i}")
                mcqs[i[0]] = choices.split(",")

        st.session_state.mcqs = mcqs 

    
