def ext_func(text):
    def int_func(word: str):
        return word.title()

    words = text.split()
    return ' '.join(list(map(lambda word: int_func(word), words)))


print(ext_func('какая то там строка'))
'''Списано((('''
