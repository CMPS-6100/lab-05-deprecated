"""
CMPS 6100  Lab 05
Author:
"""

## Add any imports here
import tabulate
import matplotlib.pyplot as plt
import time
##

def selection_sort(L):
    """ done. """
    lst = list(L)
    # For every position in the list
    for position in range(len(lst)):

        # find the minimum element from that position to the end
        minimum_element_index = position 
        for index in range(position,len(lst)):
            element = lst[index]
            # if the current element is smaller than the smallest found so far
            if element < lst[minimum_element_index]:
                # update the minimum element index
                minimum_element_index = index

        # and swap it into position
        lst[position], lst[minimum_element_index] = lst[minimum_element_index], lst[position]
    return lst

def merge_sort(lst):
    """ done. """
    if len(lst) == 1 or len(lst) == 0:
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists, left and right, into one sorted list.
    This function is implemented iteratively to avoid recursion depth
    issues.

    done.
    """
    merged_list = []
    l = 0
    r = 0
    # Repeatedly move the smallest of left and right to the new list
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1
    # There will only be elements left in one of the original two lists.

    # Append the remains of left (l..end) on to the new list.
    merged_list.extend(left[l:])
    # Append the remains of right (r..end) on to the new list.
    merged_list.extend(left[r:])
    return merged_list

def is_sorted(lst):
    """
    Return True if lst is sorted, False otherwise

    Params:
        lst.....a list of values

    Returns:
        True if the list is sorted, False otherwise
    """
    # TO-DO: Implement this
    pass

def test_is_sorted():
    """ done. """
    assert is_sorted([])
    assert is_sorted([1])
    assert is_sorted([1,2])
    assert not is_sorted([2,1])

    assert is_sorted([1,2,3,4,5])
    assert not is_sorted([1,2,3,5,4])
    assert not is_sorted([5,4,3,2,1])
    assert not is_sorted([2,3,1,5,4])

def test_selection_sort():
    """ done. """
    assert is_sorted(selection_sort([]))# == []
    assert is_sorted(selection_sort([101]))# == [101]
    assert is_sorted(selection_sort([1,2,3,4,5]))# == [1,2,3,4,5]
    assert is_sorted(selection_sort([5,4,3,2,1]))# == [1,2,3,4,5]
    assert is_sorted(selection_sort([2,3,1,5,4]))# == [1,2,3,4,5]

def test_merge_sort():
    """ done. """
    assert is_sorted(merge_sort([]))# == []
    assert is_sorted(merge_sort([101]))# == [101]
    assert is_sorted(merge_sort([101, 99]))# == [99, 101]
    assert is_sorted(merge_sort([101, 99, 97]))# == [97, 99, 101]
    assert is_sorted(merge_sort([1,2,3,4,5]))# == [1,2,3,4,5]
    assert is_sorted(merge_sort([5,4,3,2,1]))# == [1,2,3,4,5]
    assert is_sorted(merge_sort([2,3,1,5,4]))# == [1,2,3,4,5]

def get_sorting_time(sort_fn, lst):
    """
    Return the number of milliseconds to run this
    sort function on the list.

    Usage:
        lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        t = get_sorting_time(selection_sort, lst)

    Note 1: You can use time.time() which returns the current 
    time in seconds. You'll have to multiple by 1000 to get 
    milliseconds.

    Params:
        sort_fn.....the sort function
        lst......the list to sort

    Returns:
        the number of milliseconds it takes to run this
        sorting function on this input.
    """
    # TO-DO: Implement this
    pass

def benchmark_sorting_algs(sizes=[ 1000,  2000,  3000,  4000,  5000,  6000,  7000,  8000,  9000, 10000, 
                                  11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]):
    """
    Get the run times of selection_sort and merge_sort on lists
    for input sizes given. The list to sort for each size 
    contains the numbers from n to 1, listed in descending order. 

    You'll use the time_to_search function to time each call.

    Usage:
        Run using the default sizes given above:

        results  = benchmark_sorting_algs()

        Run using custom sizes

        results2 = benchmark_sorting_algs([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

    Params:
        sizes.......a list of input sizes. For each size, a list
                    of numbers from n to 1 will be generated and
                    selection_sort and merge_sort will be on it.

    Returns:
        A list of tuples of the form
        (n, selection_sort_time, merge_sort_time)
        indicating the number of milliseconds it takes
        for each method to run on each value of n
    """
    # TO-DO: Implement this
    results = []
    return results

def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
        headers=['n', 'Selection Sort', 'Merge Sort'],
        floatfmt=".3f",
        tablefmt="github"))
