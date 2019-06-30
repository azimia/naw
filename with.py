with open('tst.txt', 'wt', encoding='utf-8') as inFile:
    try:
        num= int(input())
        line = str('1/'+ str(num) + ' = ' + str(1 / num))
        print(line)
        inFile.write(line)
    except ValueError:
        num='ля'
        inFile.write(num)
