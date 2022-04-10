import sys


Q = []
A = []
T = []
F = []
S = -1

f = open(str(sys.argv[1] + '.in'), 'r')
#f = open('dfa_config_file.in', 'r')

file_lines = f.readlines()
f.close()
file_lines = [x.split() for x in file_lines]
#print(file_lines)

valid = True
finish = False
start = False

i = 0 
while i < len(file_lines):
    if 'Sigma' in file_lines[i][0]:
        i += 1
        while file_lines[i] != ['End']:
            #test in caz de mai multe litere in loc de una singura 
            if len(file_lines[i][0]) > 1:
                valid = False
                break
            A.append(file_lines[i][0])
            i += 1
    if 'States' in file_lines[i][0]:
        i += 1
        while file_lines[i] != ['End']:   
            Q.append(int(file_lines[i][0][0]))
            #test in caz de mai multe starturi
            if 'S' in file_lines[i] and str(file_lines[i]).count('S') != 1:
                valid = False
                break 
            elif file_lines[i].count('S') >= 1 and start :
                valid = False
                break
            elif file_lines[i].count('S') == 1:
                S = int(file_lines[i][0][0]) 
                start = True
            if 'F' in file_lines[i]:
                F.append(int(file_lines[i][0][0]))
                finish = True
            i += 1
    if 'Transitions' in file_lines[i][0]:
        i += 1
        while file_lines[i] != ['End']:   
            lista = [int(file_lines[i][0][0]), int(file_lines[i][0][4]), file_lines[i][0][2]]
            T.append(tuple(lista))
            i += 1
    i += 1

if(not start or not finish):
    valid = False


if valid: 
    D = [[[] for _ in range(len(Q))] for _ in range(len(Q))]
    for i in T:
        D[i[0]][i[1]].append(i[2]);   

    for line in D:
        for list in line:
            for letter in A:
                counter = list.count(letter)
                if counter > 1:
                    valid = False
                    break
    


if valid: 
    print("Datele din fisier sunt valide")
else:
    print("Datele din fisier nu sunt invalide")


                        
