import sys
Q = []
A = []
T = []
F = []
S = -1

f = open(str(sys.argv[1] + '.in'), 'r')
f = open('nfa_config_file.in', 'r')
file_lines = f.readlines()
f.close()
file_lines = [x.split() for x in file_lines]
#print(file_lines)

valid = True
finish = False

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
            if 'S' in file_lines[i] and str(file_lines[i]).count('S') != 1:
                valid = False
                break 
            elif file_lines[i].count('S') == 1:
                S = int(file_lines[i][0][0])
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



cuv = sys.argv[2]
# cuv = input()
s = S
ch = 0
aux = len(cuv)
poz = 0

D = [[[] for _ in range(len(Q))] for _ in range(len(Q))]

for i in T:
    D[i[0]][i[1]].append(i[2]);   

coada = [[s]]


while len(coada) and len(min(coada, key=len)) < len(cuv) + 1:
    j = coada[0][-1]
    for i in range(len(D[j])):
        if cuv[ch] in D[j][i]:
            aux = coada[0].copy()
            aux.append(i)
            coada.append(aux)
    coada.pop(0)
    if len(coada) and  len(min(coada, key=len)) > ch + 1:
        ch += 1

if(len(coada)):
    k = 0
    for i in coada:
        if i[-1] in F:
            k = 1

    if k == 1:
        print("Merge, are picioare")
    else:
        print("Nu merge ca nu are picioare")
else:    
    print("NO")