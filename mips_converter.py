#this function converts a given 32 bit binary to a 8 digit hexadecimal code
def binary_to_hex(val):
    #dictionary to convert 4 bit binary to hexadecimal
    hex_dict={
        '0000':'0' ,'0001':'1' ,'0010':'2' ,'0011':'3' ,'0100':'4' ,'0101':'5' ,'0110':'6' ,'0111':'7' ,'1000':'8' ,'1001':'9' ,'1010':'A' ,'1011':'B' ,'1100':'C' ,'1101':'D' ,'1110':'E' ,'1111':'F'
    }
    hex_ans='0x'
    #takes the binary string 4 digits at a time and converts to hexadeciaml and concats to the result string
    for i in range(8):
        temp=i*4
        sepr=val[temp:temp+4]
        hex_eq=hex_dict[sepr]
        hex_ans+=hex_eq
    return hex_ans

#Returns the menmonic type of the command
def mnemonic_type(var):
    #arrays containing menmonics in their respective types
    i_type=['addi','addiu','andi','beq','bne','lbu','lhu','ll','lui','lw','ori','slti','sltiu','sb','sc','sh','sw']
    r_type=['add','addu','and','jr','nor','or','slt','sltu','sll','srl','sub','subu']
    if var in i_type:
        return 'i_type'
    elif var in r_type:
        return 'r_type'
    else:
        print("Invalid Mnemonic")
        exit()

#returns the integer equivalent of the register
def register_val(reg):
    #dictionary of register:int value (key:value) pairs
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
    return(reg_dict[reg])

 #returns the binary equivalent of the menmonic.
 #returns opcode for i type commands and funct for r type commands        
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

#returns a binary equivalent of the entered decimal value
def decimalToBinary(N):
     
    # To store the binary number
    B_Number = 0
    cnt = 0
    while (N != 0):
        rem = N % 2
        c = pow(10, cnt)
        B_Number += rem * c
        N //= 2
         
        # Count used to store exponent value
        cnt += 1
     
    return str(B_Number)

 #calls various other functions to convert a assembly language code to 32 bit binary equivalent string and returns it   
def converter(assm_code):
    #splits the command string into its parts like mnemonic, register, offset, immediate
    commands = assm_code.split(' ')
    type = mnemonic_type(commands[0])

    #if the mnemonic is i_type the the below code if executed
    if type == 'i_type':
        #initialising the 32 bit binary as is the stndard for i type commands
        binary=['000000','00000','00000','0000000000000000']
        binary[0]=mnemonic_binary(commands[0])
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        reg1 = register_val(commands[1])
        if commands[2][0] in alphabets:
            reg2 = register_val(commands[2])
            off_imm = decimalToBinary(int(commands[3]))
        else:
            reg2 = register_val(commands[3])
            off_imm = decimalToBinary(int(commands[2]))
        reg1_bin = decimalToBinary(reg1)
        reg2_bin = decimalToBinary(reg2)
        
        #the deficite digits than the standard number is calculated for registers
        defict_reg1=5-len(reg1_bin)
        defict_reg2=5-len(reg2_bin)

        #the deficit number of zeros are added in the beginning for registers
        for i in range(defict_reg1):
            reg1_bin='0'+reg1_bin
        for i in range(defict_reg2):
            reg2_bin='0'+reg2_bin

        #changing the respective values in the main binary array
        binary[1]=reg1_bin
        binary[2]=reg2_bin

        #the deficite digits than the standard number is calculated for immediate and offset
        defict_off_imm=16-len(off_imm)
        #the deficit number of zeros are added in the beginning for immediate and offset
        for i in range(defict_off_imm):
            off_imm='0'+off_imm
        #changing the respective values in the main binary array
        binary[3] = off_imm
        return binary

    #if the mnemonic is r_type the the below code if executed
    elif type == 'r_type':
        #initialising the 32 bit binary as is the stndard for r type commands
        binary=['000000','00000','00000','00000','00000','000000']
        binary[5]=mnemonic_binary(commands[0])
        reg1 = register_val(commands[2])
        reg2 = register_val(commands[3])
        reg3 = register_val(commands[1])

        reg1_bin = decimalToBinary(reg1)
        reg2_bin = decimalToBinary(reg2)
        reg3_bin = decimalToBinary(reg3)

        defict_reg1=5-len(reg1_bin)
        defict_reg2=5-len(reg2_bin)
        defict_reg3=5-len(reg3_bin)

        for i in range(defict_reg1):
            reg1_bin='0'+reg1_bin
        for i in range(defict_reg2):
            reg2_bin='0'+reg2_bin
        for i in range(defict_reg3):
            reg3_bin='0'+reg3_bin

        binary[1]=reg1_bin
        binary[2]=reg2_bin
        binary[3]=reg3_bin
        return binary

#below function is used to replace the unnecessary part of the command inputs and to write the outputs to the output.txt file
def restructure_write(lines):
    for i in range(len(lines)):
        cmd=lines[i]
        cmd = cmd.replace(')',' ')
        cmd = cmd.replace('(','')
        cmd = cmd.replace(',','')
        cmd = cmd.replace('$','')
        lines[i] = cmd

    #opening the output.txt file in write mode
    f = open('output.txt','w')

    count=0
    for line in lines:
        count+=1
        ans = converter(line)
        str_temp=""
        for elem in ans:
            str_temp+=elem
        hx_ans=binary_to_hex(str_temp)
        if count<len(lines):
            #write the outputs to the output.txt file
            f.write(hx_ans+'\n')
        else:
            f.write(hx_ans)
    #closing the output.txt file
    f.close()

#below function is used to reamove some unnecessary part of the input file
def clean_lines(lines):
    #removing the '\n' part at the end of each line due to new line start
    for i in range(len(lines)-1):
        temp=lines[i][:-1]
        lines[i]=temp

    #removing empty lines from the file
    for line in lines:
        if line == '':
            lines.remove(line)
    return lines

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#Main programs and function calls start from here

#we open the data.asm file in read mode
#data.asm file contains the inputs
data = open('data.asm', 'r')
#read all lines of the file and stores it into 'lines' array
lines=data.readlines()
#close the file data.asm
data.close()

lines=clean_lines(lines)

restructure_write(lines)