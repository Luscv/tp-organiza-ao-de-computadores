arq = open('entrada.asm', 'r')
cria_arq = open('saida.txt', 'w')
text = arq.readlines()
Add = []
Sub = [0, 0, 34]
And = [0, 0, 36]
Or = [0, 0, 37]
Nor = [0, 0, 39]
Andi = [12, 100]
Ori = [13, 100]
Sll = [0, 0, 10, 0]
Srl = [0, 0, 10, 2]
for line in text:
    (inst, reg1, reg2, reg3) = line.split(" ")
    #print("instruçao:", inst, "registrador 1:", reg1, "registrador 2:", reg2, "registrador 3:", reg3)
    if inst == "add":
        Add.append('0,0,32')
        saida = Add
        cria_arq.writelines(saida)
    elif inst == "sub":
        Sub.append('0,0,34')

        cria_arq.writelines(Sub)
    elif inst == "and":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "or":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "nor":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "andi":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "ori":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "and":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "sll":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
    elif inst == "srl":
        Add.append('0,0,32')

        cria_arq.writelines(Add)
print(saida)
arq.close()
cria_arq.close()