---
{
  "module": "Nc/Rate/Transfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Rate/Transfer.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Rate/Transfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Descent of circuits to an algebraically closed field of the same characteristic

A circuit over a field F for a polynomial with integer coefficients has finitely many constants. F and an algebraically
closed field KK of the same characteristic lie in a common ring T. The constants generate a finitely generated
KK-algebra in T, which has a homomorphism to KK by Hilbert's Nullstellensatz (Zariski's lemma). The image of the circuit
has the same number of gates and computes the same polynomial, now over KK. For approximate circuits the constants are
first cut off to Laurent polynomials (Nc/Rate/Truncate.lean) and the homomorphism is applied to their coefficients.


### `exists_common_ring.`

 Two fields of the same characteristic have homomorphisms to a common nonzero ring, namely their tensor product over
the prime field. 

### `exists_specialisation`

 Zariski's lemma, in the form of Hilbert's Nullstellensatz: finitely many elements of a nonzero ring T that contains
an image of the algebraically closed field KK lie in a subring of T that has a homomorphism to KK. 

### `mem_range_mapRingHom_subtype`

 A Laurent polynomial over T with all coefficients in the subring A comes from a Laurent polynomial over A. 
