escort=''
with open('gold.txt', 'r', encoding='utf-8') as File:
    for word in File:
        escort=word
alp=["q","w",'e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',"Q","W",'E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

words="England"
long=len(words)
delta = open('gold.txt', 'w')
delta.close
toch = 0
cif=0
slovo=""
with open('gold.txt', 'a', encoding='utf-8') as File:
    for line in escort:
        if line in alp:
            slovo+=line
        elif slovo == words:
            File.write(" Kg ")
            slovo=""
            continue
        else:
            print(slovo)
            File.write(slovo+" ")
            slovo=""
    for line in range(1):
        if line in alp:
            slovo+=line
        elif slovo == words:
            File.write(" Kg ")
            slovo=""
            continue
        else:
            print(slovo)
            File.write(slovo+" ")
            slovo=""
                
        
        

            
                
        
