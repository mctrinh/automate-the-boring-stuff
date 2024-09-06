"""Create a DOCX file with custom invites for each name in the list."""

import os
import docx

def read_guest_names(filename):
    """Read guest names from a file and return them as a list."""
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        exit(1)
    
    with open(filename, 'r') as f:
        names = [line.strip() for line in f.readlines()]
    return names

def create_invitation_docx(names, output_file):
    """Create a DOCX file with custom invitations for each name."""
    document = docx.Document()
    
    styles = {
        'Custom 1': 'Normal',
        'Custom 2': 'Normal',
        'Custom 3': 'Normal',
        'Custom 4': 'Normal',
        'Custom 5': 'Normal'
    }

    for name in names:
        document.add_paragraph('It would be a pleasure to have the company of', style=styles.get('Custom 1', 'Normal'))
        document.add_paragraph(name, style=styles.get('Custom 2', 'Normal'))
        document.add_paragraph('at 11010 Memory Lane on the Evening of', style=styles.get('Custom 3', 'Normal'))
        document.add_paragraph('April 1st', style=styles.get('Custom 4', 'Normal'))
        document.add_paragraph("at 7 o'clock", style=styles.get('Custom 5', 'Normal'))
        
        document.add_page_break()
    
    document.save(output_file)
    print(f"File has been created and saved as '{output_file}'")

def main():
    """Main function to generate invites."""
    guests_file = 'guests.txt'
    output_file = 'invites.docx'
    
    names = read_guest_names(guests_file)
    create_invitation_docx(names, output_file)

if __name__ == '__main__':
    main()
