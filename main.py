from pdfText import PDFTextExtractor

def main():
    pdf_path = input("Enter the path of the PDF file: ")
    start_word = input("Enter the starting word: ")
    end_word = input("Enter the ending word: ")
    output_path = 'output.md'

    extractor = PDFTextExtractor(pdf_path)
    text = extractor.extract_text()
    matches = extractor.find_text_between_start_end(text, start_word, end_word)
    extractor.write_to_md(matches, output_path)

if __name__ == "__main__":
    main()
