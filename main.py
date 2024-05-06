#!/usr/bin/env python3

import PyPDF2
import io

def remove_pdf_password(file_path, password):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        if pdf_reader.isEncrypted:
            pdf_reader.decrypt(password)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            decrypted_pdf = io.BytesIO()
            pdf_writer.write(decrypted_pdf)
            decrypted_pdf.seek(0)
            return decrypted_pdf
        else:
            return None

if __name__ == "__main__":
    file_path = input("Ingrese la ruta del archivo PDF encriptado: ")
    password = input("Ingrese la contraseña del PDF: ")

    decrypted_pdf = remove_pdf_password(file_path, password)

    if decrypted_pdf is not None:
        output_file_path = input("Ingrese la ruta de salida para el PDF desencriptado: ")
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decrypted_pdf.read())
        print("El PDF ha sido desencriptado con éxito.")
    else:
        print("El PDF no está encriptado o la contraseña proporcionada es incorrecta.")
