from docx import Document

def extract_text(docx_file):
    """Extracts all text from a .docx file."""
    doc = Document(docx_file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def find_differences(old_text, new_text):
    """Finds differences between two texts."""
    old_set = set(old_text.split())
    new_set = set(new_text.split())
    differences = new_set - old_set
    return differences

def save_differences_to_file(differences, output_file):
    """Saves the differences to a text file."""
    with open(output_file, 'w') as f:
        for word in sorted(differences):
            f.write(word + '\n')

# Paths to the files
old_docx_file = "UN GUERRERO DE DOS MUNDOS - DR. OVIDIO INDACOCHEA GARCIA v2.docx"  # Replace with the path to your old .docx file
new_docx_file = "Un guerrero de 2 mundos - Ovidio Indacochea.docx"  # Replace with the path to your converted .docx file
output_file = "diferencias.txt"  # Output file for differences

# Extract text from both files
old_text = extract_text(old_docx_file)
new_text = extract_text(new_docx_file)

# Find differences
differences = find_differences(old_text, new_text)

# Save differences to a file
save_differences_to_file(differences, output_file)

print(f"Diferencias extraídas y guardadas en: {output_file}")
