#!/usr/bin/env python3
"""
Convert BibTeX file to YAML for Jekyll publications page.
Handles LaTeX special characters, curly braces, and proper author formatting.
"""

import re
import sys

def clean_latex_text(text):
    """Remove LaTeX formatting and curly braces from text."""
    if not text:
        return ""
    
    # Remove outer curly braces that protect capitalization
    text = re.sub(r'\{([^{}]+)\}', r'\1', text)
    
    # Handle nested braces by repeating
    while '{' in text:
        text = re.sub(r'\{([^{}]*)\}', r'\1', text)
    
    # LaTeX special characters
    replacements = {
        r'\_': '_',
        r'\&': '&',
        r'\%': '%',
        r'\$': '$',
        r'\#': '#',
        r'--': '—',  # em dash
        r'---': '—',  # em dash
        r"\'e": 'é',
        r"\'a": 'á',
        r"\'i": 'í',
        r"\'o": 'ó',
        r"\'u": 'ú',
        r'\`e': 'è',
        r'\`a': 'à',
        r'\"o': 'ö',
        r'\"u': 'ü',
        r'\"a': 'ä',
        r'\~n': 'ñ',
        r'\textgreater': '>',
        r'\textless': '<',
    }
    
    for latex, replacement in replacements.items():
        text = text.replace(latex, replacement)
    
    # Clean up any remaining backslashes before common commands
    text = re.sub(r'\\text[a-z]+\{([^}]+)\}', r'\1', text)
    
    # Remove any remaining isolated backslashes
    text = text.replace('\\', '')
    
    # Clean up extra whitespace
    text = ' '.join(text.split())
    
    return text.strip()

def parse_authors(author_string):
    """Parse author string and return formatted list."""
    if not author_string:
        return ""
    
    # Clean the string first
    author_string = clean_latex_text(author_string)
    
    # Split by 'and'
    authors = [a.strip() for a in author_string.split(' and ')]
    
    formatted_authors = []
    for author in authors:
        if not author:
            continue
        
        # Remove any leading/trailing commas or spaces
        author = author.strip(' ,')
        
        # If author has comma, it's "Last, First" format
        if ',' in author:
            parts = [p.strip() for p in author.split(',', 1)]
            if len(parts) == 2:
                # Keep as "Last, First" but clean up
                formatted_authors.append(f"{parts[0]}, {parts[1]}")
            else:
                formatted_authors.append(author)
        else:
            # Already in "First Last" format or single name
            formatted_authors.append(author)
    
    return ', '.join(formatted_authors)

def parse_bibtex_file(filename):
    """Parse BibTeX file and return list of publication dictionaries."""
    publications = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all entries
    entry_pattern = r'@(\w+)\{([^,]+),\s*(.*?)\n\}'
    entries = re.finditer(entry_pattern, content, re.DOTALL)
    
    for entry in entries:
        entry_type = entry.group(1).lower()
        cite_key = entry.group(2)
        fields_text = entry.group(3)
        
        # Skip non-article entries if desired
        if entry_type not in ['article', 'inproceedings', 'book', 'incollection', 'misc']:
            continue
        
        pub = {'type': 'journal' if entry_type == 'article' else entry_type}
        
        # Parse fields
        field_pattern = r'(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}'
        fields = re.finditer(field_pattern, fields_text, re.DOTALL)
        
        for field in fields:
            field_name = field.group(1).lower()
            field_value = field.group(2).strip()
            
            if field_name == 'title':
                pub['title'] = clean_latex_text(field_value)
            elif field_name == 'author':
                pub['authors'] = parse_authors(field_value)
            elif field_name == 'year':
                try:
                    pub['year'] = int(field_value)
                except:
                    pub['year'] = field_value
            elif field_name == 'journal':
                pub['venue'] = clean_latex_text(field_value)
            elif field_name == 'booktitle':
                pub['venue'] = clean_latex_text(field_value)
            elif field_name == 'doi':
                pub['doi'] = field_value.strip()
            elif field_name == 'volume':
                pub['volume'] = field_value
            elif field_name == 'number':
                pub['number'] = field_value
            elif field_name == 'pages':
                pub['pages'] = field_value.replace('--', '-')
            elif field_name == 'publisher':
                pub['publisher'] = clean_latex_text(field_value)
        
        # Only add if we have minimum required fields
        if 'title' in pub and 'year' in pub:
            publications.append(pub)
    
    return publications

def write_yaml_file(publications, output_file):
    """Write publications to YAML file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# _data/publications.yml\n")
        f.write("#\n")
        f.write("# Publications list generated from BibTeX\n")
        f.write("#\n\n")
        
        for pub in publications:
            f.write(f'- title: "{pub.get("title", "").replace(chr(34), chr(39))}"')
            f.write("\n")
            
            if 'authors' in pub:
                f.write(f'  authors: "{pub["authors"].replace(chr(34), chr(39))}"')
                f.write("\n")
            
            if 'year' in pub:
                f.write(f'  year: {pub["year"]}\n')
            
            if 'type' in pub:
                f.write(f'  type: "{pub["type"]}"\n')
            
            if 'venue' in pub:
                venue = pub['venue'].replace('"', "'")
                f.write(f'  venue: "{venue}"\n')
            
            if 'doi' in pub:
                f.write(f'  doi: "{pub["doi"]}"\n')
            
            if 'volume' in pub:
                f.write(f'  volume: "{pub["volume"]}"\n')
            
            if 'number' in pub:
                f.write(f'  number: "{pub["number"]}"\n')
            
            if 'pages' in pub:
                f.write(f'  pages: "{pub["pages"]}"\n')
            
            if 'publisher' in pub:
                f.write(f'  publisher: "{pub["publisher"]}"\n')
            
            f.write("\n")

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'publications2.bib'
    output_file = '_data/publications.yml'
    
    print(f"Reading from {input_file}...")
    publications = parse_bibtex_file(input_file)
    
    print(f"Parsed {len(publications)} publications")
    
    print(f"Writing to {output_file}...")
    write_yaml_file(publications, output_file)
    
    print("Done!")
    
    # Print some examples
    if publications:
        print("\nFirst few publications:")
        for i, pub in enumerate(publications[:3]):
            print(f"\n{i+1}. {pub.get('title', 'No title')}")
            print(f"   Authors: {pub.get('authors', 'No authors')[:100]}...")
            print(f"   Year: {pub.get('year', 'N/A')}")

if __name__ == '__main__':
    main()
