def encoder(text, shift):
    alp = False
    new_text = ''
    for c in text:
        if c in eng_letters:
            alp = True
            break
    if alp == True:
        for i in text:
            if i.isalpha() and i.islower():
                new_char = (ord(i) - ord('a') + shift) % 26 + ord('a')
                new_text += chr(new_char)
            elif i.isalpha() and i.isupper():
                new_char = (ord(i) - ord('A') + shift) % 26 + ord('A')
                new_text += chr(new_char)
            else:
                new_text += i
    else:
        for i in text:
            if i.isalpha() and i.islower():
                new_char = (ord(i) - ord('а') + shift) % 32 + ord('а')
                new_text += chr(new_char)
            elif i.isalpha() and i.isupper():
                new_char = (ord(i) - ord('А') + shift) % 32 + ord('А')
                new_text += chr(new_char)
            else:
                new_text += i
        
    return new_text


def decoder(text, shift):
    alp = False
    new_text = ''
    for c in text:
        if c in eng_letters:
            alp = True
            break
    if alp == True:
        for i in text:
            if i.isalpha() and i.islower():
                new_char = (ord(i) - ord('a') - shift) % 26 + ord('a')
                new_text += chr(new_char)
            elif i.isalpha() and i.isupper():
                new_char = (ord(i) - ord('A') - shift) % 26 + ord('A')
                new_text += chr(new_char)
            else:
                new_text += i
    else:
        for i in text:
            if i.isalpha() and i.islower():
                new_char = (ord(i) - ord('а') - shift) % 32 + ord('а')
                new_text += chr(new_char)
            elif i.isalpha() and i.isupper():
                new_char = (ord(i) - ord('А') - shift) % 32 + ord('А')
                new_text += chr(new_char)
            else:
                new_text += i
    return new_text

rus_letters = 'йцукенгшщзхъфывапролджэяячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
eng_letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
what = input('декодировать или закодировать сообщение: ')
text = input('введите текст: ')
shift = int(input('введите ключ: '))
if what == 'декодировать':
    print(decoder(text,shift))
elif what == 'закодировать':
    print(encoder(text, shift))
else:
    print('error/ошибка')