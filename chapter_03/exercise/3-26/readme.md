(a) just use a 2d matrix to store the minimum
(b) stuck by thinking how to find the minimum in log(n). It implies it must traverse some tree structure. But minimum is aggreagte data. If traverse the blanaced binary tree version of the arr means need to traverse all tree. Then it is the same as iterating the array.

Then it struck me that i can store the aggregate data at node. Each node represent certain range. (e.g. i=1, j=5).

The space complexity is n + n/2 + n/4 + ... + 1 <= n + n = 2n = O(n)
time complexity is O(log(n))