f1=open("in1.txt","r")
f2=open("out1.txt","w")
start=int(f1.readline())
end=int(f1.readline())
for j in range(start,end+1,1):
    for i in range(1,11,1):
        
        result = j * i
        print(j, i, result)
        
        f2.write(f"{j} x {i} = {result}\n")
    print()
f2.close()
