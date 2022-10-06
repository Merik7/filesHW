READLINES_COUNT = {}


f1 = open('1.txt', encoding='utf8')
READLINES_COUNT['1.txt'] = len(f1.readlines())
f1.close()

f2 = open('2.txt', encoding='utf8')
READLINES_COUNT['2.txt'] = len(f2.readlines())
f2.close()

f3 = open('3.txt', encoding='utf8')
READLINES_COUNT['3.txt'] = len(f3.readlines())
f3.close()

sorted_READLINES_COUNT = {}
sorted_keys = sorted(READLINES_COUNT, key=READLINES_COUNT.get)
for i in sorted_keys:
    sorted_READLINES_COUNT[i] = READLINES_COUNT[i]


with open('result.txt', 'w', encoding='utf8') as file:
    for file_name, readline_count in sorted_READLINES_COUNT.items():
        f = open(file_name, encoding='utf8')
        file.write(f'{file_name}\n')
        file.write(f'{readline_count}\n')
        file.write(f'{f.read()}\n')
        f.close()
