---
{
  "module": "Paper/Circuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Circuit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Circuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "One scale is all scales": small circuits are accelerators


### `universal_symbols_ne`

 In a nonzero ring the two symbols of a universal automaton are different: with one symbol the words of two plain
instances of equal size, with the values 1 and 0, would be equal. 

### `lem_circuit_universal`

 **Paper: proof of Lemma lem:circuit, Φ for the universal automaton.** "By Corollary cor:clauses a circuit for the
permanent gives one for Φ ... By Proposition prop:universal its value is pv(z) at the code of a plain z": an affine
projection of every family that is complete for clause sums, of degree at most n = v^(H−32)+1, with these values. The
symbols of other letters than the two of words of trees are set to 0. 

### `lem_circuit_program`

 **Paper: proof of Lemma lem:circuit, the program.** "Lemma lem:lowdeg turns it into a program with v^O(a+1) constants
that takes v^(H−32)((a+1) lg v)^O(1) ≤ v^(H−16) steps, as n bounds the degree. All its runs halt, its names have
O((a+1) lg v) bits, and B = 1": for n = v^(H−32)+1, the degree bound n and a circuit over any commutative ring. 

### `lem_circuit_names`

 **Paper: proof of Lemma lem:circuit, the names.** "Its names have O((a+1) lg v) bits": less than the L² bits that
Definition def:acc allows. 

### `lem_circuit_bound`

 The arithmetic of the constants of Lemma lem:circuit. 

### `lem_circuit`

 **Paper: Lemma lem:circuit.** "There are constants B₀, C, v₀ such that for all integers a ≥ 0 and v ≥ v₀ with
(lg v)^(Ca) ≤ v: if PERM_m has a circuit with at most v^a gates over a field R that is an A-algebra in which 2 ≠ 0, for
some m ≥ v^B₀, then R has an accelerator of size v^(C(a+1)) at scale v." In this general form G is any family that is
complete for grid sums, as the permanent (2 ≠ 0) and the Hamiltonian cycle polynomial are; see lem_circuit_perm. 

### `lem_circuit_perm`

 **Paper: Lemma lem:circuit, as printed**, for the permanent. 
