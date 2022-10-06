# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# Декодинг RLE:

def decompressing(given_file): 
    decode = '' 
    count = '' 
    for char in given_file:
        char = str(char)
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 

    return decode


compressed_file = open('compressed.txt', 'r')
compressed_file = list(compressed_file)
print(compressed_file)
decoding = []
for i in range(len(compressed_file)):
    decoding.append(decompressing(compressed_file[i]))

decompressed_data = open('tocompress.txt', 'w')
for i in range(len(decoding)):
    decompressed_data.write(decoding[i])
print(decoding)