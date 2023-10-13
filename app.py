import streamlit as st 
from stageOne import StageOne
from stageTwo import StageTwo
from stageThree import StageThree
from fillTypes import fillTypes
from blank_selector import blank_selector
# from weasyprint import HTML
from preview import Preview
import pandas as pd
import ast
import re 
import base64
# import json



st.set_page_config(layout='wide')

# "st.session_state object:", st.session_state  



if 'page' not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def omr_section():
    st.session_state.page = 4

def home_page():
    st.session_state.page = 0


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

    # gap_list.extend(st.session_state.extras.split(","))

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
    st.session_state.text =  re.sub(r'[,.!?]', '', text)
    st.button("Next", on_click=next_page)

elif st.session_state['page'] == 1:     
    blank_selector.selector() 


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
    options = st.selectbox(label='select', options=['Show words', "Don't show words", "Show only first letter", "Show only spaces", "Show spaces along with first letter", "No vowels", "No consonents", "Anagrams (Show random letters)", "Inline", "Box and Bounded","OMR Friendly Boxes"])

    st.write("Settings and preview")

    ft = fillTypes()
    # mcqs = st.session_state.mcqs
    extra_words = st.session_state.extra_words
    result, gapper = ft.fill(options, content, gap_list, gaps, extra_words)
    st.session_state.result = result


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

    ###################### WEASYPRINT START ###################

    # title = st.session_state.title + "<br/><br/>"
    # html_content = title + st.session_state.result


    # with open("gap_html.html", "wb") as file:
    #     file.write(html_content.encode('utf-8'))
    # file.close() 

    # pdf_file = HTML(string=html_content).write_pdf()
    # st.download_button("Download PDF", pdf_file, key="download_pdf", file_name="gap_generator.pdf")



    ###################### WEASYPRINT END ########################

    df = st.session_state.correct_options

    df = pd.DataFrame(df)

    # df.to_csv('output.csv', index=False)

    def download_csv(dataframe):
        csv = dataframe.to_csv(header=False, index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<button style="border:1px solid #909090; border-radius: 5px; font-size:24px; background-color: white;"><a href="data:file/csv;base64,{b64}" download="data.csv" style="text-decoration: none;">Download CSV</a></button>'
        st.markdown(href, unsafe_allow_html=True)
    if len(df) > 0:
        download_csv(df)

    json_string = st.session_state.json
    def download_json(json_string):
        b64 = base64.b64encode(json_string.encode()).decode()
        href = f'<button style="border:1px solid #909090; border-radius: 5px; font-size:24px; background-color: white;"><a href="data:file/json;base64,{b64}" download="template.json" style="text-decoration: none;">Download template.json</a></button>'
        st.markdown(href, unsafe_allow_html=True)
    download_json(json_string)