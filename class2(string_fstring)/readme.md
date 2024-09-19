# Python Crash Course - Strings and String Methods

Welcome to the Python Crash Course! In this class, we will cover essential string operations in Python. This document will guide you through the topics we discussed in class.

## Topics Covered

1. **Strings**
   - **Definition**: A string is a sequence of characters enclosed in quotes.
   - **Example**:
     ```python
     my_string = "Hello, World!"
     ```

2. **F-Strings**
   - **Definition**: Formatted string literals (f-strings) allow you to embed expressions inside string literals using `{}` braces.
   - **Example**:
     ```python
     name = "Alice"
     age = 30
     greeting = f"My name is {name} and I am {age} years old."
     print(greeting)
     ```

3. **Multiline Strings**
   - **Definition**: Multiline strings are enclosed in triple quotes (`"""` or `'''`) and can span multiple lines.
   - **Example**:
     ```python
     multiline_string = """This is a string
     that spans multiple lines.
     It maintains the line breaks."""
     print(multiline_string)
     ```

4. **String Methods**
   - **Definition**: Python provides a variety of methods to perform operations on strings.
   - **Common Methods**:
     - `casefold()`: Converts the string to lowercase for case-insensitive comparisons.
       ```python
       text = "HELLO"
       print(text.casefold())  # Output: "hello"
       ```
     - `lower()`: Converts all characters to lowercase.
       ```python
       text = "HELLO"
       print(text.lower())  # Output: "hello"
       ```
     - `lstrip()`: Removes leading whitespace.
       ```python
       text = "  hello"
       print(text.lstrip())  # Output: "hello"
       ```
     - `rstrip()`: Removes trailing whitespace.
       ```python
       text = "hello  "
       print(text.rstrip())  # Output: "hello"
       ```
     - `strip()`: Removes whitespace from the beginning and end of the string.
       ```python
       text = "  hello  "
       print(text.strip())  # Output: "hello"
       ```
     - `title()`: Capitalizes the first letter of each word.
       ```python
       text = "hello world"
       print(text.title())  # Output: "Hello World"
       ```
     - `upper()`: Converts all characters to uppercase.
       ```python
       text = "hello"
       print(text.upper())  # Output: "HELLO"
       ```
     - `replace()`: Replaces a specified substring with another substring.
       ```python
       text = "hello world"
       print(text.replace("world", "Python"))  # Output: "hello Python"
       ```
     - `split()`: Splits the string into a list based on a specified delimiter.
       ```python
       text = "hello world"
       print(text.split())  # Output: ["hello", "world"]
       ```
     - `capitalize()`: Capitalizes the first letter of the string.
       ```python
       text = "hello"
       print(text.capitalize())  # Output: "Hello"
       ```
     - `center()`: Centers the string in a field of a given width.
       ```python
       text = "hello"
       print(text.center(10, "-"))  # Output: "--hello---"
       ```
     - `count()`: Counts the number of occurrences of a substring.
       ```python
       text = "hello hello"
       print(text.count("hello"))  # Output: 2
       ```
     - `endswith()`: Checks if the string ends with a specified substring.
       ```python
       text = "hello world"
       print(text.endswith("world"))  # Output: True
       ```
     - `startswith()`: Checks if the string starts with a specified substring.
       ```python
       text = "hello world"
       print(text.startswith("hello"))  # Output: True
       ```
     - `index()`: Finds the first occurrence of a substring and returns its index.
       ```python
       text = "hello world"
       print(text.index("world"))  # Output: 6
       ```
     - `find()`: Finds the first occurrence of a substring and returns its index, or -1 if not found.
       ```python
       text = "hello world"
       print(text.find("world"))  # Output: 6
       ```
     - `isalnum()`: Checks if all characters in the string are alphanumeric.
       ```python
       text = "hello123"
       print(text.isalnum())  # Output: True
       ```
     - `isalpha()`: Checks if all characters in the string are alphabetic.
       ```python
       text = "hello"
       print(text.isalpha())  # Output: True
       ```
     - `islower()`: Checks if all characters in the string are lowercase.
       ```python
       text = "hello"
       print(text.islower())  # Output: True
       ```
     - `isspace()`: Checks if all characters in the string are whitespace.
       ```python
       text = "   "
       print(text.isspace())  # Output: True
       ```
     - `istitle()`: Checks if the string is in title case (first letter of each word capitalized).
       ```python
       text = "Hello World"
       print(text.istitle())  # Output: True
       ```
     - `swapcase()`: Swaps the case of all characters in the string.
       ```python
       text = "Hello World"
       print(text.swapcase())  # Output: "hELLO wORLD"
       ```

## Conclusion

In this class, we explored the basics of strings in Python, including how to use f-strings for formatting, work with multiline strings, and apply various string methods. Practice these concepts to become proficient in handling strings in Python!

For any questions or further clarification, feel free to reach out.

Happy coding!
