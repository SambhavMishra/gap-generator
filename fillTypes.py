import streamlit as st 
import random 
import base64
from boxes import box_and_bound


class fillTypes:


    @staticmethod 
    def fill(options, content, gap_list, gaps, extra_words):

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
            box = box_and_bound() 
            result = box.create_boxes(content, gap_list)

        if options == "OMR Friendly Boxes":
            box = box_and_bound()
            result = box.create_omr_boxes(content, gap_list, extra_words)

        return result, gapper