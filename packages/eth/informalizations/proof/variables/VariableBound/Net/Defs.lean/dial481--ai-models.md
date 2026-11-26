---
{
  "module": "proof/variables/VariableBound/Net/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix D, Step 3: a network with two kinds of marks. Definitions and interface statements

## How to read it

* D = (ψ, 𝓛) is the data of a network: the formula ψ (a list of m clauses) and the list 𝓛 of checks,
  each check a list of numbers of clauses. The text numbers checks 1, …, r and nodes 1, …, g; Lean
  0, …, r − 1 and 0, …, g − 1.
* An object is a triple (κ, e, j): (0, e, 0) is the clause number e, (1, e, j) is the incidence (E,
  j) of the clause number e and the check number j. Objects are named by their position o in the
  list `objs D`.
* The variable v is held by the node v / ⌈n/g⌉ (`qv g n` = ⌈n/g⌉), the home of check j is j % g (in
  Lean's numbering from 0, which shifts the text's homes by one; nothing depends on which home a
  check has).
* A setting z_a is a word: ⌈n/g⌉ value bits, then one mark bit for each object that touches a, in
  the order of `tch`.
* A profile is a number y; its digits in base I + m + 1 are the numbers μ: `mu g D y a a κ` is
  μ_(a,κ), and `mu g D y a b κ` is μ_(a,b,κ) for a ≠ b.
* The set S_a of a network in Lean is always the set of all words of one length (`PNet.Presents`).
  «S_a restricted to the settings in which exactly …» is therefore written into W_a: W_a is 0 at the
  other settings. The same holds for
  value bits of variables with numbers ≥ n at the last nodes: they must be 0.
* The flag fl says which sum: false for X (|Π₀| = n̄ + 1, no sign), true for F (|Π₀| ≤ n̄, sign
  (−1)^|Π₀|).
* A set P of (positions of) objects stands for a tuple (Π₀, …, Π_r). 

 ### Objects, homes, touches, owners, tests, settings 

### `Dat`

 The formula and the list of checks. 

### `objs`

 The objects: the clauses (kind 0), then the incidences (E, j) with E ∈ Λ_j (kind 1). 

### `obAt`

 The object at the place o; for o beyond the list, the triple (0, m, 0), which is no object. 

### `clOf`

 The clause of the object o. 

### `home`

 The home h(j) ≡ j (mod g) of check j. 

### `tchB`

 The object o touches the node a: a holds a variable of its clause, or o is an incidence (E, j)
and a = h(j). 

### `tch`

 The objects that touch a, in order. 

### `linkB`

 {a, b} with a < b is a test of o: a and b are neighbours in the chain a₁ < … < a_t of the nodes
that o touches. 

### `ownB`

 a is the owner of o: the least node that o touches. 

### `tst`

 The objects of kind κ with the test {a, b}, in order; their number is t_(a,b,κ). 

### `mark`

 The mark that the setting z of node a gives to the object o. 

### `str`

 The string of the marks of the t_(a,b,κ) objects, in a fixed order. 

 ### «The total»: ranks of subsets 

### `rank`

 The position of a string in the list, in lexicographic order with 0 before 1, of all strings of
its length with as many ones. 

### `cw`

 ⌈log C(t, μ)⌉. 

 ### Profiles and the network of one profile 

### `mu`

 The number that the profile y prescribes: μ_(a,κ) for b = a, μ_(a,b,κ) = μ_(b,a,κ) for b ≠ a. 

### `capD`

 c_(a,b) = Σ_κ ⌈log C(t_(a,b,κ), μ_(a,b,κ))⌉. 

### `labD`

 The label that a shows to b: for each kind the position of the string of marks, in ⌈log C(t, μ)⌉
bits. 

### `qj`

 q_j at the node a: the number of marked incidences of check j. 

### `okD`

 The setting z of the node a belongs to the network of the profile y and no marked object has a
true literal at a. 

### `WD`

 W_a(z_a): 0 if a marked object has a true literal at a (or z_a is not a setting of the profile);
otherwise ∏_(j : h(j) = a) σ_(q_j), times, for F only, (−1)^q, where q is the number of marked
clauses owned by a. 

### `DCtx`

 ((g, n in unary), ((ψ, 𝓛), (profile, flag))). 

### `netD`

 The network of one profile, as functions. 

### `netDN`

 The network that netD presents. Ψ_(a,b) factors through c_(a,b) bits: f_(a,b)(z, θ) = [the label
of z is θ]. 

### `rep`

 n in unary. 

### `ctx`

 The context of the network of the profile y. 

### `tot`

 Σ_a μ_(a,κ). 

### `totP`

 μ_κ = Σ_({a,b}) μ_(a,b,κ). 

### `admD`

 The profile y is admissible: μ_(a,b,κ) ≤ t_(a,b,κ), Σ_({a,b}) μ_(a,b,κ) ≤ (k − 1 + κ)·Σ_a
μ_(a,κ), Σ_a μ_(a,0) = n̄ + 1 (for F: ≤ n̄) and Σ_a μ_(a,1) ≤ M. The digits of y at the places that
no μ reads, below 2g², are 0
(the sums run over y < `nPr`, so no higher digit occurs), so that every profile is one number. 

### `nPr`

 The number of numbers y that are tried as profiles: (I + m + 1)^(2g²). 

 ### Sets of marked objects 

### `WfD`

 ψ has clauses of 1 to k literals on variables below n; the checks are lists without repetition
of numbers of clauses. 

### `vset`

 The objects whose clause σ violates. 

### `kP`

 The members of P of kind κ. 

### `chP`

 The members of P that are incidences of check j. 

### `oc`

 The number of members of P of kind κ that the node a owns. 

### `pw`

 The number of members of P among the objects of kind κ with the test {a, b}. 

### `wt`

 The value of the term of P in display (65): ∏_j σ_(|Π_j|), for F times (−1)^|Π₀|. 

### `Match`

 P belongs to the profile y. 

### `Lim`

 |Π₀| = n̄ + 1 (for F: ≤ n̄) and |Π₁| + … + |Π_r| ≤ M. 

 ### The right sides of display (65) 

### `chks`

 The list 𝓛 of checks as sets of clauses of ψ. 

### `rhsXF`

 The right side of display (65): of its first line for fl = false, of its second line for fl =
true. 

### `rhsD`

 The right side of display (65) for the formula ψ on n variables and the list 𝓛. 

### `colD`

 load(E) for the clause number e: the number of checks of the list that contain e. 

### `StChks`

 For well-formed data (WfD), the list of sets has the numbers of the list of lists: r, |Λ_j| and
load(E). 

 ### Rank.lean: the labels 

### `StLab`

 The labels have c_(a,b) bits; two settings of the profile (the strings have μ ones) have the
same label iff they give the same marks to every object with the test {a, b}. 

 ### Val.lean: the network of one profile 

### `StPresents`

 The plain functions `netD` present the network `netDN`, in every context. 

### `StVal`

 Step 3: «the nonzero terms are the tuples (ξ, Π₀, …, Π_r), each once, with the values in (65)»,
for the network of one profile y, admissible or not: for g > 0 and well-formed data (WfD), its value
is the sum over ξ and the
sets P of objects with violated clauses that belong to the profile. 

 ### Prof.lean: profiles 

### `StProf`

 Step 3, «Profiles»: «every nonzero term belongs to exactly one profile», and that profile is
admissible iff |Π₀| = n̄ + 1 (for F: ≤ n̄) and Σ_j |Π_j| ≤ M. In Lean: for g > 0, well-formed data
(WfD) and a set P of places of
objects, the number of admissible profiles y < `nPr` to which P belongs is 1 if P is within these
limits, and 0 otherwise. 

### `StNPr`

 Step 3, «Profiles»: the numbers tried as profiles (`nPr`), and so the admissible profiles, are
at most (I + m + 1)^(2(g² + g)), with I ≤ r·s incidences if every check has at most s clauses. 

 ### Tuples.lean, Total.lean: sets of objects and tuples (Π₀, …, Π_r) 

### `StTuples`

 For well-formed data (WfD): the sum over ξ and the sets P of objects with violated clauses,
within the limits, is the right side of display (65). 

### `StTotal`

 Step 3, «Profiles»: «each right side of (65) is the sum of the values of the networks of the
admissible profiles», for g > 0 and well-formed data (WfD). 

 ### SizeU.lean, SizeP.lean, SizeB.lean, SizeSmall.lean, Fit.lean: «The total» and «The parameters» 

### `Setting`

 The setting of Step 3 for m > n̄: the data are well formed (WfD), every variable occurs in at
most Δ ≥ 2 clauses, m ≤ Δn, n̄ is the number of the text, and the list has r ≤ M checks, M ≥ 1, with |Λ_j|
≤ s̄ = 16m/n̄. 

### `StU`

 Display (68), before display (61) is used: for g > 0, in the setting of Step 3 for m > n̄
(`Setting`), the network of an admissible profile has U ≤ 6(k−1)(n + log(2Δ)) + 2kM·log(96Δ·log(2Δ)) +
2g². 

### `StUPrinted`

 Display (68) as printed, with M ≤ 14n from display (61): for g > 0, in the setting of Step 3 for
m > n̄ (`Setting`), the network of an admissible profile has U ≤ 6k(n + log(2Δ)) +
28kn·log(96Δ·log(2Δ)) + 2g². 

### `UbD`

 Display (68) with the logarithms rounded up, on g = 3K⁸ nodes: a number that can be computed and
does not depend on the formula. 

### `P0`

 P₀ = ⌈n/g⌉(1 + Δ(t̄ + 3)) + ⌈r̄/g⌉·s̄. 

### `PD`

 P = ⌈2P₀⌉. 

### `BD`

 B = (k + 1)M + 1. 

### `StSized`

 Step 3, «The parameters»: for a list with display (67), the network of an admissible profile
satisfies conditions (i) and (ii) of the definition of a network with P = ⌈2P₀⌉ and B = (k + 1)M + 1.
Needs: g > 0, s̄ ≥ 0, well-formed data (WfD), every variable in at most Δ clauses, r ≤ r̄, |Λ_j| ≤
s̄, load(E) ≤ t̄ + 2. 

### `StP`

 Display (69): gP ≤ 2(n + g)(1 + Δ(t̄ + 3)) + 2(10n + g)·s̄ + g, for g > 0, s̄ ≥ 0 and r̄ ≤ 10n,
with P = ⌈2P₀⌉. 

### `tbMax`

 Bounds for t̄ and s̄ that do not depend on the formula: t̄ ≤ log m + 33·log(2Δ) + 1 with m ≤ Δn,
and s̄ < 32Δ·log(2Δ). 

### `sbMax`

 The bound for s̄: 32Δ·⌈log(2Δ)⌉. 

### `PbD`

 P = ⌈2P₀⌉ on g = 3K⁸ nodes with r̄ = 10n, t̄ = `tbMax` and s̄ = `sbMax`: it does not depend on
the formula. 

### `BbD`

 B = (k + 1)M + 1 with M = 14n. 

### `Fit`

 What one evaluation asks: ψ and the checks are well formed (WfD), every variable lies in at most
Δ ≥ 2 clauses, m ≤ Δn, n̄ is the number of the text (AppVariables.IsNb), M ≤ 14n, the list has r ≤
10n checks, and load(E) ≤ `tbMax` + 2 for
every clause. Further, either m > n̄, and then r ≤ M, M ≥ 1 and |Λ_j| ≤ 16m/n̄ for every j (display (67)
with the bounds of display (61)), or m ≤ n̄ and the list is empty. 

### `StTbMax`

 t̄ ≤ log m + 33·log(2Δ) + 1 gives t̄ ≤ `tbMax`, for 1 ≤ m ≤ Δn. 

### `StFit`

 For a formula ψ with clauses of 1 to k literals on variables below n, every variable in at most
Δ ≥ 2 clauses, m ≤ Δn, n̄ the number of the text and M ≤ 14n: if m > n̄, a list with display (67)
for r̄ ≤ 10n, r̄ ≤ M,
1 ≤ M and t̄ ≤ `tbMax` is fit for an evaluation; if m ≤ n̄, the empty list is. 

### `StSize`

 «The total» and «The parameters» with bounds that do not depend on the formula, the case m ≤ n̄
included: on g = 3K⁸ nodes, K > 0, for a list that is fit for an evaluation (`Fit`), the network of
an admissible profile has
size `PbD`, values of at most `BbD` bits and total at most `UbD`. 

### `objMax`

 A bound for the number I + m of objects that does not depend on the formula, and the number of
profiles that goes with it. 

### `nPrMax`

 The number of numbers tried as profiles on 3K⁸ nodes, if there were `objMax` objects. 

### `StNPrMax`

 For a list that is fit for an evaluation (`Fit`), the number of numbers tried as profiles on 3K⁸
nodes is at most `nPrMax`. 

### `StBounds`

 Bounds for the arithmetic of Step 4, on g = 3K⁸ nodes, for n ≥ 1 and Δ ≥ 2: `UbD` ≤
140·k·n·⌈log(2Δ)⌉ + 2g², and g·`PbD` is at most the right side of display (69) with t̄ = `tbMax` and
s̄ = `sbMax`. 

### `StSmall`

 The case m ≤ n̄ as printed: for g > 0, the empty list of checks, ψ well formed (WfD) with at
most n̄ clauses, every variable in at most Δ of them, and an admissible profile: U ≤ 2(k − 1)n̄ (the
text adds ≤ 2kn, which needs n̄ ≤ n and is not part of this statement), and
P = 2⌈n/g⌉(1 + Δ) and B = 1 will do. 

 ### Ev.lean: the two sums as programs 

### `evD`

 One evaluation: the sum, over the admissible profiles, of the values of their networks, each
computed by the clique solver as an exact integer. 

### `evX`

 X(𝓛): the sum reduced modulo 2^β. 

### `evF`

 F(𝓛): the sum reduced modulo 2^(n+1). 

### `StEvD`

 One evaluation is the right side of display (65), if the solver is right at the indices with
`ok`, ok i, K ≥ 2, the list is fit for an evaluation (`Fit`), and the pad fits: it is at least as
long as the number `nPr` of
numbers tried as profiles and as 2^`needNet` for the bounds `UbD`, `PbD`, `BbD`. 

### `StEvXF`

 The programs compute X(𝓛), and F(𝓛) if X(𝓛) = 0: display (65) and «the residues determine the
numbers». Needs the hypotheses of `StEvD` (solver right, ok i, K ≥ 2, `Fit`, the two conditions on
the pad), M ≥ β − 1 + r and
M ≥ n + r, with β = n + ⌈log C(m, n̄ + 1)⌉ + 1. 

 ### Cert*.lean: polynomial time 

### `StCertRank`

 Step 3, «The parameters»: binomial coefficients C(t, μ) are polynomial-time for t and μ given in
unary; the position of a string among those with as many ones is polynomial-time; and ⌈log C(t, μ)⌉
is
given in unary for t given in unary and μ polynomial-time. 

### `StCertNet`

 Condition (iii) of the definition of a network: «counting marks, multiplying powers of 2 and
finding the position of a string among those with as many ones take τ = n^O(1) operations». 

### `StCertAdm`

 The test «admissible» is polynomial-time jointly in all its arguments, for g given in unary and
the other arguments polynomial-time. 

### `StCertEvD`

 One evaluation is polynomial-time jointly in all its arguments, the width k included, for a
polynomial-time solver, with k, n and Δ given in unary and the other arguments polynomial-time. 
