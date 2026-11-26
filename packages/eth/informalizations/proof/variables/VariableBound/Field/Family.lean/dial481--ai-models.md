---
{
  "module": "proof/variables/VariableBound/Field/Family.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Family.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Family.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The list `famD m a` is the family of Lemma 13 (Family of checks)

The field is 𝔽 = `FW g`, the residues modulo X^s + g for the irreducible polynomial found by the
search; its elements are written as strings of s bits by `bitsW g`; ϑ_E is the residue that the word
of the number E stands for. `setD_gamW`: the list `gamW m a g u` lists the set Γ_u
(`AppVariables.Gam`) of the proof of Lemma 13. `stFamD`: from Lemma 13 over an arbitrary field with
2^s elements (`AppVariables.LemFamily`, a hypothesis
here, proved in proof/variables/VariableBound/Family) follows the statement `StFamD` on the list. 

 ### Two tests on words 

### `all_take_iff`

 The first k bits of a word w of n bits are 0, as a test on the list and as a statement on the
places i < n. 

### `sum_bitR_mul`

 The sum over the places of the products of the bits of two words of n bits is, modulo 2, the
number of places where both bits are set. 

### `ipW_iff`

 `ipW` is the inner product ⟨·,·⟩ modulo 2 of the proof of Lemma 13, for two words of n bits. 

 ### The field, ϑ, and the quadruples 

### `fintypeFW`

 The ring of residues is finite: its elements are written as strings of s bits. 

### `thetaW`

 ϑ_E: the residue that the word of the number E stands for; distinct for distinct E < m ≤ 2^s. 

### `decQ`

 The quadruple of residues that a quadruple of words stands for. 

### `decQ_inj`

 Distinct quadruples of words of s bits stand for distinct quadruples of residues. 

### `decQ_surj`

 Every quadruple of residues is written by a quadruple of words of s bits. 

 ### The listed sets are the sets Γ_u 

### `setD_gamW`

 Let X^s + g be irreducible, s ≥ 1 the length of g, and m ≤ 2^s. For a quadruple u of words of s
bits, the list `gamW m a g u` lists the set Γ_u of Lemma 13 (Family of checks), for v = 2^a. 

### `length_gamW`

 Let X^s + g be irreducible, s ≥ 1 the length of g, and m ≤ 2^s. For a quadruple u of words of s
bits, the list `gamW m a g u` has |Γ_u| members. 

 ### The statement 

### `fam_of`

 Lemma 13 (Family of checks) for the list made with any word g of s bits for which X^s + g is
irreducible: let 1 ≤ a, 2^a ≤ m and 16m ≤ 2^s < 32m, and let Lemma 13 hold over every field with 2^s
elements. Then the list is not empty, has fewer than (32m)⁴ members, every member is an increasing
list of numbers below m, and the members, indexed by their places, have (a), (b), (c) for v = 2^a. 

### `stFamD`

 Lemma 13 (Family of checks) for the listed family `famD m a`, from Lemma 13 over an arbitrary
field with 2^s elements. 
