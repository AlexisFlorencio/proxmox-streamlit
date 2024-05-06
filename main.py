#!/usr/bin/env python3

import streamlit as st
import PyPDF2
import io

def remove_pdf_password(uploaded_file, password):
    pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(password)
        return pdf_reader
    else:
        return None

st.title("PDF Password Remover")

uploaded_file = st.file_uploader("Carga el PDF con contraseña", type="pdf")

if uploaded_file is not None:
    password = st.text_input("Introduce la contraseña del PDF")
    if st.button("Eliminar contraseña"):
        try:
            pdf_reader = remove_pdf_password(uploaded_file, password)
            if pdf_reader is not None:
                st.success("Contraseña eliminada con éxito.")
                st.write("Aquí está el contenido del PDF:")
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    st.write(page.extractText())
            else:
                st.error("El PDF no tiene contraseña o la contraseña proporcionada es incorrecta.")
        except PyPDF2.PdfReadError:
            st.error("Se produjo un error al leer el PDF. Asegúrate de que el archivo es un PDF válido.")