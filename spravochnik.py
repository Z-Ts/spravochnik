from fileinput import close

def vvod():
    print ('введите имя фамилию телефон и описание')
    a1 = input()
    a1 = a1.split()
    return a1

def vopros():
    print ('добавить нового человека? да/нет')
    o = input ()
    if o == 'да':
        a = vvod()
        with open("base.txt", "a") as file:
            for  i in a:
                file.write( i + ' ')
            file.write(' \n')
        return vopros()
    if o == 'нет':
        exit
vopros()

print('вывести через пустую строку (п) или через ;')
p = input()


if p =='п':
    f= open('log.csv', 'w')
    with open('base.txt', 'r') as file:
        for n, line in enumerate(file, 1):
            line = line.rstrip('\n')
            f.write(line + '\n')
            f.write('' + '\n')
    f.close()
if p ==';':
    f= open('log.csv', 'w')
    with open('base.txt', 'r') as file:
        for n, line in enumerate(file, 1):
            line = line.rstrip('\n')
            f.write(line + ';' +'\n')
    f.close()