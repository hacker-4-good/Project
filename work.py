"""
Project Name :- Care4Doc

Implementation Plan:-

-> We have divided implementation into few stages/phases:-

Phase 1-> (API for user interaction):- We first thought of finding right API which will interact with user. It is where user can upload the
document. For this we have use streamlit library of python which have provide us frontend and API for our project.

Phase 2-> (Extraction of text):- Now next, we have to find out algorithm to extract the text from uploaded file (.jpeg, .pdf, .txt). This 
is provided by pytesseract and PyPDF2 library of python.

Phase 3-> (Correction):- Now since we have extract the text, now in next step we have to correct misprint text which is not extracted properly.
So for this we have used TextBlob library of python which will help to replace wrong words present in document.

Phase 4-> (Display):- At last, once we have get the corrected text from document. Now simply we will display it to our user below so that user
can configure then and there

"""
import streamlit as st        # streamlit :- Design of interface for user interaction
import PyPDF2 as pdf          # PyPDF2 :- Used to extract text from pdf
from textblob import TextBlob # TextBlob :- Used to correct and replace the wrong word
import  pytesseract           # pytesseract :- Used to extract the text from image 


wdFormatPDF = 17


# option for user to select based upon service want to take
st.title("Care4Doc")
option = st.selectbox("Select the option: ",("Choose option","PDF","Text","JPG/JPEG"))


# Uploading of file
file = st.file_uploader("Upload Document")


# Getting the path of document from the user
path = st.text_input("Copy the document path")


if(st.button("Submit")):


    if(option=="PDF"):
        # Read of the text from file
        PDF = pdf.PdfFileReader(file)
        for i in range(PDF.numPages):
            # access to particular page and extract text and simultaneously rectify them
            res = TextBlob(PDF.getPage(i).extract_text()).correct()
            st.text(res)
            st.text("page {}".format(i))


    if(option=="Text"):
        # opening of text document and extract text
        with open(file.name) as f:
            # reading particular line of text document and simultanoeusly rectify error
            res = TextBlob(f.readline()).correct()
            st.text(res)
    

    if(option=="JPG/JPEG"):
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        # extracting of text from image and convert to string and store it in a variable name "string"
        string = pytesseract.image_to_string(path)
        # solving error words by passing complete "string" in TextBlob library object
        res = TextBlob(string).correct()
        st.text(res)
