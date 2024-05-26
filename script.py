import sys

inputPath = '/home/ubuntu/mydir/FrontEnd1/fileManipulator/Input.txt'
outputPath = '/home/ubuntu/mydir/FrontEnd1/fileManipulator/Output.txt'

input = ''

with open(inputPath) as f:
    input = f.read()

# reverse
def reverse():
    output = ''
    for i in range(len(input)-1, -1, -1):
        output += input[i]

    with open(outputPath, 'w') as f:
        f.write(output)
        
# copy
def copy():
    output = input
    with open(outputPath, 'w') as f:
        f.write(output)

# duplicate
def duplicate(n):
    output = ''
    for i in range(0,n,+1):
        output += input

    with open(outputPath, 'w') as f:
        f.write(output)

# replace a with b
def replace(replaceFrom, replaceTo):
    output = ''    
    output = input.replace(replaceFrom, replaceTo)

    with open(outputPath, 'w') as f:
        f.write(output)

if len(sys.argv) == 2 and sys.argv[1] == "reverse":
    reverse()
elif len(sys.argv) == 2 and sys.argv[1] == "copy":
    copy()
elif len(sys.argv) == 3 and sys.argv[1] == "duplicate":
    duplicate(int(sys.argv[2]))
elif len(sys.argv) == 4 and sys.argv[1] == "replace":
    replace(sys.argv[2], sys.argv[3])



