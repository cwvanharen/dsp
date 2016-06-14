# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both compound data types used to group together values. They are also both Sequence Types which means their elements can be accessed efficiently using integer indices. The big difference between them is that lists are mutable; elements in lists can be changed or deleted and elements can be added to lists. Tuples are immutable; though a tuple can contain elements that are themselves mutable, the elements in the tuple cannot be changed or deleted. Tuples can be used as keys in dictionaries, but lists can't. Because any element in a list can be changed or deleted at any time, they would function very poorly as a store for dictionary keys.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both compound data types used to group together values. Sets are not a Sequence Type, they are unordered. Sets also contain no duplicate elements whereas lists can. 

>> ```
>>> ex_list = [1, 3, 4, 'str', 1, 3, 'str']
>>> ex_list[0:3]
[1, 3, 4]
>>> ex_set = set(ex_list)
>>> ex_set
set([1, 3, 4, 'str'])
>>> ex_set[0:3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
```
Sets also support mathematical operations like unions, intersections and tests for subset, superset and disjointedness. 
```
>>> set1 = set([3, 4, 5])
>>> set2 = {5, 6, 7}
>>> set1 & set2
set([5])
>>> set1 < set2
False
```
Finding an element in a set is more efficient than a list because sets are hashable.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda is a way to make anonymous functions (functions without names). It's used to create one-off functions, often within a higher-order function like `map()`, `filter()`, `reduce()` or `sort()`.

>> For example:
```
t = [1, -1, 56, -20, -5, 8]
s = sorted(t, key=lambda x: x**2)
```
Creates a new list 's' sorted by the value of the squares of the elements in 't'. Another example:
```
v = map(lambda x: x%2, t)
```
Creates a list 'v' where an even number in 't' returns a 0 and an odd number returns a 1.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way to perform an operation on each element of a list and return a new list. They can be used for this purpose in place of `for` loops or in place of built-in functions like `map` and `filter`. 

>> For example, using set 't' above, we can use list comprehension to create a list equivalent to 'v'.
```
u = [x%2 for x in t]
```
We could use `filter` to keep only the even numbers in 't':
```
def even(x):
    return x%2 == 0
w = filter(even, t)
```
Or we could accomplish the same thing in a simpler way with list comprehension:
```
y = [x for x in t if x%2 == 0]
```
List comprehensions can be used for more complex or specific operations than `map` and `filter`. `map` and `filter` provide a more straighforward, easily readable, way to accomplish simple operations on lists. It seems that in most cases you could use either approach, but that the one suited to the task will be shorter and simpler. 

>> Set and dictionary comprehensions are similar to list comprehensions, but return sets or dictionaries.

>> A set comprehension:
```
set = {x*3 for x in range(1,10)}
```
A dictionary comprehension:
```
d = {x: x**10 for x in range(1,10) if x % 2 != 0}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7,850 days   

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





