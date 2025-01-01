def read_text_file(file_path):
    """Reads a text file and returns its content as a string."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def find_text_differences(old_text, new_text):
    """Finds differences between two strings."""
    old_set = set(old_text.split())
    new_set = set(new_text.split())
    differences = new_set - old_set
    return differences

def save_differences_to_file(differences, output_file):
    """Saves the differences to a text file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(differences):
            f.write(word + '\n')

# Paths to the text files
old_txt_file = "UN GUERRERO DE DOS MUNDOS - DR. OVIDIO INDACOCHEA GARCIA.txt"  # Replace with the path to your old .txt file
new_txt_file = "Un guerrero de 2 mundos - Ovidio Indacochea.txt"  # Replace with the path to your new .txt file
output_file = "diferencias_txt.txt"  # Output file for differences

# Read text from both files
old_text = read_text_file(old_txt_file)
new_text = read_text_file(new_txt_file)

# Find differences
differences = find_text_differences(old_text, new_text)

# Save differences to a file
save_differences_to_file(differences, output_file)

print(f"Diferencias extraídas y guardadas en: {output_file}")
