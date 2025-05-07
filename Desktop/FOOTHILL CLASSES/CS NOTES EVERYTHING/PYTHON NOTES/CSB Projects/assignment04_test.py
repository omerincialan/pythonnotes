import unittest
from assignment04 import NotGate, AndGate, OrGate, XorGate, Input, Output  

class TestLogicGates(unittest.TestCase):

    def test_input_behavior(self):
        gate = NotGate("TestNotGate")
        self.assertIsNone(gate.input.value, "Input value should initially be None.")
        gate.input.value = True
        self.assertTrue(gate.input.value, "Input value should be True after setting to True.")
        gate.input.value = False
        self.assertFalse(gate.input.value, "Input value should be False after setting to False.")

    def test_output_behavior(self):
        gate = NotGate("TestNotGate")
        self.assertIsNone(gate.output.value, "Output value should initially be None.")
        gate.input.value = True  # Trigger evaluation
        self.assertFalse(gate.output.value, "Output value should be False when NOT gate input is True.")

    def test_not_gate_logic(self):
        gate = NotGate("TestNotGate")
        gate.input.value = True
        self.assertFalse(gate.output.value, "NOT gate output should be False when input is True.")
        gate.input.value = False
        self.assertTrue(gate.output.value, "NOT gate output should be True when input is False.")

    def test_and_gate_logic(self):
        
        gate = AndGate("TestAndGate")
        test_cases = [(False, False, False), (False, True, False), (True, False, False), (True, True, True)]
        for _input0, _input1, expected in test_cases:
            with self.subTest(_input0=_input0, _input1=_input1, expected=expected):
                gate._input0.value = _input0
                gate._input1.value = _input1
                self.assertEqual(gate.output.value, expected, f"AND gate failed with inputs ({_input0}, {_input1})")

    def test_or_gate_logic(self):
        
        gate = OrGate("TestOrGate")
        test_cases = [(False, False, False), (False, True, True), (True, False, True), (True, True, True)]
        for _input0, _input1, expected in test_cases:
            with self.subTest(_input0=_input0, _input1=_input1, expected=expected):
                gate._input0.value = _input0
                gate._input1.value = _input1
                self.assertEqual(gate.output.value, expected, f"OR gate failed with inputs ({_input0}, {_input1})")

    def test_xor_gate_logic(self):
        gate = XorGate("TestXorGate")
        test_cases = [(False, False, False), (False, True, True), (True, False, True), (True, True, False)]
        for _input0, _input1, expected in test_cases:
            with self.subTest(_input0=_input0, _input1=_input1, expected=expected):
                gate._input0.value = _input0
                gate._input1.value = _input1
                self.assertEqual(gate.output.value, expected, f"XOR gate failed with inputs ({_input0}, {_input1})")

    def test_gate_connections(self):
        # Test NOT-NOT connection
        not_gate1 = NotGate("FirstNotGate")
        not_gate2 = NotGate("SecondNotGate")
        not_gate1.output.connect(not_gate2.input)
        not_gate1.input.value = False
        self.assertFalse(not_gate2.output.value, "Second NOT gate output should be False when first NOT gate input is True.")

        # Test AND-NOT connection
        and_gate = AndGate("TestAndGate")
        not_gate = NotGate("TestNotGate")
        and_gate.output.connect(not_gate.input)
        and_gate._input0.value = True
        and_gate._input1.value = True
        self.assertFalse(not_gate.output.value, "NOT gate output should be False when AND gate inputs are both True.")

if __name__ == '__main__':
    unittest.main()
    
  
