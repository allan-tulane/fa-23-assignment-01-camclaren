"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb

def longest_run(mylist, key):
    current_seq = 0
    max_seq = 0

    for i in mylist:
        if i == key:
            current_seq += 1
        else:
            if current_seq > max_seq:
                max_seq = current_seq
            current_seq = 0


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    # if there's no items, the key does not cover any of the range of the list
    if len(mylist) == 0:
        return Result(0, 0, 0, False)
    # if there's only one item, that one item is the key; therefore the key covers the entire range of the list
    elif len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(1, 1, 1, False)
    else:
        halves = len(mylist) // 2
        left = longest_run_recursive(mylist[:halves], key)
        right = longest_run_recursive(mylist[:halves], key)

        if mylist[halves] == mylist[halves - 1] == key:
            whole = left.right_size + right.right_size
            is_entire_range = left.is_entire_range and right.is_entire_range

        else:
            if left.longest_size > right.longest_size:
                whole = left.longest_size
            else:
                whole = right.longest_size
            is_entire_range = False
        if left.left_size > right.right_size:
            return Result(left.left_size, right.right_size, left.left_size, is_entire_range)
        else:
            return Result(left.left_size, right.right_size, right.right_size, is_entire_range)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


