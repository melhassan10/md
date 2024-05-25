import pymupdf
import re

def pdf_to_text(pdf_path):
    text = ''
    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            text +=page.get_text()
    return text

def find_text_between_start_end(text, start_word, end_word):
    matches = re.findall(f'{start_word}(.+?){end_word}', text, re.DOTALL)
    return matches

def write_to_md(matches, output_path):
    with open(output_path, 'w') as file:
        for match in matches:
            file.write(f'```\n{match.strip()}\n```\n\n')

def main(pdf_path, start_word, end_word, output_path):
    text = pdf_to_text(pdf_path)
    matches = find_text_between_start_end(text, start_word, end_word)
    write_to_md(matches, output_path)

if __name__ == "__main__":
    pdf_path = 'input.pdf'  # Change this to your PDF file path
    start_word = 'NEW QUESTION'
    end_word = 'Answer:'
    output_path = 'output.md'  # Change this to your desired output file path
    main(pdf_path, start_word, end_word, output_path)