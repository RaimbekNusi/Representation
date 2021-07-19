import numpy as np
ln=[]
lp=[]
ls=[]
l=[]
newl=[]
k = input("Write the name of the .txt file")
f = open(k, "r")
for line in f:
    l.append(line)
for i in l:
    new = i.split(",")
    newl.append(new)
for i in newl:
    k = i[2].split()
    i[2] = k[0]
for i in newl:
    ln.append(i[0])
    lp.append(i[1])
    ls.append(i[2])
n = np.array(ln)
p = np.array(lp).astype(float)
s = np.array(ls).astype(float)
sump = np.sum(p)
sums = np.sum(s)
exp = (p/float(sump))*float(sums)
exp = np.around(exp)
comparison = s[:] > exp[:]
resulto = np.where(comparison == True)
resultu = np.where(comparison == False)
over = n[resulto[0]]
overs = s[resulto[0]]
overe = exp[resulto[0]]
under = n[resultu[0]]
unders = s[resultu[0]]
undere = exp[resultu[0]]
print("Based on population, the following provinces are over-represented:")
for i in range(len(over)):
    print(over[i], " Expected: ", int(overe[i]), " Actual: ", overs[i])
print("\nThe following provinces are under-represented:")
for i in range(len(under)):
    print(under[i], " Expected: ", int(undere[i]), " Actual: ", unders[i])
