---
{
  "module": "proof/statements/AppRunningTimeStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/AppRunningTimeStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/AppRunningTimeStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix A: pieces with parameters (ρ, c) (Definition 7), the grouping step and two size bounds of Lemma 8, Theorem A on the general recursion

Definitions and statements only, in the order of the appendix. Every `def … : Prop` or
`structure … : Prop` is a statement of the appendix; nothing is proved here.

**How «within T operations» is rendered.** The appendix counts operations of a random-access machine
and queries to tables. In this development an algorithm is a pure function of its input and of a
pad (a list of units, type `U`). It is polynomial-time in the length of input and pad on Mathlib's
multi-stack Turing machine (`PolyT`; `Unary` for a number written in unary); every
exponential loop is cut off by the pad; and it is right as soon as the pad has at least T units. So
«within T operations» becomes «`PolyT`, and right if the pad has T units». Factors that
the appendix multiplies become separate lower bounds on the pad. Tables of cliques are written out
(`PInst`), not queried. The end statements (parts (c) and (d) of the theorem) are about
steps of a Turing machine and have no pad. 

 ## Pieces with parameters (ρ, c) (Definition 7) 

### `ValQ`

 The argument of the program for the value of a piece: (pad, (λ in unary, number i of the piece),
(x, y, u, v)). 

### `IsPieces`

 The definition of pieces with parameters (ρ, c). The programs are the fields of `P`
(`ClauseBound.Alg.PiecesF`), read at its parameter h = 0, which the appendix does not have; the
index set 𝓘 is
{0, …, cnt − 1}; `A lam i` is the function A_i for strings of λ = lam bits; c^row_i =
`P.cap false 0 lam i`, c^col_i = `P.cap true 0 lam i`; `P.top`, `P.bot` are the two functions of a
factorization and `val` computes A_i. 

### `IsPieces.rho_ge`

 ½ ≤ ρ < 1 real, c ≥ 1 an integer, d ≥ 1 

### `IsPieces.sum`

 (a) Σ_{i ∈ 𝓘} A_i = d·[x = v][y = u] 

### `IsPieces.row`

 (b) A_i factors through c^row_i bits as a function of (x,y) and (u,v) 

### `IsPieces.col`

 (b) and through c^col_i bits as a function of (x,u) and (y,v) 

### `IsPieces.caps`

 (b) where c^row_i + c^col_i ≤ 4ρλ + c·log(2λ) 

### `IsPieces.card`

 (c) |𝓘| ≤ (2λ)^c (so the elements of 𝓘 are below 2^{(2λ)^c} as well) 

### `IsPieces.size_d`

 (c) d and all values of the A_i and of the functions of these factorizations are below
      2^{(2λ)^c} in absolute value 

### `IsPieces.time_cnt`

 (c) one algorithm computes each of them, and 𝓘, c^row_i, c^col_i, from λ, i and the arguments
      within 2^{cλ} operations. Here: |𝓘|, d, c^row_i, c^col_i are computed in time polynomial in λ;
      the two functions of a factorization and the value of A_i are polynomial-time in the length of
      pad and arguments, and right once the pad has 2^{cλ} units. 

### `Exist`

 «There are pieces with parameters (ρ, c).» 

### `MayAssume`

 «We may and do assume c^row_i, c^col_i ≤ 2λ»: pieces with parameters (ρ, c) give pieces with the
same d, 𝓘 and A_i and with all numbers of bits at most 2λ: a longer factorization is replaced
by F(z,z') = Σ_θ [z = θ]·F(θ,z'). The appendix replaces c by c + 2, which pays for computing c^row_i
or c^col_i first; here c stays, because the new functions tell from the length of θ which
factorization is meant. 

 ## Lemma 8: the grouping and the sizes 

### `Cases`

 The two cases of the lemma, for the numbers c_{a,b} of shared bits of a network on [g] with
parameter P: (i) g = 3K⁸ and ζ = 1/(2K), or (ii) K divides g, c_{a,b} ≤ P/g for all a ≠ b, and
2ζ²g ≥ K·ln(2gK). 

### `Lof`

 L = ⌈(U + 2ζgP)/K²⌉. 

### `B'of`

 B' = ⌈2gP/K⌉ + g²B. 

### `SomeGrouping`

 The first step of the proof: «Some grouping has at most 2g/K nodes in every group and Y_{γ,γ'} ≤
L for all γ ≠ γ'.» (P ≥ 1 as in the definition of a network, here and below.) 

### `GroupingSizes`

 Two facts from the end of the proof: «K ≤ g in both cases and L ≤ gP + 1». 

 ## Theorem A: the general recursion 

### `alpha'`

 α' = log(1/ρ). 

### `PartA`

 Part (a), for the numbers K_ℓ, g_ℓ, ζ_ℓ, e_ℓ of display (40) (`Levels.Gen` in
`LevelsStatement.lean`). 

### `PartA.logK`

 log K_ℓ = (3x₀+6)·2^ℓ − 6ℓ − 2x₀ − 6 

### `PartA.K_lt_le`

 so K_ℓ < K_{ℓ+1} ≤ K_ℓ^10 

### `PartA.e_bounds`

 ½ρ^ℓ ≤ e_ℓ ≤ 0.85·ρ^ℓ 

### `PartA.rho_pow`

 where ρ^ℓ ≤ ((3x₀+6)/log K_ℓ)^{α'} 

### `PartB`

 Part (b): one deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and the tables, outputs the value
of the (K_ℓ, λ)-clique within 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²} operations. The algorithm is `run`, a
function of
(pad, ℓ in unary, instance), with the tables written out in the instance; `need ℓ λ B` is the
logarithm of the number of units that the pad must have. The bound of the appendix is a bound for
the length of
the pad; the number of steps of a Turing machine is polynomial in that length and in the length of
the input, so in steps the exponent e_ℓK_ℓ²λ holds up to a constant factor only.
This says that SOME function `run` exists; it does not name the recursion. The forms that name it,
the recursion `ClauseBound.Alg.solveG` on the schedule of display (40), are
`GeneralPieces.StSolveG2`, `StChain2` and `StRate2` in
`proof/rates/GeneralPieces/Defs.lean` and `GeneralPieces.Tied.PartB` in
`proof/rates/GeneralPieces/Tied/Defs.lean`. 

### `ThmRunningTime`

 The theorem on the general recursion: suppose that there are pieces with parameters (ρ, c), and
let x₀ ≥ 18 be an integer with 2^x₀ ≥ c + 5. (The pieces need not have c^row_i, c^col_i ≤ 2λ:
`MayAssume`
gets there and keeps c.) 

### `ThmRunningTime.a`

 (a) needs neither pieces nor 2^x₀ ≥ c + 5. 

### `ThmRunningTime.b`

 (b); C₀ depends only on c. 

### `ThmRunningTime.c_m`

 (c), first sentence: one machine counts the satisfying assignments of a k-CNF with m ≥ 1
  clauses in which every variable occurs within C·2^{C·km/(log₂(m+2))^{α'}} steps; machine and C do
  not depend on
  k, which is part of the input. The appendix takes any formula, numbers the variables that occur in
  a preparation and counts their assignments; here the input is promised to contain every one of its
  n
  variables, so there is no preparation. All steps are counted, so the polynomial in the length of
  the formula is absorbed. As a statement this only says that some machine exists: it does not name
  the algorithm. 

### `ThmRunningTime.c_n`

 (c), second sentence: for every fixed k and n variables, 2^{O(n·log log n/(log n)^{α'})}
  steps. The appendix asks in addition that a number between 0.85ρ^ℓ and ρ^ℓ can be computed from ℓ
  in time polynomial
  in K_ℓ; the proof in this development does not need that. Likewise: some machine exists; the
  statement does not name the algorithm. 

### `ThmRunningTime.d`

 (d): one machine decides 3-SAT on n variables within 2^{O(n/(log n)^{α'/10})} steps. Here this
  follows from the bound with the exponent 3/19 (`Sat3.inRateTM`), because α'/10 ≤ 1/10 < 3/19; the
  appendix's proof of (d), through the sparsification lemma with ε = (log n)^{−α'/10}, is not
  formalized. 

### `ThmHalfPieces`

 The theorem on pieces with ρ = 1/√2 (Appendix B), with the running time, for the functions of
its proof: there are pieces with parameters (1/√2, c), for an absolute constant c, namely, with h =
`AppHalfPieces.hOf λ`
and μ(x) the partition of h with number x in the lexicographic list: 𝓘 = {−2h, …, 2h}, numbered here
from 0 to 4h, d = h!, A_s = `AppHalfPieces.piece`, c^row_s = ⌈log R^row_s⌉ and c^col_s = ⌈log
R^col_s⌉. 

### `BoundInM`

 The bound in m of the paper's Theorem 1 (the Main Theorem), from the two theorems: #k-SAT with m
clauses within 2^{O(km/√(log m))} steps, one machine for all k.
It names none of the objects of the two appendices, so by itself it says nothing about the route of
a proof. The proof in this folder takes the theorem on pieces with ρ = 1/√2 and the first sentence
of part (c) of the
theorem on the general recursion; the statements that name these objects (`GeneralPieces.StSolveG2`,
`StChain2`, `StRate2` in proof/rates/GeneralPieces/Defs.lean and `GeneralPieces.Tied.PartB` in
proof/rates/GeneralPieces/Tied/Defs.lean) are the forms in which those two theorems are proved. 
