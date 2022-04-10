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

newQ = [frozenset([0])]
newT = []
newF = []

table = [{x : [] for x in A} for _ in range(2 ** len(Q))]


for trans in T:
    if S == trans[0]:
        table[0][trans[2]].append(trans[1])

for x in table[0].keys():
    table[0][x] = frozenset(table[0][x])


crtState = []
crtRow = 1
for state in table:
    for symbol in A:
        if len(state[symbol]) > 0 and state[symbol] not in newQ:
            crtState = state[symbol]
            newQ.append(crtState)
            for newSymbol in A:
                for transition in T:
                    if transition[0] in crtState and transition[2] == newSymbol:
                        table[crtRow][newSymbol].append(transition[1])
                table[crtRow][newSymbol] = frozenset(table[crtRow][newSymbol])
            crtRow += 1
        
#getting rid of non-existent states
for i in range(len(table) - 1, len(newQ) - 1, -1):
   table.remove(table[i])
            

transformationDict = {x : y for x,y in zip(newQ, range(len(newQ)))}
newQ =[transformationDict[x] for x in newQ]

for state in table:
    for transitions in state.values():
        for finalState in F:
            if finalState in transitions and transitions not in newF:
                newF.append(transitions)

newF = [transformationDict[x] for x in newF]

for i in range(len(table)):
    for key in table[i].keys():        
        table[i][key] = transformationDict[table[i][key]]
        transition = (i, key, table[i][key])
        newT.append(transition)

print("Sigma :")
for l in A:
    print(f"\t{l}")
print("End")

print("States : ")

for state in newQ:
    if state in newF:
        print(f"\t{state},F")
    elif state == S:
        print(f"\t{state},S")
    else:
        print(f"\t{state}")
print("End")


print("Transitions : ")
for transition in newT:
    print(f"\t{transition[0]},{transition[1]},{transition[2]}")
print("End")
