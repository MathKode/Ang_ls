import random
choix = input('Mettre à jour la liste [1], Interrogation [2] -> ')
if choix == '1':
    file = open('ls.txt','r')
    contenu = file.read().split("\n")
    file.close()
    ls_c = []
    for i in contenu :
        l = i.split("=")
        i2 = ":".join(l)
        l2 = i2.split(":")
        try :
            l3 = []
            for i3 in l2:
                while i3[0] == ' ':
                    i3 = i3[1:]
                while i3[-1] == ' ':
                    i3 = i3[:-1]
                l3.append(i3.lower())
        except :
            print("ER")
        if len(l3) == 2 :
            ls_c.append(l3)
    final = []
    for i in ls_c:
        final.append(":".join(i))
    final = "\n".join(final)
    file = open("ls2.txt",'w')
    file.write(final)
    file.close()
if choix == '2':
    print('Write STOP to close the game and get your result')
    file = open('ls2.txt','r')
    contenu = file.read().split('\n')
    file.close()
    ls = []
    for i in contenu:
        ls.append(i.split(':'))
    score = 0
    total = 0
    oldnb = 0
    while True:
        nb = random.randint(0,len(ls)-1)
        lg = random.randint(0,1)
        rep = input(f'{ls[nb][lg]} -> ')
        lg += 1
        if lg == 2 :
            lg = 0
        if rep.lower() == ls[nb][lg]:
            print('TRUE : ',ls[nb][0],'->',ls[nb][1])
            score += 1
        elif rep == 'STOP':
            break
        elif rep == 'SUPP':
            del ls[nb]
            final = []
            for i in ls:
                final.append(":".join(i))
            final = "\n".join(final)
            file = open("ls2.txt","w")
            file.write(final)
            file.close()
        elif rep == 'MODIF':
            print(ls[oldnb])
            ls[oldnb][0] = input("1 -> ")
            ls[oldnb][1] = input("2 -> ")
            final = []
            for i in ls:
                final.append(":".join(i))
            final = "\n".join(final)
            file = open("ls2.txt","w")
            file.write(final)
            file.close()
            total -= 1
        else :
            print('FALSE : ',ls[nb][0],'->',ls[nb][1])
        oldnb = nb
        total += 1
    print(f'Score => {str(score)}/{str(total)}')
