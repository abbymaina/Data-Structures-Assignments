s = input().strip()
stack = []
queue = []

for char in s:
    stack.append(char)
    queue.append(char)

is_palindrome = True
while stack and queue:
    stack_char = stack.pop()
    queue_char = queue.pop(0)
    if stack_char != queue_char:
        is_palindrome = False
        break

if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")