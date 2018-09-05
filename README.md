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
5. TicTacToe (LeetCode, my AI side project and React official site)

Some other interesting problems
1. (Meta string) Checking if two strings contain the same characters regardless of order
2. Regular Expression Puzzle: http://jimbly.github.io/regex-crossword

## LeetCode favorite list

- easy(12): https://leetcode.com/list/1emvu11
- medium(12): https://leetcode.com/list/1emw747
- hard(12): https://leetcode.com/list/1emdws5

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
1. (breakpoint) debugging while using Jest

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

## How to debug Python, Go and Node.js with breakpoints

Select the file in VS code, then select the cooresponding config in Debug panel to launch.

## Build and Debug C++ (experimental)

Take `LeetCodeTests/1-twoSum.cpp` as an example.

- ~~in terminal, type `g++ -g 1-twoSum.cpp`, then `a.out` (default name) will be generated.~~
- select this file in VS code, then choose `C++: currentFile_build-debug` in Debug panel to build+launch.

`.vscode/launch.json or tasks.json` are for macOS, please read https://code.visualstudio.com/docs/languages/cpp to modify the cpp part of them if yours OS is not macOS.

**issue**

- need a framework to test all

## `C#`

**Installation**

Follow https://docs.microsoft.com/zh-tw/dotnet/core/tutorials/with-visual-studio-code to install .NET Core SDK and VSCode extension.

Then `dotnet restore` to install project dependencies.

**Dev**

Make your classes like `LeetCodeTests/Solution1.cs`, rules:
1. class name is the same as file name.
2. no duplicate file names.
3. write your test case in `test_solution` function.
4. (optional) add `[TestClass]` and `[TestMethod]` for run_all_tests runner.

**Debug**

- select this file in VS code, then choose `.NET Core: Current File` in Debug panel to build+launch.

**Run all tests at once**

- execute `dotnet test` to run all tests function which have ``[TestMethod]``
