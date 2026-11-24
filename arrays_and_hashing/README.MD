# Module 01 — Arrays & Hashing

## 1. Objective

Master array and hashing-based problem-solving patterns by understanding when, why and how to apply them.

The objective is not to memorize solutions but to develop the ability to recognize patterns in unfamiliar problems.

## 2. Underlying Data Structures

| Data Structure | Python | Java Equivalent |
|---|---|---|
| Dynamic Array | list | ArrayList |
| Hash Table | dict | HashMap |
| Hash Set | set | HashSet |
| Frequency Map | Counter | HashMap |
| Default Dictionary | defaultdict | HashMap with computeIfAbsent |
| Immutable Sequence | tuple | No exact equivalent |

## 3. Problem-Solving Patterns

| # | Pattern | Data Structure | Use Case |
|---|---|---|---|
| 1 | Membership Lookup | HashSet | Duplicate detection, existence check |
| 2 | Frequency Counting | HashMap | Counting occurrences |
| 3 | Complement Lookup | HashMap | Finding pairs with a target sum |
| 4 | Set Intersection | HashSet | Finding common elements |
| 5 | Grouping by Signature | HashMap | Grouping similar elements |
| 6 | Frequency Ranking | HashMap, Heap | Finding most frequent elements |
| 7 | Prefix and Suffix | Array | Cumulative computations |
| 8 | Constraint Validation | HashSet | Detecting rule violations |
| 9 | Sequence Detection | HashSet | Finding consecutive sequences |

## 4. Pattern Recognition Cheat Sheet

| Problem Statement Clue | Possible Pattern |
|---|---|
| Does an element already exist? | Membership Lookup |
| Find duplicate elements | HashSet |
| Count occurrences | Frequency Counting |
| Find two numbers adding to a target | Complement Lookup |
| Find common elements | Set Intersection |
| Group similar elements | Grouping by Signature |
| Find the K most frequent elements | Frequency Map + Heap |
| Find consecutive numbers | Sequence Detection |
| Avoid repeated searching | Hashing |

These are pattern recognition clues, not absolute rules. Always evaluate the constraints before choosing an approach.

## 5. Time Complexity Cheat Sheet

| Operation | Python List | Python Set | Python Dict |
|---|---|---|---|
| Membership lookup | O(n) | O(1)* | O(1)* |
| Insert | O(n) | O(1)* | O(1)* |
| Append | O(1)** | N/A | N/A |
| Delete by value/key | O(n) | O(1)* | O(1)* |
| Access by index | O(1) | N/A | N/A |
| Iteration | O(n) | O(n) | O(n) |

\* Average-case complexity. Hash collisions can degrade performance.

\** Amortized complexity.

## 6. Practice Problems

| # | LeetCode | Problem | Difficulty | Pattern | Status |
|---|---|---|---|---|---|
| 01 | 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Membership Lookup | Pending |
| 02 | 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Frequency Counting | Pending |
| 03 | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Complement Lookup | Pending |
| 04 | 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | Set Intersection | Pending |
| 05 | 387 | [First Unique Character](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | Frequency Counting | Pending |
| 06 | 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | Frequency Counting | Pending |
| 07 | 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Grouping | Pending |
| 08 | 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Frequency Ranking | Pending |
| 09 | 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix and Suffix | Pending |
| 10 | 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | Constraint Validation | Pending |
| 11 | 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Sequence Detection | Pending |
| 12 | 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix Sum + HashMap | Pending |

## 7. Problem-Solving Methodology

For every problem:

1. Understand the problem statement.
2. Analyze the constraints.
3. Identify the underlying pattern.
4. Identify the appropriate data structure.
5. Implement the brute-force solution.
6. Identify bottlenecks.
7. Implement the optimized solution.
8. Perform a dry run.
9. Analyze time and space complexity.
10. Write unit tests.
11. Submit the optimized solution to LeetCode.
12. Document key learnings.
13. Commit and push to GitHub.

## 8. Study Resources

- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Abdul Bari — Hashing](https://www.youtube.com/results?search_query=abdul+bari+hashing+technique)
- [VisuAlgo — Hash Tables](https://visualgo.net/en/hashtable)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Collections](https://docs.python.org/3/library/collections.html)
- [Big-O Complexity Cheat Sheet](https://www.bigocheatsheet.com/)
- [NeetCode — Arrays and Hashing](https://www.youtube.com/results?search_query=neetcode+arrays+and+hashing)

## 9. Key Learnings

This section will be updated after completing each problem.

### 1.1 Membership Lookup

- When to use:
- Why it works:
- Underlying data structure:
- Time complexity:
- Space complexity:
- Limitations:
- Related problems:

### 1.2 Frequency Counting

To be completed.

### 1.3 Complement Lookup

To be completed.

## 10. Module Progress

- Total problems: 12
- Completed: 0
- Remaining: 12
- Patterns mastered: 0/9

---

**AlgoForge — Don't memorize solutions. Master the patterns.**