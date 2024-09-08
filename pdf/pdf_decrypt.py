"""Finds and decrypts all encrypted PDF files in the folder tree starting from the CWD.

Usage:
pdf_decrypt.py <password>
"""

import os
import sys
import PyPDF2

def decrypt_pdf(path, password):
    try:
        with open(path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if pdf_reader.is_encrypted:
                if pdf_reader.decrypt(password) == 1:
                    pdf_writer = PyPDF2.PdfWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))
                    
                    decrypted_path = path[:-4] + '_decrypted.pdf'
                    with open(decrypted_path, 'wb') as decrypted_file:
                        pdf_writer.write(decrypted_file)
                    return True
                else:
                    return False
            return False
    except Exception as e:
        print(f"Error processing {path}: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: pdf_decrypt.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    decrypt_failed = []

    for root, _, filenames in os.walk('.'):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                path = os.path.join(root, filename)
                if not decrypt_pdf(path, password):
                    print(f'{filename} failed to decrypt.')
                    decrypt_failed.append(filename)

    if decrypt_failed:
        print("All encrypted PDFs, except those listed above, were "
              "decrypted successfully. All of the original files have been kept.")
    else:
        print("All encrypted PDFs in the folder tree were decrypted successfully. "
              "The original files have been kept.")

if __name__ == "__main__":
    main()
