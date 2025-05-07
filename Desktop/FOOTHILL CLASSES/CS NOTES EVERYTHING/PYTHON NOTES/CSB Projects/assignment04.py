"""
CS3B, Assignment #04, Logic Gates Simulation - Part 1
Omer Incialan

In this assignment, I wrote a program that simulates logic gates.

I created 3 main classes called Input, Output and LogicGate. Inside these classes 
I defined their specific instance attributes and class methods. These classes 
will serve as a base to actual logicgates function to work as switches.

In addition to these 3 main classes I created 4 more classes to simulate actual 
conditions. These classes are called NotGate, AndGate, OrGate, XorGate. 
They are inheriting some attributes of LogicGate class and some instances
 of input and output classes based on their intended design

These classes used polymorphism and inheritance functionality of python.  

In addition to that I created connection methods where output of certain 
logicgates are used as input to different gates.

In the second file named assignment04_test.py , I prepared a unittest to the 
code I presented here. 


"""

class LogicGate:
    def __init__(self, name):
        self._name = name
        self._output = None  

    @property
    def name(self):
        return self._name

    @property
    def output(self):
        return self._output

    def __str__(self):
        pass

    def evaluate(self):
        # this method will be overridden
        pass
    
class Input:
    def __init__(self, owner):
        if not isinstance(owner, LogicGate):
            raise TypeError("Owner must be a LogicGate instance")
        self._owner = owner
        self._value = None  

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)  # Convert new_value to boolean
        self._owner.evaluate()  # Trigger gate evaluation when input value changes

    def __str__(self):
        return str(self._value) if self._value is not None else "(no value)"

class Output:
    def __init__(self):
        self._value = None
        self._connections = []  # List to hold connections to other inputs

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)  # Convert new_value to boolean
        for input_ in self._connections:
            input_.value = self._value  # Update all connected inputs

    def connect(self, input_):
        """Connects this output to another gate's input."""
        if not isinstance(input_, Input):
            raise TypeError("Can only connect to an Input instance")
        if input_ not in self._connections:
            self._connections.append(input_)
            # If this output already has a value, update the connected input immediately
            if self._value is not None:
                input_.value = self._value

    def __str__(self):
        return str(self._value) if self._value is not None else "(no value)"


class NotGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input = Input(self)  # Create an Input instance owned by this gate
        self._output = Output()  # Initialize the output

    @property
    def input(self):
        return self._input

    def evaluate(self):
        if self._input.value is not None:  # Check if the input has a value
            self._output.value = not self._input.value  # Set the output to the opposite of the input value

    def __str__(self):
        return f"Gate '{self.name}': input={self._input}, output={self._output}"

class AndGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # First input
        self._input1 = Input(self)  # Second input
        self._output = Output()

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
        if self._input0.value is not None and self._input1.value is not None:
            # Perform AND operation and set the output
            self._output.value = self._input0.value and self._input1.value

    def __str__(self):
        return f"Gate '{self.name}': input0={self._input0}, input1={self._input1}, output={self._output}"


class OrGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)
        self._input1 = Input(self)
        self._output = Output()

    def evaluate(self):
        if self._input0.value is not None and self._input1.value is not None:
            self._output.value = self._input0.value or self._input1.value

class XorGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)
        self._input1 = Input(self)
        self._output = Output()

    def evaluate(self):
        if self._input0.value is not None and self._input1.value is not None:
            self._output.value = self._input0.value != self._input1.value
