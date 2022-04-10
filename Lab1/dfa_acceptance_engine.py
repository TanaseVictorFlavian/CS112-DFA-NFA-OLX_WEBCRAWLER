import sys
Q = []
A = []
T = []
F = []
S = -1

f = open(str(sys.argv[1] + '.in'), 'r')

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
s = S
ch = 0
aux = len(cuv)
poz = 0
D = [[[] for j in range(len(Q))] for i in range(len(Q))]
for i in T:
    D[i[0]][i[1]].append(i[2]);


def solve(s, ch):
    for i in range(len(D[s])):
        found = False
        if cuv[ch] in D[s][i]:
            found = True
            break
    # nu exista legatura in graf
    if not found:
        return -1 
    #cazul de oprire
    if ch == aux - 1:
        if i in F:
            return 1
        else:
            return -1
    else:
        ch = ch + 1
        return solve(i, ch)


if solve(S, 0) == 1:
    print('Cuvantul este valid')
else:
    print('Cuvantul nu este valid')
                
