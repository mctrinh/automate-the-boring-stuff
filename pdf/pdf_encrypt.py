"""Encrypts all unencrypted PDFs in a folder tree starting from the CWD.

Usage:
    pdf_encrypt.py <password>
    - Encrypts all unencrypted PDFs in the current directory and its subdirectories
      with the provided password.
"""

import os
import sys
import PyPDF2

def encrypt_pdf(file_path, password):
    """Encrypt a PDF file and save the encrypted version."""
    try:
        pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
        
        if pdf_reader.is_encrypted:
            print(f"{file_path} is already encrypted. Skipping.")
            return False

        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        encrypted_path = file_path[:-4] + '_encrypted.pdf'
        with open(encrypted_path, 'wb') as encrypted_file:
            pdf_writer.encrypt(password)
            pdf_writer.write(encrypted_file)

        # Verify the encryption
        pdf_reader = PyPDF2.PdfReader(open(encrypted_path, 'rb'))
        if pdf_reader.is_encrypted and pdf_reader.decrypt(password) == 1:
            os.remove(file_path)
            return True
        else:
            print(f"Encryption verification failed for {file_path}.")
            return False
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
        return False

def main():
    """Main function to encrypt PDFs."""
    if len(sys.argv) != 2:
        print("Usage: pdf_encrypt.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    encrypt_failed = []

    for root, dirs, files in os.walk('.'):
        for file_name in files:
            if file_name.lower().endswith('.pdf'):
                file_path = os.path.join(root, file_name)
                if not encrypt_pdf(file_path, password):
                    encrypt_failed.append(file_name)

    if encrypt_failed:
        print('The following files failed their encryption checks and were '
              'not deleted:')
        for file_name in encrypt_failed:
            print(file_name)
    else:
        print("All PDF files in the folder tree have been encrypted successfully. "
              "The original files have been deleted.")

if __name__ == '__main__':
    main()
