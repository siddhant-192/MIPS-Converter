def mnemonic_type(var):
    i_type=['addi','addiu','andi','beq','bne','lbu','lhu','ll','lui','lw','ori','slti','sltiu','sb','sc','sh','sw']
    r_type=['add','addu','and','jr','nor','or','slt','sltu','sll','srl','sub','subu']
    if var in i_type:
        return 'i_type'
    elif var in r_type:
        return 'r_type'
    else:
        print("Invalid Mnemonic")
        exit()

def register_val(reg):
    reg_dict={
        'zero': 0 ,
        'at': 1,
        'v0': 2, 'v1': 3,
        'a0': 4, 'a1': 5, 'a2': 6, 'a3': 7,
        't0': 8, 't1': 9, 't2': 10, 't3': 11, 't4': 12, 't5': 13, 't6': 14, 't7': 15, 't8': 24, 't9': 25,
        's0': 16, 's1': 17, 's2': 18, 's3': 19, 's4': 20, 's5': 21, 's6': 22, 's7': 23,
        'k0': 26, 'k1': 27,
        'gp': 28,
        'sp': 29,
        'fp': 30,
        'ra': 31
    }

def int_to_binary(num):
    arr = []
    def DecimalToBinary(n):
        if n >= 1:
            DecimalToBinary(n // 2)
        arr.append(n%2)
    DecimalToBinary(num)
    binary=""
    for i in arr:
        binary+=str(i)
    return binary

def mnemonic_binary(name):
    if name=="add":
        return "010100"
    elif name=="addi":
        return "001000"
    elif name=="addiu":
        return "001001"
    elif name=="addu":
        return "100001"
    elif name=="and":
        return "100100"
    elif name=="andi":
        return "001100"
    elif name=="beq":
        return "000100"
    elif name=="bne":
        return "000101"
    elif name=="lbu":
        return "100100"
    elif name=="lhu":
        return "100101"
    elif name=="ll":
        return "110000"
    elif name=="lui":
        return "001111"
    elif name=="lw":
        return "100011"
    elif name=="nor":
        return "00111"
    elif name=="or":
        return "100101"
    elif name=="ori":
        return "001101"
    elif name=="slt":
        return "101010"
    elif name=="slti":
        return "001010"
    elif name=="sltiu":
        return "001011"
    elif name=="sltu":
        return "101011"
    elif name=="sll":
        return "000000"
    elif name=="srl":
        return "000010"
    elif name=="sb":
        return "101000"
    elif name=="sc":
        return "111000"
    elif name=="sh":
        return "101001"
    elif name=="sw":
        return "101011"
    elif name=="sub":
        return "100010"
    elif name=="subu":
        return "100011"
    else:
        print("Invalid Menmonic.")
        exit()

def converter(assm_code):
    commands = assm_code.split(' ')
    type = mnemonic_type(commands[0])
    if type == 'i_type':
        binary=['000000','00000','00000','0000000000000000']
        binary[0]=mnemonic_binary(commands[0])
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        reg1 = register_val(commands[1])
        if commands[2][0] in alphabets:
            reg2 = register_val(commands[2])
            off_imm = int_to_binary(int(commands[3]))
        else:
            reg2 = register_val(commands[3])
            off_imm = int_to_binary(int(commands[2]))
        reg1_bin = int_to_binary(reg1)
        reg2_bin = int_to_binary(reg2)
        
        defict_reg1=5-len(reg1_bin)
        defict_reg2=5-len(reg2_bin)

        for i in range(defict_reg1):
            reg1_bin='0'+reg1_bin
        for i in range(defict_reg2):
            reg2_bin='0'+reg2_bin

        binary[1]=reg1_bin
        binary[2]=reg2_bin

        defict_off_imm=16-len(off_imm)
        for i in range(defict_off_imm):
            off_imm='0'+off_imm
        return binary


        
data = open('data.txt', 'r')
lines=data.readlines()
data.close()

for cmd in lines:
    cmd = cmd.replace(',','')
    cmd = cmd.replace('$','')

converter('addi s0 t1 5')