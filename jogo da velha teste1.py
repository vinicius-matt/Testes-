from random import choice
from random import randint
from random import  choices
from time import sleep
 
''' NÃO FINALIZADO ! '''
 
xo = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
xatack = []
iainicio = empate = vez = vit = der = emp = vtx = vto =0
vencedor = 'ninguém'
iaxo = iafn = dif = 'nada'
cx = '\033[1;37m'
co = '\033[1;37m'
cor = '\033[1m'
vd = '\033[32m'
vm = '\033[31m'
print('[1] Jogar sozinho\n'
'[2] Jogar com mais alguém')
modo = int(input('Opção: '))
ialista = [1,2,3,4,5,6,7,8,9]
if modo == 1:
    while True:
        print('X ou O?')
        iaxo = str(input()).lower().strip()[:1]
        if iaxo in 'xo':
            break
    while True:
        print('Normal/Impossível? [N/I]')
        iafn = str(input()).lower().strip()[:1]
        if iafn in 'ni':
            dif = iafn
            break
while True:
    rodadas = int(input('Quantas partidas? '))
    if rodadas > 0: break
print("\n"*40+f'''\033[1m
                                              |     |      
                                           {co}{'1'+cor}  |  {co}{'2'+cor}  |  {co}{'3'+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {co}{'4'+cor}  |  {co}{'5'+cor}  |  {co}{'6'+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {co}{'7'+cor}  |  {co}{'8'+cor}  |  {co}{'9'+cor}  
                                              |     |    
                                       
                                       
                                       
                                       
                                       
                                       
                                  \033[37m Pressione \033[34;1mEnter\033[37m para continuar >>\033[1m''')
print('\n'*9)
input()
cx = '\033[1;32m'
co = '\033[1;31m'
segundo = vez = choice([0, 1])
for c in range(0, rodadas):
    vd = '\033[32m'
    vm = '\033[31m'
    cx = '\033[1;32m'
    co = '\033[1;31m'
    if segundo == 0:
        vez = 1
    else: vez = 0
    segundo = vez
    while True:
        t = randint(1,3)
        if vez == 0:
            print('\n'*8)
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |      
                                           {cx if xo[1] in 'X ' else co}{xo[1]+cor}  |  {cx if xo[2] in 'X ' else co}{xo[2]+cor}  |  {cx if xo[3] in 'X ' else co}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {cx if xo[4] in 'X ' else co}{xo[4]+cor}  |  {cx if xo[5] in 'X ' else co}{xo[5]+cor}  |  {cx if xo[6] in 'X ' else co}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {cx if xo[7] in 'X ' else co}{xo[7]+cor}  |  {cx if xo[8] in 'X ' else co}{xo[8]+cor}  |  {cx if xo[9] in 'X ' else co}{xo[9]+cor}  
                                              |     |     ''')
            print('\n\n'+' '*46+'Jogador \033[32;1mX\033[1m')
            if iaxo == 'o':
                print('\n'*4+' '*45+'\033[1mPensando...'+'\n'*9)
                sleep(t)
                if iafn == 'i':
                    if segundo == 0:
                        if iainicio == 0:
                            x = choice([1,1,2,3,3,4,5,5,5,6,7,7,8,9,9])
                        elif iainicio == 2:
                            if xatack[0] == 1:
                                if xatack[1] == 5 or xatack[1] == 7 or xatack[1] == 3:
                                    x = 9
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    x = 7
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    x = 3
                                elif xatack[1] == 9:
                                    x = choice([7,3])
                            elif xatack[0] == 2:
                                if xatack[1] == 7 or xatack[1] == 4:
                                    x = 1
                                elif xatack[1] == 9 or xatack[1] == 6:
                                    x = 3
                                elif xatack[1] == 1 or xatack[1] == 3:
                                    x = 5
                                elif xatack[1] == 8:
                                    x = choice([4, 6])
                                elif xatack[1] == 5:
                                    x = choice([1, 3])
                                    iafn = 'n'
                            elif xatack[0] == 3:
                                if xatack[1] == 5 or xatack[1] == 1 or xatack[1] == 9:
                                    x = 7
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    x = 9
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    x = 1
                                elif xatack[1] == 7:
                                    x = choice([1,9])
                            elif xatack[0] == 4:
                                if xatack[1] == 9 or xatack[1] == 8:
                                    x = 7
                                elif xatack[1] == 3 or xatack[1] == 2:
                                    x = 1
                                elif xatack[1] == 7 or xatack[1] == 1:
                                    x = 5
                                elif xatack[1] == 6:
                                    x = choice([8, 2])
                                elif xatack[1] == 5:
                                    x = choice([7, 1])
                                    iafn = 'n'
                            elif xatack[0] == 5:
                                if xatack[1] == 2:
                                    x = choice([3, 1])
                                elif xatack[1] == 4:
                                    x = choice([1, 7])
                                elif xatack[1] == 8:
                                    x = choice([7, 9])
                                elif xatack[1] == 6:
                                    x = choice([9, 3])
                                elif xatack[1] == 1:
                                    x = 9
                                elif xatack[1] == 3:
                                    x = 7
                                elif xatack[1] == 7:
                                    x = 3
                                elif xatack[1] == 9:
                                    x = 1
                            elif xatack[0] == 6:
                                if xatack[1] == 1 or xatack[1] == 2:
                                    x = 3
                                elif xatack[1] == 7 or xatack[1] == 8:
                                    x = 9
                                elif xatack[1] == 3 or xatack[1] == 9:
                                    x = 5
                                elif xatack[1] == 8:
                                    x = choice([2, 8])
                                elif xatack[1] == 5:
                                    x = choice([3, 9])
                                    iafn = 'n'
                            elif xatack[0] == 7:
                                if xatack[1] == 5 or xatack[1] == 1 or xatack[1] == 9:
                                    x = 3
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    x = 1
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    x = 9
                                elif xatack[1] == 7:
                                    x = choice([1,9])
                            elif xatack[0] == 8:
                                if xatack[1] == 3 or xatack[1] == 6:
                                    x = 9
                                elif xatack[1] == 1 or xatack[1] == 6:
                                    x = 7
                                elif xatack[1] == 9 or xatack[1] == 7:
                                    x = 5
                                elif xatack[1] == 2:
                                    x = choice([6, 4])
                                elif xatack[1] == 5:
                                    x = choice([9, 7])
                                    iafn = 'n'
                            elif xatack[0] == 9:
                                if xatack[1] == 5 or xatack[1] == 7 or xatack[1] == 3:
                                    x = 1
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    x = 3
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    x = 7
                                elif xatack[1] == 1:
                                    x = choice([7,3])
 
                            xatack.append(x)
 
                        elif iainicio == 4:
                            if xatack[0] == 1:
                                if xatack[1] == 9:
                                    if xatack[2] == 7:
                                        if xatack[3] == 4:
                                            x = 3
                                        else:
                                            x = 4
                                    else:
                                        if xatack[3] == 2:
                                            x = 7
                                        else:
                                            x = 2
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 2:
                                        x = 5
                                    else:
                                        x = 2
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 3:
                                        x = 7
                                    elif xatack[3] == 7:
                                        x = 3
                                    else:
                                        if xatack[3] == 2:
                                            x = 8
                                        elif xatack[3] == 4:
                                            x = 6
                                        elif xatack[3] == 8:
                                            x = 2
                                        elif xatack[3] == 6:
                                            x = 4
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 4:
                                        x = 5
                                    else:
                                        x = 4
                                    iafn = 'n'
                                elif xatack[1] == 7:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 3
                                    iafn = 'n'
                                elif xatack[1] == 3:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 7
                                    iafn = 'n'
                            elif xatack[0] == 2:
                                if xatack[1] == 9 or xatack[1] == 6:
                                    if xatack[3] == 1:
                                        x = 5
                                    else:
                                        x = 1
                                    iafn = 'n'
                                elif xatack[1] == 7 or xatack[1] == 4:
                                    if xatack[3] == 3:
                                        x = 5
                                    else:
                                        x = 3
                                    iafn = 'n'
                                elif xatack[1] == 1 or xatack[1] == 3:
                                    if xatack[3] == 8:
                                        if xatack[1] == 1:
                                            x = 7
                                        else:
                                            x = 9
                                        iafn = 'n'
                                    else:
                                        x = 8
                                elif xatack[1] == 8:
                                    if xatack[3] == 7:
                                        x = 9
                                    elif xatack[3] == 9:
                                        x = 7
                                    elif xatack [3] == 5:
                                        if xatack[2] == 4:
                                            x = 1
                                        else:
                                            x = 3
                                    elif xatack[3] == 1 or xatack[3] == 3:
                                        x = 5
                                    iafn = 'n'
                            elif xatack[0] == 3:
                                if xatack[1] == 7:
                                    if xatack[2] == 1:
                                        if xatack[3] == 2:
                                            x = 9
                                        else:
                                            x = 2
                                    else:
                                        if xatack[3] == 6:
                                            x = 1
                                        else:
                                            x = 6
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 1:
                                        x = 9
                                    elif xatack[3] == 9:
                                        x = 1
                                    else:
                                        if xatack[3] == 2:
                                            x = 8
                                        elif xatack[3] == 4:
                                            x = 6
                                        elif xatack[3] == 8:
                                            x = 2
                                        elif xatack[3] == 6:
                                            x = 4
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 2:
                                        x = 5
                                    else:
                                        x = 2
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 6:
                                        x = 5
                                    else:
                                        x = 6
                                    iafn = 'n'
                                elif xatack[1] == 9:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 1
                                    iafn = 'n'
                                elif xatack[1] == 1:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 9
                                    iafn = 'n'
                            elif xatack[0] == 4:
                                if xatack[1] == 3 or xatack[1] == 2:
                                    if xatack[3] == 7:
                                        x = 5
                                    else:
                                        x = 7
                                    iafn = 'n'
                                elif xatack[1] == 9 or xatack[1] == 8:
                                    if xatack[3] == 1:
                                        x = 5
                                    else:
                                        x = 1
                                    iafn = 'n'
                                elif xatack[1] == 7 or xatack[1] == 1:
                                    if xatack[3] == 6:
                                        if xatack[1] == 7:
                                            x = 9
                                        else:
                                            x = 3
                                        iafn = 'n'
                                    else:
                                        x = 6
                                elif xatack[1] == 6:
                                    if xatack[3] == 9:
                                        x = 3
                                    elif xatack[3] == 3:
                                        x = 9
                                    elif xatack [3] == 5:
                                        if xatack[2] == 8:
                                            x = 7
                                        else:
                                            x = 1
                                    elif xatack[3] == 7 or xatack[3] == 1:
                                        x = 5
                                    iafn = 'n'
                            elif xatack[0] == 5:
                                if xatack[1] == 1:
                                    if xatack[3] != 7 or xatack[3] != 3:
                                        if xatack[3] == 4 or xatack[3] == 6:
                                            x = 7
                                        elif xatack[3] == 2 or xatack[3] == 8:
                                            x = 3
                                    elif xatack[3] == 7:
                                        x = 4
                                    else:
                                        x = 2
                                elif xatack[1] == 2:
                                    if xatack[2] == 1:
                                        if xatack[3] == 9:
                                            x = 7
                                        else:
                                            x = 9
                                    elif xatack[2] == 3:
                                        if xatack[3] == 7:
                                            x = 9
                                        else:
                                            x = 7
                                elif xatack[1] == 3:
                                    if xatack[3] != 1 or xatack[3] != 9:
                                        if xatack[3] == 2 or xatack[3] == 8:
                                            x = 1
                                        elif xatack[3] == 6 or xatack[3] == 4:
                                            x = 9
                                    elif xatack[3] == 1:
                                        x = 2
                                    else:
                                        x = 6
                                elif xatack[1] == 4:
                                    if xatack[2] == 7:
                                        if xatack[3] == 3:
                                            x = 9
                                        else:
                                            x = 3
                                    elif xatack[2] == 1:
                                        if xatack[3] == 9:
                                            x = 3
                                        else:
                                            x = 9
                                elif xatack[1] == 6:
                                    if xatack[2] == 3:
                                        if xatack[3] == 7:
                                            x = 1
                                        else:
                                            x = 7
                                    elif xatack[2] == 9:
                                        if xatack[3] == 1:
                                            x = 7
                                        else:
                                            x = 1
                                elif xatack[1] == 7:
                                    if xatack[3] != 9 or xatack[3] != 1:
                                        if xatack[3] == 8 or xatack[3] == 2:
                                            x = 9
                                        elif xatack[3] == 4 or xatack[3] == 6:
                                            x = 1
                                    elif xatack[3] == 9:
                                        x = 8
                                    else:
                                        x = 4
                                elif xatack[1] == 8:
                                    if xatack[2] == 9:
                                        if xatack[3] == 1:
                                            x = 3
                                        else:
                                            x = 1
                                    elif xatack[2] == 7:
                                        if xatack[3] == 3:
                                            x = 1
                                        else:
                                            x = 3
                                elif xatack[1] == 9:
                                    if xatack[3] != 3 or xatack[3] != 7:
                                        if xatack[3] == 6 or xatack[3] == 4:
                                            x = 3
                                        elif xatack[3] == 8 or xatack[3] == 2:
                                            x = 7
                                    elif xatack[3] == 3:
                                        x = 2
                                    else:
                                        x = 4
                                iafn = 'n'
                            elif xatack[0] == 6:
                                if xatack[1] == 7 or xatack[1] == 8:
                                    if xatack[3] == 3:
                                        x = 5
                                    else:
                                        x = 3
                                    iafn = 'n'
                                elif xatack[1] == 1 or xatack[1] == 2:
                                    if xatack[3] == 9:
                                        x = 5
                                    else:
                                        x = 9
                                    iafn = 'n'
                                elif xatack[1] == 3 or xatack[1] == 9:
                                    if xatack[3] == 4:
                                        if xatack[1] == 3:
                                            x = 1
                                        else:
                                            x = 7
                                        iafn = 'n'
                                    else:
                                        x = 4
                                elif xatack[1] == 4:
                                    if xatack[3] == 1:
                                        x = 7
                                    elif xatack[3] == 7:
                                        x = 1
                                    elif xatack [3] == 5:
                                        if xatack[2] == 2:
                                            x = 3
                                        else:
                                            x = 9
                                    elif xatack[3] == 3 or xatack[3] == 9:
                                        x = 5
                                    iafn = 'n'
                            elif xatack[0] == 7:
                                if xatack[1] == 3:
                                    if xatack[2] == 1:
                                        if xatack[3] == 4:
                                            x = 9
                                        else:
                                            x = 4
                                    else:
                                        if xatack[3] == 8:
                                            x = 1
                                        else:
                                            x = 8
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 1:
                                        x = 9
                                    elif xatack[3] == 9:
                                        x = 1
                                    else:
                                        if xatack[3] == 2:
                                            x = 8
                                        elif xatack[3] == 4:
                                            x = 6
                                        elif xatack[3] == 8:
                                            x = 2
                                        elif xatack[3] == 6:
                                            x = 4
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 8:
                                        x = 5
                                    else:
                                        x = 8
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 4:
                                        x = 5
                                    else:
                                        x = 4
                                    iafn = 'n'
                                elif xatack[1] == 9:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 1
                                    iafn = 'n'
                                elif xatack[1] == 1:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 9
                                    iafn = 'n'
                            elif xatack[0] == 8:
                                if xatack[1] == 1 or xatack[1] == 4:
                                    if xatack[3] == 9:
                                        x = 5
                                    else:
                                        x = 9
                                    iafn = 'n'
                                elif xatack[1] == 3 or xatack[1] == 6:
                                    if xatack[3] == 7:
                                        x = 5
                                    else:
                                        x = 7
                                    iafn = 'n'
                                elif xatack[1] == 9 or xatack[1] == 7:
                                    if xatack[3] == 2:
                                        if xatack[1] == 9:
                                            x = 3
                                        else:
                                            x = 1
                                        iafn = 'n'
                                    else:
                                        x = 2
                                elif xatack[1] == 2:
                                    if xatack[3] == 3:
                                        x = 1
                                    elif xatack[3] == 1:
                                        x = 3
                                    elif xatack [3] == 5:
                                        if xatack[2] == 6:
                                            x = 9
                                        else:
                                            x = 7
                                    elif xatack[3] == 9 or xatack[3] == 7:
                                        x = 5
                                    iafn = 'n'
                            elif xatack[0] == 9:
                                if xatack[1] == 1:
                                    if xatack[2] == 7:
                                        if xatack[3] == 8:
                                            x = 3
                                        else:
                                            x = 8
                                    else:
                                        if xatack[3] == 6:
                                            x = 7
                                        else:
                                            x = 6
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 2:
                                        x = 5
                                    else:
                                        x = 2
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 3:
                                        x = 7
                                    elif xatack[3] == 7:
                                        x = 3
                                    else:
                                        if xatack[3] == 2:
                                            x = 8
                                        elif xatack[3] == 4:
                                            x = 6
                                        elif xatack[3] == 8:
                                            x = 2
                                        elif xatack[3] == 6:
                                            x = 4
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 6:
                                        x = 5
                                    else:
                                        x = 6
                                elif xatack[1] == 7:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 3
                                    iafn = 'n'
                                elif xatack[1] == 3:
                                    if xatack[3] != 5:
                                        x = 5
                                    else:
                                        x = 7
                                    iafn = 'n'
 
                    else:
                        if iainicio == 1:
                            if xatack[0] == 1 or xatack[0] == 3 or xatack[0] == 7 or xatack[0] == 9:
                                x = 5
                            elif xatack[0] == 2 or xatack[0] == 4 or xatack[0] == 6 or xatack[0] == 8:
                                if xatack[0] == 2:
                                    x = 8
                                elif xatack[0] == 4:
                                    x = 6
                                elif xatack[0] == 6:
                                    x = 4
                                else:
                                    x = 2
                                iafn = 'n'
                            else:
                                x = choice([1, 3, 7, 9])
                                iafn = 'n'
                        elif iainicio == 3:
                            if xatack[2] == 1:
                                if xatack[1] == 9:
                                    x = choice([7, 3])
                            elif xatack[2] == 3:
                                if xatack[1] == 7:
                                    x = choice([1, 9])
                            elif xatack[2] == 7:
                                if xatack[1] == 3:
                                    x = choice([1, 9])
                            elif xatack[2] == 9:
                                if xatack[1] == 1:
                                    x = choice([7, 3])
                            iafn = 'n'
                        else:
                            iafn = 'n'
 
                elif iafn == 'n':
 
                    if ((xo[2] == 'X' and xo[3] == 'X') or (xo[9] == 'X' and xo[5] == 'X') or (xo[4] == 'X' and xo[7] == 'X')) and xo[1] not in 'XO': x = 1
                    elif ((xo[1] == 'X' and xo[3] == 'X') or (xo[8] == 'X' and xo[5] == 'X')) and xo[2] not in 'XO': x = 2
                    elif ((xo[1] == 'X' and xo[2] == 'X') or (xo[7] == 'X' and xo[5] == 'X') or (xo[9] == 'X' and xo[6] == 'X')) and xo[3] not in 'XO': x = 3
                    elif ((xo[1] == 'X' and xo[7] == 'X') or (xo[5] == 'X' and xo[6] == 'X')) and xo[4] not in 'XO': x = 4
                    elif ((xo[1] == 'X' and xo[9] == 'X') or (xo[2] == 'X' and xo[8] == 'X') or (xo[3] == 'X' and xo[7] == 'X') or (xo[4] == 'X' and xo[6] == 'X')) and xo[5] not in 'XO': x = 5
                    elif ((xo[3] == 'X' and xo[9] == 'X') or (xo[4] == 'X' and xo[5] == 'X')) and xo[6] not in 'XO': x = 6
                    elif ((xo[1] == 'X' and xo[4] == 'X') or (xo[3] == 'X' and xo[5] == 'X') or (xo[8] == 'X' and xo[9] == 'X')) and xo[7] not in 'XO': x = 7
                    elif ((xo[2] == 'X' and xo[5] == 'X') or (xo[7] == 'X' and xo[9] == 'X')) and xo[8] not in 'XO': x = 8
                    elif ((xo[1] == 'X' and xo[5] == 'X') or (xo[3] == 'X' and xo[6] == 'X') or (xo[7] == 'X' and xo[8] == 'X')) and xo[9] not in 'XO': x = 9
 
                    elif ((xo[2] == 'O' and xo[3] == 'O') or (xo[9] == 'O' and xo[5] == 'O') or (xo[4] == 'O' and xo[7] == 'O')) and xo[1] not in 'XO': x = 1
                    elif ((xo[1] == 'O' and xo[3] == 'O') or (xo[8] == 'O' and xo[5] == 'O')) and xo[2] not in 'XO': x = 2
                    elif ((xo[1] == 'O' and xo[3] == 'O') or (xo[7] == 'O' and xo[5] == 'O') or (xo[9] == 'O' and xo[6] == 'O')) and xo[3] not in 'XO': x = 3
                    elif ((xo[1] == 'O' and xo[7] == 'O') or (xo[5] == 'O' and xo[6] == 'O')) and xo[4] not in 'XO': x = 4
                    elif ((xo[1] == 'O' and xo[9] == 'O') or (xo[2] == 'O' and xo[8] == 'O') or (xo[3] == 'O' and xo[7] == 'O') or (xo[4] == 'O' and xo[6] == 'O')) and xo[5] not in 'XO': x = 5
                    elif ((xo[3] == 'O' and xo[9] == 'O') or (xo[4] == 'O' and xo[5] == 'O')) and xo[6] not in 'XO': x = 6
                    elif ((xo[1] == 'O' and xo[4] == 'O') or (xo[3] == 'O' and xo[5] == 'O') or (xo[8] == 'O' and xo[9] == 'O')) and xo[7] not in 'XO': x = 7
                    elif ((xo[2] == 'O' and xo[5] == 'O') or (xo[7] == 'O' and xo[9] == 'O')) and xo[8] not in 'XO': x = 8
                    elif ((xo[1] == 'O' and xo[5] == 'O') or (xo[3] == 'O' and xo[6] == 'O') or (xo[7] == 'O' and xo[8] == 'O')) and xo[9] not in 'XO': x = 9
 
                    else:
                        x = choice(ialista)
                else:
                    x = choice(ialista)
            else:
                x = int(input('\n'*14+' '*46+'Quadrado: '))
            if xo[x] not in 'XO':
                xatack.append(x)
                iainicio += 1
                xo.pop(x)
                xo.insert(x, 'X')
                vez = 1
                empate += 1
                if ((xo[1] == 'X' and xo[2] == 'X' and xo[3] == 'X') or
                    (xo[1] == 'X' and xo[5] == 'X' and xo[9] == 'X') or
                    (xo[1] == 'X' and xo[4] == 'X' and xo[7] == 'X') or
                    (xo[4] == 'X' and xo[5] == 'X' and xo[6] == 'X') or
                    (xo[7] == 'X' and xo[8] == 'X' and xo[9] == 'X') or
                    (xo[2] == 'X' and xo[5] == 'X' and xo[8] == 'X') or
                    (xo[3] == 'X' and xo[6] == 'X' and xo[9] == 'X') or
                    (xo[3] == 'X' and xo[5] == 'X' and xo[7] == 'X')):
                    vencedor = 'X'
                    break
                elif empate == 9:
                    break
                if x in ialista:
                    ialista.remove(x)
            else:
                vez = 0
                if x in ialista:
                    ialista.remove(x)
        if vez == 1:
            print('\n'*13)
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |      
                                           {cx if xo[1] in 'X ' else co}{xo[1]+cor}  |  {cx if xo[2] in 'X ' else co}{xo[2]+cor}  |  {cx if xo[3] in 'X ' else co}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {cx if xo[4] in 'X ' else co}{xo[4]+cor}  |  {cx if xo[5] in 'X ' else co}{xo[5]+cor}  |  {cx if xo[6] in 'X ' else co}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {cx if xo[7] in 'X ' else co}{xo[7]+cor}  |  {cx if xo[8] in 'X ' else co}{xo[8]+cor}  |  {cx if xo[9] in 'X ' else co}{xo[9]+cor}  
                                              |     |     ''')
            print('\n\n' + ' ' * 46 + 'Jogador \033[1;31mO\033[1m')
            if iaxo == 'x':
                print('\n'*4+' '*45+'\033[1mPensando...'+'\n'*9)
                sleep(t)
                if iafn == 'i':
                    if segundo == 1:
                        if iainicio == 0:
                            o = choice([1,1,2,3,3,4,5,5,5,6,7,7,8,9,9])
                        elif iainicio == 2:
                            if xatack[0] == 1:
                                if xatack[1] == 5 or xatack[1] == 7 or xatack[1] == 3:
                                    o = 9
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    o = 7
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    o = 3
                                elif xatack[1] == 9:
                                    o = choice([7,3])
                            elif xatack[0] == 2:
                                if xatack[1] == 7 or xatack[1] == 4:
                                    o = 1
                                elif xatack[1] == 9 or xatack[1] == 6:
                                    o = 3
                                elif xatack[1] == 1 or xatack[1] == 3:
                                    o = 5
                                elif xatack[1] == 8:
                                    o = choice([4, 6])
                                elif xatack[1] == 5:
                                    o = choice([1, 3])
                                    iafn = 'n'
                            elif xatack[0] == 3:
                                if xatack[1] == 5 or xatack[1] == 1 or xatack[1] == 9:
                                    o = 7
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    o = 9
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    o = 1
                                elif xatack[1] == 7:
                                    o = choice([1,9])
                            elif xatack[0] == 4:
                                if xatack[1] == 9 or xatack[1] == 8:
                                    o = 7
                                elif xatack[1] == 3 or xatack[1] == 2:
                                    o = 1
                                elif xatack[1] == 7 or xatack[1] == 1:
                                    o = 5
                                elif xatack[1] == 6:
                                    o = choice([8, 2])
                                elif xatack[1] == 5:
                                    o = choice([7, 1])
                                    iafn = 'n'
                            elif xatack[0] == 5:
                                if xatack[1] == 2:
                                    o = choice([3, 1])
                                elif xatack[1] == 4:
                                    o = choice([1, 7])
                                elif xatack[1] == 8:
                                    o = choice([7, 9])
                                elif xatack[1] == 6:
                                    o = choice([9, 3])
                                elif xatack[1] == 1:
                                    o = 9
                                elif xatack[1] == 3:
                                    o = 7
                                elif xatack[1] == 7:
                                    o = 3
                                elif xatack[1] == 9:
                                    o = 1
                            elif xatack[0] == 6:
                                if xatack[1] == 1 or xatack[1] == 2:
                                    o = 3
                                elif xatack[1] == 7 or xatack[1] == 8:
                                    o = 9
                                elif xatack[1] == 3 or xatack[1] == 9:
                                    o = 5
                                elif xatack[1] == 8:
                                    o = choice([2, 8])
                                elif xatack[1] == 5:
                                    o = choice([3, 9])
                                    iafn = 'n'
                            elif xatack[0] == 7:
                                if xatack[1] == 5 or xatack[1] == 1 or xatack[1] == 9:
                                    o = 3
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    o = 1
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    o = 9
                                elif xatack[1] == 7:
                                    o = choice([1,9])
                            elif xatack[0] == 8:
                                if xatack[1] == 3 or xatack[1] == 6:
                                    o = 9
                                elif xatack[1] == 1 or xatack[1] == 6:
                                    o = 7
                                elif xatack[1] == 9 or xatack[1] == 7:
                                    o = 5
                                elif xatack[1] == 2:
                                    o = choice([6, 4])
                                elif xatack[1] == 5:
                                    o = choice([9, 7])
                                    iafn = 'n'
                            elif xatack[0] == 9:
                                if xatack[1] == 5 or xatack[1] == 7 or xatack[1] == 3:
                                    o = 1
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    o = 3
                                elif xatack[1] == 4 or xatack[1] == 6:
                                    o = 7
                                elif xatack[1] == 1:
                                    o = choice([7,3])
 
 
                        elif iainicio == 4:
                            if xatack[0] == 1:
                                if xatack[1] == 9:
                                    if xatack[2] == 7:
                                        if xatack[3] == 4:
                                            o = 3
                                        else:
                                            o = 4
                                    else:
                                        if xatack[3] == 2:
                                            o = 7
                                        else:
                                            o = 2
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 2:
                                        o = 5
                                    else:
                                        o = 2
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 3:
                                        o = 7
                                    elif xatack[3] == 7:
                                        o = 3
                                    else:
                                        if xatack[3] == 2:
                                            o = 8
                                        elif xatack[3] == 4:
                                            o = 6
                                        elif xatack[3] == 8:
                                            o = 2
                                        elif xatack[3] == 6:
                                            o = 4
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 4:
                                        o = 5
                                    else:
                                        o = 4
                                    iafn = 'n'
                                elif xatack[1] == 7:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 3
                                    iafn = 'n'
                                elif xatack[1] == 3:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 7
                                    iafn = 'n'
                            elif xatack[0] == 2:
                                if xatack[1] == 9 or xatack[1] == 6:
                                    if xatack[3] == 1:
                                        o = 5
                                    else:
                                        o = 1
                                    iafn = 'n'
                                elif xatack[1] == 7 or xatack[1] == 4:
                                    if xatack[3] == 3:
                                        o = 5
                                    else:
                                        o = 3
                                    iafn = 'n'
                                elif xatack[1] == 1 or xatack[1] == 3:
                                    if xatack[3] == 8:
                                        if xatack[1] == 1:
                                            o = 7
                                        else:
                                            o = 9
                                        iafn = 'n'
                                    else:
                                        o = 8
                                elif xatack[1] == 8:
                                    if xatack[3] == 7:
                                        o = 9
                                    elif xatack[3] == 9:
                                        o = 7
                                    elif xatack [3] == 5:
                                        if xatack[2] == 4:
                                            o = 1
                                        else:
                                            o = 3
                                    elif xatack[3] == 1 or xatack[3] == 3:
                                        o = 5
                                    iafn = 'n'
                            elif xatack[0] == 3:
                                if xatack[1] == 7:
                                    if xatack[2] == 1:
                                        if xatack[3] == 2:
                                            o = 9
                                        else:
                                            o = 2
                                    else:
                                        if xatack[3] == 6:
                                            o = 1
                                        else:
                                            o = 6
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 1:
                                        o = 9
                                    elif xatack[3] == 9:
                                        o = 1
                                    else:
                                        if xatack[3] == 2:
                                            o = 8
                                        elif xatack[3] == 4:
                                            o = 6
                                        elif xatack[3] == 8:
                                            o = 2
                                        elif xatack[3] == 6:
                                            o = 4
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 2:
                                        o = 5
                                    else:
                                        o = 2
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 6:
                                        o = 5
                                    else:
                                        o = 6
                                    iafn = 'n'
                                elif xatack[1] == 9:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 1
                                    iafn = 'n'
                                elif xatack[1] == 1:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 9
                                    iafn = 'n'
                            elif xatack[0] == 4:
                                if xatack[1] == 3 or xatack[1] == 2:
                                    if xatack[3] == 7:
                                        o = 5
                                    else:
                                        o = 7
                                    iafn = 'n'
                                elif xatack[1] == 9 or xatack[1] == 8:
                                    if xatack[3] == 1:
                                        o = 5
                                    else:
                                        o = 1
                                    iafn = 'n'
                                elif xatack[1] == 7 or xatack[1] == 1:
                                    if xatack[3] == 6:
                                        if xatack[1] == 7:
                                            o = 9
                                        else:
                                            o = 3
                                        iafn = 'n'
                                    else:
                                        o = 6
                                elif xatack[1] == 6:
                                    if xatack[3] == 9:
                                        o = 3
                                    elif xatack[3] == 3:
                                        o = 9
                                    elif xatack [3] == 5:
                                        if xatack[2] == 8:
                                            o = 7
                                        else:
                                            o = 1
                                    elif xatack[3] == 7 or xatack[3] == 1:
                                        o = 5
                                    iafn = 'n'
                            elif xatack[0] == 5:
                                if xatack[1] == 1:
                                    if xatack[3] != 7 or xatack[3] != 3:
                                        if xatack[3] == 4 or xatack[3] == 6:
                                            o = 7
                                        elif xatack[3] == 2 or xatack[3] == 8:
                                            o = 3
                                    elif xatack[3] == 7:
                                        o = 4
                                    else:
                                        o = 2
                                elif xatack[1] == 2:
                                    if xatack[2] == 1:
                                        if xatack[3] == 9:
                                            o = 7
                                        else:
                                            o = 9
                                    elif xatack[2] == 3:
                                        if xatack[3] == 7:
                                            o = 9
                                        else:
                                            o = 7
                                elif xatack[1] == 3:
                                    if xatack[3] != 1 or xatack[3] != 9:
                                        if xatack[3] == 2 or xatack[3] == 8:
                                            o = 1
                                        elif xatack[3] == 6 or xatack[3] == 4:
                                            o = 9
                                    elif xatack[3] == 1:
                                        o = 2
                                    else:
                                        o = 6
                                elif xatack[1] == 4:
                                    if xatack[2] == 7:
                                        if xatack[3] == 3:
                                            o = 9
                                        else:
                                            o = 3
                                    elif xatack[2] == 1:
                                        if xatack[3] == 9:
                                            o = 3
                                        else:
                                            o = 9
                                elif xatack[1] == 6:
                                    if xatack[2] == 3:
                                        if xatack[3] == 7:
                                            o = 1
                                        else:
                                            o = 7
                                    elif xatack[2] == 9:
                                        if xatack[3] == 1:
                                            o = 7
                                        else:
                                            o = 1
                                elif xatack[1] == 7:
                                    if xatack[3] != 9 or xatack[3] != 1:
                                        if xatack[3] == 8 or xatack[3] == 2:
                                            o = 9
                                        elif xatack[3] == 4 or xatack[3] == 6:
                                            o = 1
                                    elif xatack[3] == 9:
                                        o = 8
                                    else:
                                        o = 4
                                elif xatack[1] == 8:
                                    if xatack[2] == 9:
                                        if xatack[3] == 1:
                                            o = 3
                                        else:
                                            o = 1
                                    elif xatack[2] == 7:
                                        if xatack[3] == 3:
                                            o = 1
                                        else:
                                            o = 3
                                elif xatack[1] == 9:
                                    if xatack[3] != 3 or xatack[3] != 7:
                                        if xatack[3] == 6 or xatack[3] == 4:
                                            o = 3
                                        elif xatack[3] == 8 or xatack[3] == 2:
                                            o = 7
                                    elif xatack[3] == 3:
                                        o = 2
                                    else:
                                        o = 4
                                iafn = 'n'
                            elif xatack[0] == 6:
                                if xatack[1] == 7 or xatack[1] == 8:
                                    if xatack[3] == 3:
                                        o = 5
                                    else:
                                        o = 3
                                    iafn = 'n'
                                elif xatack[1] == 1 or xatack[1] == 2:
                                    if xatack[3] == 9:
                                        o = 5
                                    else:
                                        o = 9
                                    iafn = 'n'
                                elif xatack[1] == 3 or xatack[1] == 9:
                                    if xatack[3] == 4:
                                        if xatack[1] == 3:
                                            o = 1
                                        else:
                                            o = 7
                                        iafn = 'n'
                                    else:
                                        o = 4
                                elif xatack[1] == 4:
                                    if xatack[3] == 1:
                                        o = 7
                                    elif xatack[3] == 7:
                                        o = 1
                                    elif xatack [3] == 5:
                                        if xatack[2] == 2:
                                            o = 3
                                        else:
                                            o = 9
                                    elif xatack[3] == 3 or xatack[3] == 9:
                                        o = 5
                                    iafn = 'n'
                            elif xatack[0] == 7:
                                if xatack[1] == 3:
                                    if xatack[2] == 1:
                                        if xatack[3] == 4:
                                            o = 9
                                        else:
                                            o = 4
                                    else:
                                        if xatack[3] == 8:
                                            o = 1
                                        else:
                                            o = 8
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 1:
                                        o = 9
                                    elif xatack[3] == 9:
                                        o = 1
                                    else:
                                        if xatack[3] == 2:
                                            o = 8
                                        elif xatack[3] == 4:
                                            o = 6
                                        elif xatack[3] == 8:
                                            o = 2
                                        elif xatack[3] == 6:
                                            o = 4
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 8:
                                        o = 5
                                    else:
                                        o = 8
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 4:
                                        o = 5
                                    else:
                                        o = 4
                                    iafn = 'n'
                                elif xatack[1] == 9:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 1
                                    iafn = 'n'
                                elif xatack[1] == 1:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 9
                                    iafn = 'n'
                            elif xatack[0] == 8:
                                if xatack[1] == 1 or xatack[1] == 4:
                                    if xatack[3] == 9:
                                        o = 5
                                    else:
                                        o = 9
                                    iafn = 'n'
                                elif xatack[1] == 3 or xatack[1] == 6:
                                    if xatack[3] == 7:
                                        o = 5
                                    else:
                                        o = 7
                                    iafn = 'n'
                                elif xatack[1] == 9 or xatack[1] == 7:
                                    if xatack[3] == 2:
                                        if xatack[1] == 9:
                                            o = 3
                                        else:
                                            o = 1
                                        iafn = 'n'
                                    else:
                                        o = 2
                                elif xatack[1] == 2:
                                    if xatack[3] == 3:
                                        o = 1
                                    elif xatack[3] == 1:
                                        o = 3
                                    elif xatack [3] == 5:
                                        if xatack[2] == 6:
                                            o = 9
                                        else:
                                            o = 7
                                    elif xatack[3] == 9 or xatack[3] == 7:
                                        o = 5
                                    iafn = 'n'
                            elif xatack[0] == 9:
                                if xatack[1] == 1:
                                    if xatack[2] == 7:
                                        if xatack[3] == 8:
                                            o = 3
                                        else:
                                            o = 8
                                    else:
                                        if xatack[3] == 6:
                                            o = 7
                                        else:
                                            o = 6
                                    iafn = 'n'
                                elif xatack[1] == 6 or xatack[1] == 4:
                                    if xatack[3] == 2:
                                        o = 5
                                    else:
                                        o = 2
                                    iafn = 'n'
                                elif xatack[1] == 5:
                                    if xatack[3] == 3:
                                        o = 7
                                    elif xatack[3] == 7:
                                        o = 3
                                    else:
                                        if xatack[3] == 2:
                                            o = 8
                                        elif xatack[3] == 4:
                                            o = 6
                                        elif xatack[3] == 8:
                                            o = 2
                                        elif xatack[3] == 6:
                                            o = 4
                                    iafn = 'n'
                                elif xatack[1] == 2 or xatack[1] == 8:
                                    if xatack[3] == 6:
                                        o = 5
                                    else:
                                        o = 6
                                elif xatack[1] == 7:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 3
                                    iafn = 'n'
                                elif xatack[1] == 3:
                                    if xatack[3] != 5:
                                        o = 5
                                    else:
                                        o = 7
                                    iafn = 'n'
                        else:
                            iafn = 'n'
                    else:
                        if iainicio == 1:
                            if xatack[0] == 1 or xatack[0] == 3 or xatack[0] == 7 or xatack[0] == 9:
                                o = 5
                            elif xatack[0] == 2 or xatack[0] == 4 or xatack[0] == 6 or xatack[0] == 8:
                                if xatack[0] == 2:
                                    o = 8
                                elif xatack[0] == 4:
                                    o = 6
                                elif xatack[0] == 6:
                                    o = 4
                                else:
                                    o = 2
                                iafn = 'n'
                            else:
                                o = choice([1, 3, 7, 9])
                                iafn = 'n'
                        elif iainicio == 3:
                            if xatack[2] == 1:
                                if xatack[1] == 9:
                                    o = choice([7, 3])
                            elif xatack[2] == 3:
                                if xatack[1] == 7:
                                    o = choice([1, 9])
                            elif xatack[2] == 7:
                                if xatack[1] == 3:
                                    o = choice([1, 9])
                            elif xatack[2] == 9:
                                if xatack[1] == 1:
                                    o = choice([7, 3])
                            iafn = 'n'
 
                        else:
                            iafn = 'n'
                elif iafn == 'n':
 
                    if ((xo[2] == 'O' and xo[3] == 'O') or (xo[9] == 'O' and xo[5] == 'O') or (xo[4] == 'O' and xo[7] == 'O')) and xo[1] not in 'XO': o = 1
                    elif ((xo[1] == 'O' and xo[3] == 'O') or (xo[8] == 'O' and xo[5] == 'O')) and xo[2] not in 'XO': o = 2
                    elif ((xo[1] == 'O' and xo[2] == 'O') or (xo[7] == 'O' and xo[5] == 'O') or (xo[9] == 'O' and xo[6] == 'O')) and xo[3] not in 'XO':o = 3
                    elif ((xo[1] == 'O' and xo[7] == 'O') or (xo[5] == 'O' and xo[6] == 'O')) and xo[4] not in 'XO': o = 4
                    elif ((xo[1] == 'O' and xo[9] == 'O') or (xo[2] == 'O' and xo[8] == 'O') or (xo[3] == 'O' and xo[7] == 'O') or (xo[4] == 'O' and xo[6] == 'O')) and xo[5] not in 'XO': o = 5
                    elif ((xo[3] == 'O' and xo[9] == 'O') or (xo[4] == 'O' and xo[5] == 'O')) and xo[6] not in 'XO': o = 6
                    elif ((xo[1] == 'O' and xo[4] == 'O') or (xo[3] == 'O' and xo[5] == 'O') or (xo[8] == 'O' and xo[9] == 'O')) and xo[7] not in 'XO': o = 7
                    elif ((xo[2] == 'O' and xo[5] == 'O') or (xo[7] == 'O' and xo[9] == 'O')) and xo[8] not in 'XO': o = 8
                    elif ((xo[1] == 'O' and xo[5] == 'O') or (xo[3] == 'O' and xo[6] == 'O') or (xo[7] == 'O' and xo[8] == 'O')) and xo[9] not in 'XO': o = 9
 
                    elif ((xo[2] == 'X' and xo[3] == 'X') or (xo[9] == 'X' and xo[5] == 'X') or (xo[4] == 'X' and xo[7] == 'X')) and xo[1] not in 'XO': o = 1
                    elif ((xo[1] == 'X' and xo[3] == 'X') or (xo[8] == 'X' and xo[5] == 'X')) and xo[2] not in 'XO': o = 2
                    elif ((xo[1] == 'X' and xo[2] == 'X') or (xo[7] == 'X' and xo[5] == 'X') or (xo[9] == 'X' and xo[6] == 'X'))and xo[3] not in 'XO': o = 3
                    elif ((xo[1] == 'X' and xo[7] == 'X') or (xo[5] == 'X' and xo[6] == 'X'))and xo[4] not in 'XO': o = 4
                    elif ((xo[1] == 'X' and xo[9] == 'X') or (xo[2] == 'X' and xo[8] == 'X') or (xo[3] == 'X' and xo[7] == 'X') or (xo[4] == 'X' and xo[6] == 'X'))and xo[5] not in 'XO': o = 5
                    elif ((xo[3] == 'X' and xo[9] == 'X') or (xo[4] == 'X' and xo[5] == 'X'))and xo[6] not in 'XO':o = 6
                    elif ((xo[1] == 'X' and xo[4] == 'X') or (xo[3] == 'X' and xo[5] == 'X') or (xo[8] == 'X' and xo[9] == 'X'))and xo[7] not in 'XO': o = 7
                    elif ((xo[2] == 'X' and xo[5] == 'X') or (xo[7] == 'X' and xo[9] == 'X'))and xo[8] not in 'XO':o = 8
                    elif ((xo[1] == 'X' and xo[5] == 'X') or (xo[3] == 'X' and xo[6] == 'X') or (xo[7] == 'X' and xo[8] == 'X'))and xo[9] not in 'XO':o = 9
 
                    else:
                        o = choice(ialista)
                else:
                    o = choice(ialista)
            else:
                o = int(input('\n' * 14 + ' ' * 46 + 'Quadrado: '))
            if xo[o] not in 'XO':
                xatack.append(o)
                iainicio += 1
                xo.pop(o)
                xo.insert(o, 'O')
                vez = 0
                empate += 1
                if ((xo[1] == 'O' and xo[2] == 'O' and xo[3] == 'O') or
                    (xo[1] == 'O' and xo[5] == 'O' and xo[9] == 'O') or
                    (xo[1] == 'O' and xo[4] == 'O' and xo[7] == 'O') or
                    (xo[4] == 'O' and xo[5] == 'O' and xo[6] == 'O') or
                    (xo[7] == 'O' and xo[8] == 'O' and xo[9] == 'O') or
                    (xo[2] == 'O' and xo[5] == 'O' and xo[8] == 'O') or
                    (xo[3] == 'O' and xo[6] == 'O' and xo[9] == 'O') or
                    (xo[3] == 'O' and xo[5] == 'O' and xo[7] == 'O')):
                    vencedor = 'O'
                    break
                elif empate == 9:
                    break
                if o in ialista:
                    ialista.remove(o)
            else:
                vez = 1
                if o in ialista:
                    ialista.remove(o)
    print('\n'*14)
    cor = '\033[1m'
    x = ['X','O']
    for v in range(0, 2):
        if v == 0:
            verde = '\033[32;1m'
            verme = '\033[31;1m'
        else:
            verde = '\033[31;1m'
            verme = '\033[32;1m'
        if (xo[1] == x[v] and xo[2] == x[v] and xo[3] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verde}{xo[1]+cor}  |  {verde}{xo[2]+cor}  |  {verde}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[4]+cor}  |  {verme}{xo[5]+cor}  |  {verme}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[7]+cor}  |  {verme}{xo[8]+cor}  |  {verme}{xo[9]+cor}  
                                              |     |     ''')
 
        elif (xo[1] == x[v] and xo[5] == x[v] and xo[9] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
 
                                              |     |    
                                           {verde}{xo[1]+cor}  |  {verme}{xo[2]+cor}  |  {verme}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[4]+cor}  |  {verde}{xo[5]+cor}  |  {verme}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[7]+cor}  |  {verme}{xo[8]+cor}  |  {verde}{xo[9]+cor}  
                                              |     |     ''')
        elif (xo[1] == x[v] and xo[4] == x[v] and xo[7] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verde}{xo[1]+cor}  |  {verme}{xo[2]+cor}  |  {verme}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verde}{xo[4]+cor}  |  {verme}{xo[5]+cor}  |  {verme}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verde}{xo[7]+cor}  |  {verme}{xo[8]+cor}  |  {verme}{xo[9]+cor}  
                                              |     |     ''')
        elif (xo[4] == x[v] and xo[5] == x[v] and xo[6] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verme}{xo[1]+cor}  |  {verme}{xo[2]+cor}  |  {verme}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verde}{xo[4]+cor}  |  {verde}{xo[5]+cor}  |  {verde}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[7]+cor}  |  {verme}{xo[8]+cor}  |  {verme}{xo[9]+cor}  
                                              |     |     ''')
        elif (xo[7] == x[v] and xo[8] == x[v] and xo[9] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verme}{xo[1]+cor}  |  {verme}{xo[2]+cor}  |  {verme}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[4]+cor}  |  {verme}{xo[5]+cor}  |  {verme}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verde}{xo[7]+cor}  |  {verde}{xo[8]+cor}  |  {verde}{xo[9]+cor}  
                                              |     |     ''')
        elif (xo[2] == x[v] and xo[5] == x[v] and xo[8] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verme}{xo[1]+cor}  |  {verde}{xo[2]+cor}  |  {verme}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[4]+cor}  |  {verde}{xo[5]+cor}  |  {verme}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[7]+cor}  |  {verde}{xo[8]+cor}  |  {verme}{xo[9]+cor}  
                                              |     |     ''')
        elif (xo[3] == x[v] and xo[6] == x[v] and xo[9] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verme}{xo[1]+cor}  |  {verme}{xo[2]+cor}  |  {verde}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[4]+cor}  |  {verme}{xo[5]+cor}  |  {verde}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[7]+cor}  |  {verme}{xo[8]+cor}  |  {verde}{xo[9]+cor}  
                                              |     |     ''')
        elif (xo[3] == x[v] and xo[5] == x[v] and xo[7] == x[v]):
            if modo == 2:
                print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
            else:
                print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
            print(f'''
                                              |     |    
                                           {verme}{xo[1]+cor}  |  {verme}{xo[2]+cor}  |  {verde}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verme}{xo[4]+cor}  |  {verde}{xo[5]+cor}  |  {verme}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {verde}{xo[7]+cor}  |  {verme}{xo[8]+cor}  |  {verme}{xo[9]+cor}  
                                              |     |     ''')
    if empate == 9 and vencedor not in 'XO':
        if modo == 2:
            print(f'''\033[34;4mRodada\033[m:     {c+1}/{rodadas}
\033[mVitória {vd}X\033[m:  {vtx}
\033[mVitória {vm}O\033[m:  {vto}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m:    {emp}\033[1m
 
 
 
''')
        else:
            print(f'''\033[34;4mRodada\033[m:  {c+1}/{rodadas}
\033[32mGanhou\033[m:  {vit}
\033[31mPerdeu\033[m:  {der}
{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[m: {emp}\033[1m
 
 
 
''')
        print(f'''
                                              |     |      
                                           {cx if xo[1] in 'X ' else co}{xo[1]+cor}  |  {cx if xo[2] in 'X ' else co}{xo[2]+cor}  |  {cx if xo[3] in 'X ' else co}{xo[3]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {cx if xo[4] in 'X ' else co}{xo[4]+cor}  |  {cx if xo[5] in 'X ' else co}{xo[5]+cor}  |  {cx if xo[6] in 'X ' else co}{xo[6]+cor}  
                                         _____|_____|_____
                                              |     |      
                                           {cx if xo[7] in 'X ' else co}{xo[7]+cor}  |  {cx if xo[8] in 'X ' else co}{xo[8]+cor}  |  {cx if xo[9] in 'X ' else co}{xo[9]+cor}  
                                              |     |     ''')
        vm = '\033[1;31m'
        vd = '\033[1;32m'
        print('\n\n\n\n\n' + ' ' * 47 + f'{vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u'+'\n' * 11)
        emp +=1
    elif vencedor == 'X':
        print('\n\n\n\n\n'+' '*46+'\033[1;32m'+vencedor,'\033[1;38mVenceu'+'\n'*11)
        vtx += 1
        if iaxo == 'x':
            vit += 1
        else:
            der +=1
    elif vencedor == 'O':
        print('\n\n\n\n\n' + ' ' * 46 + '\033[1;31m' + vencedor, '\033[1;38mVenceu'+'\n' * 11)
        vto += 1
        if iaxo == 'o':
            vit += 1
        else:
            der +=1
 
    xo = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ialista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    xatack = []
    vencedor = 'ninguém'
    iainicio = empate = 0
    iafn = dif
    sleep(5)
vd = '\033[32;1m'
vm = '\033[31;1m'
if modo == 2:
    if vtx > vto:
        vencedor = '\033[32;1m X\033[1m Venceu'
    elif vtx < vto:
        vencedor = '\033[31;1m O\033[1m Venceu'
    else:
        vencedor = '\033[32;1m E\033[31;1mm\033[32;1mp\033[31;1ma\033[32;1mt\033[31;1mo\033[32;1mu\033[1m'
    print('\n' * 30 + f'''\033[1m                                            \033[1mVitória \033[32;1mX\033[1m:  {vtx}                  
                                           \033[1mVitória \033[31;1mO\033[1m:  {vto}
                                           {vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[1m:    {emp}
                                                 
                                               
                                             
                                             
                                             
                                             {vencedor}''')
    print('\n'*13)
else:
    print('\n'*30+f'''\033[1m                                              \033[32;1mGanhou\033[1m:  {vit}                  
                                             \033[31;1mPerdeu\033[1m:  {der}
                                             {vd}E{vm}m{vd}p{vm}a{vd}t{vm}o{vd}u\033[1m: {emp}''')
    print('\n'*15)
