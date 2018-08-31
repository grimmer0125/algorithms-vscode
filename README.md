Some other coding problems in my inteviews

1. reverse a string
2. judge if a string is the substring of another string
3. Hanoi tower
4. use two stacks to implement a queue (pseudo code), https://leetcode.com/problems/implement-stack-using-queues/

Some questions in my interviews
1. time complexity of merge sort
2. what is the quickest search
3. what is the worse case of hash table
4. mouse maze, similar to LeetCode-490 The Maze (medium): https://leetcode.com/articles/the-maze/

Some other interesting problems
1. (Meta string) Checking if two strings contain the same characters regardless of order
2. Regular Expression Puzzle: http://jimbly.github.io/regex-crossword

## LeetCode favorite list

- easy(12): https://leetcode.com/list/1emvu11
- medium(12): https://leetcode.com/list/1emw747
- hard(10): https://leetcode.com/list/1emdws5

`12` in `easy(12)` means that the first 12 problems in the list are in the first 200 leetcode problems which are used frequently.

## Tips on LeetCode

Do not uncomment some pre-definition classes which are defined somewhere already, the system comments are just exploration e.g.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
```

## interesting skills

two pointer method (caterpillar method), e.g:
- https://app.codility.com/programmers/lessons/15-caterpillar_method/
- https://leetcode.com/articles/two-pointer-technique/
- https://www.geeksforgeeks.org/find-number-of-triangles-possible/

Sometimes it is used in linked-list problems.

## Node.js

Install:
- yarn install

Test:
- yarn test (find all `*.test.js` in the root folder)
- yarn test specific_folder (only that folder)

Todo:
1. (breakpoint) debugging when using jest

## Python

Install:
- pip install -U pytest

Test:
- pytest -s (find all `*-*.py test_*.py` files in the current folder)
- pytest -s single_file (only that file)

## Go

Run:
1. in each folder, execute `go build` and executed the generated binary file

Test:
1. in each folder, execute `go test`
2. in root folder, `go test ./...` to test all sub folders
