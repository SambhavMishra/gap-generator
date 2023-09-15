import streamlit as st
class Preview:

    @staticmethod
    def render(title, text, gaps):
        header =  """
            <style>

                .small {
                    font-size: 12px;
                    margin-bottom: -100%;
                }

                .css-5rimss, .e1nzilvr5 {
                    margin-top: 10px;
                    margin-bottom: 10px;    
                }
            </style>
            
            """
        st.markdown(header, unsafe_allow_html=True)
        st.write(title)
        # st.write(text)
        if len(gaps) > 0:
            st.write("&NewLine;" + gaps + "&NewLine;")
        st.write(text, unsafe_allow_html=True)

        footer = """
        <style>
                p[d] {
                    margin-bottom: 10px;
                    font-size: 12px;
                    margin-top: 10px;
                }
        </style>
        <p class="small">Press ctrl+p to print</p>
        """
        st.write("&NewLine; &NewLine; &NewLine;", unsafe_allow_html=True)
        
        st.markdown(footer, unsafe_allow_html=True)
            


