words = ['hello', 'world', 'city', 'seattle', 'bratislava']
# print(words)

# 1) Print the word inside the words list
for i in range(len(words)):
  words[i]

for word in words:
  word

for index,value in enumerate(words):
  value

# print(words[::])
# print(words[1::])
# print(words[0][::])
# print(words[0][1::])
# print(words[:2:])
# print(words[1:2:])
# print(words[::3])
# print(words[2::2])
# 2) Print words in reverse
for i in range(len(words)-1,-1,-1):
  words[i]

# print(words[::-1])

# 3) Print words in reverse and skip one element
for i in range(len(words)-1,-1,-2):
  words[i]

# 4) Print the first letter of the word in the list
for i in range(len(words)):
  words[i][0]

words2 = ['hello', 'hello', 'hello', 'world', 'city', 'seattle', 'bratislava','seattle']
# print(words2)
# Dictionary
dictionary = {} # initialize

# to add an key-value in the dictionary
dictionary["age"] = 1
dictionary

# to iterate over the dictionary
for item in dictionary:
  item

# 5)
# tip # 1 iterate through the lists word2
# tip # 2 access the value of the lists in word2, use that value as the key in the dictionary.
# tip # 3 add word as key in the dictionary and 1 as the value for the key
# expecting unique words in the dictionary

# word_dict = {}
# # for i in range(len(words2)):
# #   word_dict[words2[i]] = 1

# # print(word_dict)


# for key, values in word_dict.items():
#   print(key, values)

# for key in word_dict.keys():
#   print(key)

# for values in word_dict.values():
#   print(values)

# 6) count the frequency of each word, then print the dictionary
# tip # 1 using if and else

# tip # 2 using the 'not' keyword
# tip # 3, if the word is not in the dictionary, add that word to the dictionary.
## Extra tip: access the word in words2, and use that as a key

# tip # 4, else if the word is in the dictionary, add plus one to the value.
word_dict = {}
for i in range(len(words2)):
  if words2[i] not in word_dict:
    word_dict[words2[i]] = 1
  else:
    word_dict[words2[i]] += 1

# print(word_dict)

# Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place / sorted
        # traverse the array from 0 to n-i-1
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
nums = [64, 34,25,12,22,11,90]

sorted_nums = bubbleSort(nums)
# print(sorted_nums)

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    return left
# print(binary_search(sorted_nums,25))
# print(binary_search(sorted_nums,64))
# print(binary_search(sorted_nums,90))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

def factorial_iterative(n):
    sum = 1
    stack = []
    stack.append(n)
    while sum == 1:
      n = stack[-1]
      if stack[-1] == 1:
          for num in stack:
              sum *= num
      else:
          stack.append(n-1)
    return sum

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
# print(fib(9))

def fibIterative(n):
    stack = []
    stack.append(n)
    sum = 0
    while(len(stack) > 0):
        n = stack.pop()
        if n == 0:
            sum += 0
        elif n == 1:
            sum += 1
        else:
            stack.append(n-1)
            stack.append(n-2)
    return sum

# print(fibIterative(9))

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None


# new_node = Node()
# print(new_node)
# print(new_node.data)
# print(new_node.next)
# newer_node = Node(100)
# print(newer_node.data)

# first_node = Node(20)
# second_node = Node(40)
# first_node.next = second_node
# print(first_node)
# print(first_node.next.data)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def addAtHead(self, data):
        self.length += 1
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def print(self):
        if self.head != None:
            current_node = self.head
            strng = str(current_node.data)
            while current_node.next != None:
                current_node = current_node.next
                strng += ("->" + str(current_node.data))
            strng += ("->" + str(current_node.next))
        print(strng)

    def get(self, index):
        current_node = self.head
        count = 0

        if index == 0:
            return self.head.data
        elif index >= self.length:
            return -1
        else:
            while current_node.next != None:
                count += 1
                if index == count:
                    return current_node.next.data
                current_node = current_node.next
    def addAtIndex(self, index, data):
        self.length += 1
        new_node = Node(data)
        current_node = self.head
        count = 0

        if index == 0:
            new_node.next = current_node
            self.head = new_node

        elif index > self.length:
            return -1
        else:
            count += 1
            while count < index:
                current_node = current_node.next
                count += 1
            new_node.next  = current_node.next
            current_node.next = new_node

            # longer code
            # dummy_node = current_node.next
            # current_node.next = new_node
            # new_node.next = dummy_node



my_linked_list = LinkedList()
# print(my_linked_list)
# print(my_linked_list.head)
# print(my_linked_list.head.data)
# print(my_linked_list.head.next)
my_linked_list.addAtHead(5)
my_linked_list.addAtHead(8)
my_linked_list.addAtHead(10)
my_linked_list.addAtHead(2)
# print(my_linked_list.head.data)
# print(my_linked_list.head.next.data)
# print(my_linked_list.length)
# print(my_linked_list.get(0))
# print(my_linked_list.get(3))
my_linked_list.addAtIndex(2,500)
# my_linked_list.addAtIndex(5,1500)
# my_linked_list.addAtIndex(8,3000)
# my_linked_list.print()


# Resource: https://www.youtube.com/watch?v=MK-NZ4hN7rs
# Find the max sum subarray of a fixed size K
# Example input: [4, 2, 1, 7, 8 ,1, 2, 8, 0]

from typing import List
import sys
INT_MIN = -sys.maxsize -1

def find_max_sum_subarray(arr: List, k: int) -> List:
    max_value: int = INT_MIN
    current_running_sum = 0
    for i in range(len(arr)):
        # adds all the values. i < values < k - 1
        # the first few loops until k - 1 would create the current running sum
        # for the first subarray
        # succeding loops would generate other current running sum for the
        # following subarray
        current_running_sum += arr[i]     # 4, 6, 7, 10, 16, 16, 11, 11, 10
        if i >= k-1:
          max_value = max(max_value, current_running_sum)
          current_running_sum -= arr[i-(k-1)]   # subtract the furthest left value of subarray
    return max_value

result = find_max_sum_subarray([4, 2, 1, 7, 8 ,1, 2, 8, 0], 3)
print(result)
