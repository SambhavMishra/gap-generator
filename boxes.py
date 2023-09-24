import random
import streamlit as st 
import base64
import streamlit as st 
import math
class box_and_bound():
    @staticmethod
    def create_boxes(content, gap_list):
        res = ''
        character = ord('A')
        charList = []
        for i in content.split(" "):
            if i == "_"*10:
                res += ' '+ f'<span style="font-size: 24px; border: 1px solid black; display: inline;">&nbsp;{chr(character)}&nbsp;</span>' + ' '
                charList.append(chr(character))
                character += 1
            else:
                res += " " + i 
        numBoxes = max([len(i) for i in gap_list])
        res += " <br/><br/>" 
        shuffler = gap_list.copy()
        random.shuffle(shuffler)
        shuffler = ', '.join(shuffler)
        res += shuffler + "<br/><br/>"

        file_ = open("images/omr_marker.jpg", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        space = '<span style="display:inline; margin-left:4px;"></span>'
        markers = f'<img src="data:image/gif;base64,{data_url}"  alt="omr marker" width="40px" style="display:inline;"/> {space*(numBoxes*6)}<img src="data:image/gif;base64,{data_url}"  alt="omr marker" width="40px" style="display: inline;"/> <br/><br/>'

        res += markers

        res += f"{space*6}Roll No.: " + f'<span style="font-size: 24px; border: 1px solid black; display: inline;">{space*6}</span>'*2 + " <br/>"

        for char in charList:
            res += f'<br/><br/> {space*4} {char} {space*4}' +  f'<span style="font-size: 24px; border: 1px solid black; display: inline;">{space*6}</span>'*numBoxes 

        res += '<br/><br/>' + markers

        result = res 

        return result 



    @staticmethod
    def create_omr_boxes(content, gap_list, extra_words):
        # st.write(extra_words)
        # if '' in extra_words:
        #     st.write("'' is present in extra_words")
        #     extra_words = extra_words.remove('')
        #     st.write(f"extra_words has now become {extra_words}")
        mcqs = set(extra_words + gap_list)
        mcqs = list(mcqs)
        mcqs = [i for i in mcqs if i != '']
        opts = mcqs.copy()
        random.shuffle(opts)
        correct_options = {
            'question': [],
            'answer': []
        }


        res = '' 
        space = '<span style="display:inline; margin-left:6px;"></span>'

        
        file_ = open("images/two_sided_omr.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        omr_image = f'<img src="data:image/gif;base64,{data_url}"  alt="omr marker" style="display:block; height:70px; width: 110%; margin-left: -5%;"/>'
        res += omr_image


        res += 'Please write this in below boxes exactly as shown here. "THE FIVE BOXING WIZARDS JUMP QUICKLY" (in capital letters)'

        sentence = "THE FIVE BOXING WIZARDS JUMP QUICKLY"

        res += f'<br/><br/> {space*4} {space*4}'

        def row(sentence, type):
            if type == 'letter':
                string = '<tr>'
                for i in sentence:
                    string += f'<td style="border: none;">{i}</td>'
                string +=  '</tr>'

            if type == 'blank':
                string = '<tr>'
                for i in sentence:
                    string += f'<td style="border: 1px solid black;">{space*2}</td>'
                string +=  '</tr>'
            return string 


        res += f'<table border="0">{row(sentence,"letter")}{row(sentence,"blank")}</table>'




        file_ = open("images/static_image_omr_cropped.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        static_image = f'<img src="data:image/gif;base64,{data_url}"  alt="omr marker" style="display:inline;"/>'
        res += static_image

        character = 1
        charList = []


        ques = ''
        for i in content.split(" "):
            if i == "_"*10:
                ques += ' '+ f'<span style="font-size: 24px; border: 1px solid black; display: inline;">&nbsp;{str(character)}&nbsp;</span>' + ' '
                charList.append(str(character))
                character += 1
            else:
                ques += " " + i 


        def table_data(quest, last):
            if quest > last:
                return f'{space}'
            else:
                line = f'<td>{space}{quest}{space}</td><td>'
                char = ord('a')
                for i in range(len(mcqs)):
                    l = f'<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}{chr(char+i)}{space}</p>'
                    line += l 
                line += '</td>'
                return line


        num_columns = 3  
        num_rows = (len(gap_list) + num_columns - 1) // num_columns
        last = len(gap_list)

        omrs = '<table border="1">'

        for row in range(num_rows):
            omrs += '<tr>'
            for col in range(num_columns):
                index = row + col * num_rows 
                omrs += table_data(index + 1, last)
            omrs += '</tr>'

        omrs += "</table>"
        res += omrs + "<br/><br/>"
        res += omr_image
        res += ques



        char = ord('a')
        mcq_section = '<br/>' 
        mcqs = list(mcqs)
        for i in range(len(mcqs)):
            mcq_section += f'({chr(char)}){mcqs[i].upper()}'
            char += 1

        res += "<br/>" + mcq_section

        for i in range(len(gap_list)):
            for j in range(len(opts)):
                if opts[j] == gap_list[i]:
                    correct_options['question'].append(f'q{i+1}')
                    correct_options['answer'].append(chr(ord('a') + j))
        st.session_state.correct_options = correct_options

        num_of_options = len(mcqs)
        block_1_origin_x = 72
        question_per_column = math.ceil(len(gap_list)  / 3) 

        json = f'{{"pageDimensions": [ 550, 800 ],"bubbleDimensions": [ 16, 16 ],"preProcessors": [{{"name": "CropPage","options": {{"morphKernel": [ 10, 10 ]}}}}],"customLabels": {{"Roll_no": ["r1","r2"]}},"fieldBlocks": {{"Roll_no": {{"fieldType":"QTYPE_INT", "origin": [ 306, 238 ],    "fieldLabels": ["r1", "r2"],    "bubblesGap": 15,    "labelsGap": 15    }},    "MCQBlock1a1": {{    "fieldType": "QTYPE_MCQ{num_of_options}",    "origin": [ 72, 395],"bubblesGap": 15,"labelsGap": 15,"fieldLabels": [    "q1..{question_per_column}"]}},"MCQBlock1a2": {{"fieldType": "QTYPE_MCQ{num_of_options}","origin": [{block_1_origin_x + num_of_options*15 + 18},    395],"bubblesGap": 15,"labelsGap": 15,"fieldLabels": ["q{question_per_column + 1}..{question_per_column * 2}"]}},"MCQBlock1a3": {{"fieldType": "QTYPE_MCQ{num_of_options}","origin": [{block_1_origin_x + num_of_options*30 + 36},    395],"bubblesGap": 15,"labelsGap": 15,"fieldLabels": ["q{question_per_column * 2 + 1}..{question_per_column*3}"]}}}}}}'
        
        st.session_state.json = json 

        result = res
        return result