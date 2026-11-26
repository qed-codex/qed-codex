---
{
  "module": "Statement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Statement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Superpolynomial lower bounds for the permanent and the Hamiltonian cycle polynomial

Definitions and statements, using Mathlib only. The proofs are in Solution.lean.


### `Computes`

 `f` has an arithmetic circuit with at most `s` gates: a list of `s` polynomials contains `f`, and each of
them is a variable, a constant, or the sum or product of two earlier ones (possibly the same one). Variables and
constants count as gates. 

### `perm`

 The permanent of the generic `m × m` matrix. 

### `hc`

 The Hamiltonian cycle polynomial: the sum over the permutations with a single cycle through all points. 

### `Beyond`

 More than `m ^ (c * (log₂ m) ^ (1/3))` gates. 

### `MainTheorem`

 **Main theorem.** There is an absolute constant `c > 0`, and for each characteristic `p` an `m₀`, such
that over every field of characteristic `p` and for every `m ≥ m₀` every circuit for `hc m`, and for
`perm m` if `p ≠ 2`, has more than `m ^ (c * (log₂ m) ^ (1/3))` gates. 

 ### Approximate circuits 

### `Approximates`

 `f` is approximated by a circuit with at most `s` gates: a circuit over the Laurent series in `ε`
computes some `q = f + ε * g`, where the coefficients of `g` are power series in `ε`. Here `a.coeff i` is
the coefficient of `ε ^ i` in the series `a`. 

### `MainTheoremApprox`

 **Main theorem, approximate form.** The same bound, for circuits that only approximate. 

 ### Valiant's classes 

### `Family`

 A family of polynomials, with finitely many variables for every `n`. 

### `Family.vars`

 the variables of the `n`-th polynomial 

### `Family.fin`

 finitely many 

### `Family.poly`

 the `n`-th polynomial 

### `VP`

 VP: the number of variables, the degree and the circuit size are polynomially bounded in `n`. 

### `VPBar`

 The closure of VP: the same with approximating circuits. 

### `VNP`

 VNP: the families `f n = ∑ g n (x, e)`, as polynomials, the sum over all vectors `e` of `r n` bits,
for some family `g` in VP. 

### `Separation`

 **VP ≠ VNP**: over every field VP is a proper subset of VNP. 

### `SeparationClosure`

 Over every field VNP is not contained in the closure of VP. 
