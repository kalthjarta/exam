import re

def file():
    f = open('kekus.txt', 'r')
    f1 = f.read()
    f.close()
    return f1

def number1(f1):
    searching = re.findall('.([А-Я]\. [А-Я][а-яё]+?)[^а-яё]', f1)
    for s in searching:
        print(s)
#задание 1

def number2(f1):
    searching = re.findall('.((?:(?:[А-Я]\. (?:[А-Я]\. )?)|(?:[А-Я][а-яё]+? ))[А-Я][а-яё]+?)[^а-яё]', f1)
    for s in searching:
        print(s)
    return searching

def main():
    final = file()
    number1(final)
    print('\n')
    number2(final)
#задание 2
    
if __name__=='__main__':
    main()
#запуск функций


    
    
