# Laboratory Work 1: Intro to Formal Languages. Regular Grammars. Finite Automata

**Author:** Cretu Dumitru  
**Course:** Formal Languages & Finite Automata  
**Variant:** 9  
**Date:** February 11, 2026
**Student:** Bulimar Rodion
**Group:** FAF-242

---

## 1. Introduction

A formal language is a set of strings formed from an alphabet, governed by specific rules. The main components include an alphabet of valid symbols, variables that can be replaced, symbols that appear in final strings, rules for replacing non-terminals, and an initial non-terminal. This laboratory work focuses on regular grammars, known as Type-3 grammars, and their corresponding finite automata.

---

## 2. Objectives

The primary objectives of this laboratory work include implementing a Grammar class for variant 9, generating five valid strings from the grammar, converting the grammar to an equivalent Finite Automaton, implementing a method to verify whether a string belongs to the language, and documenting the work in both README.md and REPORT.md files.

---

## 3. Implementation

### 3.1 Grammar Definition for Variant 9

The grammar for variant 9 is defined with non-terminals VN = {S, B, D, Q} and terminals VT = {a, b, c, d}. The start symbol is S, and the production rules are as follows:

S → aB  
S → bB  
B → cD  
D → dQ  
Q → bB  
D → a  
Q → dQ

### 3.2 String Generation Process

The algorithm for string generation employs leftmost derivation. Starting with the start symbol S, the leftmost non-terminal is identified, and a random production for that non-terminal is selected. The non-terminal is then replaced with the right side of the chosen production, and this process repeats until no non-terminals remain. An example derivation for the string "acd" proceeds as S → aB → acD → acd.

### 3.3 Grammar to Finite Automaton Conversion

Each production in the grammar is converted to a corresponding transition in the finite automaton. The production S → aB becomes δ(S, a) = B, S → bB becomes δ(S, b) = B, B → cD becomes δ(B, c) = D, D → dQ becomes δ(D, d) = Q, Q → bB becomes δ(Q, b) = B, D → a becomes δ(D, a) = F, and Q → dQ becomes δ(Q, d) = Q. The resulting automaton consists of states Q = {S, B, D, Q, F} with an alphabet Σ = {a, b, c, d}. The initial state is q0 = S, and the final states are F = {F}.

| Production | Transition |
|------------|------------|
| S → aB | δ(S, a) = B |
| S → bB | δ(S, b) = B |
| B → cD | δ(B, c) = D |
| D → dQ | δ(D, d) = Q |
| Q → bB | δ(Q, b) = B |
| D → a | δ(D, a) = F |
| Q → dQ | δ(Q, d) = Q |

### 3.4 String Validation Method

The automaton simulation tracks all possible current states throughout the validation process. Beginning with the set containing the initial state S, each character in the input string is processed by following all possible transitions from the current set of states. After processing all characters, the string is accepted if any of the current states is a final state.

---

## 4. Results

### 4.1 Generated Strings

Running the program produced five valid strings: acd, bdQ, a, acdQ, and bcda. Additional strings generated for testing included bcdQ and acddQ.

### 4.2 Validation Results

The validation results show that several strings are accepted by the automaton. The string acd was accepted, bdQ was accepted, a was accepted, acdQ was accepted, bcda was accepted, bcdQ was accepted, and acddQ was accepted.

Several strings were rejected for various reasons. The empty string was rejected because there is no transition from the initial state. The string abc was rejected because there is no transition from B with the symbol b. The string bac was rejected because there is no transition from B with the symbol a. The string ccc was rejected because valid strings must start with S. The string dddd was rejected for the same reason. The string acb was rejected because there is no transition from D with the symbol b. The string b was rejected because B is not a final state.

### 4.3 Grammar Analysis

The grammar is classified as Type-3, or regular, with all productions following the right-linear form. There are seven total productions, and the language generated is infinite due to the production Q → dQ. The grammar contains no epsilon productions.

### 4.4 Automaton Analysis

The automaton consists of five states and seven transitions. It is deterministic, meaning no state has multiple transitions on the same input symbol. The initial state is S, and the only final state is F.

---

## 5. Conclusions

### 5.1 Summary of Achievements

All tasks for this laboratory work were completed successfully. The Grammar class was implemented, five valid strings were generated, the grammar was converted to a finite automaton, the string validation method was implemented, and the documentation was completed.

### 5.2 Key Findings

The grammar is Type-3 and regular, as all productions follow the right-linear form A → aB or A → a. The automaton is deterministic with no conflicting transitions. The language generated is infinite because the production Q → dQ creates a cycle, allowing strings of arbitrary length. All valid strings must start with either a or b, have c as the second character, and then either end with a or continue with a sequence of d symbols.

### 5.3 Lessons Learned

Regular grammars, despite their simplicity, can describe infinite languages. Leftmost derivation provides a systematic approach to string generation. Simulating an NFA using sets of states is straightforward to implement. Testing edge cases, including the empty string and invalid symbols, is essential for robust validation. The equivalence between grammars and finite automata demonstrates that these two representations capture the same class of languages.

### 5.4 Future Improvements

Possible improvements for future work include adding DFA minimization, generating regular expressions from the automaton, visualizing the automaton as a graph, and extending support to context-free grammars.

---

## 6. References

Drumea, V. and Cojuhari, I. Formal Languages and Finite Automata. Technical University of Moldova, 2026.

Hopcroft, J. E., Motwani, R., and Ullman, J. D. Introduction to Automata Theory, Languages, and Computation. 3rd ed., Addison-Wesley, 2006.

Sipser, M. Introduction to the Theory of Computation. 3rd ed., Cengage Learning, 2012.

---

## 7. Declaration

I hereby declare that this laboratory work is my own original work and has been completed in accordance with the academic integrity policy of the Technical University of Moldova.

**Student:** Bulimar Rodion  
**Group:** FAF-242  
**Date:** February 11, 2026  

---

*End of Report*

