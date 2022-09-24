data = open('data.txt', 'r')
lines=data.readlines()
data.close()

for cmd in lines:
    cmd = cmd.replace(',','')
    cmd = cmd.replace('$','')
    print(cmd)