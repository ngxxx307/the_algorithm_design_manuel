Solved by imagining the strings as number.

If the root node match the prefix, add the root node and recursively search both left and right.
If root node is smaller than the prefix, recursively search right only.
If root node is larger than the prefix, recursively search left only. 