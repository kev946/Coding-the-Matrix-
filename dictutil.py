import python_lab

## Task 2
def dict2list(dct, keylist): return python_lab.dict2list(dct, keylist)

def list2dict(L, keylist): return python_lab.list2dict(L, keylist)

## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    return list2dict(L, range(0, len(L) - 1))

