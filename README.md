# Formal Languages & Finite Automata - Laboratory Work 1

## 📋 Variant 9

**Grammar Definition:**
- VN = {S, B, D, Q}
- VT = {a, b, c, d}
- Start Symbol = S
- Productions:
S → aB
S → bB
B → cD
D → dQ
Q → bB
D → a
Q → dQ


## 📁 Project Structure
```bash
formal-languages-lab/
├── main.py # Main program entry point
├── grammar.py # Grammar class implementation
├── finite_automaton.py # Finite Automaton class implementation
├── models.py # Production data model
├── README.md # Project documentation (this file)
└── REPORT.md # Academic laboratory report
```


## How to Run

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/formal-languages-lab
cd formal-languages-lab

# Run the program
python main.py
```

## Features
- Grammar representation with non-terminals, terminals, and production rules

- Random valid string generation using leftmost derivation

- Grammar to Finite Automaton conversion

- String validation using NFA simulation

- Determinism check for automaton

- No external dependencies - uses only Python standard library

## Example Output
``` bash
Generated 5 valid strings:
1: acd
2: bdQ
3: a
4: acdQ
5: bcda

Finite Automaton:
States: {'F', 'S', 'B', 'D', 'Q'}
Alphabet: {'a', 'b', 'c', 'd'}
Initial State: S
Final States: {'F'}
Transitions:
  δ(S, a) = B
  δ(S, b) = B
  δ(B, c) = D
  δ(D, d) = Q
  δ(D, a) = F
  δ(Q, b) = B
  δ(Q, d) = Q
```

## Test Results

Valid Strings (Accepted):
```bash
acd     → S → aB → acD → acd
bdQ     → S → bB → bcD → bdQ
a       → S → aB → acD → a
acdQ    → S → aB → acD → acdQ
bcda    → S → bB → bcD → bcdQ → bcda
bcdQ    → S → bB → bcD → bcdQ
acddQ   → S → aB → acD → acdQ → acddQ
```

Invalid Strings (Rejected):
```bash
""      (empty string)
abc     (no transition from B with 'b')
bac     (no transition from B with 'a')
ccc     (must start with S)
dddd    (must start with S)
acb     (no transition from D with 'b')
b       (B is not a final state)
c       (no transition from S with 'c')
d       (no transition from S with 'd')
```

## Requirements

```bash
Python 3.6 or higher
No external libraries required

## Usage Examples

from grammar import Grammar
from finite_automaton import FiniteAutomaton

# Create grammar
grammar = Grammar()

# Generate a valid string
string = grammar.generate_string()
print(f"Generated: {string}")

# Convert to Finite Automaton
fa = grammar.to_finite_automaton()

# Check if string is valid
result = fa.string_belongs_to_language("acd")
print(f"Is 'acd' valid? {result}")  # True
```

## Class Overview

Grammar Class:
__init__()	- Initializes grammar with variant 9 rules
generate_string()	- Generates one random valid string
generate_valid_strings(n)	- Generates n valid strings
to_finite_automaton()	- Converts grammar to FA

FiniteAutomaton Class:
string_belongs_to_language(s) -	Checks if string s is accepted
is_deterministic()	- Checks if automaton is DFA
display()	- Prints automaton configuration

##  Objectives Achieved

- Implement Grammar class for variant 9
- Generate 5 valid strings from the language
- Convert Grammar to Finite Automaton
- Implement string validation method
- Document with README.md and REPORT.md
- Push to GitHub repository
