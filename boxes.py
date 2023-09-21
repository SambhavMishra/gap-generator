import random
import streamlit as st 
import base64
import streamlit as st 
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
        mcqs = set(extra_words + gap_list)
        mcqs = list(mcqs)
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


        def table_data(quest):
            if quest > len(mcqs)+1:
                return f'{space}'
            else:
                line = f'<td>{quest}{space}'
                char = ord('a')
                for i in range(len(mcqs)):
                    l = f'<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}{chr(char+i)}{space}</p>'
                    line += l 
                line += '</td>'
                return line


        omrs = '<table border=none>'
        for ch in range(0,len(mcqs),3):
            line = f'<tr>{table_data(ch+1)}{table_data(ch+2)}{table_data(ch+3)}</tr>'
            omrs += line

        omrs += "</table>"
        res += omrs + "<br/><br/>"

        res += omr_image

        res +=ques 



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

        result = res
        return result