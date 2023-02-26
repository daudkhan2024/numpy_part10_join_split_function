import numpy as np
print("Topic: join & Split Function")

#join array
var = np.array([1,2,3,4])
var1 = np.array([9,8,7,6])

ar = np.concatenate((var,var1))
print(ar)

print()
print("in 2D array")
vr = np.array([[1,2],[2,3]])
vr1 = np.array([[9,8],[7,6]])

ar_new = np.concatenate((vr,vr1),axis=1)
print(vr)
print()
print(vr1)
print()
print(ar_new)

print()
print("same we can also do with stackfunction")
var_1 = np.array([1,2,3,4])
var_2 = np.array([9,8,7,6])

a_new = np.stack((var_1,var_2),axis=1)
print(a_new)


print(" to merge with row we use hstack")
var_1 = np.array([1,2,3,4])
var_2 = np.array([9,8,7,6])

a_new = np.hstack((var_1,var_2))
print(a_new)

print()
print("to merge in column we use vstack")
var_1 = np.array([1,2,3,4])
var_2 = np.array([9,8,7,6])

a_new1 = np.vstack((var_1,var_2))
print(a_new1)

print()
print("to merge with height shaoe we use dstack")
var_1 = np.array([1,2,3,4])
var_2 = np.array([9,8,7,6])

a_new2 = np.dstack((var_1,var_2))
print(a_new2)

print()

print()
print("Topic : Split array")
var4 = np.array([1,2,3,4,5,6])
print(var4)
print()
ar = np.array_split(var,3)
print(ar)
print(type(ar))
print()
print(ar[0])


print()
print("Topic : 2D array")
var5 = np.array([[1,2],[3,4],[3,4]])
print(var5)
ar2= np.array_split(var5,3)
print()
ar4= np.array_split(var5,3,axis=1)
print("ar2 :",ar2)
print("ar4 : ",ar4)