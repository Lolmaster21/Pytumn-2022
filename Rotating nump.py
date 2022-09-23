import numpy

m = numpy.array([[1,2],
                 [3,4]], int)

m = numpy.rot90(m)
print(m, "\n")

m = numpy.rot90(m,2)
print(m, "\n")



m = numpy.arange(8).reshape((2,2,2))
numpy.rot90(m, 1, (1,2))

print(m)
print("Wait you can code?")
