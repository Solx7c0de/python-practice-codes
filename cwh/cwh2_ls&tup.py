# friends= ["a","bcd", 654, 78, False ]

# print(friends[0])

# friends[0] = "cutie"
# friends.append("vish")
# print( friends)

# lnum = [1,45,76,34]

# a= lnum.sort()
# print(lnum)
# b= lnum.sort(reverse=True)
# print(lnum)
# c= lnum.insert(0,69)
# print(lnum)
# print(type(lnum))


#tuples

tup1 = ("immutable", "like string", 34, 45, False)

a, b, c, d, e = tup1 #unpacking a tuple's members to a variable

print(a, c, e)

print( tup1.count("immutable"))

print( tup1.index("immutable"))
