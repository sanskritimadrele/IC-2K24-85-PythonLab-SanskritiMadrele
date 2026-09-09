'''SNIPPET 1

Time complexity: O(n)
Space complexity: O(1)

Justify: The loop checks each element once, so time is O(n), and only a few extra variables are used regardless of input size, so space is O(1).

SNIPPET 2

Time complexity: O(n²)
Space complexity: O(1)

Justify: There are two nested loops comparing pairs of elements, giving O(n²) time, while only i, j, and a few variables are used, giving O(1) extra space.

SNIPPET 3

Time complexity: O(log n)
Space complexity: O(log n)

Justify: Each recursive call removes one decimal digit using n // 10, so there are O(log n) calls, and the recursion stack also requires O(log n) space.

SNIPPET 4
Time complexity: O(n²)
Space complexity: O(n²)

Justify: Both loops run n times, producing n² pairs, and the result list stores all n² pairs.

SNIPPET 5
Time complexity: O(log n)
Space complexity: O(1)

Justify: Each iteration cuts the search range approximately in half, while only a constant number of variables are used.

SNIPPET 6

Time complexity: O(n³)
Space complexity: O(n²)

Justify: Three nested loops each run n times, giving n³ operations, and the result matrix requires n² space.

SNIPPET 7

Let:

m = number of rows
n = number of columns
k = number of non-zero elements

Time complexity: O(m × n)
Space complexity: O(k)

Justify: The nested loops examine every one of the m × n elements, while triples stores only the k non-zero elements.

SNIPPET 8

Time complexity: O(n²)

Justify: The first loop takes O(n) time, while the two nested loops take O(n²); therefore the total is O(n²).

SNIPPET 9

Time complexity: O(n)

Justify: The outer loop runs n times and the inner loop always runs exactly 10 times, so 10n = O(n).

SNIPPET 10

Time complexity: O(n)
Space complexity: O(n)

Justify: The loop visits every element once, and the new reversed_arr list stores all n elements.

SNIPPET 11

Time complexity: O(n)
Space complexity: O(1)

Justify: The loop runs approximately n/2 times to swap elements, which is O(n), and only a constant number of variables are used.

SNIPPET 12

Time complexity: O(n)
Space complexity: O(n)

Justify: The function makes n recursive calls, and the recursion stack stores n calls.

SNIPPET 13

Time complexity: O(2^n)
Space complexity: O(n)

Justify: Each call creates two recursive calls, producing exponential time, while the maximum recursion depth is n.

Note: A tighter bound for the time is O(φ^n), where φ ≈ 1.618, but O(2^n) is the standard answer for this activity.

SNIPPET 14

Time complexity: O(n)
Space complexity: O(n)

Justify: The array is traversed once and set operations are O(1) on average, while seen can store up to n elements.

SNIPPET 15

Time complexity: O(n × 2^n)
Space complexity: O(n)

Justify: There are 2^n possible subsets and each subset requires checking n elements; the temporary subset list can contain up to n elements.

Snippet 16

Time complexity: O(n + m)
Space complexity: O(n + m)

Justify: Each element of arrays a and b is processed at most once, and the result list stores all n + m elements.

Here, n = len(a) and m = len(b).

SNIPPET 17

Time complexity: O(n + m)
Time complexity: O(n)
Space complexity: O(n)

Justify: Creating the reversed string takes O(n) time and O(n) extra space.

SNIPPET 18

Time complexity: O(m × n)
Space complexity: O(m × n)

Justify: The nested loops visit all m × n elements, and the flat list stores all m × n elements.

SNIPPET 19

Time complexity: O(exp)
Space complexity: O(exp)

Justify: The exponent decreases by 1 in every recursive call, creating exp calls and requiring O(exp) recursion-stack space.

SNIPPET 20

Time complexity: O(log exp)
Space complexity: O(log exp)

Justify: The exponent is divided by 2 at every recursive call, resulting in O(log exp) calls and recursion-stack space.

SNIPPET 21

Time complexity: O(n × m)
Space complexity: O(1)

Justify: For every element of a (size n), the code may check every element of b (size m), while no extra data structure is created.

SNIPPET 22

Time complexity: O(n)
Space complexity: O(n)

Justify: The loop processes each element once and dictionary operations are O(1) on average; the dictionary can store up to n distinct values.
'''