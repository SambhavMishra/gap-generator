import streamlit as st 
import random 
import base64

class fillTypes:


    @staticmethod 
    def fill(options, content, gap_list, gaps):

        gapper = []
        if options == 'Show words':
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
            result = res + content + "&NewLine;"
            gapper = gaps 
            
        if options == "Don't show words":
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
            result = res +  content
            gapper = []

        if options == "Show only first letter":
            idx = 0 
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
            for i in content.split(" "):
                if i == "_"*10:
                    res += ' '+ gap_list[idx][0] + "&lowbar;"*9 + ' '
                    idx += 1
                else:
                    res += " " + i 
            result = res

        if options == "Show only spaces":
            # res = ''
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
            for i in content.split(" "):
                if i == "_"*10:
                    res +=  " _"*5
                else:
                    res += " " + i 
            result = res
            gapper = []


        if options == "Show spaces along with first letter":
            idx = 0 
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
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
                    if i in 'aeiouAEIOU':
                        res += '&lowbar;'
                    else:
                        res += i 
                # res += ""
                return res 
            
            idx = 0 
            # res = ''
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
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
                    if j not in 'aeiouAEIOU':
                        res += "&lowbar;"
                    else:
                        res += j
                return res 
            
            idx = 0 
            # res = ''
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
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
            # res = ''
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
            for i in content.split(" "):
                if i == "_"*10:
                    res += ' '+ anagram(gap_list[idx]) + ' '
                    idx += 1
                else:
                    res += " " + i 
            result = res 
            gapper = []


        if options == 'Inline':
            # res = ''
            res = 'Student Name: _________________________________ <br/>'
            res += 'Student Roll No.: ________________________________ <br/><br/><br/>'
            idx = 0
            for i in content.split(" "):
                if i == "_"*10:
                    res += "&nbsp;" +"&lowbar;"*10 + f"&nbsp;[{gap_list[idx]}]" + '&nbsp;'
                    idx += 1
                else:
                    res += " " + i 
            result = res 
            gapper = []

        if options == "Box and Bounded":
            res = ''
            idx = 0
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
            res += " <br/>" 
            shuffler = gap_list.copy()
            random.shuffle(shuffler)
            shuffler = ', '.join(shuffler)
            res += shuffler + "<br/>"

            file_ = open("omr_marker.jpg", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
            space = "&nbsp;"
            markers = f'<img src="data:image/gif;base64,{data_url}"  alt="omr marker" width="80px" style="display:inline;"/> {space*numBoxes*11}<img src="data:image/gif;base64,{data_url}"  alt="omr marker" width="80px" style="display: inline;"/> <br/><br/>'

            res += markers

            res += f"{space*16}Roll No.: " + f'<span style="font-size: 24px; border: 1px solid black; display: inline;">{space*6}</span>'*2 + " <br/>"

            for char in charList:
                res += f'<br/> {space*16} {char} &nbsp;&nbsp;&nbsp;&nbsp;' +  f'<span style="font-size: 24px; border: 1px solid black; display: inline;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>'*numBoxes 

            res += '<br/><br/>' + markers

            result = res 

            

        return result, gapper