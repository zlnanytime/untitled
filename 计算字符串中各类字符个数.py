s = input('input a string:\n')
letters = 0
speace = 0
digit = 0
other = 0
arr_letters = []
arr_digit = []
arr_other = []
for i in s:
    if i.isalpha():
        letters+=1
        arr_letters.append(i)
    elif i.isspace():
        speace+=1
    elif i.isnumeric():
        digit+=1
        arr_digit.append(i)
    else:
        other+=1
        arr_other.append(i)
print('英文字符：')
for b in range(len(arr_letters)):
    print(str(arr_letters[b]+'\t'),end='')
print('\n数字字符:')
for c in range(len(arr_digit)):
    print(str(arr_digit[c] + '\t'), end='')
print('\n其他字符:')
for d in range(len(arr_other)):
    print(str(arr_other[d] + '\t'), end='')
print('\n英文：%s,空格：%s,数字：%s,其他：%s' % (letters,speace,digit,other))