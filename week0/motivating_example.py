# Late binding problem

functions = []
for i in range(5):

    def func(x):
        return x + i
        
    functions.append(func)

for f in functions:
    print(f(12))

### Confusions and trials

## i guessed it will show error bcz at 7th line we never gave parameter as we defined it with (x)
## but then i remebered oh nah this is just the current function object appending into list
## func --> just the function obj like saving the phone number
## func() --> invoking the functino like calling the phone number

## now it should return x + 0, x + 1 , .., x + 4 so it should print like 12, ..., 16

# i am not getting it bcz i am just thinking in range(5) the object is func + i and i will be selceted before running the loop
# so i is 0 then first loop starts thn it reaches to func(x) and then wheneever it called since it was set previously i as 0 
# then it should call it with 0 i mean why even changing later when loop started itself with the value of i


### Understanding

# now it clicked ahh this was simple but yh
# so what was ahppening actually loop ran 5 times starting form 0 ended at 4 
# and then it called the function now the func is x + i and the current value of i is 4 
# so it should print 12 + i which is 16 every time 
# so output is 

# 16
# 16
# 16
# 16
# 16