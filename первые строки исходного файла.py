# программа1.py
input_file = "D:/corpus/ruwiki.xml-p1p224167"      
output_file = "D:/corpus/sample_text.txt"  
num_lines = 10000  

with open(input_file, 'r', encoding='utf-8', errors='ignore') as fin, \
     open(output_file, 'w', encoding='utf-8') as fout:
    for i, line in enumerate(fin):
        fout.write(line)
        if i >= num_lines - 1:
            break

print(f"Создан примерный файл {output_file} с {num_lines} строками")
