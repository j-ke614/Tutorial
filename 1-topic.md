[Welcome Page](welcome.md)

# Stacks 

    - Last in first out
    - Insetion Deletion happen on same end
    - Linear data structure

Stack is a data structure that is well know as "Last in, First out" (LIFO), 
Think about a train, there are several cars all connected together. When you add a car you add it to the back and then to get to the
car in front of it you have to take that car off. This is how stacks work, last in, first out. 
Now when we add to the stack in python it is called a 'Push' and when we take the last item off the stack it is called a 'POP'

Think about when you are working in excel or writing a paper and you make a mistake, you can hit CTRL+Z to undo the last thing you did. 
This is an example of a stack, probalvy the one most people are familiar with. You can hit CTRL+Z a numbe of times, each time it 'POPS' the last 
item off of the stack, or UNDOes the last item. 

In Python there are a couple of 'Stack Operations' to be aware of:
    Stack Operations

    - push(value)       python code >>> my_stack.append('item to be appended(added)')
    - pop()             python code >>> value = my_stack.pop()

## Example

[Example](stack.py)

## Problem

Now try to build a simple to-do list using stack.



    