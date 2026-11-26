---
{
  "module": "proof/statements/CircuitLowerBoundStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/CircuitLowerBoundStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/CircuitLowerBoundStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The statement of the circuit lower bound for E^NP (Section 7): E^NP does not have circuits of linear size

The statement of the paragraph «Circuit lower bounds» in Section 7 of the paper: E^NP, the class of
languages decided in time 2^{O(n)} with an oracle for NP, does not have linear-size circuits, that
is, some language in E^NP is not decided by
(non-uniform) Boolean circuits of size O(n).

This file has definitions only (no theorem, no proof) and imports Mathlib only: it can be read
without any other file of this development.

## How to read it

* A language (`Lang`) is a set of words over {0,1}.
* A circuit is a straight-line program. On an input of n bits it has the wires 0, 1, 2, …: the wires
  0 … n−1 carry the input bits, and the wire n + t carries the value of gate number t. A gate
  (`Gate`) is ANY function of
  two bits (all 16 are allowed, so also constants, copies and negations) together with the numbers
  of the two wires that it reads. A circuit (`Circuit`) is the list of its gates, in order. Its
  output is the value of its last
  wire. Its size is the number of its gates; the inputs are not counted. All 16 functions are
  allowed because this makes a lower bound strongest: a circuit over a smaller basis (say AND, OR,
  NOT) is such a circuit
  with the same number of gates.
* A gate that names a wire that does not exist yet (its own wire, a later one, or none at all) reads
  0 there. This gives circuits nothing: for n ≥ 1 such a gate can be replaced by a gate that reads
  the wire 0 and ignores it. It
  is allowed so that no circuit is excluded, and so that a word of length 0 is no exception (a gate
  with a constant value needs no wire).
* L is decided by circuits of size O(n) (`HasLinearCircuits`): for some number c and for EVERY n
  there is a circuit with at most c·(n+1) gates that, on every word x of length n, outputs 1 if and
  only if x ∈ L. There is one circuit for
  each n and nothing is asked on how it depends on n (non-uniform). The «+1» lets the bound also
  cover c·n + c and n = 0. Asking for every n is the same as asking for all large n, because
  finitely many n can be
  paid for by a larger c. So the negation says: for every c there are infinitely many n at which no
  circuit with at most c·(n+1) gates decides L.
* The oracle is satisfiability of formulas in conjunctive normal form (`SAT`), which is NP-complete:
  «an oracle for NP» in the paper. A formula is a list of clauses, a clause is a list of literals, a
  literal is a variable (a natural
  number) with the value that it wants. As a word (`encCnf`): a literal is 1, then the variable in
  unary (1ᵛ0), then its sign; a clause ends with 01; the formula ends with 00. A word that is not
  the code of a formula is not in SAT.
* FIRST FORM, oracle machines (`OTM`, `InENP`). An oracle machine is one of Mathlib's multi-stack
  machines (`Turing.FinTM2`: deterministic, finitely many labels and states, finitely many stacks,
  one of them for the input and one,
  possibly the same, for the output) with one more choice: a query stack over {0,1} and three labels
  «ask», «yes», «no». A step at the label «ask» hands the word on the query stack, top first, to the
  oracle, empties the query stack, and
  goes on at «yes» if the word is in the oracle language, at «no» if not; the statement that the
  program has at «ask» is never run. Every other step is a step of Mathlib's machine (`TM2.step`: it
  runs the statement at the current
  label as far as a `goto` or `halt`; a bounded number of pushes and pops for a fixed machine). A
  query costs one step, whatever its length; the machine has had to push it bit by bit.
* `OTM.Outputs`: started with x on the input stack, the machine halts within T steps with exactly
  the one bit b on its output stack, all other stacks empty and its internal state back at the
  initial one (Mathlib's
  `initList`, `haltList`, `EvalsToInTime`). Mathlib does not ask that every stack has a finite
  alphabet, so `InENP` does.
* «Time 2^{O(n)}»: at most 2^{c·(n+1)} steps on every word of length n, with one number c for the
  machine. Queries may therefore have length up to 2^{c·(n+1)}, as usual for E^NP.
* SECOND FORM, without a new kind of machine (`Protocol`, `InENP'`). An ordinary machine of Mathlib
  is started on x together with the answers given so far, and returns either the result or the next
  query; then it is started
  again. There are at most 2^{c·(n+1)} rounds of at most 2^{c·(n+1)} steps each. The two forms
  define the same class: an oracle machine can be run again from the start after each answer, which
  squares its time, and a machine with a query
  stack can run the rounds one after the other. This equivalence is NOT proved in this file; it is
  the reason why both forms are stated.
* The circuit lower bound for E^NP (Section 7) is stated twice at the end of this file, once with
  the first form and once with the second. In both there is ONE language for all c. 

 ### Languages and circuits 

### `Lang`

 A language: a set of words over {0,1}. 

### `Gate`

 A gate with two inputs: any function of two bits, and the numbers of the two wires that it
reads. 

### `Circuit`

 A circuit: its gates, in order. 

### `wires`

 The values of all wires on the input x: first the bits of x, then the values of the gates, one
after the other. A wire that does not exist yet reads 0. 

### `eval`

 The output of the circuit on the input x: the value of the last wire (0 if there is no wire at
all). 

### `HasCircuits`

 L is decided by circuits with at most s(n) gates on the words of length n, for every n. 

### `HasLinearCircuits`

 L is decided by circuits of size O(n). 

 ### The oracle: satisfiability of formulas in conjunctive normal form 

### `Cnf`

 A formula: a list of clauses; a clause is a list of (variable, wanted value). 

### `Sat`

 Some assignment makes a literal of every clause true. 

### `encLit`

 A literal as a word: 1, the variable in unary, the sign. 

### `encCnf`

 A formula as a word: the literals of each clause, 01 after each clause, 00 at the end. 

### `SAT`

 The words that are codes of satisfiable formulas. 

 ### First form: oracle machines 

### `OTM`

 One of Mathlib's multi-stack machines with input and output over {0,1}, a query stack over {0,1}
and the labels «ask», «yes», «no». 

### `OTM.step`

 One step with the oracle O. At «ask»: the word on the query stack, top first, is handed to the
oracle, the query stack is emptied, and the machine goes on at «yes» or at «no». Otherwise: a step
of the machine. 

### `OTM.Outputs`

 M with the oracle O, started on x, halts within T steps with the one bit b as output. 

### `InENP`

 L is in E^NP: decided in time 2^{O(n)} with an oracle for SAT. 

### `CorCircuits`

 The circuit lower bound for E^NP (Section 7): there is a language in E^NP that is not decided by
circuits of size O(n). 

 ### Second form: an ordinary machine is started again after every answer 

### `roundInput`

 The input of a round: every bit b of x as 1b, then 0, then the answers so far. 

### `Round`

 M, started on x and the answers so far, halts within T steps with the word w as output. 

### `Protocol`

 After the answers «ans», and within r more queries, the result is b. A round returns 0b (the
result is b) or 1w (the query w); every round takes at most T steps. 

### `InENP'`

 L is in E^NP, second form: at most 2^{O(n)} queries to SAT, and at most 2^{O(n)} steps before
each query and before the result. 

### `CorCircuits'`

 The circuit lower bound for E^NP (Section 7), with the second form of E^NP. 
