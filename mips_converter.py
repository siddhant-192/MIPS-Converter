data = open('data.txt', 'r')
  
while True:
    # Get next line from file
    line = data.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break
    print(line.strip())
  
data.close()