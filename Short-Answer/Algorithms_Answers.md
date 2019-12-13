#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(N)
There are several operations but the simplified complexity is O(n) since the times loop/operations run depends on the number n.

b)
O(Log N)
There are two nested loops but the inner loop's variable is increased exponentially by a constant amount.

c)
O(N)
There is one loop that happens recursively and ends when the length reaches 0.
## Exercise II

Go to the middle of the n-story building.
If egg breaks, f is in first half, take first half
If eggs doesn't break, f is in second half, take second half
Repeat until one item left, f.

O(Log N) -> minimizing dropped+broken eggs by selecting the middle instead of go thtouhg each item
