def sum_lists(lists):
    """
    Given a list of lists, return a new list where each list is replaced by
    the sum of its elements.
    """
    output = [0] * len(lists)
    print("heres i'm -->", output, len(lists))
    for i in range(len(lists)):
        inner_list = lists[i]
        print("heres the list -->", inner_list, i)
        total = 0
        for j in inner_list:
            print("heres j -->", j)
            total += j
        print("heres total -->", total)
        output[i] = total
        print("heres i'm -->", output)
    return output


print(sum_lists([[5, 6], [3, 2]]))   # [11, 5]

## here i first noticed whatshappening by printing each line i noticed its stopped at ths line output[i] = total
# then i noticed the oouter loop variable i but i get onfused with other langages like c, java, luau where scope acts like block
# block of code fnished the variable is also finished but here the inner loops i variable was just changed 
# which was outer loop variable due to inner loop so here i changed the innner loop vairable from i to j 



def reverse_all(inp):
    """
    given a list of lists, return a new list of lists but with all of the inner
    lists reversed, without modifying the input list

    Example:

    >>> input1 = [[1, 2], [3, 4]]
    >>> reverse_all(input1)
    [[2, 1], [4, 3]]
    """
    output_copy = []
    # for i in inp
    for i in inp:
        output_copy += [i[::-1]]   # used bcz mit in website material exclusively told this line
                                   # "This gives us yet another cute shorthand, x[::-1], 
                                   #  which makes a new list with all of the references from x but in the reverse order."

    return output_copy
    

print("output list", reverse_all([[1, 2], [3, 4]]))


## i[::-1] this is the life saver but still its just a shalow copy with 1 layer of depth
# but with deepcopy or recursion based we can solve this problem for infinte depth
# its like new_list = copy.deepcopy(original_list)
# and then we can reverse it 
