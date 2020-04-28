from sys import argv
script ,filename=argv
txt=open(filename)
print("here is ur file {}",filename)
print(txt.read())
print("type the file name again")
fileagain=input('> ')
txtagain=open(fileagain)
print(txtagain.read())
