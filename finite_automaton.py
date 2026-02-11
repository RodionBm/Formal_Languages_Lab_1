from typing import Set, Dict, Optional
from collections import deque

class FiniteAutomaton:
    
    def __init__(self, 
                 states: Set[str],
                 alphabet: Set[str],
                 transitions: Dict[str, Dict[str, Set[str]]],
                 initial_state: str,
                 final_states: Set[str]):
        
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states
    
    def string_belongs_to_language(self, input_string: str) -> bool:
        current_states = {self.initial_state}
        for char in input_string:
            if char not in self.alphabet:
                return False
            
            next_states = set()
            for state in current_states:
                if state in self.transitions and char in self.transitions[state]:
                    next_states.update(self.transitions[state][char])
            
            if not next_states:
                return False
            
            current_states = next_states
        return bool(current_states & self.final_states)
    
    def is_deterministic(self) -> bool:
        for state in self.transitions:
            for symbol in self.transitions[state]:
                if len(self.transitions[state][symbol]) > 1:
                    return False
        return True
    
    def display(self) -> None:
        print("\nFinite Automaton:")
        print(f"States: {self.states}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Initial State: {self.initial_state}")
        print(f"Final States: {self.final_states}")
        print(f"Deterministic: {self.is_deterministic()}")
        print("Transitions:")
        
        for from_state in sorted(self.transitions.keys()):
            for symbol in sorted(self.transitions[from_state].keys()):
                for to_state in sorted(self.transitions[from_state][symbol]):
                    print(f"  δ({from_state}, {symbol}) = {to_state}")
        print()
    
    def __str__(self) -> str:
        result = []
        result.append(f"FA( Q={self.states},")
        result.append(f"    Σ={self.alphabet},")
        result.append(f"    q0={self.initial_state},")
        result.append(f"    F={self.final_states} )")
        return "\n".join(result)