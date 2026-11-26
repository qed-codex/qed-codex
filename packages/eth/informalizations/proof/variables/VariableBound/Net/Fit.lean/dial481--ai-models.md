---
{
  "module": "proof/variables/VariableBound/Net/Fit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Fit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Fit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3: bounds that do not depend on the formula

The program of Step 4 hands the clique solver one bound for the total U, one for the size P and one
for the number B of bits of the values, for all networks of all lists of checks that are tried.
These bounds
(`UbD`, `PbD`, `BbD`) are the right side of the bound on U displayed in Step 3 of Appendix D, and P =
⌈2P₀⌉ and B = (k + 1)M + 1 of that Step, with the logarithms rounded up and with r̄ ≤ 10n, M ≤ 14n,
s̄ < 32Δ·log(2Δ) and t̄ ≤ log m + 33·log(2Δ) + 1 put in. Proved here:
`stTbMax` (the bound for t̄), `stFit` (a list with the three bounds displayed at the end of Step 2,
on r, on |Λ_j| and on load(E), is fit for an evaluation), `stNPrMax` (the number of profiles),
`stBounds` (the bounds in closed form) and `stSize` (every network of an
admissible profile is within the bounds, the case m ≤ n̄ included). Arithmetic and gluing only: the
bound on U as printed (`StUPrinted`), «The parameters» (`StSized`), the case m ≤ n̄ (`StSmall`), the
bound on gP displayed in «The parameters» (`StP`),
the count of profiles (`StNPr`) and s̄ < 32Δ·log(2Δ) (`ParamIneq`) come in as hypotheses;
proof/variables/VariableBound/Net/Main.lean discharges them. 

 ### Logarithms 

### `two_mul_le`

 2Δ ≤ 2^⌈log(2Δ)⌉. 

### `two_le_LD`

 ⌈log(2Δ)⌉ ≥ 2 for Δ ≥ 2. 

### `lg_mono`

 log x ≤ log y for 0 < x ≤ y. 

### `lg_le_clog`

 log x ≤ ⌈log x⌉ for a natural number x. 

### `lg_two_mul_le`

 log(2Δ) ≤ ⌈log(2Δ)⌉. 

### `clog_le`

 ⌈log(96Δ·⌈log(2Δ)⌉)⌉ ≤ 2·⌈log(2Δ)⌉ + 5 for Δ ≥ 2. 

 ### The number n̄ 

### `nb_pos`

 n̄ ≥ 1. 

### `nb_le`

 n̄ ≤ n/log(2Δ) gives n̄ ≤ n, for Δ ≥ 1. 

### `n_lt`

 n/(2·log(2Δ)) < n̄ gives n < 2n̄·⌈log(2Δ)⌉. 

### `row_le`

 A check of at most s̄ = 16m/n̄ clauses, with m ≤ Δn and n̄ as in «Setting and parameters» of
Appendix D, has at most 32Δ·⌈log(2Δ)⌉ clauses. 

 ### The statements 

### `stTbMax`

 «Setting and parameters»: t̄ ≤ log m + 33·log(2Δ) + 1 gives t̄ ≤ ⌈log(Δn)⌉ + 33·⌈log(2Δ)⌉ + 1,
for 1 ≤ m ≤ Δn. 

### `stFit`

 For a formula ψ with clauses of 1 to k literals on variables below n, every variable in at most
Δ ≥ 2 clauses, m ≤ Δn, n̄ as in «Setting and parameters» of Appendix D and M ≤ 14n: if m > n̄, a
list with the three bounds displayed at the end of Step 2, for
r̄ ≤ 10n, r̄ ≤ M, 1 ≤ M and t̄ ≤ `tbMax` is fit for an evaluation; if m ≤ n̄, the empty list is. 

### `Fit.row_le`

 Every check of a list that is fit for an evaluation has at most 32Δ·⌈log(2Δ)⌉ clauses. 

### `stNPrMax`

 Step 3, «Profiles»: for a list that is fit for an evaluation, the number of numbers that are
tried as profiles is at most `nPrMax`, which does not depend on the formula. Uses I ≤ r·s (`StNPr`). 

### `stBounds`

 The bounds in closed form, for n ≥ 1 and Δ ≥ 2: the bounds on U and gP displayed in Step 3 of
Appendix D with the logarithms rounded up, U ≤ 140kn·⌈log(2Δ)⌉ + 2g² and gP ≤ 2(n + g)(1 + Δ(t̄ + 3)) +
2(10n + g)·s̄ + g, on g = 3K⁸ nodes, with the
bounds `tbMax` and `sbMax` for t̄ and s̄. Uses the displayed bound on gP (`StP`). 

### `sized_mono`

 A network of size P with values of at most B bits is one of every larger size, with values of
any larger number of bits. 

### `ub_real`

 The right side of the bound on U displayed in Step 3 of Appendix D, on g = 3K⁸ nodes, is at most
`UbD`, for Δ ≥ 2. 

### `small_le_PbD`

 On g = 3K⁸ nodes, P = 2⌈n/g⌉(1 + Δ), the size for m ≤ n̄, is at most `PbD`. 

### `stSize`

 Step 3, «The total» and «The parameters», with bounds that do not depend on the formula: on g =
3K⁸ nodes, K > 0, for a list that is fit for an evaluation, the network of an admissible profile has
size `PbD`,
values of at most `BbD` bits and total at most `UbD`. For m > n̄ by the bound on U of Step 3 as
printed (`StUPrinted`), by «The parameters» (`StSized`) and by s̄ < 32Δ·log(2Δ) (`ParamIneq`); for m
≤ n̄ by the last sentence
of Step 3 (`StSmall`). 
