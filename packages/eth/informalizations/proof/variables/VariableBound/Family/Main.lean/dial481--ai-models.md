---
{
  "module": "proof/variables/VariableBound/Family/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Family/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Family/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 13 (Family of checks)

The end of the printed proof, one theorem for each of its steps, with fractions cleared: a
probability is a number of quadruples u = (u₁, u₂, u₃, u₄) ∈ 𝔽⁴, out of |𝔽|⁴.
Throughout, 𝔽 is a finite field, `bits` writes its elements as strings of s bits (linearly over the
field with two elements), ϑ gives the m clauses distinct elements of 𝔽, and v = 2^a.

* `card_odd`: as (u₃, u₄) is independent of (u₁, u₂), |Γ_u ∩ V| is odd with probability at least 2/3
  · 15/32 = 5/16.
* `card_mem`: a clause lies in Γ_u with probability at most 1/v.
* `markov`: |Γ_u| > 16m/v with probability at most 1/16.
* `card_Om`: |Ω| ≥ (15/16)·|𝔽|⁴.
* `card_Om_lt`, `part_a`, `part_b`, `part_c`: |Ω| < (32m)⁴ and the parts (a), (b), (c) of the lemma.
* `lemFamily`: Lemma 13 without its claim that the sets can be listed in time polynomial in m (that
  claim is `VariableBound.Fld.StCertFamD`, proof/variables/VariableBound/Field/Defs.lean), with 0 < |Ω|
  added. 

### `card_quad`

 Proof of Lemma 13 (Family of checks): (u₃, u₄) is independent of (u₁, u₂). The quadruples u with
a property of the two pairs are counted pair by pair. 

### `card_univ_quad`

 𝔽⁴ has |𝔽|⁴ elements. 

### `mem_Gam`

 A clause E lies in Γ_u if and only if H_E holds for the pair (u₁, u₂) and ⟨u₃^E, u₄⟩ = 1 for the
pair (u₃, u₄). This is the definition of Γ_u, written with the two pairs. 

### `card_odd`

 Proof of Lemma 13 (Family of checks): |Γ_u ∩ V| is odd with probability at least 2/3 · 15/32 =
5/16, for a set V of more than v = 2^a clauses, if 1 ≤ a, a − 1 ≤ s and 16m ≤ 2^s:
16 times the number of these u is at least 5·|𝔽|⁴. 

### `card_mem`

 Proof of Lemma 13 (Family of checks): a clause lies in Γ_u with probability at most 1/v, v =
2^a, if 1 ≤ a and a − 1 ≤ s: v times the number of these u is at most |𝔽|⁴. 

### `markov`

 Proof of Lemma 13 (Family of checks): |Γ_u| > 16m/v with probability at most 1/16, v = 2^a, if 1
≤ a, a − 1 ≤ s and 1 ≤ m: 16 times the number of these u is at most |𝔽|⁴. 

### `card_Om_add`

 Ω and the set of the u with |Γ_u| > 16m/v together are 𝔽⁴. 

### `card_Om`

 Proof of Lemma 13 (Family of checks): |Ω| ≥ (15/16)·|𝔽|⁴, if 1 ≤ a, a − 1 ≤ s and 1 ≤ m. 

### `card_Om_lt`

 Lemma 13 (Family of checks): |Ω| < (32m)⁴, if 2^s < 32m, because |Ω| ≤ |𝔽|⁴ = 2^(4s). 

### `part_a`

 Lemma 13 (Family of checks), part (a): |Γ_u| ≤ 16m/v for all u ∈ Ω, v = 2^a. This is the
definition of Ω. 

### `part_b`

 Lemma 13 (Family of checks), part (b): every clause lies in Γ_u for at most (16/(15v))·|Ω|
indices u ∈ Ω, v = 2^a, if 1 ≤ a, a − 1 ≤ s and 1 ≤ m. 

### `part_c`

 Lemma 13 (Family of checks), part (c): for every set V of more than v = 2^a clauses, |Γ_u ∩ V|
is odd for at least |Ω|/4 indices u ∈ Ω, if 1 ≤ a, a − 1 ≤ s, 1 ≤ m and 16m ≤ 2^s;
because 5/16 − 1/16 = 1/4. 

### `lemFamily`

 Lemma 13 (Family of checks), without its claim that the sets can be listed in time polynomial in
m: for v = 2^a with 2 ≤ v ≤ m and a field 𝔽 with 2^s elements, 16m ≤ 2^s < 32m, the sets Γ_u, u ∈ Ω,
have 0 < |Ω| < (32m)⁴ and (a), (b), (c). 
