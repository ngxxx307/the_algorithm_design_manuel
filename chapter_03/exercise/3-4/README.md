confused for a while not knowing how to impelement find_min to be O(1) while simultaneously implementing delete to be O(1).

After taking hints from gemini that

> Hint 2: The "Snapshot" Concept
> In a stack, elements are added and removed in a strict order. When you push an element onto the stack, the "state of the world" (including what the minimum is at that exact moment) is frozen for everything below it.

I decide to use another stack to store the minimum value
