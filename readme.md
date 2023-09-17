# gap-generator
For teachers who want to create fill in the blanks. This platform is for you.

Streamlit link: https://sambhavmishra-gap-generator-app-4suf68.streamlit.app/

Tip to download original html content instead of ctrl + p

If you want to download the original html as a pdf, follow the below steps:

1.  clone the repository using  ``` git clone https://github.com/SambhavMishra/gap-generator.git ```

2. In the app.py uncomment the line ``` from weasyprint import HTML ``` and 

``` 
    # title = st.session_state.title + "<br/><br/>"
    # html_content = title + st.session_state.result


    # with open("gap_html.html", "wb") as file:
    #     file.write(html_content.encode('utf-8'))
    # file.close() 

    # pdf_file = HTML(string=html_content).write_pdf()
    # st.download_button("Download PDF", pdf_file, key="download_pdf", file_name="gap_generator.pdf")
```

and, you are done, now you can run the streamlit app and download the original html as pdf after installing weasyprint, run

```
pip install weasyprint
```

in command line.