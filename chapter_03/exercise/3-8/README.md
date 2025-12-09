Cannot solve the problem. Originally thought to use 2n of space to store integer of row of column, and 2 more for diagonal. But it cannot check if input ofo sequence is valid.

Afterward I asked gemini 3.0 pro on that solution, and it replies

> The Logic (Plain Text)
> To solve this without storing the whole board (which would be too big), we track the "score" of each row, column, and diagonal.
>
> Assign Values:
>
> Let Player 1 be equal to +1.
> Let Player 2 be equal to -1.
> Tracking:
>
> We keep a list of numbers to track the sum of each Row.
> We keep a list of numbers to track the sum of each Column.
> We keep one number for the Diagonal (top-left to bottom-right).
> We keep one number for the Anti-Diagonal (top-right to bottom-left).
> Making a Move:
>
> When a player makes a move at a specific row and col, we add their value (+1 or -1) to the count for that specific row and column.
> If the move is on the main diagonal (where row equals col), we add their value to the Diagonal counter.
