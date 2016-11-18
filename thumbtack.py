import sys

database = {}
inverse = {} #used to maintain runtime of numequalto

def SET(name, value):
    if name in database.keys():
        old_val = database[name]
        inverse[old_val] -=1

    database[name] = value
    
    if value in inverse.keys():
        inverse[value]+=1
    else:
        inverse[value] = 1

def GET(name):
    if (name in database.keys()):
        print(">", database[name])
    else:
        print("> NULL")

def UNSET(name):
    val = database[name]
    del database[name]
    inverse[val]-=1

def NUMEQUALTO(value):
    if (value in inverse.keys()):
        print(">", inverse[value])
    else:
        print("> 0")
        

def simpleDB():
    for line in sys.stdin:
        if (line == "END"):
            print("END")
            break
        inputs = line.split()
        command = inputs[0]

        sys.stdout.write(line)
        if (command == "SET"):
            SET(inputs[1], inputs[2])

        elif (command == "GET"):
            GET(inputs[1])

        elif (command == "UNSET"):
            UNSET(inputs[1])

        elif (command == "NUMEQUALTO"):
            NUMEQUALTO(inputs[1])

        else:
            print("Error: no command found")
            
simpleDB()
