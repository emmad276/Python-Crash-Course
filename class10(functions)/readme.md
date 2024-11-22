# Generator Function

- Python me generator function ek special tarike ka function hota hai jo ek bar me ek value yield karta hai, bajaye saari values ko ek saath return karne ke. Yeh memory-efficient hote hain aur iterables jaisa behave karte hain. Generator functions ka use tab hota hai jab hume ek saath bahut saari values process karni ho, lekin saari memory me load nahi karna chahte.

### Generator Function Syntax
Generator functions normal functions ki tarah likhe jaate hain, lekin inke andar return ki jagah yield ka use hota hai.

### Kaise kaam karta hai:
- Jab generator function ko call karte ho, woh execution nahi karta, balki ek generator object return karta hai.
- Jab aap generator object par next() call karte ho, tab function tab tak execute hota hai jab tak pehla yield statement na mile.
- Har baar next() call karne par function wahi se continue karta hai jahan pichli baar yield hua tha.
- Jab generator me aur values nahi bachi, tab StopIteration exception raise hota hai.

```
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

```
### Advantages of Generator Functions:
- Memory Efficiency: Sirf ek value memory me rakhta hai, jo badi datasets ke liye helpful hai.
- Lazy Evaluation: Execution tab tak nahi hota jab tak next() ya for loop se call na kiya jaaye.
- Infinite Sequence Handling: Aap bina memory overflow ki chinta ke infinite values ko generate kar sakte ho.



# Decorator Function
Python mein decorator functions ek tarah ke wrapper functions hain jo kisi doosre function ko modify karte hain bina uske original code ko directly change kiye. Ye function pe ek layer ya feature add karte hain, jaise logging, authentication, ya timing.

```
# Decorator function
def my_decorator(func):
    def wrapper():
        print("Function call se pehle kuch kaam ho raha hai...")
        func()  # Original function ko call karna
        print("Function call ke baad kuch kaam ho raha hai...")
    return wrapper

# Function jo hum decorate karenge
@my_decorator
def say_hello():
    print("Hello, World!")

# Function ko call karte hain
say_hello()




// Output
Function call se pehle kuch kaam ho raha hai...
Hello, World!
Function call ke baad kuch kaam ho raha hai...

```


### Breakdown:
- my_decorator(func):

Ye ek decorator function hai jo kisi bhi function ko input ke taur par leta hai aur ek wrapped version return karta hai.
- wrapper():

Ye ek nested function hai jo naye behavior ko implement karta hai.
Original function ko modify karte hue naye kaam add karta hai.
- @my_decorator:

Ye syntax decorator ko say_hello function pe apply karta hai. Iska matlab hai, say_hello ab wrapper ban chuka hai.

### Example 2: Argument waale function ke liye decorator
Agar function arguments leta hai, toh decorator ko bhi unhe handle karna hota hai.

```
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function call se pehle kuch kaam ho raha hai...")
        result = func(*args, **kwargs)  # Original function ko call karna
        print("Function call ke baad kuch kaam ho raha hai...")
        return result
    return wrapper

@my_decorator
def add_numbers(a, b):
    return a + b

# Function ko call karte hain
print(add_numbers(5, 10))



//Output
Function call se pehle kuch kaam ho raha hai...
Function call ke baad kuch kaam ho raha hai...
15

```


### Real-Life Usage: Logging ka example
```
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))



// Output
Calling function 'multiply' with arguments (3, 4) and {}
Function 'multiply' returned 12
12

```


- Decorators kaafi useful hote hain repetitive tasks (jaise logging, validation, ya error handling) ko simplify karne ke liye.

