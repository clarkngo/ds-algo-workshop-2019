# Data Structures and Algorithms with Python 2019 @ City University of Seattle

Find me on linkedin: https://www.linkedin.com/in/clarkngo/

Join our group: http://smartandsecurecomputing.org/

For CityU students, contact me at clarkngo@cityuniversity.edu

# Topics
- Big O
- Lists
- Dictionary
- Linear Search
- Bubble Sort
- Binary Search
- Recursion
- Dynamic Programming
- Node
- Linked List
- Sliding Window

# Data Structures
## Dictionary
URL Shortener

Implement a URL shortener with the following methods:

- shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
- restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

<details>
<summary>Hint #1 What Do I Skills do I need?</summary>
<ul>
  <li>For loop</li>
  <li>While loop</li>
  <li>Concatenating strings</li>
  <li>Random picker</li>
  <li>Creating a dictionary</li>
  <li>Accessing a dictionary</li>
</ul>

</details>

<details>
<summary>Hint #2 Steps</summary>
<ol>

  <li>
    <details>
      <summary>
        Generate the six-character alphanumeric string
      </summary>
      <ul>
        options:
        <li>Create a dictionary that has a-z, A-Z, 0-9</li>
        <li>Use <code>string.ascii_uppercase</code>, <code>string.ascii_lowercase</code>, and <code>string.digits</code></li>
      </ul>
    </details>
  </li>

  <li>
    <details>
      <summary>
        Store in a dictionary
      </summary>
      <ul>
        <li>Check if the generated shortened URL exists in the dictionary</li>
      </ul>
    </details>
  </li>

  <li></li>
</ol>
</details>

## List

## Dictionary
- Initialize
print(my_dict.keys())
print(my_dict.values())
for i in my_dict.values():
  print(i)

- Print unique names
- Print unique numbers

## 1) Sort by Frequency
## 2) Sort by Order: i.e. if two values have the same frequency, order must be retained.

- Input: [8,2,4,2,1,7,8,7,2,2]
- Output: [2,2,2,2,8,8,7,7,4,1]

```
def sort(arr):
  dict = {}
  frequency = 1

  # iterate over array
  for index, value in enumerate(arr):
    if not str(value) in dict:
      dict.update({str(value):[frequency,index]})
    else:
      dict[str(value)][0] += 1

  new_list = []

  for key, value in dict.items():
    new_list.append([int(key),value[0],value[1]])

  from operator import itemgetter
  new_list = sorted(new_list, key=itemgetter(1), reverse=True)

  solution_list = []
  for i in new_list:
      for j in range(i[1]):
        solution_list.append(i[0])
  return solution_list

```

## Linked List
https://github.com/clarkngo/python-projects/blob/master/linked-list/design_with_length.py

https://github.com/clarkngo/python-projects/blob/master/linked-list/design_with_tail.py


# Algorithms
O(n) — Linear Time:
Scenario: Only one student in my class who hid my bag knows about it.

Approach: I will have to ask each student individually in the class if they have my bag. If they don’t, I move on to ask the next student.

Worst-Case Scenario: In the worst case scenario, I will have to ask n questions.

Show me the code!
```
def search_for_bag(data):
    found = False
    for i,name in enumerate(data):
        # Have to go through each student to find who has my bag
            if data[name] is True:
                found = True
                return name

data = {
    'Jane' : False,
    'James' : False,
    'Jon' : False,
    'Joe': True
    }
print(search_for_bag(data)) #Joe has my bag.
#o/p: The bag is with Joe
```

O(1) — Constant Time
Scenario: Student who hid my bag name is known to me.

Approach : Since I know Joe has my bag, I’ll directly ask him to give it to me.

Show me the code!
```
#If I know the persons name, I have to take only one step to check
def get_bag(name):
    return data[name]
data = {
    'Jane' : False,
    'James' : False,
    'Jon' : False,
    'Joe': True
    }
print("Is bag with Joe ? " +str(get_bag('Joe')))
#o/p: Is bag with Joe ? True
```

O(n²) — Quadratic Time:
Scenario: In the entire class, only one student knows on which student desk my bag is hidden.

Approach: I will start questioning each student individually and ask him about all the others students too. If I don’t get the answer from the first student, I will move on to the next one.

Worst-Case Scenario: In the worst case scenario, I will have to ask n2 questions, questioning each student about other students as well.

Show me the code!
```
def search_bag(data):
    n = len(data)
    for x in range(n):
       answer = input("Do you have my bag, "+data[x] + "?")
       # each student individually if they have my bag
       if answer == 'yes':
         return "Ha! Found it "+ data[x] + "had my bag"
       else:
        # If they don't have it, ask about all other students.
         for y in range(x+1, n):
            new_answer = input("You think my bag is with " +data[y])
            if new_answer == 'yes':
                return 'Your bag is with '+data[y]
data=  ['Jane','James','Jon', 'Joe']  # Here Joe has the bag
print(search_bag(data))
```
O(log n) — Logarithmic time:
Scenario: Here, all the students know who has my bag but will only tell me if I guessed the right name.

Approach: I will divide the class in half, then ask: “Is my bag on the left side, or the right side of the class?” Then I take that group and divide it into two and ask again, and so on.

Worst Case Scenario: In the worst case, I will have to ask log n questions.

Show me the code!
```
def binary_bag_search(data, target, low = 0, high = None):
    if high is None:
        high = len(data)-1
    if low > high :
        return False
    else:
        mid = (low + high)// 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
           return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data,target, mid+1, high)
data=  ['Jane','James','Jon', 'Joe']  # Here Joe has the bag
found = binary_bag_search(data, 'Joe')
print("Bag Found ?" + found)
```
Source: https://dev.to/jainroe/the-ultimate-guide-to-big-o-notation--learning-through-examples-5ecp

## Linear Search

## Linear Search with two pointers

## Bubble Sort
https://github.com/clarkngo/python-projects/blob/master/algorithms/bubble_sort.py

## Binary Search
```
def search(nums: list, target: int) -> int:
    left = 0;
    right = len(nums) - 1;
    while left < right:
        mid = left + (right - left) // 2
        if mid == target:
            right = mid
        else:
            left = mid + 1
        print(left)
    return left

print(search([1,2,3,4,5,6,7,8,9,10],2))
```

Source: https://github.com/clarkngo/python-projects/blob/master/algorithms/binary_search.py

## Recursion and Dynamic Programming
https://github.com/clarkngo/python-projects/blob/master/math/factorial_iterative.py
https://github.com/clarkngo/python-projects/blob/master/math/fibonacci_iterative.py

## Sliding Window
https://github.com/clarkngo/python-projects/blob/master/algorithms/sliding_window/fixed_size_max_subarray.py
https://github.com/clarkngo/python-projects/blob/master/algorithms/sliding_window/maximum_subarray.py


# Resources
## Big O
https://www.bigocheatsheet.com/

## Python Editor
https://repl.it/languages/python3

