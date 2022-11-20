import os
from glob import glob
import regex

path = ''
filepaths = glob(f'{path}/**/*.hpp', recursive=True)
filepaths.extend(glob(f'{path}/**/*.cpp', recursive=True))
filepaths.sort()

func_pattern = [
    r'sin[fl]?',
    r'cos[fl]?',
    r'tan[fl]?',
    r'asin[fl]?',
    r'acos[fl]?',
    r'atan[fl]?',
    r'atan2[fl]?',
    r'exp[fl]?',
    r'log[fl]?',
    r'loq10[fl]?',
    r'log2[fl]?',
    r'pow[fl]?',
    r'sqrt[fl]?',
    r'cbrt[fl]?',
    r'hypot[fl]?',
    r'f?abs[fl]?',
    r'ceil[fl]?',
    r'floor[fl]?',
    r'trunc[fl]?',
    r'round[fl]?',
    r'f?mod[fl]?'
]

patterns = []
for fp in func_pattern:
    patterns.append(r'(?<!std::)(?<![a-zA-Z0-9])'+fp+r'(?=[ ]*\()')

ans = []

class Ans:
    def __init__(self, filepath, line, match):
        self.filepath = filepath
        self.line = line
        self.match = match


for filepath in filepaths:
    try:
        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()
    except:
        print(f'{filepath}')
        raise
    for i, line in enumerate(lines, 0):
        for pattern in patterns:
            match = regex.search(pattern, line)
            if match:
                ans.append(Ans(filepath, i+1, match))

for a in ans:
    file_name = a.filepath.split('\\')[-1]
    print(f'{file_name}:  {a.line}:  {a.match}')