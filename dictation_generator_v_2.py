# -*- coding: UTF-8 -*-
import random, subprocess
from pathlib import Path

# generator to generate cut list
def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    # min avoid over boundary
    yield list_a[i: min(len(list_a), i + chunk_size)]

def generate_table(eng, chi, ans):
    table_content = ''
    doc = ''
    # cut eng into separate lists
    eng = list(split(eng, 40))
    chi = list(split(chi, 40))
    # for each sublist, generate a table
    for eng, chi in zip(eng, chi):
        i=0
        if ans:
            for eng_word, chi_word in zip(eng, chi):
                table_content += eng_word + ' & ' + chi_word
                if i==0:
                    table_content += ' & '
                else:
                    table_content += ' \\\\ \n'
                i = (i+1)%2
        else:
            for eng_word in eng:
                table_content += eng_word + ' & '
                if i==0:
                    table_content += ' & '
                else:
                    table_content += ' \\\\ \n'
                i = (i+1)%2    
        
        
        head = r"\begin{tblr}{hlines,vlines,row{1-" + str(int(len(eng)/2)+1) + "}={12mm},column{1-4}={37mm,c}}"
        tail = r"\end{tblr}" + '\n'
        table_content = head + table_content + tail
        doc += table_content
        
        table_content = ''
    return doc
  
# prompt
print("""File format:
hello
goodbye
-
你好
再見
""")
print("Name your text dict.txt and put it in the script directory")
print()

directory = str(Path(__file__).parent.resolve())
# do not use os.getcwd as directory, since it recognize the directory of the current py file in idle, but not in CMD (since the working
# directory is in user file when using CMD)

while True:
  try:
    print(f"Opening {directory}/dict.txt ...")
    f = open(f"{directory}/dict.txt")
  except OSError:
    print("\033[91mError: Name your text as dict.txt.")
    if input("\033[91mEnter any character to try again. Enter 0 to terminate._")=="0":
      exit()
    else:
      continue
  else:
    print("File is read successfully")
    break
  
# don't use split('\n')
eng_chi = f.read().splitlines()

eng = eng_chi[:eng_chi.index('-')]
chi = eng_chi[eng_chi.index('-')+1:]

# document head
head = r"""\documentclass[UTF8]{article}
\usepackage{xeCJK}
\setCJKmainfont{Songti SC}
\usepackage{geometry}
\geometry{a4paper, portrait, margin=0.5in}
\usepackage{tabularray}
\begin{document}
"""

doc = head + generate_table(eng=eng, chi=chi, ans=False) + "\n\\newpage\n\n" + generate_table(eng=eng, chi=chi, ans=True) + "\n\\end{document}"


doc_file = open(f"{directory}/Dict_questions.tex", "w")
doc_file.write(doc)
doc_file.close()

print("File write successfully.")

if (input("Is latex installed on this computer? (Y/N)") in ['Y', 'y']):
  print("Trying to compile latex to PDF(This only works when executing this script using terminal)...")
else:
  print("Program terminates.")


command = "xelatex -output-directory=" + directory + " " + directory + "/Dict_questions.tex"
# don't use os.system
#.run(command)
try:
  print(f"Creating PDF in", directory)
  a = []
  a = ["xelatex", f"-output-directory={directory}", f"{directory}/Dict_questions.tex"]
  print(f"Executing: {a}")
  print("\033[96m--------------------------------------------")
  subprocess.run(a)
  print("PDF compiled successfully. PDF is created in script path.")
except FileNotFoundError:
  print("\033[91mError: PDF generation failed. You may try to type the following command into CMD to manually generate PDF:")
  print("\033[96m", command)

print("Program terminates.")
