import numpy

hello_world = numpy.genfromtxt("hello_world.txt",delimiter=',',dtype=str)

print(type(hello_world))
print(hello_world)

# print(help(numpy.genfromtxt))

vector = numpy.array([1,2,'1',4.0])
print(type(vector))

print(vector)
print(hello_world[1,2])

print(hello_world[:,1])
print(hello_world[1,:])
print(hello_world[:,1:3])
print("**********")
print(hello_world[3:,1:3])

vector = numpy.array([5,10,15,20])
print(vector==10)

print(hello_world == 'Zoe')
hello_worldH = (hello_world[:,1] == 'Zoe')
print(hello_worldH)
print("&&&&&&&&&")
print(hello_world[hello_worldH,:])
hello_worldM = (hello_world[1,:]=='Zoe')
print(hello_worldM)
print(hello_world[:,hello_worldM])

vector = numpy.array([1,5,11,15,19,10])
vectorH = (vector == 10) | (vector == 5)
print(vectorH)

vector = numpy.array(['1','2','3'])
print(vector.dtype)
print(vector.astype(float).dtype)