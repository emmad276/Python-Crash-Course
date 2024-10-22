# Hashable Data Types
* A hashable object has a hash value that is consistent during its lifetime and can be compared to other objects. Hashable objects must implement the __hash__() and __eq__() methods.
* Hashable objects can be used as keys in dictionaries and as elements in sets.
* Hashable data types are immutable by nature, meaning their content cannot change after creation.

### Common hashable data types:
* int
* float
* str
* tuple (if it contains only hashable elements)
* bool
* frozenset



# Unhashable Data Types
* An unhashable object does not have a fixed hash value or may not implement the __hash__() method. This is typically because the object is mutable, meaning its contents can change after it’s created.
* Unhashable objects cannot be used as dictionary keys or set elements.

### Common unhashable data types:

* list
* set
* dict