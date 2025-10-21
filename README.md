# Pair Cleansing and Swap

You have within the starting template file an initial list formed from paired data, where each value comes immediately after its corresponding name. So, for example, you might have something like

```python
data = ['A', 1, 'B', 2, 'C', 3, 'D', 4, 'E', 5]
```

You also start with a list of names that must be removed from the data list, along with their corresponding values. So, for instance, something like:

```python
blacklist = ['B', 'E']
```

Your goal in this problem is to write a function with takes both the data list and the blacklist as arguments, and then _mutates the data list in place_ to satisfy the following conditions:

- **Cleansing**: Any name that shows up in the blacklist is immediately dropped from the data list, alongside its corresponding value
- **Reordering**: The remaining entries should be reordered so that all names appear first in the list, followed by their corresponding values, maintaining their original relative order.

So, in the above given examples, after your function runs the contents of the `data` list would look like:

```python
['A', 'C', 'D', 1, 3, 4]
```

Note that because your function is modifying the original list, it needs not (and should not) return anything.

In the spirit of mutating the original list, you must abide by the following constraints:

- Strictly in-place: You can not reassign the `data` list to something else
- No slicing assignment: You can not assign slices of `data` (No `data[:] = ...`)
- No non-mutable generators: You can not use list comprehensions or similar functions to create temporary lists that you then reassign

