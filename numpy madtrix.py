import numpy

a = numpy.array([[1, 2], [6, 2]])
b = numpy.array([4, 0])
x = numpy.linalg.solve(a, b)

print("Numpy Matrix is:")
print(x)

determinant = numpy.linalg.det(x)

print("\nDeterminant of given 2X2 matrix:")
print(int(determinant))

