import sys
from pdfminer.high_level import extract_text

def convert_pdf_to_txt(pdf_path, txt_path):
    try:
        text = extract_text(pdf_path)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Successfully extracted {pdf_path} to {txt_path}")
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf.py <pdf_path> <txt_path>")
    else:
        convert_pdf_to_txt(sys.argv[1], sys.argv[2])
