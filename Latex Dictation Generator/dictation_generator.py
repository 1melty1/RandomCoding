# -*- coding: UTF-8 -*-
import random

# generator to generate cut list
def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    # min avoid over boundary
    yield list_a[i: min(len(list_a), i + chunk_size)]

def generate_table(shuffle, eng, chi, ans):
    if shuffle=='Y':
        random.shuffle(eng)
    table_content = ''
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
        print(table_content)
        
        table_content = ''

# prompt
print("""File format:
hello
goodbye
-
你好
再見
""")
route = input("directory of file(drag and drop file on terminal, \'\' can be included):")
f = open(f"{route[1:-1]}", "r")
# don't use split('\n')
eng_chi = f.read().splitlines()

eng = eng_chi[:eng_chi.index('-')]
chi = eng_chi[eng_chi.index('-')+1:]

shuffle = input("Shuffle?(Y/N) ")

# document head
print(r"""\documentclass[UTF8]{article}
\usepackage[fontset=ubuntu]{ctex}
\usepackage{geometry}
\geometry{a4paper, portrait, margin=0.5in}
\usepackage{tabularray}
\begin{document}
""")

shuffle = False
generate_table(shuffle, eng, chi, False)
generate_table(shuffle, eng, chi, True)

print(r"\end{document}")