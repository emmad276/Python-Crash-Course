# Python Crash Course - Class 2: Strings and String Operations

In this class, we explored various aspects of working with strings in Python. Strings are one of the most commonly used data types, and mastering them is essential for any Python programmer. Below are the key topics covered:

## Topics Covered

### 1. Strings
- **Strings** in Python are sequences of characters enclosed in single (`' '`) or double (`" "`) quotes. Strings are immutable, meaning once created, they cannot be changed.

### 2. String Concatenation
- **String concatenation** refers to combining two or more strings using the `+` operator. This is useful for constructing dynamic text.
  - Example: 
    ```python
    "Hello, " + "World!"  # Output: Hello, World!
    ```

### 3. F-strings (Formatted String Literals)
- **F-strings** are a more readable way to include variables and expressions inside strings. Introduced in Python 3.6, they allow you to embed expressions directly inside the string using curly braces `{}`.
  - Example:
    ```python
    name = "Alice"
    print(f"Hello, {name}!")  # Output: Hello, Alice!
    ```

### 4. Multiline Strings
- **Multiline strings** allow for strings that span multiple lines, enclosed within triple quotes (`'''` or `"""`). They are useful for long text blocks or documentation.
  - Example:
    ```python
    multiline = """This is a
    multiline string that spans
    several lines."""
    ```

### 5. `.format()` Method
- The **`.format()` method** is used to insert values into placeholders (`{}`) within a string. It's an older formatting technique compared to f-strings but still widely used.
  - Example:
    ```python
    "Hello, {}!".format("World")  # Output: Hello, World!
    ```

### 6. String Methods and Attributes
- **String methods** are built-in functions that allow manipulation of string data. Some commonly used string methods include:
  - `.upper()`: Converts the entire string to uppercase.
  - `.lower()`: Converts the entire string to lowercase.
  - `.strip()`: Removes any leading or trailing whitespace.
  - **Attributes**: Strings in Python have attributes like length, accessed using `len()`, which returns the number of characters in the string.

  - Example:
    ```python
    text = " Hello World! "
    print(text.upper())  # Output: " HELLO WORLD! "
    print(text.strip())  # Output: "Hello World!"
    print(len(text))  # Output: 13
    ```

## Summary
This class focused on understanding strings in Python, covering string operations such as concatenation, formatting, and the various methods to manipulate strings. These are foundational skills for working with text data in Python.

