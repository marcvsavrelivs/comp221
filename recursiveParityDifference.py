def recursiveParity(numArray, n, odd, even):
	if n >= len(numArray):
		return [odd - even]
	elif numArray[n] % 2 == 0:
		even = even + 1
		return recursiveParity(numArray, n + 1, odd, even)
	elif numArray[n] % 2 == 1:
		odd = odd + 1
		return recursiveParity(numArray, n + 1, odd, even)
	else: #case where numArray[n] is not an integer
		return recursiveParity(numArray, n + 1, odd, even)
		
def testRecursiveParity():
    assert recursiveParity([1, 2, 3], 0, 0, 0) == [1], 'failed your most basic example!'
    assert recursiveParity([1, 2, 3, 3], 0, 0, 0) == [2], 'failed your second most basic example!'
    assert recursiveParity([2, 2, 2], 0, 0, 0) == [-3], 'fails on all evens'
    assert recursiveParity([], 0, 0, 0) == [0], 'fails on empty set'
    assert recursiveParity([5, 7, 9, 3], 0, 0, 0) == [4], 'fails on all odds'
    assert recursiveParity([1, 2, 3, 7, 3, 4, 8, 2, 4, 7, 9, 3, 7, 107], 0, 0, 0) == [4], 'fails on large set'
    assert recursiveParity([1, -2, 3, -7], 0, 0, 0) == [2], 'fails on set with negative values'
    assert recursiveParity([1, 2.4, 3, 7.9, 3, 107, 2], 0, 0, 0) == [3], 'fails on set with non-integers'

testRecursiveParity()