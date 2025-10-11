f2=open('demo2.txt','w+')
f2.write('yes sir')
f2.seek(0)
x=f2.read()
print(x)
f2.close()

