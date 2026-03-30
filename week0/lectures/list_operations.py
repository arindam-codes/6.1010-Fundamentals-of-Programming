# x = ["baz", 302, 303, 304]

# y = x

# x[0] = 314

# print(x)

# print(y)


# expected same bcz i am printing y after chaging x so both now points to the same memory place 

# a = [301, 302, 303]

# b = [a, a, a]

# b[0][0] = 304

# print(a)
# print(b)

# i thought i just changed b ntg to do with a so only b will hcange a will remain the same but i am
# confused now a also changed
# need help of claude ig
# ahh now i get it b is a list containing the 3 items which referse to the same obj in memory a 
# so if we change that its just changing a 

# mit question: In the example above, how many total Python list objects were created while that program was running?

## if we closely look its not 5 its just 2 list obj that reated one is a and another oe is b and 3 inside b are just the refernces not the obj created

## practice problems of slicing
# x = [9, 8, 7, 6, 5, 4, 3, 2]
# print(x[1:3])

# print(x[:4])

# print(x[:-3])

# print(x[3:])

# print(x[-3:])

# x = [[9, 8], [7, 6, 5]]

# y1 = x

# y2 = x[:]

# x[0] = 20
# x[1][0] = 30

# print(x)
# print(y1)
# print(y2)

# my lgoic was since i alreacy shalow copied the x for y2 y2 should print he original x but smehow it changed to 30 im confused
# time for claude 
# after getting the environment diagrams i got that its not the copy i thought when i said 
# y2 = x[:] this lines created another list and the list items refers still to the old list items so if 
# the inner item list changed then ofc y2 will be changed but since i copied the outer one 
# now if i try to chnage the outer list and since the copy has no refernce to the old outer lis it will ne be changed 

### mit line: The main takeaway here is that if you notice similar kinds of behaviors in your own programs 
# ("I only changed that in x! Why is it showing up in y?"), be on the lookout for accidental aliasing of this form! ###

## practice problems
# x = [7, 7, 7, 7, 7]

# x.insert(2, 8)

# print(x)

#Consider a list defined by x = [1, 2, 3]. We perform some operation x.______([4, 5]), and then, 
# when printing x, we see [1, 2, 3, 4, 5]. What operation did we perform, append or extend?
# -- i think extend

# x = [1, 2, 3]
# x.append([4, 5])
# print(x)

# it will just append the one new element unlike extend which would extend the list

## practice problems 
# Consider a list defined by x = [6, 7, 5, 9, 0, 2, 3, 8, 4, 1]. After running x.pop(N) 
# (for some non-negative value of N), printing x shows the following value: [6, 7, 5, 0, 2, 3, 8, 4, 1]
# What value of N was used?
# -- 3

# Consider a list defined by x = [1, 2, 3, 4, 5, 4, 3, 2, 1]. After running x.remove(3), what is the new value of x? 
# Enter your answer as a Python list in the box below: 
# -- [1, 2, 4, 5, 2, 1] but nah it removes only only the first element occured in the list 
# seeming i am forgetting some 6.100L concepts which is due to lack of practice 

## concatenation
# extend, append, +=(behaves like extend) those are mutating but concatenation will create a new list

## practice problems
# a = [1, 2]
# b = a
# c = b + [3]
# b += [4]

# b refers to the same object as a 
# c is concatenation so c is a brand new list [1, 2, 3]

# -- so a and b are aliases

# -- value of a is [1, 2, 4] bcz adding to b is just manipulating the same a object
# -- value of b is just a which is [1, 2, 4]

# -- vlue of c is [1, 2, 3] this happened before b += [4] so c will get the original one

## more practice problems

# b = [311]
# a = [307, [308], [309, 310], b, [b]]

# a = [0, [4, 5]]
# d = [2, 3, a[0], a[1]]

# c = [a[0], 1, a[1], d]


## 6.1 tuples

a = () # i think yes empty tuple
b = 6.101 #nah
c = 6.101, # yes
d = 6, 1, 0, 1 # yes
e = 6, 1, 0, 1, # yes
f = (6.101) # nah
g = (6.101,) # yes
h = (6, 1, 0, 1) # yes
i = (6, 1, 0, 1, ) #yes

## , represents tuple | () - used for grouping | () empty tuple()

## x[1][0] = 20 will raise no exception bcz its just mutating a list
# y = x will rasie no exception bczits just reassigning the variable