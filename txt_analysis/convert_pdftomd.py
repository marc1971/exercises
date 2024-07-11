import os
from pdfminer.high_level import extract_text

def pdf_to_markdown(pdf_path, md_path):
    # Extract text from the PDF
    text = extract_text(pdf_path)
    
    # Write the extracted text to a Markdown file
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(text)

if __name__ == "__main__":
    # Paths to the input PDF and output Markdown file
    pdf_path = r'C:\Users\COPE_Eyer_Marc\Documents\Projects\git_tasks\txt_analysis\docs\doc1.pdf'
    md_path = r'C:\Users\COPE_Eyer_Marc\Documents\Projects\git_tasks\txt_analysis\docs\doc1.md'
    
    # Convert PDF to Markdown
    pdf_to_markdown(pdf_path, md_path)

    print(f"Markdown file created at: {os.path.abspath(md_path)}")
