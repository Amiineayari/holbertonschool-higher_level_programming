Introduction
Python deservedly has a reputation for being an easy language to read and write. It’s got great documentation and a community that is very welcoming to beginners.

As we dig deeper, we may find many aspects of the Python language that surprise us, as one aspect that deserves in-depth explanation is How Everything in Python is an Object? Since Python is an object-oriented programming language, everything in Python is an object, every integer, string, list, and function. Before discussing how everything in Python is an object, let's discuss What is an object?
What is an object?
Since we already know that Python is an object-oriented programming language and also that Everything in Python is an object, the main point of discussion here is first, what is an object? So In object-oriented programming languages like Python, an object is an entity that contains data along with associated metadata or functionality; these data contained in an object are known as the object’s data attributes. These attributes are simply variables that reference the data. The procedures or series of activities conducted in a certain order or manner that an object performs are known as the methods. An object’s methods are functions that perform operations on the object's data attributes.

There can be multiple instances of an object in a program. Different programming languages define “object” in different ways. In some, it means that all objects must-have attributes and methods; in others, it simply means that all objects are subclassable. In Python programming language, its definition is looser as some objects have neither attributes nor methods, and not all objects are subclassable.

But the statement that “Everything in Python is an object” means that it can be assigned to a variable or passed as an argument to a function. So the objects are the building blocks of an object-oriented program, as the program that uses object-oriented technology is basically a collection of objects. Hence programs written in python are also a collection of these objects in the form of variables. So it is important to revise everything in Python object, meaning that the strings are objects, Lists are objects, Functions are objects, and Even modules are objects.

Also See, Intersection in Python

Everything in Python is an Object 
In Python, almost everything is an object, whether a number, a function, or a module. Python is using a pure object model where classes are instances of a meta-class “type” in Python, the terms “type” and “class” are synonyms. And “type” is the only class that is an instance of itself. This object model can be useful when we want information about a particular resource in Python. Except for the Python keywords like “if def, globals”, using type(<name>) or dir(<name>) or just typing the resource name and pressing enter- it will work on pretty much anything. Let’s make it clear what this statement means “Everything in Python is an object”.

Must Read Python List Operations

Consider the following 
As we know it very well that Python has types; however, the types are linked not to the variable names but to the object themselves. Earlier in object-oriented programming languages like Python, an object is an entity that contains data along with associated metadata and/or functionality. In Python, everything is an object, which means every entity has some metadata called “attributes” and associated functionality called “methods”. These attributes and methods are accessed via the dot syntax.

For example, we saw that lists have an append method, which adds an item to the list and is accessed via the dot (“.”) syntax:

While it might be expected for compound objects like lists to have attributes and methods, what is sometimes unexpected is that in Python even simple types have attached attributes and methods.

For example, numerical types have a real and image attribute that returns the real and imaginary part of the value, if viewed as a complex number.

Methods are like attributes, except they are functions that you can call using opening and closing parentheses. For example, floating point numbers have a method called is_integer that checks whether the value is an integer. 

When we say that everything in Python is an object, we really mean that everything is an object – even the attributes and methods of objects are themselves objects with their own type information:

Implementation through C programming language:-

Let’s now dive into the C implementation to see how objects are represented.

Those objects are manipulated under the hood as a C structure called PyObject. Ironically, the CPython object model is implemented using C, a language that is not object-oriented. From there, we will notice the two following attributes:

Firstly a reference count, which keeps track of how many other objects and variables reference it. This is changed in the C code through the macros Py_INCREF() and Py_DECREF().
 
Secondly, a type (PyTypeObject structure), allows Python to determine the type or class of the object at runtime. That type contains various methods used to describe the class's behavior. What function to call to allocate the type, to deallocate the type, to cast as a number, etc?