import codewars_test as test
def nth_smallest(arr, pos):
    arr = sorted(arr)
    return arr[pos-1]









test.assert_equals(nth_smallest([3,1,2],2),2)
test.assert_equals(nth_smallest([15,20,7,10,4,3],3),7)
test.assert_equals(nth_smallest([-5,-1,-6,-18],4),-1)
test.assert_equals(nth_smallest([-102,-16,-1,-2,-367,-9],5),-2)
test.assert_equals(nth_smallest([2,169,13,-5,0,-1],4),2)