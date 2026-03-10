Original has no clue. That click topic and see monotonic stack and get the idea behinds it.

Implement the first solution by assuming all height different is 1, but this is not true. 

Then i have to cacluate `(i - left_i - 1) * (left_h - lowest)` instead of just `(i - left_i - 1)`

Then test case 2 does not pass. And i figure out it is still issue arised by assuming height difference is 1.

Then i solve the bug and submit it.

Asked AI and it said it can reduce the space complexity from O(n) to O(1) but i didn't implement it