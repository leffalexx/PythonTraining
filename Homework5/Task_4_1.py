# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# Кодировка RLE:

def compressing(given_file):
    encoding = '' 
    prev_char = '' 
    count = 1 
    for char in given_file: 
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
                count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding

given_file = open('tocompress.txt', 'r')
given_file = list(given_file)
print(given_file)
encoding = []
for i in range(len(given_file)):
    encoding.append(compressing(given_file[i]))
print(encoding)
compressed_file = open('compressed.txt', 'w')
for i in range(len(encoding)):
    compressed_file.write(encoding[i])