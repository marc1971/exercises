## This is a script to extract Author and Title of the Theses

import re

def read_markdown_file(doc):
    with open(doc, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_title_author(content):
    # Split the content into lines
    lines = content.split('\n')
    
    # Initialize variables to hold the title and author
    title = None
    author = None
    
    # Iterate through lines to find the title and author
    for i, line in enumerate(lines):
        if line.strip().isdigit():
            continue  # Skip the year
        if not title and line.strip():
            title = line.strip()  # First non-empty, non-date line is the title
        if "PÄDAGOGISCHE HOCHSCHULE BERN" in line:
            author = lines[i + 1].strip()  # The line after this is the author
            break
    
    return title, author

def main(doc):
    content = read_markdown_file(doc)
    title, author = extract_title_author(content)
    
    print(f"Title: {title}")
    print(f"Author: {author}")

# Example usage

if __name__ == "__main__":
# Paths to the input PDF and output Markdown file
    doc = r'C:\Users\COPE_Eyer_Marc\Documents\Projects\git_tasks\txt_analysis\docs\doc1.md'
    main(doc)
