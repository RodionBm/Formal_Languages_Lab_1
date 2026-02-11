import random
from typing import Set, List, Dict, Optional
from models import Production
from finite_automaton import FiniteAutomaton

class Grammar:
    
    def __init__(self):
        self.VN: Set[str] = {'S', 'B', 'D', 'Q'}
        self.VT: Set[str] = {'a', 'b', 'c', 'd'}
        self.productions: List[Production] = [
            Production('S', 'aB'),
            Production('S', 'bB'),
            Production('B', 'cD'),
            Production('D', 'dQ'),
            Production('Q', 'bB'),
            Production('D', 'a'),
            Production('Q', 'dQ')
        ]
        self.start_symbol: str = 'S'
        self.random = random.Random()
    
    def get_productions_for_nonterminal(self, nonterminal: str) -> List[Production]:
        return [p for p in self.productions if p.left == nonterminal]
    
    def contains_nonterminal(self, string: str) -> bool:
        return any(nt in string for nt in self.VN)
    
    def get_leftmost_nonterminal(self, string: str) -> Optional[str]:
        indices = []
        for nt in self.VN:
            idx = string.find(nt)
            if idx != -1:
                indices.append((idx, nt))
        
        if not indices:
            return None
        
        return min(indices, key=lambda x: x[0])[1]
    
    def generate_string(self) -> str:
        current = self.start_symbol
        
        while self.contains_nonterminal(current):
            nonterminal = self.get_leftmost_nonterminal(current)
            if not nonterminal:
                break
    
            productions = self.get_productions_for_nonterminal(nonterminal)
            selected = self.random.choice(productions)
            current = current.replace(nonterminal, selected.right, 1)
        
        return current
    
    def generate_valid_strings(self, count: int = 5) -> List[str]:
        strings = []
        print(f"\nGenerated {count} valid strings:")
        print("=" * 40)
        
        for i in range(count):
            s = self.generate_string()
            strings.append(s)
            print(f"{i + 1}: {s}")
        
        print()
        return strings
    
    def to_finite_automaton(self) -> 'FiniteAutomaton':
        states: Set[str] = self.VN.copy()
        states.add('F')  
        alphabet: Set[str] = self.VT.copy()
        initial_state: str = self.start_symbol
        final_states: Set[str] = {'F'}
        transitions: Dict[str, Dict[str, Set[str]]] = {state: {} for state in states}
        for prod in self.productions:
            from_state = prod.left
            right = prod.right
        
            if len(right) == 1:
                terminal = right
                if terminal not in transitions[from_state]:
                    transitions[from_state][terminal] = set()
                transitions[from_state][terminal].add('F')
                
            else:
                terminal = right[0]
                to_state = right[1:]
                if terminal not in transitions[from_state]:
                    transitions[from_state][terminal] = set()
                transitions[from_state][terminal].add(to_state)
        
        return FiniteAutomaton(
            states=states,
            alphabet=alphabet,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )
    
    def __str__(self) -> str:
        result = []
        result.append("Grammar:")
        result.append(f"VN = {self.VN}")
        result.append(f"VT = {self.VT}")
        result.append(f"Start Symbol = {self.start_symbol}")
        result.append("Productions:")
        for prod in self.productions:
            result.append(f"  {prod}")
        return "\n".join(result)