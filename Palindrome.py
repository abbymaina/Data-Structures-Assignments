class Solution:
    def __init__(self):
        self.stack = []

    def push_character(self, ch):
        self.stack.append(ch)

    def pop_character(self):
        return self.stack.pop()


def check_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalpha())

    obj = Solution()

    for char in cleaned:
        obj.push_character(char)

    for char in cleaned:
        if char != obj.pop_character():
            return False

    return True


def main():
    s = input("Enter a word or sentence to check if it is a palindrome: ").strip()

    if not any(c.isalpha() for c in s):
        print("Please enter a valid string containing letters.")
        return

    result = check_palindrome(s)
    if result:
        print(f"The input, '{s}', is a palindrome.")
    else:
        print(f"The input, '{s}', is not a palindrome.")


if __name__ == "__main__":
    main()
