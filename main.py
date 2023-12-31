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

    if key not in mylist:
        return 0
    else:
        for i in mylist:
            if i == key:
                current_seq += 1
            else:
                if current_seq > max_seq:
                    max_seq = current_seq
                current_seq = 0
        return max_seq


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
        return 0
    # if there's only one item, that one item is the key; therefore the key covers the entire range of the list
    elif len(mylist) == 1:
        if mylist[0] == key:
            return 1
        else:
            return 0
    else:
        list_split = len(mylist) // 2
        left = longest_run_recursive(mylist[:list_split], key)
        right = longest_run_recursive(mylist[list_split:], key)

        return left + right

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([12, 1, 1, 1, 1, 3, 1, 1, 4], 1) == 4


