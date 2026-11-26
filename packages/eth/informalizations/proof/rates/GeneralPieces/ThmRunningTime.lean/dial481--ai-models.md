---
{
  "module": "proof/rates/GeneralPieces/ThmRunningTime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/ThmRunningTime.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/ThmRunningTime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (the running time as a function of m and n), assembled

Parts (a) to (d) as stated in `AppRunningTimeStatement.lean`. "Suppose that there are pieces with
parameters (ρ, c)": by "we may and do assume", the recursion has programs whose numbers of bits are
at most 2λ, with the
same c. Parts (b) and (c) run the recursion through case (ii) of Lemma 8 at every level, with an x₀
of the theorem; for part (c) it is the least one,
x₀ = max(18, ⌈log(c + 5)⌉). The top levels of part (c), which turn a k-CNF into networks on 3K⁸
nodes and rebalance each once, call case (i) of Lemma 8 (`GeneralPieces.Top`); the remaining
arguments,
for the bound in m and the bound in n, take as given the display in the paper's proof of part (c)
(`Num/TopDisplay.lean`) and part (a) (`Num/PartAUse.lean`). Part (d) follows from a stronger bound
on 3-SAT (`PartD.thmRunningTime_d`), which does not go through parts (a) to (c). 

### `x₀Of_ge`

 x₀Of c ≥ 18. 

### `x₀Of_pow`

 2^{x₀Of c} ≥ c + 5. 

### `seq2`

 Parts (a) and (b) in the form that the top levels use, with every interface statement proved. 

### `solver_poly`

 The solver that a family of pieces gives is polynomial-time, if the programs of the pieces are. 

### `K_idx`

 The solver has K_ℓ nodes at the index of level ℓ. 

### `partC_m_tied`

 Part (c), first sentence, for the named programs: pieces whose numbers of bits are at most 2λ
and any x₀ of the theorem. The network of the formula is rebalanced by case (i) of Lemma 8
(`Top.stCountG2`); the exponent is bounded through the display in the paper's proof of part (c) and
"every term after 2ekm is O(k·m^{1−1/90})" (`TopDisplay.top_level`, `top_arith`); the level is "the
largest ℓ with K_ℓ ≤ m^{1/9}", and e_ℓ = O((log m)^{−α'}) there by
part (a) (`PartAUse.e_le_rPow`). 

### `endO2`

 The top level in n, for a solver with a sequence of levels; every network of marks is rebalanced
by case (i) of Lemma 8. 

### `partC_n`

 Part (c), second sentence, for programs whose numbers of bits are at most 2λ and any x₀ of the
theorem; what the choice of the level needs of K_ℓ and e_ℓ comes from part (a)
(`PartAUse.inv_two_pow_le_e`, `two_pow_le_div`, `e_mul_le`). 

### `rho_of_exist`

 ½ ≤ ρ < 1 is part of the definition of pieces. 

### `par_of_isPieces`

 The programs that the recursion runs on, for pieces (P, val) with parameters (ρ, c): "we may and
do assume" (`trimV`), read in the form of the recursion (`atZero`); they have m = 1 and the same c. 

### `thmRunningTime_b_tied`

 Part (b) for the named program, from pieces as in the definition of the appendix; C₀ depends
only on c. 

### `thmRunningTime_c_m_tied_at`

 Part (c), first sentence, for the named programs, from pieces as in the definition of the
appendix, with any x₀ of the theorem. 

### `thmRunningTime_c_m_tied`

 The same with the least x₀ of the theorem. 

### `thmRunningTime_a`

 Part (a). 

### `thmRunningTime_b`

 Part (b); C₀ depends only on c. This form says "there is a program" and does not name the
recursion; `thmRunningTime_b_tied` does. The pieces are first brought to numbers of bits at most 2λ
by "we may and do assume" as printed (`exist_par_one`). 

### `thmRunningTime_c_m`

 Part (c), first sentence. This form says "there is a machine" and does not name the programs;
`thmRunningTime_c_m_tied` does (the proof below does not use it). The proof goes as the appendix
does: take pieces, "we may and do assume" that their numbers of bits are at most 2λ


### `thmRunningTime_c_n`

 Part (c), second sentence. Only this form, which says "there is a machine", is stated; no form
names the programs. The appendix's proviso (a number between 0.85ρ^ℓ and ρ^ℓ computable from ℓ in
time polynomial in
K_ℓ) is not needed. 

### `thmRunningTime_d`

 Part (d). It is derived in `PartD.thmRunningTime_d` from a bound on 3-SAT with the exponent
3/19, which the paper does not state and which is proved with a lemma on groupings other than Lemma
8; parts (a) to (c) do not use that bound. 

### `thmRunningTime`

 Theorem A, all four parts. 
