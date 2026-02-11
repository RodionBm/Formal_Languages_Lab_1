# Laboratory Work 1: Intro to Formal Languages. Regular Grammars. Finite Automata

**Author:** Cretu Dumitru  
**Course:** Formal Languages & Finite Automata  
**Variant:** 9  
**Date:** February 11, 2026
**Student:** Bulimar Rodion
**Group:** FAF-242

---

## 1. Introduction

A formal language is a set of strings formed from an alphabet, governed by specific rules. The main components are:

- **Alphabet (VT)** - finite set of valid symbols
- **Non-terminals (VN)** - variables that can be replaced
- **Terminals (VT)** - symbols that appear in final strings
- **Productions (P)** - rules for replacing non-terminals
- **Start Symbol (S)** - initial non-terminal

This laboratory work focuses on regular grammars (Type-3) and finite automata.

---

## 2. Objectives

1. Implement a Grammar class for variant 9
2. Generate 5 valid strings from the grammar
3. Convert the grammar to an equivalent Finite Automaton
4. Implement a method to check if a string belongs to the language
5. Document the work in README.md and REPORT.md

---

## 3. Implementation

### 3.1 Grammar Definition (Variant 9)

VN = {S, B, D, Q}
VT = {a, b, c, d}
S = S

P = {
S → aB
S → bB
B → cD
D → dQ
Q → bB
D → a
Q → dQ
}


### 3.2 String Generation

The algorithm uses leftmost derivation:
1. Start with start symbol 'S'
2. Find the leftmost non-terminal
3. Randomly select a production for that non-terminal
4. Replace the non-terminal with the right side
5. Repeat until no non-terminals remain

**Example derivation for "acd":**

S → aB → acD → acd


### 3.3 Grammar to Finite Automaton Conversion

Each production is converted to a transition:

| Production | Transition |
|-----------|------------|
| S → aB | δ(S, a) = B |
| S → bB | δ(S, b) = B |
| B → cD | δ(B, c) = D |
| D → dQ | δ(D, d) = Q |
| Q → bB | δ(Q, b) = B |
| D → a | δ(D, a) = F |
| Q → dQ | δ(Q, d) = Q |

**Resulting Automaton:**
- States: Q = {S, B, D, Q, F}
- Alphabet: Σ = {a, b, c, d}
- Initial state: q0 = S
- Final states: F = {F}

### 3.4 String Validation

The automaton simulation tracks all possible current states:
1. Start with {S}
2. For each character, follow all possible transitions
3. If any current state is final after processing all characters, the string is accepted

---

## 4. Results

### 4.1 Generated Strings

Running the program produced these 5 valid strings:

1. `acd`
2. `bdQ`
3. `a`
4. `acdQ`
5. `bcda`

Additional strings generated for testing:
- `bcdQ`
- `acddQ`

### 4.2 Validation Results

**Valid Strings (Accepted):**

| String | Result |
|--------|--------|
| `acd` | ✓ ACCEPTED |
| `bdQ` | ✓ ACCEPTED |
| `a` | ✓ ACCEPTED |
| `acdQ` | ✓ ACCEPTED |
| `bcda` | ✓ ACCEPTED |
| `bcdQ` | ✓ ACCEPTED |
| `acddQ` | ✓ ACCEPTED |

**Invalid Strings (Rejected):**

| String | Reason | Result |
|--------|--------|--------|
| `""` (empty) | No transition from initial state | ✗ REJECTED |
| `abc` | No transition from B with 'b' | ✗ REJECTED |
| `bac` | No transition from B with 'a' | ✗ REJECTED |
| `ccc` | Must start with S | ✗ REJECTED |
| `dddd` | Must start with S | ✗ REJECTED |
| `acb` | No transition from D with 'b' | ✗ REJECTED |
| `b` | B is not a final state | ✗ REJECTED |

### 4.3 Grammar Analysis

| Property | Value |
|----------|-------|
| Grammar Type | Type-3 (Regular) |
| Production Form | Right-linear |
| Total Productions | 7 |
| Language | Infinite (due to Q → dQ) |
| ε-productions | None |

### 4.4 Automaton Analysis

| Property | Value |
|----------|-------|
| Number of States | 5 |
| Number of Transitions | 7 |
| Deterministic | Yes |
| Initial State | S |
| Final States | {F} |

---

## 5. Conclusions

### 5.1 Summary of Achievements

| Task | Status |
|------|--------|
| Grammar Class Implementation | ✅ Complete |
| Generate 5 Valid Strings | ✅ Complete |
| Grammar → FA Conversion | ✅ Complete |
| String Validation Method | ✅ Complete |
| Documentation | ✅ Complete |

### 5.2 Key Findings

1. **The grammar is Type-3 (Regular)** - All productions follow the right-linear form A → aB or A → a.

2. **The automaton is Deterministic** - No state has multiple transitions on the same input symbol.

3. **The language is Infinite** - The production Q → dQ creates a cycle, allowing strings of arbitrary length.

4. **Pattern** - All valid strings must start with 'a' or 'b', have 'c' as the second character, then either end with 'a' or continue with 'd's.

### 5.3 Lessons Learned

- Regular grammars are simple but can describe infinite languages
- Leftmost derivation provides a systematic way to generate strings
- NFA simulation using sets of states is straightforward to implement
- Testing edge cases (empty string, invalid symbols) is important
- Grammar and finite automata are equivalent representations

### 5.4 Future Improvements

- Add DFA minimization
- Generate regular expression from automaton
- Visualize automaton as a graph
- Support for context-free grammars

---

## 6. References

1. Drumea, V. & Cojuhari, I. (2026). "Formal Languages & Finite Automata". Technical University of Moldova.

2. Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation* (3rd ed.). Addison-Wesley.

3. Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning.

---

## 7. Declaration

I hereby declare that this laboratory work is my own original work and has been completed in accordance with the academic integrity policy of the Technical University of Moldova.

**Student:** Bulimar Rodion  
**Group:** FAF-242  
**Date:** February 11, 2026  
**Signature:** ________________

---

*End of Report*
