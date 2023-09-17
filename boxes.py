import random
import streamlit as st 
import base64
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

        file_ = open("omr_marker.jpg", "rb")
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
    def create_omr_boxes(content, gap_list, mcqs):
        res = '' 
        res += 'Please write this in below boxes exactly as shown here. "THE FIVE BOXING WIZARDS JUMP QUICKLY" (in capital letters)'

        sentence = "THE FIVE BOXING WIZARDS JUMP QUICKLY"
        space = '<span style="display:inline; margin-left:4px;"></span>'

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




        file_ = open("static_image_omr.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        static_image = f'<img src="data:image/gif;base64,{data_url}"  alt="omr marker" style="display:inline;"/><br/><br/>'
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

        rows = len(mcqs) // 3 + 1 


        omrs = '<table border=none>'
        for ch in range(0,len(mcqs),2):
            line = f'<tr><td>{ch+1}{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}a{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}b{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}c{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}d{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}e{space}</p></td><td>{ch+2}{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}a{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}b{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}c{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}d{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}e{space}</p></td><td>{ch+3}{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}a{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}b{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}c{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}d{space}</p>{space}<p style="display: inline; border: 1px solid black; border-radius: 50%;">{space}e{space}</p></td></tr>'
            omrs += line

        omrs += "</table>"
        res += omrs + "<br/><br/>"

        res +=ques 

        choices = []
        for i in mcqs.keys():
            choices.append([i] + mcqs[i])


        mcq_section = ''
        for i, num in enumerate(choices): 
            number = num.copy()
            random.shuffle(number)
            line = f'<br/>{str(i+1)}{space}(a){number[0]}{space}(b){number[1]}{space}(c){number[2]}{space}(d){number[3]}{space}(e){number[4]}{space}'
            mcq_section += line

        res += "<br/>" + mcq_section

        res += "<br/><br/>"

        res += f'<br/>{",".join(gap_list).upper()}</br>'
        result = res

        return result