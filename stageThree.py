import streamlit as st
class StageThree:

    @staticmethod
    def render():
        header =  """
            <style>
                .text-container {
                    display: flex;
                    justify-content: space-between;
                    width: 100%;
                    margin-top: -20px;
                }
                .text {
                    width: 30%;
                    text-align: center;
                    color: blue;
                }
                .text p {
                    font-size: 12px;
                    margin-top: -15px;
                }
                .current-stage{
                    background-color: #22cc33;
                    width: 20px;
                    color: white;
                    margin-left: 48%;
                }

            </style>
            <div class='text-container'>
                <div class='text'>
                    <p>1</p>
                    <p>ENTER TITLE AND TEXT</p>
                </div>
                <div class='text'>
                    <p>2</p>
                    <p>INTERACTIVE GAPS ADDER</p>
                </div>
                <div class='text'>
                    <p class="current-stage">3</p>
                    <p>SETTINGS, PREVIEW AND PRINT</p>
                </div>
            </div>
            """
        st.write(
        header,
        unsafe_allow_html=True,
        )




            


