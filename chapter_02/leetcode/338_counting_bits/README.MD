Tried to solve this problem by counting the current power and current offset but in futile, because it needs log(n) dynamic variables to store the power and offset.

Then took the hints from leetcode `You should make use of what you have produced already.`. I drew the table from 0 to 9 and notice the pattern.

| Decimal | Binary | Bits |
| :------ | :----- | :--- |
| 0       | 0      | 1    |
| 1       | 1      | 1    |
| 2       | 10     | 2    |
| 3       | 11     | 2    |
| 4       | 100    | 3    |
| 5       | 101    | 3    |
| 6       | 110    | 3    |
| 7       | 111    | 3    |
| 8       | 1000   | 4    |
| 9       | 1001   | 4    |
