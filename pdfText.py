import pymupdf
import re

class PDFTextExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        text = ''
        with pymupdf.open(self.pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    @staticmethod
    def find_text_between_start_end(text, start_word, end_word):
        pattern = re.compile(f'{start_word}(.*?){end_word}', re.DOTALL)
        matches = pattern.findall(text)
        return matches

    @staticmethod
    def write_to_md(matches, output_path):
        with open(output_path, 'w') as file:
            for match in matches:
                file.write(f'```\n{match.strip()}\n```\n\n')

    
    
    
