delta = open('text.txt', 'w')
#print (delta.read (5))


delta.write('Hi, it\'s me')

#for line in delta:
#    print(line)
            
delta.close()

"""with open('gold.txt','w', encoding='utf-8') as File:
    for word in File:
        if word=='смелость':
            File.write('zlo')"""
