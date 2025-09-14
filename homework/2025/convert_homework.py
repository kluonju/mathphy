#!/usr/bin/env python3
"""
Convert 2024 homework files to 2025 with new styling
Author: AI Assistant
"""

import os
import re
from datetime import datetime

def convert_homework_file(source_path, target_path, hw_number):
    """Convert a single homework file from 2024 to 2025 with new styling"""
    
    # Read the source file
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the main content (problems) by finding content between \begin{document} and \end{document}
    doc_match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
    if not doc_match:
        print(f"Warning: Could not find document content in {source_path}")
        return
    
    document_content = doc_match.group(1).strip()
    
    # Extract due date from original file to update to 2025
    date_match = re.search(r'\\zhdate\{2024/(\d+)/(\d+)\}', content)
    if date_match:
        month, day = date_match.groups()
    else:
        # Default date if not found
        month, day = "10", "08"
    
    # Convert problems to hwproblem environment and fix \imath to \ii
    document_content = re.sub(r'\\begin\{problem\}', r'\\begin{hwproblem}{PROBLEM_NUM}', document_content)
    document_content = re.sub(r'\\end\{problem\}', r'\\end{hwproblem}\n\n\\vspace{0.5cm}', document_content)
    document_content = re.sub(r'\\imath', r'\\ii', document_content)
    
    # Remove old formatting commands that are handled by the style file
    lines_to_remove = [
        r'\\renewcommand\{\\labelenumi\}.*',
        r'\\renewcommand\{\\labelenumii\}.*',
    ]
    for pattern in lines_to_remove:
        document_content = re.sub(pattern, '', document_content)
    
    # Split problems and number them
    problems = re.split(r'\\begin\{hwproblem\}\{PROBLEM_NUM\}', document_content)
    
    # Rebuild content with proper problem numbering
    new_content = problems[0]  # content before first problem
    problem_count = 1
    
    for i in range(1, len(problems)):
        new_content += f'\\begin{{hwproblem}}{{{problem_count}}}'
        new_content += problems[i]
        problem_count += 1
    
    # Create the new file content with style file
    new_file_content = f"""\\documentclass[11pt]{{article}}

\\usepackage{{hw_style}}

% Set due date for this homework (updated to 2025)
\\setduedate{{{month}}}{{{day}}}

% Setup homework number and header
\\hwnumber{{{hw_number}}}

\\begin{{document}}

{new_content.strip()}

\\hwrequirements

\\end{{document}}"""
    
    # Write the new file
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_file_content)
    
    print(f"Converted {source_path} -> {target_path}")

def main():
    """Main conversion function"""
    source_dir = "/home/kluo/Documents/repos/kluo/mathphy/homework/2024"
    target_dir = "/home/kluo/Documents/repos/kluo/mathphy/homework/2025"
    
    # Ensure target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # Process all homework files
    for i in range(1, 11):  # hw1.tex to hw10.tex
        source_file = f"hw{i}.tex"
        source_path = os.path.join(source_dir, source_file)
        target_path = os.path.join(target_dir, source_file)
        
        if os.path.exists(source_path):
            convert_homework_file(source_path, target_path, i)
        else:
            print(f"Warning: {source_path} not found")
    
    # Also convert template file
    template_source = os.path.join(source_dir, "hw_template.tex")
    template_target = os.path.join(target_dir, "hw_template.tex")
    
    if os.path.exists(template_source):
        # Special handling for template
        template_content = """\\documentclass[11pt]{article}

\\usepackage{hw_style}

% Set due date for this homework (update as needed)
\\setduedate{11}{07}

% Setup homework number and header (change number as needed)
\\hwnumber{1}

\\begin{document}

\\begin{hwproblem}{1}

\\end{hwproblem}

\\vspace{0.5cm}

\\begin{hwproblem}{2}

\\end{hwproblem}

\\vspace{0.5cm}

\\begin{hwproblem}{3}

\\end{hwproblem}

\\vspace{0.5cm}

\\begin{hwproblem}{4}

\\end{hwproblem}

\\vspace{0.5cm}

\\begin{hwproblem}{5}

\\end{hwproblem}

\\vspace{0.5cm}

\\begin{hwproblem}{6}

\\end{hwproblem}

\\vspace{0.5cm}

\\begin{hwproblem}{7}

\\end{hwproblem}

\\vspace{0.5cm}

\\hwrequirements

\\end{document}"""
        
        with open(template_target, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        print(f"Created template: {template_target}")

if __name__ == "__main__":
    main()