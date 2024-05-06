#!/usr/bin/env python3

def remove_pdf_password(file_path):
    password = int(input("Ingrese la contraseña del PDF (número entero): "))
    with open(file_path, 'rb') as file:
        file_content = file.read()
        if file_content.startswith(b'%PDF-1.') and b'/Encrypt' in file_content:
            # PDF está encriptado
            decrypted_content = bytearray()
            for byte in file_content:
                decrypted_byte = byte ^ password
                decrypted_content.append(decrypted_byte)
            return decrypted_content
        else:
            # PDF no está encriptado
            return None

if __name__ == "__main__":
    file_path = input("Ingrese la ruta del archivo PDF encriptado: ")

    decrypted_pdf_content = remove_pdf_password(file_path)

    if decrypted_pdf_content is not None:
        output_file_path = input("Ingrese la ruta de salida para el PDF desencriptado: ")
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decrypted_pdf_content)
        print("El PDF ha sido desencriptado con éxito.")
    else:
        print("El PDF no está encriptado o la contraseña proporcionada es incorrecta.")
