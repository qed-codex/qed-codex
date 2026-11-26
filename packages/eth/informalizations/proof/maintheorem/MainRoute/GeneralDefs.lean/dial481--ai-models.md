---
{
  "module": "proof/maintheorem/MainRoute/GeneralDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/GeneralDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/GeneralDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The chain for every solver: definitions and statements

**Why.** proof/maintheorem/MainRoute/Defs.lean states the seven items of the route for ONE algorithm
for cliques, the recursion of Appendix A on the pieces of Appendix B
(`RecursionWithPieces.solverAB P₀ val c`), and for ONE function for the bound in m
(`ClauseBound.Alg.AM` on it). The proof uses little of the two. Of the algorithm for cliques: that
it is polynomial-time, has a sequence of levels, that a
number in [e_ℓ, 2e_ℓ] is computed, and that e_ℓ = O((log K_ℓ)^(−1/2)). Of the function for the bound
in m: that some machine computes it, and that every machine that computes it meets the bound in m.
Here items (3), (4), (6) and (7) are stated for every solver and every function with these
properties. So the Main Theorem's bound follows from ANY algorithm for cliques as in the hypothesis
of Theorem D (a) with
e_ℓ = O((log K_ℓ)^(−1/2)) and ANY function with the bound in m; the chain on the recursion of
Appendix A is an instance, and so is a chain on any other form of Theorem A (b) that gives such a
solver.

**What is stated here.**
* `RouteOn S Q num fm em n₁`: items (3), (4), (6) and (7) of the route of
  proof/maintheorem/MainRoute/Defs.lean, with `RecursionToBound.count S n₁ Q.pick num` and
  `RecursionToBound.expo S n₁ Q.pick num` as the function of Steps 1 to 5 and its exponent, fm and
  em for the bound in m, and K₀ = `S.K (Q.idx 0)`. Each bound is stated for EVERY machine that is
  made in the printed way, and existence is stated apart.
* `RouteOnEverySolver`: `RouteOn` holds, for all n₁ ≥ n₀, where n₀ depends only on S, Q and `num`,
  for every polynomial-time solver S with a sequence Q of levels, every `num` that computes a number
  in [e_ℓ, 2e_ℓ], if e_ℓ ≤ a/√(log K_ℓ) for all ℓ, and for all fm and em such that some machine with
  finite alphabets computes fm with the exponent em and every machine that does meets the bound in
  m.
* `BoundInMOnEverySolver`: item (5) for every such solver: some machine computes the function for
  the bound in m (`ClauseBound.Alg.AM`) on S, and every machine that does meets the bound in m.
* `BothBoundsOnEverySolver`: the chain with this function in the place of fm: both bounds from ONE
  algorithm for cliques, as in the paper, with nothing assumed of a function for the bound in m.

**What is not here.** Items (1) and (2), which are about the pieces and the recursion: they are the
hypotheses on S and Q. What differs from the text is what proof/maintheorem/MainRoute/Defs.lean
lists. The items (1) to (7) of the route are numbered as in that file; all numbers of theorems,
corollaries, appendices and of the Steps of Appendix D are those of the paper. 

### `RouteOn`

 Items (3), (4), (6) and (7) of the route for the solver S with the sequence Q of levels, the
function `num` for the number in [e_ℓ, 2e_ℓ], the function fm with the exponent em for the bound in
m, and the bound n₁ below which the function of Steps 1 to 5 tries all assignments. K₀ is K at the
level 0. 

### `RouteOn.da`

 (3) Theorem D (a): EVERY machine that computes the function of Steps 1 to 5 on S has the
      conclusion of Theorem D (a) for this sequence 

### `RouteOn.variablesBFromTheBody`

 (4) Step 6, from the BODY of Theorem D (a): for EVERY machine Ma with the conclusion of
      Theorem D (a) for this sequence and EVERY machine Mb that tries all assignments, EVERY machine
      that chooses between them as Step 6 says meets the bound of Theorem D (b) 

### `RouteOn.tries`

 EVERY machine that computes exhaustive counting tries all assignments within 2^{cb·n}·n^{cb·k}
  steps, for some cb that depends on the machine 

### `RouteOn.db`

 (4) Step 6, for the named function: EVERY machine made as Step 6 says meets the bound of
      Theorem D (b) 

### `RouteOn.cor`

 (6) Corollary 11, from the BODIES of Theorem A (c) and Theorem D (b): for EVERY machine M₁
      that meets the bound in m and EVERY machine M₂ that meets the bound of Theorem D (b), EVERY
      machine that runs them in alternation behind a renaming meets the bound of Corollary 11 

### `RouteOn.main`

 (6), (7) Corollary 11, which is the Main Theorem, for the named function and fm: EVERY machine
  assembled as printed meets the bound of Corollary 11 and that of Theorem 1 on the compact code 

### `RouteOn.decides`

 the same for deciding, with `someBit` (“some bit is 1”) after either machine 

### `RouteOn.exist`

 there IS a machine built as printed, for counting and for deciding: finite alphabets,
  polynomial-time front ends and test, and the named computations `choose` and `alt` carried out 

### `RouteOnEverySolver`

 **The chain for every solver.** Let S be a polynomial-time solver for cliques with a sequence Q
of levels, let `num` compute a number in [e_ℓ, 2e_ℓ] (the hypothesis of Theorem D (a)), and let e_ℓ
≤ a/√(log K_ℓ) for all ℓ, for a natural number a. Let fm, with the exponent em, be a function of
(input, padding string) such that some machine with finite alphabets computes it and EVERY machine
that computes it meets the bound in m (`MinOfBounds.MeetsBoundInM`). All of these are arbitrary.
Then `RouteOn S Q num fm em n₁` holds for every n₁ ≥ n₀, where n₀ is chosen after S, Q and `num` and
before a, fm and em: every machine assembled in the printed way from machines that compute the
function of Steps 1 to 5 on S, exhaustive counting and fm has the bound of the Main Theorem, and
such a machine exists. 

 ### Item (5) on every solver, and both bounds from one algorithm 

### `BoundInMOnEverySolver`

 Item (5) of the route for EVERY solver. The paper has the first sentence of Theorem A (c) for
the recursion of Theorem A only; this is its printed proof, at α′ = 1/2 and for formulas in which
every variable occurs, carried out for any solver with levels: K_ℓ > m^(1/(9C₀)) stands for the
printed K ≥ m^(1/90). Let S be a polynomial-time solver for cliques with a sequence Q of levels and
e_ℓ ≤ a/√(log K_ℓ) for all ℓ, for a natural number a. Then (i) some machine with finite alphabets
computes `ClauseBound.Alg.AM` (the network of the formula, rebalanced and handed to the solver) on S
with the exponent
`ClauseBound.Alg.eM`, the level picked by `Q.pick` for ⌊m^(1/9)⌋; (ii) EVERY machine that computes
this function with this exponent meets the bound in m (`MinOfBounds.MeetsBoundInM`) with some
constant. 

### `BothBoundsOnEverySolver`

 **Both bounds from ONE algorithm for cliques.** Let S be a polynomial-time solver for cliques
with a sequence Q of levels, let `num` compute a number in [e_ℓ, 2e_ℓ], and let e_ℓ ≤ a/√(log K_ℓ)
for all ℓ. Then (5) EVERY machine that computes the function for the bound in m on S meets the bound
in m; and for every n₁ ≥ n₀, where n₀ is chosen after S, Q and `num` and before a, the chain
`RouteOn` holds with this function: every machine
assembled in the printed way from machines that compute the function of Steps 1 to 5 and the
function for the bound in m, both on S, and exhaustive counting has the bound of the Main Theorem,
and such a machine exists. Nothing is assumed of a function for the bound in m. 
