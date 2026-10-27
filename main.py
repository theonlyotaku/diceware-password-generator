import secrets
import string

sr = secrets.SystemRandom()
list = open("list.txt", "r")

lines = list.readlines()

## rolling the dices ##
dices = 5
ncomb = ""
passphrase = ""
length = int(input("Enter desired length for password: "))

print("\nYour words are: \n")
for _ in range(length):
    ## rolling the dices ##
    for x in range(dices):
        ncomb += str(sr.randint(1,6))
    for i in range(len(lines)):
    ## generating the words ##
        if lines[i][0:5] == ncomb:
            acomb = lines[i][6:len(lines[i])-1] 
            print(acomb,end=" ")
            passphrase += acomb
    
    ncomb = ""


print()
print("\nYour Passphrase is: \n")
print(passphrase)
