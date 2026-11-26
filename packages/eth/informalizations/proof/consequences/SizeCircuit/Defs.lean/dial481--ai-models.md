---
{
  "module": "proof/consequences/SizeCircuit/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the 3-CNF Γ that says |S| = s (definitions and statements only)

The paper, in the proof of Corollary 7: «a circuit with O(n) gates of two inputs tests whether |S| =
s; a new variable for each gate, clauses of at most 3 literals that force it to equal the value of
the gate, and a clause that makes the output true give a 3-CNF Γ with O(n) variables and O(n)
clauses.
Each S of size s extends to exactly one satisfying assignment of Γ, and no other S to any. Add the
clause {¬x_u, ¬x_v} for each edge uv; Corollary 6 then counts the independent sets of size s.»

* A circuit is a list of gates given as data (`CircuitLowerBound.GateD`: the four values of the
  gate's function on 00, 01, 10, 11, and the numbers of the two wires that it reads). The wires 0 …
  n−1 are the inputs x₀ … xₙ₋₁; gate number t has the wire n + t; the output is the last wire.
  `CircuitLowerBound.WF n K`: every gate reads inputs and earlier gates only. Its value on a word is
  `ENP.eval` of CircuitLowerBoundStatement.lean.
* `gateClauses`, `formulaOf`: one variable for every wire, four clauses of 3 literals for every
  gate, one clause for the output. These are general: `StForces` holds for every gate, also one that
  reads one wire twice or reads its own wire; `StUniqueExtension` holds for every non-empty circuit
  whose gates read earlier wires only.
* `TestsSize gates a`: what is asked of a family of circuits gates n s: at most a·(n+1) gates, and
  the output is 1 exactly on the words with s ones. `sizeGates`
  (proof/consequences/SizeCircuit/CircuitDefs.lean, definitions only) is the family that is built,
  and `StSizeGates` there says that it tests the size; this file does not need to know it.
* `gamma gates n s` is Γ. `StGamma`: the paper's two sentences about it. `StGammaCount`: ψ ∧ Γ has
  as many satisfying assignments as ψ has with exactly s true variables.
* `sizedBy gates E`: ONE call of the procedure E for #3-SAT-or-wider on ψ ∧ Γ. `StSizedBy`: it does
  what the interface `GraphProblems.StSized` asks. Everything above that interface in
  proof/consequences/GraphProblems/ is used unchanged.

Different from the paper: a gate gets four clauses (one for each pair of input values), where the
paper says only «clauses of at most 3 literals»; if a gate reads one wire twice a clause may hold a
literal twice or a literal and its negation, which does no harm; clauses that come out twice are
struck out (`List.dedup`), because the procedure asks for that. For n = 0 no non-empty circuit
satisfies `CircuitLowerBound.WF 0` (its first gate would have to read a wire numbered below 0);
there Γ has no variable and is written directly. `TestsSize` asks for a circuit for every s, also s >
n (there a constant gate would do; `sizeGates` uses its general comparison there too), with one
constant a for all n and s; the paper needs only the given s.
«Corollary 6» is used in the form `Eight.Serves` / `Eight.StEngine` /
`Eight.ViaGrouping.EngineCounts`: the machine for #k-SAT cut into steps, without its reader, since
Turing machines of Mathlib cannot be composed.
For dominating sets the paper adds the clauses of the closed neighborhoods TO Γ and then shortens
them; proof/consequences/GraphProblems/ shortens these clauses alone, and the machine that counts a
leaf, here `sizedBy`, puts Γ beside the formula of the leaf. The numbers are the same; the order
differs.
This file has no theorem. 

 ### From a circuit to clauses 

### `gateClauses`

 «clauses of at most 3 literals that force it to equal the value of the gate»: for the gate g
with the wire i, one clause against each pair of input values with the wrong value of i. 

### `wiresFormula`

 The clauses of all gates of a circuit on n inputs. 

### `formulaOf`

 The clauses of all gates, «and a clause that makes the output true». 

### `Holds`

 The assignment a makes a literal of every clause true. 

### `StForces`

 The four clauses hold exactly if the variable of the wire has the value of the gate. 

### `StUniqueExtension`

 For every circuit K on n inputs in which gates read earlier wires only: every assignment of x₀ …
xₙ₋₁ extends in exactly one way to the variables of the gates so that the clauses of all gates hold,
and then the variable of the last wire has the value of the circuit. (K has at least one gate.) 

 ### The circuit that tests |S| = s 

### `TestsSize`

 «a circuit with O(n) gates of two inputs tests whether |S| = s»: for all n ≥ 1 and all s, gates
n s is a circuit on n inputs with at least one and at most a·(n+1) gates, every gate reads earlier
wires only, and on a word x of length n its output is 1 exactly if x has s ones. Every s is allowed,
also s > n.
(On no inputs there is no such circuit: the first gate would have to read a wire with a number below
0, so `CircuitLowerBound.WF 0 K` fails for every K ≠ []. For n = 0, Γ is written directly; see
`gamma`.) 

### `CertGates`

 The circuits are computed in polynomial time from (n in unary, s in binary). 

 ### Γ 

### `gamma`

 **Γ.** For n = 0 there is no circuit: Γ has no variable; it has no clause if s = 0 and is the
empty clause if s ≥ 1. 

### `numVars`

 The number of variables of Γ: x₀ … xₙ₋₁ and one for each gate (none for n = 0). 

### `StGamma`

 «give a 3-CNF Γ with O(n) variables and O(n) clauses. Each S of size s extends to exactly one
satisfying assignment of Γ, and no other S to any.» S is given by its indicator x : Fin n → Bool.
For n ≥ 1, where Γ = `formulaOf n (gates n s)` on n + (number of gates) variables (written out so,
to have the type of b without a cast). 

### `StGammaCount`

 So a formula ψ on x₀ … xₙ₋₁ together with Γ has as many satisfying assignments as ψ has
satisfying assignments with exactly s true variables. For every n, also n = 0. 

 ### One call of the procedure for counting 

### `withGamma`

 From (n in unary, s, ψ): (number of variables in unary, ψ and Γ, every clause once). 

### `sizedBy`

 «Corollary 6 then counts …»: one call of the procedure E on ψ ∧ Γ; the word that E returns is
read as a number. 

### `StSizedBy`

 **For EVERY procedure E.** Let gates test the size with at most a·(n+1) gates, let w be a width
and δ > 0, and let E serve as the procedure for #max(w,3)-SAT with an exponent δ_E ≥ 0 such that
δ_E·(a+1) ≤ δ. Then `sizedBy gates E` returns, on (n in unary, s, ψ) for s ≤ n (as in
`GraphProblems.StSized`; the machine itself would not need it: its states are those of E on ψ ∧ Γ,
and Γ has at most a·(n+1) gates for every s) and ψ of width at most w on x₀ … xₙ₋₁,
the number of satisfying assignments of ψ with exactly s true variables, within c'·2^{δn} steps, on
states of size polynomial in n and the number of clauses. «All these formulas have O(n) variables,
so Corollary 6, applied with a small enough value in place of δ, gives time O(2^{δn}).» 

### `StSizedCert`

 The steps of `sizedBy gates E` are polynomial time if those of E are and the circuits are
computed in polynomial time. 

### `StCircuitExists`

 There is such a family of circuits. (The proof names it: `sizeGates`.) 

### `StSizedFromEngine`

 **The interface `GraphProblems.StSized` of proof/consequences/GraphProblems/ with its machine
named.** From Corollary 6 for machines cut into steps (`Eight.StEngine`): for every family of
circuits that tests the size and is computed in polynomial time, every width w and every δ > 0, the
machine that does what `StSized` asks is `sizedBy gates E`, for a procedure E for #max(w,3)-SAT with
an exponent small enough for the O(n) variables of Γ. 

### `StSizedFromEngines`

 **With the procedure named.** For EVERY family En k ℓ τ of procedures for #k-SAT of which
Corollary 6 for machines cut into steps holds (`Eight.ViaGrouping.EngineCounts`;
`SplitCount.ENGINEsplit` is the family of the printed proof of Corollary 6), every family of
circuits that tests the size and is computed in polynomial time, every width w and every δ > 0: for
some level ℓ and threshold parameter τ, the machine that does what `GraphProblems.StSized` asks is
`sizedBy gates (En (max w 3) ℓ τ)`. 

### `StSizedViaGamma`

 With the family of circuits, the interface `GraphProblems.StSized` of
proof/consequences/GraphProblems/; `StSizedFromEngine` above names the machine. 
