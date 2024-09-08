"""Carries out a brute-force password attack on an encrypted PDF."""

import PyPDF2

def try_decrypt(pdf_reader, password):
    """Attempt to decrypt the PDF with the given password."""
    return pdf_reader.decrypt(password) == 1

def main():
    file = input('Enter the absolute path of the PDF you wish to break: ').strip()

    with open('dictionary.txt') as f:
        words = [line.strip() for line in f]

    try:
        with open(file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for word in words:
                lower = word.lower()
                upper = word.upper()
                if try_decrypt(pdf_reader, lower):
                    print(f'Password = {lower}')
                    break
                elif try_decrypt(pdf_reader, upper):
                    print(f'Password = {upper}')
                    break
            else:
                print('Password not found.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
