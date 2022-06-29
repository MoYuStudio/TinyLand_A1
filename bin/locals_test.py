createVar = locals()

a = globals()

for i in range(9):
    createVar['thread'+ str(i)] = i

for j in range(9):
    a['window'+str(j)] = j

print(window3)