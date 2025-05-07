

"""
CS3B, Assignment #5, Logic gate simulation (Part 2)

In this assignemnt I expanded the logic gate simulation program by adding 
3 more main classes. I used solution code to part 1 of professor Yang to build
this second part.

I defined 3 main classes called CostMixin, NodeMixin and Circuit.
Purpose of CostMixin is to provide a cost tracking ability to logic gates and 
finally Circuit class.

Purpose of NodeMixin class is to build a linked list structure to track and 
capture the chain of gates. 

last one is the Circuit Class that aims to simulate a circuit with ability of
holding different gates and their chain relationship, their costs.

Finally I created a global function called full_adder to show how useful the 
logic gates are and to test their functionalities.

"""


class Input:
    def __init__(self, owner):
        if not isinstance(owner, LogicGate):
            raise TypeError("Owner must be a LogicGate instance.")
        self._owner = owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, bool) and value is not None:
            raise ValueError("Input value must be True, False, or None.")
        self._value = value
        self._owner.evaluate()  # Trigger re-evaluation of the gate logic



class Output:
    def __init__(self):
        self._value = None
        self._connections = []  # List of inputs connected to this output

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, bool) and new_value is not None:
            raise ValueError("Output value must be True, False, or None.")
        self._value = new_value
        for input_ in self._connections:  # Update all connected inputs
            input_.value = new_value

    def connect(self, input_):
        if not isinstance(input_, Input):
            raise TypeError("Can only connect to an Input instance.")
        if input_ not in self._connections:
            self._connections.append(input_)
            input_.value = self._value  # Update the input with the current value


class LogicGate:
    """Base class for all logic gates."""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class CostMixin:
    COST_MULTIPLIER = 10  #  cost multiplier as class constant

    def __init__(self, number_of_components):
        self._number_of_components = number_of_components

    @property
    def cost(self):
        """Calculate and return the cost of the gate."""
        return self.COST_MULTIPLIER * (self._number_of_components ** 2)

class NodeMixin:
    def __init__(self):
        self._next = None  # Pointer to the next node in the circuit

    @property
    def next(self):
        """Get the next node in the circuit."""
        return self._next

    @next.setter
    def next(self, next_node):
        """Set the next node in the circuit, ensuring it's either None or a NodeMixin instance."""
        if next_node is not None and not isinstance(next_node, NodeMixin):
            raise TypeError("next_node must be an instance of NodeMixin or None")
        self._next = next_node


class Circuit:
    def __init__(self):
        self.head = None  # Starts the linked list of gates in the circuit

    def add(self, gate):
        """Add a gate to the circuit."""
        if not isinstance(gate, NodeMixin):
            raise TypeError("Gate must be an instance of NodeMixin to be added to the circuit.")
        if self.head is None:
            self.head = gate
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = gate

    @property
    def cost(self):
        """Calculate and return the total cost of the circuit."""
        total_cost = 0
        current = self.head
        while current:
            # checking the current node has a cost attribute before adding it
            if isinstance(current, CostMixin):
                total_cost += current.cost
            current = current.next
        return total_cost
class UnaryGate(LogicGate, CostMixin, NodeMixin):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        CostMixin.__init__(self, number_of_components=2)  # 1 input + 1 output
        NodeMixin.__init__(self)
        self._input = None
        self._output = None

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input_value):
        self._input = input_value
        self.evaluate()  # Re-evaluate the gate's logic whenever the input changes

    @property
    def output(self):
        return self._output

    def evaluate(self):
        # This method will be overridden in subclasses.
        pass

    def connect(self, other_gate):
        """
        Connect the output of this gate to the input of another gate.
        This method assumes that `other_gate` has an `input` property that can be set.
        """
        if not hasattr(other_gate, 'input'):
            raise AttributeError(f"The gate {other_gate.name} does not have an input property.")
        other_gate.input = self.output

class BinaryGate(LogicGate, CostMixin, NodeMixin):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        CostMixin.__init__(self, number_of_components=3)  # 2 inputs + 1 output
        NodeMixin.__init__(self)
        self._input0 = None
        self._input1 = None
        self._output = None

    @property
    def input0(self):
        return self._input0

    @input0.setter
    def input0(self, input_value):
        self._input0 = input_value
        self.evaluate()  # Re-evaluate the gate's logic when the input changes

    @property
    def input1(self):
        return self._input1

    @input1.setter
    def input1(self, input_value):
        self._input1 = input_value
        self.evaluate()  # Re-evaluate the gate's logic when the input changes

    @property
    def output(self):
        return self._output

    def evaluate(self):
        # This method will be implemented in subclasses
        pass

    def connect(self, other_gate, input_index=0):
        """
        Connect the output of this gate to one of the inputs of another binary gate.
        This method assumes that `other_gate` has `input0` and `input1` properties.
        """
        if not (hasattr(other_gate, 'input0') and hasattr(other_gate, 'input1')):
            raise AttributeError(f"The gate {other_gate.name} does not have binary inputs.")

        if input_index == 0:
            other_gate.input0 = self.output
        elif input_index == 1:
            other_gate.input1 = self.output
        else:
            raise ValueError("input_index must be 0 or 1.")

class NotGate(UnaryGate, CostMixin, NodeMixin):
    def __init__(self, name, circuit=None):
        UnaryGate.__init__(self, name)
        CostMixin.__init__(self, number_of_components=2)  # 1 input + 1 output
        NodeMixin.__init__(self)
        if circuit:
            circuit.add(self)

    def evaluate(self):
        if self.input is not None:
            self._output = not self.input


class AndGate(BinaryGate, CostMixin, NodeMixin):
    def __init__(self, name, circuit=None):
        BinaryGate.__init__(self, name)
        CostMixin.__init__(self, number_of_components=3)  # 2 inputs + 1 output
        NodeMixin.__init__(self)
        if circuit:
            circuit.add(self)

    def evaluate(self):
        if self.input0 is not None and self.input1 is not None:
            self._output = self.input0 and self.input1

class OrGate(BinaryGate, CostMixin, NodeMixin):
    def __init__(self, name, circuit=None):
        BinaryGate.__init__(self, name)
        CostMixin.__init__(self, number_of_components=3)  # 2 inputs + 1 output
        NodeMixin.__init__(self)
        if circuit:
            circuit.add(self)

    def evaluate(self):
        if self.input0 is not None and self.input1 is not None:
            self._output = self.input0 or self.input1

class XorGate(BinaryGate, CostMixin, NodeMixin):
    def __init__(self, name, circuit=None):
        BinaryGate.__init__(self, name)
        CostMixin.__init__(self, number_of_components=3)  # 2 inputs + 1 output
        NodeMixin.__init__(self)
        if circuit:
            circuit.add(self)

    def evaluate(self):
        if self.input0 is not None and self.input1 is not None:
            self._output = self.input0 != self.input1

def full_adder(A, B, Ci):
    # Creating a new circuit
    circuit = Circuit()

    # Instantiating the gates required for the full adder
    xor1 = XorGate("XOR1", circuit)
    xor2 = XorGate("XOR2", circuit)
    and1 = AndGate("AND1", circuit)
    and2 = AndGate("AND2", circuit)
    or_gate = OrGate("OR", circuit)

    # Connecting the gates according to the full adder logic
    # First XOR gate for the first sum operation
    # Second XOR gate to include the carry-in
  # 1
    xor1.input0 = A
    xor1.input1 = B

  # 2
    xor2.input0 = xor1.output
    xor2.input1 = Ci

    # First AND gate for the first part of the carry-out calculation
    # Second AND gate for the second part of the carry-out calculation
    
  # 1
    and1.input0 = A
    and1.input1 = B

  # 2
    and2.input0 = xor1.output
    and2.input1 = Ci

    # OR gate to combine the two AND gate outputs for the final carry-out
    # The sum and carry-out results
  # 1 
    or_gate.input0 = and1.output
    or_gate.input1 = and2.output

  # 2
    S = xor2.output  # Final sum output
    Co = or_gate.output  # Final carry-out

    # Evaluate the full adder by evaluating the last gate in the series,
    # which forces evaluation of all preceding gates due to the connected inputs.
    # This will propagate through the circuit and evaluate all gates

    or_gate.evaluate() 
    
    # Return the sum, carry-out, and the total cost of the full adder circuit
    return S, Co, circuit.cost

# This is to present a simple test case for full_adder
# More detailed test is conducted inside unittest. 
S, Co, cost = full_adder(True, False, True)
print(f"Sum: {S}, Carry Out: {Co}, Circuit Cost: {cost}")
# Output should be Sum: False, Carry Out: True, and the cost of the circuit


