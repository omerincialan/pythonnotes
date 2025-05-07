"""
CS3B, Assignment #02, RPN Calculator
Omer Incialan
In this assignment, I wrote a program that calculates RPN operations. 
RPN is another way of writing math expression in which operator is placed 
after operands in a left to right order.
In this program, I first benefited from the Mystack class I was provided to 
use as an instantiator. Inside this Mystack class, operations related to 
stack creating, and manipulating (push(), pop(), clear()) were placed already.
I created another class called RpnCalculator in which I define the rules 
and requirements for RPN calculations.
I benefited from staticmethods eval, parse, eval_tokens and multiply to build 
functionality.
"""
import numpy as np

class MyStack:
    # Constants
    MAX_CAPACITY = 100000
    DEFAULT_CAPACITY = 20

    # Initializer method
    def __init__(self, default_item, capacity=DEFAULT_CAPACITY):
        # If the capacity is bad, fail right away
        if not self.validate_capacity(capacity):
            raise ValueError("Capacity " + str(capacity) + " is invalid")
        self._capacity = capacity
        self._default_item = default_item

        # Make room in the stack and make sure it's empty to begin with
        self.clear()

    def clear(self):
        # Allocate storage the storage and initialize top of stack
        self._stack = np.empty(self._capacity, dtype=type(self._default_item))
        self._top_of_stack = 0

    @classmethod
    def validate_capacity(cls, capacity):
        return 0 <= capacity <= cls.MAX_CAPACITY

    def push(self, item_to_push):
        if self.is_full():
            raise OverflowError("Push failed - capacity reached")

        self._stack[self._top_of_stack] = item_to_push
        self._top_of_stack += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop failed - stack is empty")

        self._top_of_stack -= 1
        return self._stack[self._top_of_stack]

    def is_empty(self):
        return self._top_of_stack == 0

    def is_full(self):
        return self._top_of_stack == self._capacity

    def get_capacity(self):
        return self._capacity

class RpnCalculator:
    # Class constants for arithmetic operations
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "//"

    @staticmethod
    def eval(rpn_expression):
        tokens = RpnCalculator.parse(rpn_expression)

        return RpnCalculator.eval_tokens(tokens)

    @staticmethod
    def parse(rpn_expression):
        return rpn_expression.split()

    
    @staticmethod
    def eval_tokens(tokens):
        
        if not tokens:
            raise ValueError("Empty RPN expression")
        
        stack = MyStack(-1, len(tokens))  # Initialize the stack

        for token in tokens:
            
            
            try:
                # Attempt to convert the token to an integer
                number = int(token)
                stack.push(number)
            except ValueError:
                # If the conversion fails, process as an operator
                if token in [RpnCalculator.ADD, RpnCalculator.SUBTRACT, RpnCalculator.MULTIPLY, RpnCalculator.DIVIDE]:
                    # Check for sufficient operands
                    if stack.is_empty() or (stack._top_of_stack < 2 and token != ""):
                        raise ValueError("Insufficient operands for operation")

                    # Perform the operation
                    b = stack.pop()
                    a = stack.pop()

                    if token == RpnCalculator.ADD:
                        stack.push(a + b)
                    elif token == RpnCalculator.SUBTRACT:
                        stack.push(a - b)
                    elif token == RpnCalculator.MULTIPLY:
                        stack.push(RpnCalculator.multiply(a, b))
                    elif token == RpnCalculator.DIVIDE:
                        stack.push(a // b)
                else:
                    # Token is neither an integer nor a recognized operator
                    raise ValueError(f"Invalid token: '{token}' is neither a digit nor a recognized operator")

        # Check for leftover operands in the stack
        if stack._top_of_stack != 1:
            raise ValueError("Invalid RPN expression: leftover operands in stack")
        

        return stack.pop()


    @staticmethod
    def multiply(a, b):
        # Helper function for recursive multiplication
        def recursive_multiply(x, y):
            if y == 0:
                return 0
        
            return x + recursive_multiply(x, y - 1)

        # Check for negative values to handle sign
        if a < 0 and b < 0:
            return RpnCalculator.multiply(-a, -b)
        elif a < 0 or b < 0:
            return -RpnCalculator.multiply(abs(a), abs(b))

        return recursive_multiply(a, b)

    
    
    
def mystack_test():
    # Instantiate two empty stacks, one of 50 ints, another of 10 strings
    s1 = MyStack(-1, 50)
    s2 = MyStack("undefined")
    # and one more with bad argument
    try:
        s3 = MyStack(None, -100)
        print("Failed test: expected __init()__ to reject negative capcity but it didn't")
    except Exception as e:
        print("Successful test: handled negative capacity: " + str(e))

    # Confirm the stack capacities
    print("------ Stack Sizes -------\n  s1: {}   s2: {}\n".
          format(s1.get_capacity(), s2.get_capacity()))

    # Pop empty stack
    print("------ Test stack ------\n")
    try:
        s1.pop()
        print("Failed test: expected pop() to raise empty-stack exception but it didn't")
    except Exception as e:
        print("Successful test: handled popping empty s1: " + str(e))

    # Push some items
    s1.push(44)
    s1.push(123)
    s1.push(99)
    s1.push(10)
    s1.push(1000)
    # try to put a square peg into a round hole
    try:
        s1.push("should not be allowed into an int stack")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s2.push(444)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s1.push(44.4)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    # Push to s2
    s2.push("bank")
    s2.push("-34")
    s2.push("should be okay")
    s2.push("a penny earned")
    s2.push("item #9277")
    s2.push("where am i?")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    try:
        s2.push("This is when stack is full")
        print("Failed test: expected push() to throw exception but it didn't")
    except Exception as e:
        print("Successful test: handled pushing when stack is full: " + str(e))
    print("\n--------- First Stack ---------\n")

    # Pop and inspect the items
    for k in range(0, 10):
        try:
            print("[" + str(s1.pop()) + "]")
        except Exception as e:
            print("Successful test: handled popping empty stack s1: " + str(e))
    print("\n--------- Second Stack ---------\n")
    for k in range(0, 10):
        print("[" + str(s2.pop()) + "]")

def demo_lost_functionalities():
    """
    In here, I focused on lost functionalities in MyStack due to 
    the use of numpy.array.

    1. Homogeneity of Data Types: numpy.array in MyStack enforces 
    the same data type for all elements, whereas Python lists can store 
    elements of different types.

    2. Fixed Size: numpy.array has a fixed size, and unlike Python lists, 
    it does not automatically resize when elements are added beyond its 
    capacity.

    3. Type Matching on Append: Appending elements of a different type 
    is not straightforward with numpy.array.
    
    4. Memory Overhead: Python lists have a higher memory overhead per 
    element compared to numpy.array. While this might not be a 'lost' 
    functionality, it's a behavioral change. numpy.array is more 
    memory-efficient, especially for large datasets, but this comes 
    at the cost of flexibility in resizing and type homogeneity.

    5. Method Availability: Python lists come with a variety of built-in 
    methods like append(), extend(), insert(), remove(), and more. 
    numpy.array doesn't support all these methods directly. Operations like
    inserting or removing elements are more complex and less efficient 
    with numpy.array.

    7. Element-wise Operations: While numpy.array excels at element-wise 
    operations (like adding a number to every element), this 
    functionality is often unnecessary for a stack data structure and 
    adds complexity when performing simple stack operations.

    8. Slicing and Indexing: Python lists offer more straightforward 
    slicing and indexing capabilities. While numpy.array also supports 
    these, the focus is more on multidimensional array operations, 
    which might be overkill for a stack implementation.
    
    """

    # Example demonstrating the homogeneity of data types
    print(f"\n----- This part is to test lost functionalities "
          "\n due to use of numpy array instead of stack ----\n")
        
    try:
        stack = MyStack(0)
        stack.push("string")  # This would fail because MyStack is initialized with an int
    except Exception as e:
        print("Homogeneity Example: " + str(e))

    # Example demonstrating fixed size
    try:
        stack = MyStack(0, 2)
        stack.push(1)
        stack.push(2)
        stack.push(3)  # This should fail due to fixed size of numpy.array
    except Exception as e:
        print("Fixed Size Example: " + str(e))
        
def test_rpn():
    # List of test RPN expressions
    test_expressions = [
        "",                         # Empty string
        " ",                        # Space character
        " 1 +",                     # First character is a space 
        "1 +",                      # Insufficient operands
        "1 1",                      # Insufficient operator
        "1 1 fly",                  # Invalid operator
        "random junk",              # Nonsensical input
        "f f",                      # invalid character
        "f",                        # invalid character
        "f f +",                    # invalid character
        "- * +",                    # All operator no operand 
        "3",                        # Single number
        "3 4 +",                    # Simple addition
        "9999999 99999999 * ",      # Large numbers multiplication
        "9999999999 99999999 + ",   # Large numbers addition
        "9999999999 99999999 - ",   # Large numbers addition
        "34+5+",                    # No space
        "3 4 + -",                  # Simple addition
        "3 4 5 +",                  # Simple addition
        "10 2 -",                   # Simple subtraction
        "1 20 -",                   # Subtraction with negative result
        "0 3 *",                    # multiplying when first value is 0
        "0 3 *",                    # multiplying when second value is 0
        "5 3 *",                    # simple multiplication
        "-4 3 *",                   # multiplication with a negative
        "-3 -5 *",                  # multiplication both negative
        "8 4 //",                   # Simple division
        "8 0 //",                   # Division by zero
        "3 4 + 5 *",                # Combined operations
        "15 7 1 1 + - // 3 * 2 1 1 + + -",  # Complex expression
 
    ]

    # Evaluate each expression and handle exceptions
    print("\n$$$$ test_rpn test results $$$$\n")
    for expr in test_expressions:
        try:
            result = RpnCalculator.eval(expr)
            print(f"({expr}) = {result}")
        except Exception as e:
           print(f'"{expr}" fails to be evaluated, \n--> FAIL REASON : {str(e)}')

if __name__ == "__main__":
    mystack_test()
    test_rpn()
    demo_lost_functionalities()



