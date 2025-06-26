from collections import deque

class PalindromeChecker:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def push_character(self, ch):
        self.stack.append(ch)

    def enqueue_character(self, ch):
        self.queue.append(ch)

    def pop_character(self):
        return self.stack.pop()

    def dequeue_character(self):
        return self.queue.popleft()

def is_palindrome(s):
    checker = PalindromeChecker()

    # Add characters to stack and queue
    for char in s:
        checker.push_character(char)
        checker.enqueue_character(char)

    # Compare characters from stack and queue
    for _ in range(len(s) // 2):
        if checker.pop_character() != checker.dequeue_character():
            return f'The word, "{s}", is not a palindrome.'

    return f'The word, "{s}", is a palindrome.'

# Sample Input
s = input("Enter a word: ").strip()
print(is_palindrome(s))
