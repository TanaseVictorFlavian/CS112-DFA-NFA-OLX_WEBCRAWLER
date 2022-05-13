from copy import deepcopy


Q = [0, 1, 2, 3, 4, 5]
A = ['a', 'b']
T = [(0, 1, 'a'), (1, 0, 'a'), (1, 3, 'b'), (0, 2, 'b'), (3, 5, 'b'),
     (3, 4, 'a'), (2, 4, 'a'), (2, 5, 'b'), (5, 5, 'b'), (5, 5, 'a'), (4, 4, 'a'), (4, 5, 'b')]
S = 0
F = [3, 2, 4]
cuv = 'aab'

D = [[[] for _ in range(len(Q))] for _ in range(len(Q))]

for i in T:
    D[i[0]][i[1]].append(i[2])

s = S
ch = 0
aux = len(cuv)
poz = 0


def verify(p, q):
    if p in F and q in F:
        return 0
    if p not in F and q not in F:
        return 0
    if p in F and q not in F:
        return 1
    if p not in F and q in F:
        return 1
    if p == -1 or q == -1:
        return 0


table = [[0 for j in range(len(Q))] for i in range(len(Q))]

va = [-1 for i in range(len(Q))]
vb = [-1 for i in range(len(Q))]

# creez tabelul ala cu tranzitiile
for i in T:
    if i[2] in 'a':
        va[i[0]] = i[1]
    if i[2] in 'b':
        vb[i[0]] = i[1]


# creez matricea initiala
for i in range(len(Q)):
    for j in range(len(Q)):
        if(j < i):
            table[i][j] = verify(i, j)

# ignor deasupra diagonalei principale
for i in range(len(Q)):
    for j in range(len(Q)):
        if(j >= i):
            table[i][j] = -4
print("before")
print(table)
print()

# fac o coipie a lui table ca sa ma pot opri cu while ul
mat_aux = deepcopy(table)

# modific prima data pe table ca sa imi mearga conditia de while
for i in range(len(Q)):
    for j in range(len(Q)):
        if table[i][j] == 0:
            if verify(va[i], va[j]) == 1 or verify(vb[i], vb[j]) == 1:
                table[i][j] = 1
            else:
                table[i][j] = 0

for i in range(len(Q)):
    for j in range(len(Q)):
        if(j >= i):
            table[i][j] = -4


# repet pana cand matricele nu mai difera(am epuizitat toate transformarile)

while(mat_aux != table):
    mat_aux = deepcopy(table)

for i in range(len(Q)):
    for j in range(len(Q)):
        if table[i][j] == 0:
            if verify(va[i], va[j]) == 1 or verify(vb[i], vb[j]) == 1:
                table[i][j] = 1
            else:
                table[i][j] = 0


# ignor deasupra diagonalei
for i in range(len(Q)):
    for j in range(len(Q)):
        if(j >= i):
            table[i][j] = -4
print("after")
print(table)


# noile stari
aux = len(Q)
q_aux = []
q_aux2 = {}
q = []
t = deepcopy(T)
f = []
al = tuple
for i in range(len(Q)):
    for j in range(len(Q)):
        if table[i][j] == 0:
            if i == S or j == S:
                S = aux
            if i in F or j in F:
                f.append(aux)
            if va[i] == j and va[j] == i:
                t.append((aux, aux, 'a'))
            if vb[i] == j and vb[j] == i:
                t.append((aux, aux, 'b'))

            if va[i] == va[j] and vb[i] == vb[j] and va[i] != i:
                t.append((aux, vb[j], 'b'))

            if va[i] == va[j] and vb[i] == vb[j] and vb[i] != i:
                t.append((aux, va[j], 'a'))

            if va[i] == -1 and vb[i] == vb[j]:
                t.append(aux, vb[i], 'b')
            if vb[i] == -1 and va[i] == va[j]:
                t.append(aux, va[i], 'a')

            for k in t:
                if k[0] == i or k[0] == j:
                    t.remove(k)
            q.append((i, j))
            aux += 1

q_aux2 = {x: y for x, y in zip(q, range(len(q)))}

print("stari")
print(q)
print("stari finale")
print(f)
print('stare initiala')
print(S)
print('tranzitii')
print(t)


# nu stiu cum sa fac vectorul de tranzitii