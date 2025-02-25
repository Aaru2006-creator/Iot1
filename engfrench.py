def inputline():
    c=0
    with open("file.txt", 'w') as f:
        for i in range(N):
            line = input("Enter line: ")
            for j in line:
                c+=1
            if c<1 or c>100:
                print("Each line must have atleast one character")
            else:
                f.write(line)
                


def count():
    tcount =0
    scount=0
    f2= open("file.txt", 'r')
    l = f2.read()
    lines = l.split()
    for i in lines:
        if (i=='s' or i=='S'):
            scount+=1
        elif (i=='t' or i=='T'):
            tcount+=1
    if(tcount>scount):
        print("Its probably English!")
    else:
        print("Its probably French!")
    f2.close()

N = int(input("Enter number of lines: "))
if N>10000:
    print("Number of lines must be less than 10000")
else:
    inputline()
    count()
