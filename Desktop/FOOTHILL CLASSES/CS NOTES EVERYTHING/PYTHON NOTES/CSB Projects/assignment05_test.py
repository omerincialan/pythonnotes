import unittest

# Assuming your logic gate classes and Circuit class are defined in a file named logic_gates.py
from assignment5 import *

class TestLogicGates(unittest.TestCase):

    def test_not_gate(self):
        not_gate = NotGate("NOT1")
        not_gate.input = True
        self.assertFalse(not_gate.output, "NOT gate with True input should have False output")
        not_gate.input = False
        self.assertTrue(not_gate.output, "NOT gate with False input should have True output")

    def test_and_gate(self):
        and_gate = AndGate("AND1")
        and_gate.input0 = True
        and_gate.input1 = False
        self.assertFalse(and_gate.output, "AND gate with one False input should have False output")
        and_gate.input1 = True
        self.assertTrue(and_gate.output, "AND gate with two True inputs should have True output")

    def test_circuit_cost(self):
        circuit = Circuit()
        NotGate("NOT1", circuit)
        AndGate("AND1", circuit)
        # Assuming the cost of a NotGate is 40 and an AndGate is 90 based on their components
        expected_cost = 40 + 90
        self.assertEqual(circuit.cost, expected_cost, f"Expected circuit cost {expected_cost}, got {circuit.cost}")

    def test_or_gate(self):
        or_gate = OrGate("OR1")
        or_gate.input0 = False
        or_gate.input1 = False
        self.assertFalse(or_gate.output, "OR gate with two False inputs should have False output")
        or_gate.input1 = True
        self.assertTrue(or_gate.output, "OR gate with at least one True input should have True output")

    def test_xor_gate(self):
        xor_gate = XorGate("XOR1")
        xor_gate.input0 = False
        xor_gate.input1 = False
        self.assertFalse(xor_gate.output, "XOR gate with two False inputs should have False output")
        xor_gate.input0 = True
        self.assertTrue(xor_gate.output, "XOR gate with one True and one False input should have True output")
        xor_gate.input1 = True
        self.assertFalse(xor_gate.output, "XOR gate with two True inputs should have False output")

    def test_complex_circuit(self):
        # Simulate a more complex circuit combining different gates
        circuit = Circuit()
        gate1 = NotGate("NOT1", circuit)
        gate2 = AndGate("AND1", circuit)
        gate3 = OrGate("OR1", circuit)

        # Setup a scenario for the circuit
        gate1.input = True  # NOT gate inverts True to False
        gate2.input0 = gate1.output  # AND gate with one False input should result in False
        gate2.input1 = True
        gate3.input0 = gate2.output  # OR gate with one False input should follow the other input
        gate3.input1 = True  # Ensuring OR gate output is True

        # Check the final output of the complex circuit
        self.assertTrue(gate3.output, "Complex circuit with the given inputs should result in True")

    def test_input_initialization(self):
        gate = NotGate("NOT")
        self.assertIsNone(gate.input, "Gate input should initially be None")

    def test_input_value_setting(self):
        gate = NotGate("NOT")
        gate.input = True
        self.assertTrue(gate.input, "Gate input value should be settable to True")

    def test_output_initialization(self):
        gate = NotGate("NOT")
        self.assertIsNone(gate.output, "Gate output should initially be None")



class TestFullAdder(unittest.TestCase):

    def test_full_adder(self):
        # Define all possible input combinations and expected outputs
        test_cases = [
            # A, B, Ci, Expected Sum, Expected Carry-Out
            (False, False, False, False, False),
            (False, False, True,  True,  False),
            (False, True,  False, True,  False),
            (False, True,  True,  False, True),
            (True,  False, False, True,  False),
            (True,  False, True,  False, True),
            (True,  True,  False, False, True),
            (True,  True,  True,  True,  True),
        ]

        for A, B, Ci, expected_S, expected_Co in test_cases:
            S, Co, _ = full_adder(A, B, Ci)  # Ignore the cost for these tests
            self.assertEqual(S, expected_S, f"Failed with inputs A={A}, B={B}, Ci={Ci}: Expected Sum={expected_S}, got {S}")
            self.assertEqual(Co, expected_Co, f"Failed with inputs A={A}, B={B}, Ci={Ci}: Expected Carry-Out={expected_Co}, got {Co}")

if __name__ == '__main__':
    unittest.main()
