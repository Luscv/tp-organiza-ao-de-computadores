
arq = open('entrada.asm', 'r')
text = arq.readlines()
for line in text:
    print(line)
for line in text:
    linha = line.split(" ")


    #Definição de instruções MIPS para decimal
    if linha[0] == "add":
        tipo = "r"
        opcode = "000000"
        shamt = "000000"
        funct = "100000"
    elif linha[0] == "sub":
        tipo = "r"
        opcode = 0
        shamt = 0
        funct = 34
    elif linha[0] == "and":
        tipo = "r"
        opcode = 0
        shamt = 0
        funct = 36
    elif linha[0] == "or":
        tipo = "r"
        opcode = 0
        shamt = 0
        funct = 37
    elif linha[0] == "nor":
        tipo = "r"
        opcode = 0
        shamt = 0
        funct = 39
    elif linha[0] == "andi":
        tipo = "i"
        opcode = 12
        shamt = 0
        funct = 100
    elif linha[0] == "ori":
        tipo = "i"
        opcode = 13
        shamt = 0
        funct = 100
    elif linha[0] == "sll":
        tipo = "r"
        opcode = 0
        shamt = 10
        funct = 100
    elif linha[0] == "srl":
        tipo = "r"
        opcode = 0
        shamt = 10
        funct = 2
    elif linha[0] == "addi":
        tipo = "i"
        opcode = 8
        shamt = 0
        funct = 0


    #Atribuição de registradores retirando as virgulas e quebra de linha
    linha[1] = linha[1].replace(',', '')
    linha[2] = linha[2].replace(',', '')
    linha[3] = linha[3].replace('\n', '')
    rs = linha[1]
    rt = linha[2]
    rd = linha[3]

    #Definição de registradores
    for i in range(1, 4):
        if linha[i] == "$t0":
            if i == 1:
                rs = 8
            elif i == 2:
                rt = 8
            elif i == 3:
                rd = 8
        if linha[i] == "$t1":
            if i == 1:
                rs = 9
            elif i == 2:
                rt = 9
            elif i == 3:
                rd = 9
        if linha[i] == "$t2":
            if i == 1:
                rs = 10
            elif i == 2:
                rt = 10
            elif i == 3:
                rd = 10
        if linha[i] == "$t3":
            if i == 1:
                rs = 11
            elif i == 2:
                rt = 11
            elif i == 3:
                rd = 11
        if linha[i] == "$t4":
            if i == 1:
                rs = 12
            elif i == 2:
                rt = 12
            elif i == 3:
                rd = 12
        if linha[i] == "$t5":
            if i == 1:
                rs = 13
            elif i == 2:
                rt = 13
            elif i == 3:
                rd = 13
        if linha[i] == "$t6":
            if i == 1:
                rs = 14
            elif i == 2:
                rt = 14
            elif i == 3:
                rd = 14
        if linha[i] == "$t7":
            if i == 1:
                rs = 15
            elif i == 2:
                rt = 15
            elif i == 3:
                rd = 15
        if linha[i] == "$s0":
            if i == 1:
                rs = "10000"
            elif i == 2:
                rt = "10000"
            elif i == 3:
                rd = "10000"
        if linha[i] == "$s1":
            if i == 1:
                rs = "10001"
            elif i == 2:
                rt = "10001"
            elif i == 3:
                rd = "10001"
        if linha[i] == "$s2":
            if i == 1:
                rs = "10010"
            elif i == 2:
                rt = "10010"
            elif i == 3:
                rd = "10010"
        if linha[i] == "$s3":
            if i == 1:
                rs = 19
            elif i == 2:
                rt = 19
            elif i == 3:
                rd = 19
        if linha[i] == "$s4":
            if i == 1:
                rs = 20
            elif i == 2:
                rt = 20
            elif i == 3:
                rd = 20
        if linha[i] == "$s5":
            if i == 1:
                rs = 21
            elif i == 2:
                rt = 21
            elif i == 3:
                rd = 21
        if linha[i] == "$s6":
            if i == 1:
                rs = 22
            elif i == 2:
                rt = 22
            elif i == 3:
                rd = 22
        if linha[i] == "$s7":
            if i == 1:
                rs = 23
            elif i == 2:
                rt = 23
            elif i == 3:
                rd = 23

    print(opcode, rs, rt, rd, shamt, funct)
    #print(linha[3])

arq.close()