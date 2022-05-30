import sys
f = open(str(sys.argv[1] + '.in'), 'r')

# f = open("cfg_config_file.in", 'r')
file_lines = f.readlines()

file_lines = [x.split('\n') for x in file_lines]

V = []
E = []
R = {}

i = 0
while i < len(file_lines):
    if 'Variables' in file_lines[i][0]:
        i += 1
        while 'End' not in file_lines[i]:
            V.append(file_lines[i][0])
            i += 1
    if 'Start state' in file_lines[i][0]:
        i += 1
        S = file_lines[i][0][0]
        if 'End' not in file_lines[i + 1]:
            print("The given configuration isn't valid") 
            break
        if S not in V:
            print("The given configuration isn't valid")
            break

    if 'Terminals' in file_lines[i][0]:
        i += 1
        while 'End' not in file_lines[i]:
            E.append(file_lines[i][0])
            i += 1
    if 'Rules' in file_lines[i][0]:
        i += 1
        while 'End' not in file_lines[i]:
            auxList = file_lines[i][0].split(" -> ")
            state = auxList[0]
            ruleList = auxList[1].split("|")
            if state not in R.keys():
                R[state] = ruleList
            else:
                for rule in ruleList:
                    R[state].append(rule)
            i += 1
    i += 1

def validateCFG():

    if not len(V) and not len(E):
        return False

    for key in R.keys():
        if key not in V:
            return False
    
    if S not in R.keys():
        return False
    
    for terminal in E:
        ok = False
        for key in R:
            for char in R[key]:
                if terminal in char:
                    ok = True
        if not ok :
            return False
    return True


if validateCFG():
    print("The given configuration is valid")
else:
    print("The given configuration isn't valid")

