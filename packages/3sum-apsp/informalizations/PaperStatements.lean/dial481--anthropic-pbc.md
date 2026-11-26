---
{
  "module": "PaperStatements.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/PaperStatements.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/PaperStatements.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Further statements of the paper

Statements of the paper «Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse
Lopsided Graphs» (Josh Alman, Virginia Vassilevska Williams) beyond the five claims of
`EndStatement.lean`, each as a proposition, with the definitions that they use; and statements that
the notions which this file and `EndStatement.lean` both define agree. The file imports
`EndStatement.lean` and Mathlib. It proves none of the statements: the proofs are in the library,
the folder `ThreeSumApsp/`. The five claims do not depend on this file: it is for a reader who wants
to believe a further lemma, equation, table or theorem of the paper.

`Challenge/PaperStatements.lean` states that the propositions hold: `PaperStatements.lemma_6` says
that `PaperStatements.Lemma_6` holds, and `ThreeSumApsp.wordRam_theorem_5` that the running-time
sentence `ThreeSumApsp.WordRam.Items.Theorem_5` holds.

The parts, in this order:

* Section 2: definitions
* Section 2: statements
* Section 3: definitions
* The reduction of Chan and He: definitions
* Section 3: statements
* Section 4: definitions
* Section 4: statements
* Section 5: definitions
* Section 5: statements
* The word RAM: problems
* Agreement with the definitions of EndStatement.lean
* The word RAM: running times

In a comment, "this part" means the part in which the comment stands.



## Section 2: definitions

Definitions used by the statements of Section 2, "Quickly computing certain entries of a thin matrix
product".  They follow the paper's order and names.  Only what the statements need, directly or
through another definition, is defined here; the other notions of the section, among them the tiling
of Section 2.3.4, are defined with the proofs.

Conventions used throughout.

* The paper numbers indices from 1; Lean's `Fin n` starts at 0.  So the paper's `x₁, x₂, x₃` are
  `LeftVar.x 0, LeftVar.x 1, LeftVar.x 2`, the paper's `p₂₁` is `LeftVar.p 1 0`, and so on.
* A string of length `L` over an alphabet `α` is a function `Fin L → α`.  The paper's level
  `ℓ ∈ {1, …, L}` is the element `ℓ - 1` of `Fin L`; the order of the levels is the order of
  `Fin L`.
* The string `s u'` (the variable `s` followed by the string `u'`) is `Fin.cons s u'`; the first
  variable of `u` is `u 0` and the rest of it is `Fin.tail u`.  The empty string is `Fin.elim0`.
* A linear form is given by the vector of its coefficients: a linear form in the left variables is a
  function `LeftVar → ℤ`.  `Pi.single s 1` is the form consisting of the single variable `s`.


 ### 2.2 Schönhage's identity for an inner product and an outer product 

### `LeftVar`

 Section 2.2: "We call x₁, x₂, x₃, p₁₁, p₁₂, p₂₁, p₂₂ the seven left variables". 

### `RightVar`

 Section 2.2: "and y₁, y₂, y₃, q₁₁, q₁₂, q₂₁, q₂₂ the seven right variables". 

### `OutVar`

 Section 2.2: "We will also use ten output variables z_ij (for 1 ≤ i, j ≤ 3) and z₀". 

### `Term`

 Section 2.2: "Schönhage's identity has ten terms, which we name P_ij (for 1 ≤ i, j ≤ 3,
corresponding to the entries of p̂ and q̂) and P₀". 

### `xForm`

 The linear form consisting of the single left variable `x_i`. 

### `pForm`

 The linear form consisting of the single left variable `p_ij`. 

### `yForm`

 The linear form consisting of the single right variable `y_j`. 

### `qForm`

 The linear form consisting of the single right variable `q_ij`. 

### `zForm`

 The linear form consisting of the single output variable `z_ij`. 

### `z0Form`

 The linear form consisting of the single output variable `z₀`. 

### `pHat`

 Section 2.2: the 3 × 3 matrix `p̂` of linear forms,
"p̂ = (p₁₁, p₁₂, 0; p₂₁, p₂₂, 0; -p₁₁-p₂₁, -p₁₂-p₂₂, 0)". 

### `qHat`

 Section 2.2: the 3 × 3 matrix `q̂` of linear forms,
"q̂ = (q₁₁, q₁₂, -q₁₁-q₁₂; q₂₁, q₂₂, -q₂₁-q₂₂; 0, 0, 0)". 

### `phi`

 Section 2.2: the linear form `φ_λ` in the left variables,
"φ_{P_ij} = x_i + p̂_ij" and "φ_{P₀} = -(x₁ + x₂ + x₃)".
Section 2.3.1: "let φ_λ(s) ∈ {0, ±1} denote the coefficient of s in φ_λ"; this is `phi lam s`. 

### `psi`

 Section 2.2: the linear form `ψ_λ` in the right variables,
"ψ_{P_ij} = y_j + q̂_ij" and "ψ_{P₀} = y₁ + y₂ + y₃".
Section 2.3.1: `ψ_λ(t)`, the coefficient of `t` in `ψ_λ`, is `psi lam t`. 

### `chi`

 Section 2.2: the linear form `χ_λ` in the output variables,
"χ_{P_ij} = z_ij + z₀" and "χ_{P₀} = z₀". 

### `Var`

 All 24 variables of the identity: the left, the right and the output variables. 

### `TriPoly`

 The polynomials in which Schönhage's identity is an identity. 

### `polyL`

 A left variable, as a polynomial. 

### `polyR`

 A right variable, as a polynomial. 

### `polyO`

 An output variable, as a polynomial. 

### `formL`

 A linear form in the left variables, as a polynomial. 

### `formR`

 A linear form in the right variables, as a polynomial. 

### `formO`

 A linear form in the output variables, as a polynomial. 

### `G`

 Section 2.2: "G := ∑_{i,j=1}^{3} x_i y_j z_ij + (∑_{i,j=1}^{2} p_ij q_ij) z₀". 

### `E`

 Lemma 6: "E := ∑_{i,j=1}^{3} (x_i q̂_ij + p̂_ij y_j + p̂_ij q̂_ij) z_ij". 

### `LeftVar.IsInner`

 Section 2.2: "We call the variables of the inner product, p, q, and z₀, inner". 

### `RightVar.IsInner`

 Section 2.2: the right variables `q` are inner, the `y` are outer. 

### `OutVar.IsInner`

 Section 2.2: the output variable `z₀` is inner, the `z_ij` are outer. 

### `Term.Contributes`

 Section 2.2: "We say that a term λ contributes to an output variable z if z appears in χ_λ." 

 ### 2.3.1 The recursion 

### `LeftStr`

 Section 2.3.1: "A left string of length L is a string u = u₁ u₂ ⋯ u_L of L left variables, and
we call u_ℓ its variable at level ℓ." 

### `RightStr`

 Section 2.3.1: right strings of length `L`. 

### `OutStr`

 Section 2.3.1: output strings of length `L`. 

### `Vertex`

 Section 2.3.1: "We refer to the call reached by choosing the terms τ₁, …, τ_k at levels 1, …, k
as the vertex τ₁ ⋯ τ_k, a string of k terms. It is at depth k". 

### `Leaf`

 Section 2.3.1: "the leaves, the vertices τ = τ₁ ⋯ τ_L at depth L". 

### `sliceAt`

 Section 2.3.1: "An array a on the left strings of length L assigns an integer a[u] to each u
that is a left string of length L."  So such an array is a function `LeftStr L → ℤ`, and likewise
for right strings, output strings and leaves.

"the slice of a at a left variable s is the array a_s on the strings of length L - 1 given by
a_s[u'] := a[s u']"; the same definition is used for every alphabet. 

### `encodeStepL`

 Section 2.3.1, step (2) of `Full`: "A_λ := ∑_s φ_λ(s) a_s". 

### `encodeStepR`

 Section 2.3.1, step (2) of `Full`: "B_λ := ∑_t ψ_λ(t) b_t". 

### `Full.run`

 Section 2.3.1: "The recursion Full(a, b), for arrays a, b on the left and right strings of
length L, returns an array on the output strings of length L:
(1) If L = 0, return the number ab.
(2) For each term λ of Schönhage's identity, form A_λ := ∑_s φ_λ(s) a_s and B_λ := ∑_t ψ_λ(t) b_t.
(3) For each term λ, recursively compute C_λ := Full(A_λ, B_λ).
(4) Return the array c whose slices are c_{z_ij} := C_{P_ij} and c_{z₀} := ∑_λ C_λ."

`Full.run` is this recursion, and it also keeps a record of the multiplications.  Its first
component is the array that is returned.  Its second component gives, for each leaf `τ`, the two
numbers that step (1) multiplies at `τ`: the leaf `λ τ'` of a call is the leaf `τ'` of its recursive
call for `λ`.

An array on the strings of length 0 has one entry, at the empty string `Fin.elim0`; that entry is
"the number". 

### `Full`

 The array that `Full(a, b)` returns. 

### `Full.multipliedAt`

 The two numbers that `Full(a, b)` multiplies at the leaf `τ`, the left one first. 

 ### 2.3.2 Unraveling the recursion computation 

### `Phi`

 Section 2.3.2: "Φ_τ(a) := ∑_u a[u] ∏_{ℓ=1}^{L} φ_{τ_ℓ}(u_ℓ)", the sum over all left strings
`u`. 

### `Psi`

 Section 2.3.2: "Ψ_τ(b) := ∑_v b[v] ∏_{ℓ=1}^{L} ψ_{τ_ℓ}(v_ℓ)", the sum over all right strings
`v`. 

### `Leaf.Contributes`

 Section 2.3.2: "a vertex τ₁ ⋯ τ_k contributes to an output string w if τ_ℓ contributes to w_ℓ at
every level ℓ ≤ k", for a leaf, that is, for `k = L`: the leaf `τ` contributes to `w` if `τ_ℓ`
contributes to `w_ℓ` at every level `ℓ`. 

### `Mult`

 Equation (2): "Mult(a, b)[w] := ∑_{τ contributing to w} Φ_τ(a) Ψ_τ(b)". 

### `gamma`

 Equation (3): "γ(s, t, z) := ∑_{λ contributing to z} φ_λ(s) ψ_λ(t)". 

 ### 2.3.3 Batch computation of multiple matrix products 

### `innerSetL`

 Section 2.3.3: "The inner set of a left string is the set of levels at which it has a p (as
opposed to an x)." 

### `innerSetR`

 Section 2.3.3: "the inner set of a right string is the set of levels at which it has a q (as
opposed to a y)". 

### `innerSetO`

 Section 2.3.3: "the inner set of an output string is the set of levels at which it has z₀ (as
opposed to a z_ij)". 

### `N0`

 Section 2.3.3: "N₀ := 3^{L-m}".  Meant for `m ≤ L`; for `m > L` the subtraction of natural
numbers is cut off at 0 and the value is 1. 

### `D`

 Section 2.3.3: "D := 4^m". 

### `K`

 Section 2.3.3: "K := binom(L, m)", the number of subsets of `{1, …, L}` of size `m`. 

### `LeftVar.outerIndex`

 The index `i` of an outer left variable `x_i` (the value at a `p` is never used). 

### `LeftVar.innerIndex`

 The index pair `(i, j)` of an inner left variable `p_ij` (the value at an `x` is never used). 

### `RightVar.outerIndex`

 The index `j` of an outer right variable `y_j` (the value at a `q` is never used). 

### `RightVar.innerIndex`

 The index pair `(i, j)` of an inner right variable `q_ij` (the value at a `y` is never used). 

### `OutVar.rowIndex`

 The first index `i` of an outer output variable `z_ij` (the value at `z₀` is never used). 

### `OutVar.colIndex`

 The second index `j` of an outer output variable `z_ij` (the value at `z₀` is never used). 

### `OuterStr`

 A string of `L - m` outer left variables `x_{i₁} ⋯ x_{i_{L-m}}`, written as the string of its
indices `i₁ ⋯ i_{L-m}`.  The same type is used for strings `y_{j₁} ⋯ y_{j_{L-m}}` of outer right
variables.  Section 2.3.3: these strings index the `N₀` rows of an `N₀ × D` matrix and the `N₀`
columns of a `D × N₀` matrix. 

### `InnerStr`

 A string of `m` inner left variables `π = p_{i₁j₁} ⋯ p_{i_m j_m}`, written as the string of its
index pairs.  The same type is used for strings `π' = q_{i₁j₁} ⋯ q_{i_m j_m}` of inner right
variables, so that the paper's `π'`, "with the same indices" as `π`, is the same element of this
type as `π`. Section 2.3.3: these strings index the `D` columns of an `N₀ × D` matrix and the `D`
rows of a `D × N₀` matrix. With this convention the paper's "(AB)[r, c] := ∑_π A[r, π] B[π', c]" is
the usual matrix product. 

### `innerLevel`

 The levels of a set `Q` of `m` levels "in the order of the levels" (Section 2.3.3): the `k`-th
lowest level of `Q`. 

### `card_compl_of_card_eq`

 The number of levels outside a set of `m` levels is `L - m`. 

### `outerLevel`

 The levels outside a set `Q` of `m` levels, in the order of the levels: the `k`-th lowest level
outside `Q`. 

### `outerPartL`

 Section 2.3.3: "its outer part is the string of its variables at the other levels", for a left
string whose inner set has `m` elements. 

### `innerPartL`

 Section 2.3.3: "The inner part of a string is the string of its variables at the levels of its
inner set, in the order of the levels", for a left string whose inner set has `m` elements. 

### `outerPartR`

 The outer part of a right string whose inner set has `m` elements. 

### `innerPartR`

 The inner part of a right string whose inner set has `m` elements. 

### `rowO`

 Section 2.3.3: "if the variables of w at the levels outside Q are z_{i₁j₁}, …, z_{i_{L-m}
j_{L-m}}, in the order of the levels, then the row of w is the string x_{i₁} ⋯ x_{i_{L-m}}". 

### `colO`

 Section 2.3.3: "and its column is the string y_{j₁} ⋯ y_{j_{L-m}}". 

### `LeftMat`

 An `N₀ × D` matrix, its rows and columns indexed by strings as in Section 2.3.3. 

### `RightMat`

 A `D × N₀` matrix, its rows and columns indexed by strings as in Section 2.3.3. 

### `arrayL`

 Section 2.3.3: "a[u] := X_Q[u] […] for all the left strings u […] whose inner set Q has exactly
m elements, and a[u] := 0 […] at every other string", where "X_Q[u]" is the entry of `X_Q` "at the
row and the column of u": the row is the outer part of `u` and the column is its inner part. The
family `X` gives a matrix `X Q` for every set `Q` of levels; only those with `|Q| = m` are used. 

### `arrayR`

 Section 2.3.3: "b[v] := Y_Q[v]" for the right strings `v` whose inner set `Q` has exactly `m`
elements, "the row given by the inner part of v and the column by the outer part", and `b[v] := 0`
at every other string. 

 ### 2.3.4 Tiling the N × D × N product by products of shape N₀ × D × N₀: the number `M` 

### `M`

 Section 2.3.4: "M := K N₀²". 

 ### 2.4.1 Sharing the encoding 

### `encodingL`

 Section 2.4.1: "The encoding of a is the array of the 10^L numbers Φ_τ(a), indexed by the leaves
τ." 

### `encodingR`

 Section 2.4.1: "The encoding of b, the array of the numbers Ψ_τ(b)". 

 ### 2.4.2 Skipping the calls that are not needed 

### `sliceSet`

 Section 2.4.2: "for a set S of output strings and an output variable z, the slice S_z is the set
of output strings w' with z w' ∈ S". 

### `childSet`

 Section 2.4.2, step (2) of `Pruned`: "let S_λ be the union of the slices S_z over the z to which
λ contributes". 

### `restrictTo`

 Section 2.4.2: "an array on S assigns an integer to each string of S".  We write such an array
as a function on all output strings that is 0 outside `S`; this restricts an array to `S`. 

### `PrunedCall`

 A call of `Pruned`.  `vertex` is the vertex `τ₁⋯τ_k` at which it is made, as the pair of its
depth `k` and the string of terms.  `passed` is the set that is passed to it, as the pair of the
length of its strings and the set. 

### `PrunedCall.under`

 The same call, seen from one level higher: the vertex `τ₁⋯τ_k` below the child `λ` is the vertex
`λ τ₁⋯τ_k`. 

### `Pruned.run`

 Section 2.4.2: "Pruned_{τ₁⋯τ_k}(S), for a set S of output strings of length L - k, returns the
array returned by the vertex τ₁⋯τ_k of Full, restricted to the strings in S: (1) If k = L, then look
up Φ_τ(a) and Ψ_τ(b) from the precomputed encodings (Section 2.4.1) and return Φ_τ(a) Ψ_τ(b) for the
leaf τ = τ₁⋯τ_L. (2) For each term λ of Schönhage's identity, let S_λ be the union of the slices S_z
over the z to which λ contributes, i.e., S_{P_ij} := S_{z_ij} ∪ S_{z₀} and S_{P₀} := S_{z₀}. (3) For
each term λ of Schönhage's identity with S_λ ≠ ∅, compute C_λ := Pruned_{τ₁⋯τ_k λ}(S_λ), an array on
S_λ. (4) Return the array c on S whose slices are c_{z_ij} := C_{P_ij} and c_{z₀} := ∑_λ C_λ,
restricted to S_{z_ij} and to S_{z₀}."

`Pruned.run` is this recursion, and it also keeps a record of the calls.  Its first component is the
array that is returned.  Its second component lists all the calls that are made, this one included,
each with the set passed to it.  Vertices are named relative to the call we start from, so for the
call at the root they are the vertices of the paper.

Here `n = L - k`.  The vertex `τ₁⋯τ_k` enters only through the look-ups of step (1), so it is passed
as the parts of the two encodings that lie below it: `encA τ'` is the entry of the encoding of `a`
at the leaf `τ₁⋯τ_k τ'`, and likewise `encB`.  At the root these are the two encodings themselves,
and the child `λ` receives their slices at `λ`.  For a term `λ` with `S_λ = ∅` no call is made:
nothing is recorded, and `C_λ` is written as the zero array; step (4) does not read it, because then
`S_{z₀}`, and `S_{z_ij}` if `λ = P_ij`, are empty.  In step (1) the number is returned as an array
on `S`, like every other result; `S` then consists of the empty string, except when `Pruned` is
called at the root with `L = 0` and `S = ∅`. 

### `Pruned`

 The array that `Pruned(S)` returns. 

### `Pruned.calls`

 All the calls that `Pruned(S)` makes, itself included, each with the set passed to it. 

### `Pruned.Visits`

 The leaves that `Pruned(U)`, called at the root, visits: the vertices at depth `L` among its
calls. 

### `Pruned.totalSize`

 The total size of the sets passed to the calls that `Pruned(U)` makes. 

### `Leaves`

 Section 2.4.2: "For a set U of output strings of length L, we write Leaves(U) for the set of
leaves that contribute to some output string of U." 

 ### 2.4.3 Few leaves contribute to a sparse set of entries 

### `OutVar.privateTerm`

 The term that the private leaf has at a level where the output string has the variable `z`:
`P₀` for `z₀` and `P_ij` for `z_ij`. 

### `privateLeaf`

 Section 2.4.3: "the leaves contributing to an output string with inner set Q are the 10^m leaves
that choose any term at each of the m levels of Q, but P_ij at every level outside Q where the
output string has z_ij. We call the one that chooses P₀ at every level of Q the private leaf of the
output string." 

### `P0Levels`

 The set of levels at which a leaf chooses `P₀`. 

### `order`

 Section 2.4.3: "we define the order of a leaf as m minus the number of levels at which it
chooses P₀." The order is an integer; it is negative for a leaf that chooses `P₀` at more than `m`
levels. 

### `alpha`

 Section 2.4.3: "α_d := binom(m, d) 9^d". 

### `beta`

 Section 2.4.3: "β_d := binom(L, m-d) 9^{L-m+d}".  Meant for `d ≤ m ≤ L`; outside this range the
subtractions of natural numbers are cut off at 0 and the value has no meaning. 


## Section 2: statements

The numbered lemmas and equations of Section 2 of the paper, and the figures that
assert something of their own.

* Equation (1) is `Eq_1`. Equations (2) and (3) are the definitions `Mult` and `gamma`. Equation (4)
  is the display of `Lemma_9`. Equation (5) is stated in three pieces: `Eq_5_ratio`, `Eq_5_bound`,
  `Eq_5`. Equation (6) is `Eq_6`.
* Lemmas 6 to 11 are `Lemma_6` to `Lemma_11`, each as one statement.
* Of Figure 3 the two worked examples of the caption are stated: `Figure_3`. Of Figure 4 the worked
  example is stated: `Figure_4`. Figure 6 is `Figure_6`; the two counts
  `Sec2_card_contributing_of_order` and `Sec2_card_outStr_of_leaf` say what its numbers count.
* Theorem 5 is a sentence about a machine. It is `Items.Theorem_5`. So of the tiling (Section 2.3.4)
  and of the proof of Theorem 5 (Section 2.4.4) nothing is stated here but the number `M` and
  equation (6): the statements of this part are about a single run of the recursion.
* Remark 12 makes no mathematical claim. Figure 2 recalls Strassen's recursion for intuition; only
  identity (1) is stated. Figure 5 makes no claim of its own. Figure 7 draws the count of Lemma 11;
  two remarks of its caption, that "the bound |U|α_d grows with d up to d ≈ 0.9m" and that the proof
  splits at a point "which is not necessarily where the two bounds cross", are not stated.

`docs/INDEX.md` says for each item of the paper what is stated and what is not.

A hypothesis that is not in the printed text is marked NOTE in the docstring. A hypothesis of the
printed text that is not needed (such as m ≥ 1, Section 2.3.3) is left out without a mark.


 ### 2.1 Strassen's recursive algorithm 

### `Eq_1`

 Equation (1) and the display after it: Strassen's seven products give the product of
two 2 × 2 matrices.  The entries may be blocks, so they are taken in a ring that need not be
commutative. 

 ### 2.2 Schönhage's identity for an inner product and an outer product 

### `Lemma_6`

 **Lemma 6**.  "Summing over the ten terms, ∑_λ φ_λ ψ_λ χ_λ = G + E, where E :=
∑_{i,j=1}^{3} (x_i q̂_ij + p̂_ij y_j + p̂_ij q̂_ij) z_ij."  An identity of polynomials with integer
coefficients in the 24 variables. 

 ### 2.3.1 The recursion 

### `Figure_3`

 Figure 3: "For instance, A_{P₃₁} = a_{x₃} - a_{p₁₁} - a_{p₂₁} and
A_{P₀} = -a_{x₁} - a_{x₂} - a_{x₃}."  (Indices are counted from 0 in Lean.) 

 ### 2.3.2 Unraveling the recursion computation 

### `Lemma_7`

 **Lemma 7**.  "At the leaf τ, Full(a, b) multiplies Φ_τ(a) by Ψ_τ(b), and it returns
Mult(a, b)." 

### `Lemma_8`

 **Lemma 8**.  "For all arrays a, b and every output string w,
Mult(a, b)[w] = ∑_{u,v} γ(u₁, v₁, w₁) γ(u₂, v₂, w₂) ⋯ γ(u_L, v_L, w_L) a[u] b[v],
the sum over all left strings u and right strings v." 

 ### 2.3.3 Batch computation of multiple matrix products 

### `Figure_4`

 Figure 4, for `L = 6` and `m = 2`.  This docstring counts levels and indices from 1,
as the paper does; the Lean text counts them from 0, so that the inner set {2, 5} is `{1, 4}` and x₁
is `.x 0`.  The strings `u = x₁ p₁₁ x₂ x₃ p₂₂ x₁`, `v = y₃ q₁₁ y₁ y₃ q₂₂ y₂` and
`w = z₁₃ z₀ z₂₁ z₃₃ z₀ z₁₂` have the inner set `{2, 5}`; `u` has the outer part `x₁x₂x₃x₁` and the
inner part `p₁₁p₂₂`; `v` has the inner part `q₁₁q₂₂` and the outer part `y₃y₁y₃y₂`; `w` has the row
`x₁x₂x₃x₁` and the column `y₃y₁y₃y₂`.  The sizes `81 × 16`, `16 × 81` and `81 × 81` of the matrices
and the number `binom(6, 2) = 15` of products, which the figure also shows, are not stated here. 

### `Lemma_9`

 **Lemma 9**.  "For the input arrays a, b above and every output string w whose inner
set Q has exactly m elements, Mult(a, b)[w] = (X_Q Y_Q)[w]."  (Equation (4).) 

 ### 2.4.2 Skipping the calls that are not needed 

### `Lemma_10`

 **Lemma 10**, its three claims together.  "Let a and b be input arrays, and let U be a
set of output strings of length L. Called at the root, Pruned(U) returns Mult(a, b) restricted to U.
The leaves it visits are exactly those of Leaves(U), and the sets passed to the calls it makes have
total size at most (L+1) |Leaves(U)|."

NOTE.  The hypothesis `0 < L ∨ U.Nonempty` of the second claim is not in the paper.  It excludes
only the case `L = 0`, `U = ∅`, in which the root is itself a leaf, so that the call at the root
visits it, while `Leaves(∅)` is empty.  In the paper `L ≥ m ≥ 1`, and `Pruned` is run only on
nonempty sets (Section 2.4.4). 

 ### 2.4.3 Few leaves contribute to a sparse set of entries 

### `Sec2_card_contributing_of_order`

 Section 2.4.3: "exactly α_d := binom(m, d) 9^d leaves of order d contribute to an output
string".  As everywhere in Section 2.4.3, the output strings are those whose inner sets have exactly
m elements. 

### `Sec2_card_outStr_of_leaf`

 Section 2.4.3: "A leaf of order d contributes to binom(L-m+d, d) output strings, one for each
inner set of size m that contains the m-d levels at which it chooses P₀."  Only the number is
stated.  As everywhere in Section 2.4.3, the output strings are those whose inner sets have exactly
m elements.

NOTE.  `m ≤ L` is left implicit in the paper. 

### `Eq_5_ratio`

 Section 2.4.3, the equality in equation (5), for every `L ≥ m` (it is used again as equation (7)
in Section 4.3): "β_d / β_{d-1} = 9(m-d+1) / (L-m+d)" for `1 ≤ d ≤ m`.

NOTE.  The paper prints the equality under `L = 19m` in (5) and under `L ≥ 10m` in (7); here it is
stated for every `L ≥ m`. 

### `Eq_5_bound`

 Section 2.4.3, the inequalities in equation (5): "if L = 19m, then for 1 ≤ d ≤ m we have
β_d / β_{d-1} = 9(m-d+1)/(L-m+d) ≤ 9m/(18m+1) < 1/2". 

### `Eq_5`

 **Equation (5)**, conclusion: if `L = 19m` then "β_d ≤ 2^{-d} M", for `0 ≤ d ≤ m`.
The inequality is multiplied out. 

### `Figure_6`

 Figure 6, for `L = 6`, `m = 2` and the output string `w = z₁₃ z₀ z₂₁ z₃₃ z₀ z₁₂` of
Figure 4: its private leaf is `P₁₃ P₀ P₂₁ P₃₃ P₀ P₁₂`, and the numbers of the figure, evaluated:
`α₀ = 1`, `α₁ = 18`, `α₂ = 81`, `binom(5, 1) = 5` and `binom(6, 2) = 15` (the "1 output string" of
the private leaf, `binom(4, 0) = 1`, is left out).  That `α_d` leaves of order `d` contribute to
`w`, and that a leaf of order `d` contributes to `binom(L-m+d, d)` output strings, is stated in
general by `sec2_card_contributing_of_order` and `sec2_card_outStr_of_leaf`. 

### `Lemma_11`

 **Lemma 11**, both inequalities together.  "For every set U of output strings whose inner
sets have exactly m elements, |Leaves(U)| ≤ ∑_{d=0}^{m} min{|U| α_d, β_d}, and if L = 19m,
then |Leaves(U)| ≤ 2^{-m/9} (2^m |U| + 2M)." 

 ### 2.4.4 Proof of Theorem 5 

### `Eq_6`

 **Equation (6)**, the second consequence of `N ≥ D^18`: "10^L ≤ 2^{-m/9} N N₀", for
`L = 19m`. 


## Section 3: definitions

Definitions used by the statements of Section 3, "Exact Triangle reduces to computing certain
entries of a thin matrix product".  They follow the paper's order and names.  Only what the
statements need, directly or through another definition, is defined here; some of the definitions
are used by the statements about programs and not by those of Section 3.

Conventions used throughout.

* A part of `n` vertices is the type `Fin n`.  A pair `(a, b) ∈ A × B` is an element of
  `Fin n × Fin n`, a triple `(a, b, c) ∈ A × B × C` an element of `Fin n × Fin n × Fin n`.
* The paper numbers the pieces from 1; here pieces and chunks are numbered from 0.
* `√D` is the real square root `Real.sqrt D`, `⌊·⌋` and `⌈·⌉` are `Nat.floor` and `Nat.ceil` of real
  numbers, and `log` is the natural logarithm `Real.log` unless a base is written.
* `x ≡ y (mod p)` is `Int.ModEq`, written `x ≡ y [ZMOD p]`.  A residue or label in `ℤ_p` is an
  element of `Fin p`.
* No definition of this part mentions time.  For the sentences of the paper about running time see
  `docs/REMARKS.md`, "Section 3: running times". 

 ### 3.1 The Lopsided All-Edges Sparse Triangle problem 

### `LopInstance`

 **Definition 13**, the input: "an unweighted undirected tripartite graph with two parts
A and B of n vertices each and a middle part M [...], with arbitrary edges in M × A and M × B.  Let
W ⊆ A × B be the set of edges between A and B."  The bound "of at most D vertices" on the middle
part is `LopInstance.MiddleAtMost`. 

### `LopInstance.M`

 The middle part `M`. 

### `LopInstance.fintypeM`

 The middle part is finite. 

### `LopInstance.adjA`

 `adjA a v`: the vertex `a ∈ A` and the middle vertex `v ∈ M` are adjacent. 

### `LopInstance.adjB`

 `adjB v b`: the middle vertex `v ∈ M` and the vertex `b ∈ B` are adjacent. 

### `LopInstance.W`

 The set `W ⊆ A × B` of edges between `A` and `B`; Section 3.1 calls its elements the query
  pairs. 

### `LopInstance.MiddleAtMost`

 Definition 13: "a middle part M of at most D vertices".  An instance of Lop-AE-SparseTri(n, D),
and of #Lop-AE-SparseTri(n, D), is an `I : LopInstance n` with `I.MiddleAtMost D`. 

### `LopInstance.commonNeighbors`

 Definitions 13 and 14: the common neighbors of `a` and `b` in `M`. 

### `LopInstance.InTriangle`

 Definition 13: the pair `(a, b)` "lies in a triangle with some vertex of M, that is, [...] a and
b have a common neighbor in M". 

### `LopInstance.numTriangles`

 **Definition 14**: "the number of triangles it lies in, that is, the number of common
neighbors of a and b in M". 

### `LopInstance.IsDetectionAnswer`

 **Definition 13**, the task: "Decide, for every edge (a, b) ∈ W, whether it lies in a triangle
with some vertex of M".  `ans` is a correct answer to the instance `I` of Lop-AE-SparseTri; its
values outside `W` are not constrained. 

### `LopInstance.ofMatrices`

 Footnote 8, Section 3.1: "An instance of #Lop-AE-SparseTri(n,D) asks for the wanted entries of a
thin matrix product of two 0/1 matrices."  This is the instance that two matrices and a set `W` of
positions describe: the middle part is the set of the `D` column indices of `X`, and adjacency means
that the entry is 1. 

 #### Cutting a set of pairs into sets of bounded size

Corollary 15 ("splitting W into sets of at most n²/√D query pairs") and the proof of Theorem 17
("cut it into chunks of at most n²/√D query pairs") cut a set of pairs into smaller sets.  The paper
does not say how; we cut along the row-major order of the pairs. 

### `pairIndex`

 The position of the pair `(a, b)` in the row-major order of `A × B`. 

### `rankIn`

 The number of pairs of `S` that come before `q` in row-major order. 

### `chunk`

 The `j`-th chunk (`j = 0, 1, …`) of `S` when `S` is cut, in row-major order, into chunks of
`cap` pairs each (the last one may be smaller). 

### `numChunks`

 The number `⌈|S| / cap⌉` of nonempty chunks of `S` (for `cap ≥ 1`). 

### `queryCap`

 The largest number of query pairs that is "at most n²/√D" (Corollary 15 and Theorem 17;
Theorem 5 has "at most N²/√D"): `⌊n²/√D⌋`. 

 ### 3.2 A deterministic reduction from Exact Triangle to Lop-AE-SparseTri 

### `TriangleInstance`

 Section 3.2: "An instance of Exact Triangle [...] consists of a complete tripartite graph on
vertex parts A, B, C of n vertices each, and an integer weight w(e) on every edge".  The three
fields are the weights `w(a,b)`, `w(b,c)` and `w(a,c)`.  The type `R` of the weights is `ℤ` in
Section 3; Section 5 also uses real weights.  The bound on the weights is a separate predicate
(`WeightsBoundedBy`, `WeightsPolyBounded`). 

### `TriangleInstance.wAB`

 `wAB a b` is the weight `w(a,b)` of the edge between `a ∈ A` and `b ∈ B`. 

### `TriangleInstance.wBC`

 `wBC b c` is the weight `w(b,c)` of the edge between `b ∈ B` and `c ∈ C`. 

### `TriangleInstance.wAC`

 `wAC a c` is the weight `w(a,c)` of the edge between `a ∈ A` and `c ∈ C`. 

### `S`

 Section 3.2: "Let S(a,b,c) := w(a,b) + w(b,c) + w(a,c)." 

### `IsZeroTriangle`

 Section 3.2: "A zero triangle is a triangle (a,b,c) ∈ A × B × C with S(a,b,c) = 0". 

### `HasZeroTriangle`

 Section 3.2: "the task is to decide whether one exists". 

### `WeightsBoundedBy`

 Every weight has absolute value at most `U`. 

### `WeightsPolyBounded`

 Section 3.2: "with |w(e)| ≤ n^ν for some constant ν ≥ 1".  `κ`, the paper's ν, is a real
number. 

### `IsSearchAnswer`

 A correct answer to the search version, Section 3.2: "the search version, which asks the
algorithm to find a zero triangle if one exists".  `some (a, b, c)` must be a zero triangle, and
`none` means that there is none. 

### `GraphHasZeroTriangle`

 Section 3.2: a zero triangle of "an instance on an arbitrary n-vertex
graph": three pairwise adjacent vertices whose three edge weights sum to zero.  `w u v` is the
weight of the edge `{u, v}`; only the values `w u v`, `w v x`, `w u x`, in this order of the
arguments, are read, so `w` need not be assumed symmetric. 

 #### Hashing modulo a prime (proof of Theorem 17) 

### `primesInRange`

 Proof of Theorem 17: the primes "p ∈ [√D/2, √D)", called "the primes in the range". 

### `countZeroMod`

 Proof of Theorem 17: "For every prime p in the range we count the triples with S(a,b,c) ≡ 0 (mod
p)."  This is that count. 

### `IsSelectedPrime`

 Proof of Theorem 17: "We select the prime with the smallest count [...] and call it p."  The
paper does not say how ties are broken, so this is a predicate: `p` is a prime in the range whose
count is smallest. 

 #### The instances (proof of Theorem 17) 

### `sOf`

 Proof of Theorem 17: "let s := ⌊√D⌋". 

### `pieceSize`

 Proof of Theorem 17: the bound "⌈s/g⌉" on the number of vertices of a piece. 

### `piece`

 Proof of Theorem 17: "split C into pieces C₁, …, C_h of at most ⌈s/g⌉ vertices each".  The paper
does not say how; we take blocks of `⌈s/g⌉` consecutive vertices.  `piece n D g k` is the paper's
`C_{k+1}`. 

### `numPieces`

 Proof of Theorem 17: the number `h` of pieces, `⌈n / ⌈s/g⌉⌉` for the blocks of `piece`
(meaningful when `⌈s/g⌉ ≥ 1`). 

### `InstanceIndex`

 The index of an instance built by the reduction of Theorem 17: a residue `ϱ ∈ ℤ_p`, the number
`j` of a chunk of `W_ϱ`, and the number `k` of a piece of `C`. 

### `residueClass`

 Proof of Theorem 17: "For ϱ ∈ ℤ_p let W_ϱ be the set of edges (a,b) ∈ A × B with w(a,b) ≡ ϱ (mod
p)". 

### `chunkOf`

 Proof of Theorem 17: "and cut it into chunks of at most n²/√D query pairs".  The `j`-th chunk of
`W_ϱ`. 

### `lopInstance`

 Proof of Theorem 17: "For each chunk 𝒬 ⊆ W_ϱ and each piece C_k form the instance of
Lop-AE-SparseTri(n, D) with query pairs W := 𝒬 and middle part C_k × ℤ_p [...], whose middle
vertices are pairs (vertex, label) [...], with a ∼ (c, σ) ⟺ σ ≡ w(a,c) + ϱ,   (c, σ) ∼ b ⟺ σ ≡
−w(b,c)   (mod p)." 

### `instanceIndices`

 Proof of Theorem 17: "For each chunk 𝒬 ⊆ W_ϱ and each piece C_k" there is an instance; these
are the indices of all the instances. This set depends only on the Exact Triangle instance and on
`D`, `g`, `p`, not on any answer of the oracle. 

 #### Witnesses (proof of Theorem 17) 

### `scanPiece`

 Proof of Theorem 17: "scan the piece C_k of its instance for a c with S(a,b,c) = 0".  The
vertices of the piece are tried in increasing order; the result is the first `c` found, or `none` if
the scan fails. 

### `acceptedPairs`

 Proof of Theorem 17: "For every query pair that the oracle accepts".  `ans ι` is the oracle's
answer to the instance with index `ι`.  The result is the set of all (instance, query pair of that
instance) that the oracle accepts; each of them calls for one scan. 

### `runScans`

 Proof of Theorem 17: the scans, one after the other, over a list of accepted pairs: "We stop as
soon as a zero triangle is found."  The result is the triangle found (or `none`) together with the
number of scans that were carried out. 

### `IsScanOrder`

 Proof of Theorem 17: "For every query pair that the oracle accepts, scan [...]".  The paper does
not say in which order.  `L` is an order of the scans: a list in which every accepted pair occurs
exactly once. 

 ### 3.4 3SUM and APSP reduce to Exact Triangle: the problems 

### `ThreeSum`

 **3SUM**, Section 1: "Given n numbers, decide whether three of them sum to 0."  This is the
question that the problem `EndStatement.ThreeSum` asks.

NOTE.  We read "three of them" as three numbers at three different positions of the input. 

### `Convolution3SUM`

 **Convolution-3SUM**, Section 1.2: "do x₀, …, x_{n−1} satisfy x_i + x_j = x_{i+j} for some
i, j?" 

### `TriangleInstance.HasNegativeTriangle`

 **Negative Triangle**, Section 1.2: "asks whether an edge-weighted graph has a triangle of
negative total weight".  The instances here are those of Exact Triangle. 

### `IsMinPlusProduct`

 **The (min,+)-product** of Theorems 21 and 22, "defined by (A⋆B)[i,j] = min_k(A[i,k] + B[k,j])"
(Section 1): `C` is the (min,+)-product of `A` and `B` if `C[i,j] = min_k (A[i,k] + B[k,j])` for all
`i, j`.  Stated for rectangular matrices because Section 5 uses them. 

### `minPlus`

 The (min,+)-product as a function, for matrices whose entries may be `+∞` (`⊤`): the minimum
over the empty set, and any sum with `+∞`, is `+∞`. 

 A directed graph on the vertices `Fin n` with edge weights in `R` is a function
`w : Fin n → Fin n → WithTop R`: `w i j` is the weight of the edge from `i` to `j`, and `⊤` (that
is, `+∞`) if there is no such edge.  A walk that starts at `i` is given by the list of the vertices
it visits after `i`. 

### `walkEnd`

 The vertex at which the walk that starts at `i` and then visits `rest` ends. 

### `walkWeight`

 The total weight of the walk that starts at `i` and then visits `rest`; it is `⊤` if one of its
edges is missing, and the empty walk has weight 0. 

### `NoNegativeCycle`

 Section 1 and Theorems 21 and 22: "no negative cycles".  Stated for closed walks, which is the
same thing: a closed walk decomposes into cycles. 

### `IsDistanceMatrix`

 **APSP**, Section 1: "compute the shortest-path distance between every pair of vertices".  `d i
j` is the least weight of a walk from `i` to `j`, and `⊤` if `j` cannot be reached from `i`. 

### `EdgeWeightsBoundedBy`

 Every edge weight of the directed graph has absolute value at most `U`. 

### `weightMatrix`

 The weight matrix of the graph, for the repeated squaring behind Theorem 21(b).  Its diagonal
entries are 0, without which repeated squaring would compute walks of exactly `2^t` edges. 

### `minPlusSquares`

 Repeated squaring, for Theorem 21(b): `minPlusSquares w t` is the weight matrix after `t`
squarings in the (min,+)-product. 

 #### The shape of the two reductions of [VW13] that Theorem 21 cites 

### `TriangleInstance.mapWeights`

 The instance on the same vertices obtained from `T` by applying one function to every weight
`w(a,b)`, one to every `w(b,c)` and one to every `w(a,c)`. 

### `TriangleTemplate`

 A rule that says where each edge weight of a triangle instance on `t` vertices per part is
copied from, given an input `x₀, …, x_{N−1}`: `some (false, i)` stands for `x_i`, `some (true, i)`
for `−x_i`, and `none` for a filler weight.  The rule does not depend on the numbers `x_i`. 

### `TriangleTemplate.eAB`

 The source of `w(a,b)`. 

### `TriangleTemplate.eBC`

 The source of `w(b,c)`. 

### `TriangleTemplate.eAC`

 The source of `w(a,c)`. 

### `templateWeight`

 The weight that a source stands for, given the input `x` and the filler weight `fill`. 

### `TriangleTemplate.instantiate`

 The triangle instance that a template produces from the input `x` and the filler weight
`fill`. 

 #### Asymptotic notation of Section 3 

### `IsPowLittleO`

 `f(n) = n^{a+o(1)}`.

NOTE.  We read it as an upper bound, as the paper uses it for times and for numbers and sizes of
instances: there is a sequence `ε(n) → 0` with `|f(n)| ≤ n^{a+ε(n)}` for all large `n`. 

### `IsPowPolylog`

 `f(n) = O(n^a (log n)^{O(1)})`. 

### `IsBigOPow`

 `f(n) = O(n^a)`. 


## The reduction of Chan and He: definitions

[CH20] is Timothy M. Chan and Qizheng He, *Reducing 3SUM to Convolution-3SUM*, Proc. 3rd SIAM
Symposium on Simplicity in Algorithms (SOSA 2020).  Theorem 21(a) of the paper cites [CH20].  What
is used is the reduction in the proof of its Theorem 5.1, a deterministic reduction from 3SUM to
polylogarithmically many instances of Convolution-3SUM.  The theorem itself is a statement about
running times, for 3SUM on three sets and Convolution-3SUM on three arrays.

This part defines such a reduction, as a function from inputs to lists of instances.  What is proved
about it is stated by `Theorem_21a_threeSum_to_convolution` and `Theorem_21a_threeSum_to_exact`.
The construction follows the proof of Theorem 5.1.  Where it differs from [CH20], and what it adds,
is listed in `docs/REMARKS.md`, "Section 3: cited results".

### Why all these definitions are trusted

The list of instances depends on the input.  A statement of the form "there is a list of instances
such that the input has a solution iff one of them has" would be true for trivial reasons.  So the
statements are about the explicitly defined function `instances`, which is built from `reduction`,
and their worth rests on the definitions of this part.

* `reduction` takes three sets of at most n integers.  It returns the nodes of a recursion tree, and
  each node stands for one instance of Convolution-3SUM on three arrays.  3SUM on three sets (are
  there a, b, c, one from each set, with a + b + c = 0?) and Convolution-3SUM on three arrays (are
  there i, j with X i + Y j = Z (i + j)?) are the problems of Definitions 2.1 and 2.2 of [CH20], for
  which Theorem 5.1 is stated.
* `instances` takes n numbers, for the problem whether three of them, at three different positions,
  sum to 0.  It returns instances of Convolution-3SUM on one array.  These are the problems of the
  paper, 3SUM in the reading fixed at `ThreeSum`.

Evaluated literally, `coll` and `heavy` compare all pairs of elements, and each search tests all its
candidates, so the definitions are a specification and not the algorithm.  Nothing in this part is
about a machine.

Every choice that the two functions make depends only on which elements collide and how many pairs
do, on which sets are empty, on binary digits of the numbers and on how often a number occurs.  None
depends on whether a solution exists, with one exception: the solution 0, 0, 0 exists exactly when 0
occurs at three positions.  So it is detected by counting, and it is reported through the three-set
input (`zeroSet x`, {0}, {0}), which has a solution exactly in that case.

In this part `ν` is a node of the recursion tree.  It is not the exponent ν of Theorem 21, which
the statements call `κ`.


 ### Collisions and heavy elements 

### `coll`

 The number of ordered pairs of distinct elements of `S` that are congruent modulo `M`. 

### `heavy`

 The elements of `S` that share their residue modulo `M` with another element of `S`.  They play
the role of the bad elements of [CH20].  The other elements of `S`, those that are alone in their
residue class modulo `M`, are called light below; they play the role of the good elements of [CH20].


 ### The arrays of one node 

### `bucket`

 The elements of `S` with remainder `r` modulo `M`. 

### `arr`

 The array of the light elements of `S`.  Cell `i` holds the element of the bucket of `i` if that
bucket has exactly one element, and the padding value `pad` otherwise. 

### `pad`

 The padding value `2U + 1`.  It is too large to take part in a solution among numbers of
absolute value at most `U`. 

### `arrXY`

 The array made from the first or the second set of a node. 

### `arrZ`

 The third array of a node.  A light element `c` of `S` is written as `-c` into the two cells `r`
and `r + M`, where `r` is the remainder of `-c`.  All other cells, and all cells from `2M` on, hold
`-pad U`. 

 ### The choice of the modulus 

### `pick`

 The least element of a finite set of natural numbers, and 1 if the set is empty. 

### `firstP`

 The first prime: the least `p` in `Q` modulo which each of the three sets has at most
`3Λ|S|²/|Q|` colliding pairs.  Here and below, `Q` is the set of candidate primes, and `Λ` bounds
how many of them divide a nonzero difference of two elements.  `reduction` takes the primes up to
`mPar n U` for `Q`, and `Lam U` for `Λ`. 

### `secondP`

 The second prime, given the first: the least `q` in `Q` such that, in each of the three sets, at
most the fraction `3Λ/|Q|` of the pairs that collide modulo `p` still collide modulo `pq`. 

### `modulus`

 The modulus of a node: the product of the two primes. 

 ### The recursion tree 

### `Node`

 A node of the recursion tree: three sets and the modulus chosen for them. 

### `Node.S₁`

 The first set. 

### `Node.S₂`

 The second set. 

### `Node.S₃`

 The third set. 

### `Node.M`

 The modulus. 

### `nodes`

 The nodes on the first `f` levels of the recursion tree with root `(S₁, S₂, S₃)`; for `f = 0`
there are none.  A triple with an empty set is not a node and has no children.  Any other triple is
a node, and each of its three children replaces one of the sets by its heavy elements. 

 ### The parameters 

### `Lam`

 `⌊log₂(2U)⌋ + 1`.  A nonzero difference of two numbers in `[-U, U]` has fewer prime divisors
than this, and this many binary digits are enough for every number in `[0, 2U]`. 

### `height`

 `⌈log₂(⌊log₂ n⌋ + 2)⌉`.  In the recursion tree of `reduction n U`, for three sets of at most
`n ≥ 1` elements each, all of absolute value at most `U` (the hypotheses of the library's lemma
`ChanHe.reduction_correct`), a set is empty after this many replacements by its heavy elements. 

### `fuel`

 The number of levels of the recursion tree that are built.  Under the hypotheses named at
`height`, each of the three sets of a node has been replaced at most `height n - 1` times, because
it is not empty.  So a node has at most `3 (height n - 1)` nodes above it. 

### `wPar`

 The number of primes that we want to choose from. 

### `mPar`

 The bound `m` on the primes.  There are at least `wPar n U` primes up to `m` (the library's
lemma `ChanHe.wPar_le_card_primesLE`). 

 ### The reduction for three sets 

### `reduction`

 **The reduction for three sets.**  Here `n` is an upper bound on the sizes of the three sets and
`U` on the absolute values of their elements; both stay fixed through the recursion.  The result is
a list of nodes.  The Convolution-3SUM instance of a node `ν` consists of the arrays
`arrXY ν.S₁ ν.M U`, `arrXY ν.S₂ ν.M U` and `arrZ ν.S₃ ν.M U`, read at any length
`N ≥ 2 * mPar n U ^ 2`. 

 ### From n numbers to three sets 

### `lab`

 The label of an element of `[-U, U]`: its value shifted into `[0, 2U]`. 

### `splitA`

 The elements of `S` whose label has the binary digit `v` at position `β`. 

### `splitB`

 The elements of `S` whose label has the other digit, `!v`, at position `β`, and the digit `w` at
position `β'`. For fixed `β`, `β'` and `v` the three sets `splitA U β v S`,
`splitB U β β' v false S` and `splitB U β β' v true S` are pairwise disjoint. 

### `twiceSet`

 The numbers `2a`, for the values `a ≠ 0` that occur at two positions or more. 

### `zeroSet`

 The set `{0}` if 0 occurs at three positions or more, and the empty set otherwise.  This is the
one place where the reduction decides a case by itself: 0 occurs at three positions exactly when
`0, 0, 0` is a solution. 

 ### Three arrays in one 

### `oneArray`

 **Three arrays in one.**  With `G = 3W + 1`, where `W` bounds the entries of the three arrays,
cell `4i + 1` holds `X i + G`, cell `4i + 2` holds `Y i + 3G`, cell `4i + 3` holds `Z i + 4G`, and
cell `4i` holds `10G`.  In an equation `y_u + y_v = y_{u+v}` the multiples of `G` have to cancel,
and they do so only when `u` and `v` have the remainders 1 and 2 modulo 4. 

### `Node.oneArray`

 The one-array instance of a node. 

 ### The whole reduction 

### `allNodes`

 All nodes that the reduction makes from `n` numbers of absolute value at most `U`.  The set of
values is split in all `2 (Lam (2U))²` ways by two binary digits, for the solutions with three
distinct values.  Two further three-set inputs are for the solutions that repeat a value.  The bound
on absolute values is `2U` throughout, because `twiceSet x` needs it. 

### `instances`

 **The whole reduction**: the list of one-array Convolution-3SUM instances made from `n` numbers
of absolute value at most `U`.  Each is read at length `8 * mPar n (2 * U) ^ 2`. 

### `scanPairs`

 **The count for the searches.**  Each node runs two searches, each search tries at most the
primes up to `m = mPar n (2 * U)`, and a trial can be decided from one remainder for each element of
the node's three sets (the library's lemma `ChanHe.coll_eq_sum`).  This is the total number of pairs
(candidate prime, element) if every search runs through all its candidates.  The definitions above
do not compute collision counts in this way (`coll` runs through all ordered pairs); the count is
for a program that would.

It is a count that we define, not a running time that we derive.  Each remainder counts as one,
whatever the size of the numbers.  The count leaves out the sieve for the primes, the sorting or
counting of the remainders, the acceptance tests of the searches, the extraction of the heavy
elements, the splitting of the input, the counting of repeated values, the computation of the
parameters, and the writing of the arrays. 

 ### Sizes for inputs of absolute value at most n ^ κ 

### `lenOf`

 The common length of the instances made from `n` numbers of absolute value at most `n ^ κ`. 

### `numBound`

 An upper bound on the number of instances made from `n ≥ 2` numbers of absolute value at most
`n ^ κ` (the library's lemma `ChanHe.length_instances_pow_le`). 

### `workBound`

 An upper bound on `scanPairs` for `n ≥ 2` numbers of absolute value at most `n ^ κ`: the product
of `numBound κ n` nodes, `2m` candidate primes for each node, and `3n` elements. 


## Section 3: statements

The claims of Section 3 of the paper, proved or cited there, that are
mathematics and not sentences about a machine.

* Theorem 17, everything but the running time: `Theorem_17`, with `Theorem_17_scanOrder_exists` (its
  hypothesis on the order of the scans can be met) and two pieces of arithmetic behind two terms of
  the additional time, `Theorem_17_hashing_sum_sq_le` and `Theorem_17_write_cost`.
* Remark 18 compares the instances of Theorem 17 with graphs of [VX20]. Stated is what the
  comparison says about the paper's own instance, namely which residues its edges and query pairs
  have: `Remark_18_block`.
* Remark 20: `Remark_20_balance`, `Remark_20_brute_force`.
* Theorem 21, which the paper cites from the literature without a proof: the correctness, the
  numbers and the sizes of the instances of the reductions, and the arithmetic behind the printed
  forms (stated for arbitrary functions, and not applied to the bounds of the reductions). Part (b):
  `Theorem_21b_repeated_squaring`, `Theorem_21b_entries_bounded`, `Theorem_21b_negative_to_exact`,
  `Theorem_21b_log_factors`. Part (a): `Theorem_21a_convolution_to_exact`, `Theorem_21a_compose`,
  and, for the reduction that the paper cites from Chan and He,
  `Theorem_21a_threeSum_to_convolution` and `Theorem_21a_threeSum_to_exact`.
* Definitions 13 and 14 are rendered by definitions. Corollaries 15 and 16 and Theorems 19 and 22
  are sentences about running time; they are stated about programs (`Items.Corollary_15` to
  `Items.Theorem_22_threeSum`).

Not stated here:

* The running time of the reduction of Theorem 17, the time bound of Theorem 21(a), and Theorem
  21(b) in its printed form ("If a deterministic algorithm solves Exact Triangle [...] in time T(s)
  [...], then [...]") have no statement.
* [VW18, Theorem 4.2] has no mathematical statement.
* Remark 23, where the paper indicates the method in one sentence and gives no proof, and
  footnote 9.
* The other sentences inside proofs, and unnumbered claims, are lemmas of the library or are not
  formalized.

`docs/INDEX.md` says for each item of the paper what is stated and what is not. `docs/REMARKS.md`,
"Section 3: running times" and "Section 3: cited results", has the details.

Hypotheses that are added or changed are marked NOTE and listed in `docs/REMARKS.md`, "Section 3:
differences".  Lower bounds that only exclude empty or degenerate cases (`1 ≤ N`, `1 ≤ U`, `0 ≤ U`,
`2 ≤ n`, `0 ≤ κ`, `0 ≤ τ` in the statements for Theorem 21) carry no NOTE.


 ### 3.2 A deterministic reduction from Exact Triangle to Lop-AE-SparseTri 

 #### Theorem 17, first step: hashing modulo a prime 

### `Theorem_17_hashing_sum_sq_le`

 Proof of Theorem 17: "each of them O(p²) word operations, so n^{ω+o(1)} D^{3/2} time over the
fewer than √D primes in the range": the sum of `p²` over the primes in the range is at most
`D^{3/2}`.  Only this sum is stated.  That the counts are read off a product of matrices over
ℤ[x]/(x^p − 1) (proof of Theorem 17) is a lemma of the library. 

 #### Theorem 17, second step: the instances 

### `Theorem_17_write_cost`

 Proof of Theorem 17: "Writing them down costs O(n² D g): the two bipartite graphs of an instance
have O(nD) entries".  The two biadjacency matrices of an instance have `2nD` entries, and there are
at most `4ng` instances.  The statement is arithmetic on the number of instances: `2nD` is a number
here, not the size of an object.  The query pairs are not counted; the paper goes on "and the chunks
are computed once and shared by the pieces".

NOTE.
* `g ≤ √D` is not needed.
* `p` is any prime of the range, selected or not. 

 #### Theorem 17, third step: witnesses 

### `Theorem_17_scanOrder_exists`

 Proof of Theorem 17: the accepted pairs can be put in some order, so the statements about every
order of the scans are not empty. 

### `Theorem_17`

 **Theorem 17** (Exact Triangle to Lop-AE-SparseTri, deterministically), everything
except the running time: "Let 16 ≤ D ≤ n, and let 1 ≤ g ≤ √D be an integer.  Exact Triangle on n
vertices per part with weights of absolute value at most n^ν reduces deterministically to at most
4ng instances of Lop-AE-SparseTri(n, D), each with at most n²/√D query pairs [...].  The reduction
is non-adaptive: it produces all the instances before it makes any oracle call".

The reduction is defined step by step as in the proof: a selected prime `p`, the instances
`T.lopInstance D g p ι` for `ι ∈ T.instanceIndices D g p`, and the scans `T.runScans D g L` of the
accepted pairs in any order `L`.  Non-adaptivity is visible in the statement: the instances do not
depend on `ans`.  The answer is that of the search version (Section 3.2): a zero triangle, or the
report that there is none.  The last clause bounds the number of scans times the size of a piece, an
upper bound on the number of triples that the scans look at; this count is behind the term
`O(ν n³ log n/g)` of the additional time (`κ` is the paper's ν).  Its constant `C` depends on
nothing. Arithmetic behind the other two terms is in `theorem_17_hashing_sum_sq_le` and
`theorem_17_write_cost`.  For the time itself see `docs/REMARKS.md`, "Section 3: running times".

NOTE.  The paper does not say that `D` is an integer; here it is a natural number, as in every use
of the theorem, and the bound on the number of chunks uses this (see the library's lemma
`TriangleInstance.totalChunks_le`). 

### `Remark_18_block`

 **Remark 18**: "With residues in place of their intervals, the block C_k × {−j} of our
instance for ϱ and C_k is their graph G_{−ϱ−j,j,ϱ}, and our instance puts the p graphs with the same
ϱ side by side."  The half of the sentence that is about our instance: a middle vertex `(c, σ)` with
`σ ≡ −j` is adjacent to `a` exactly if `w(a,c) ≡ −ϱ − j` and to `b` exactly if `w(b,c) ≡ j`, while
the query pairs have `w(a,b) ≡ ϱ`; these three residues, in this order, are the index of the graph.
The instance has the index `(ϱ, i, k)`: residue, chunk, piece.  The comparison with the graphs of
[VX20] is not formalized. 

 ### 3.3 Exact Triangle in truly subcubic time

Theorem 19 is a statement about running time: `Items.Theorem_19`.
Stated here: Remark 20. 

### `Remark_20_balance`

 **Remark 20**: "With g = D^η and a saving D^γ per instance, the instances cost n³
D^{η−γ} and the scans n³ D^{−η} [...].  They balance at η = γ/2": the larger of the two exponents
`η − γ` and `−η` is smallest, namely `−γ/2`, exactly at `η = γ/2`. 

### `Remark_20_brute_force`

 **Remark 20**: "With the straightforward algorithm (O(n²/g) per instance, since every
vertex of A has O(√D/g) neighbors in the middle part) the reduction recovers the brute-force bound
n³": `n²/√D` query pairs times `⌈s/g⌉` neighbors is at most `2n²/g`, and `4ng` instances at `2n²/g`
each come to `8n³`.  (That a vertex of `A` has at most `⌈s/g⌉` neighbors in the middle part is the
library's lemma `TriangleInstance.ncard_nbr_lopInstance_le`.)  The paper adds "up to a logarithmic
factor".  The cost of the instances has no such factor; the term ν n³ log n/g of Theorem 17, for the
scans, has one.  Only the cost of the instances is treated here. 

 ### 3.4 3SUM and APSP reduce to Exact Triangle

Theorem 22 is a statement about running time (`Items.Theorem_22_first`, `Items.Theorem_22_second`,
`Items.Theorem_22_threeSum`).  Theorem 21 is cited from the literature, part (a) from [CH20, VW13]
and part (b) from [VW10, VW18, VW13], and the paper gives no proof.  The route taken here:

* for (a), from 3SUM to Convolution-3SUM [CH20, Theorem 5.1], and from there to Exact Triangle
  [VW13, Theorem 4.3];
* for (b), from Negative Triangle to Exact Triangle [VW13, Theorem 3.3], from the (min,+)-product to
  Negative Triangle [VW18, Theorem 4.2], and from APSP to the (min,+)-product by repeated squaring.

Stated here: the parts of this route that are mathematics, among them the combinatorial content of
the two reductions of [VW13]. 

### `Theorem_21b_repeated_squaring`

 For **Theorem 21(b)**, repeated squaring: if no closed walk has negative weight, then squaring
the weight matrix `⌈log₂ n⌉` times in the (min,+)-product yields the distance matrix.
(`Nat.clog 2 n` is `⌈log₂ n⌉`.)  Stated for weights in any linearly ordered commutative group, so
that it covers integer and real weights. 

### `Theorem_21b_entries_bounded`

 For **Theorem 21(b)**, repeated squaring: a bound on the entries.  If the edge weights have
absolute value at most `U`, every finite entry of every matrix of the repeated squaring has absolute
value at most `nU`; with `U = n^ν` this is `n^{ν+1}`.

NOTE.  A missing edge has the weight `⊤` here, while the (min,+)-product of Theorem 21(b) is on
integer matrices with entries of absolute value at most `U` (`IsMinPlusProduct`).  Nothing is stated
here about replacing `⊤` by a large number. 

### `Theorem_21b_log_factors`

 For **Theorem 21(b)**: the logarithmic factors.  Let `τ` be the time of Exact Triangle and `τ'`
that of Negative Triangle, both on `n^{1/3}` vertices per part.  With `τ' = O(τ log U)`, the bound
`O(n² τ' log U)` of [VW18, Theorem 4.2] becomes `O(n² τ log² U)`, and `⌈log₂ n⌉` products with
`U = n^{κ+1}` cost `O(n² τ log³ n)`.  Here `κ` is the paper's ν, and `τ` stands for the `T(n^{1/3})`
of Theorem 21(b); `τ` and `τ'` are arbitrary numbers, so the statement is arithmetic only.

NOTE.
* Both halves are stated for `U = n^{κ+1}`, the first one too.
* The condition that T(s)/s is nondecreasing, and the like condition of [VW18, Theorem 4.2], do not
  occur. 

### `Theorem_21b_negative_to_exact`

 The combinatorial content of [VW13, Theorem 3.3] in the form needed for **Theorem 21(b)**:
whether an instance with weights in `[−U, U]` has a negative triangle is decided by asking
`O(log U)` times whether there is a zero triangle, each time after changing the weights, edge by
edge, to numbers of absolute value `O(U)`.  The instances are obtained from the given one by
applying to each weight a function that depends only on `U`, on the number of the instance and on
which of the three parts' pairs the edge joins.  There are at most `2⌊log₂ U⌋ + 6` of them, and
their weights are at most `6U` in absolute value. 

### `Theorem_21a_convolution_to_exact`

 The combinatorial content of [VW13, Theorem 4.3] in the form needed for **Theorem 21(a)**:
whether an array of `N` integers is a yes-instance of Convolution-3SUM is decided by asking `O(√N)`
times whether there is a zero triangle, each time in an instance with `O(√N)` vertices in each part
whose weights are entries of the array, up to sign, or a filler.  There are at most `2t` instances,
each with `t ≤ √N + 1` vertices in every part.  Each of their weights is a copy of some `±x_i`, at a
position `i` that does not depend on the numbers, or the filler `2U + 1`, where `U` bounds the
`|x_i|`. 

### `Theorem_21a_compose`

 For **Theorem 21(a)**: the arithmetic of the composition of the two reductions.  The first
reduction [CH20] takes time `E₁ = Õ(n^{3/2})` and produces `Num₁` arrays, polylogarithmically many,
of length `N = Õ(n)`; the second [VW13], on an array of length `N`, takes time `E₂ = N^{3/2+o(1)}`
and produces `Num₂ = O(√N)` instances with `size₂ = O(√N)` vertices in each part.  Together:
`n^{1/2+o(1)}` instances, each on `n^{1/2+o(1)}` vertices per part, in `n^{3/2+o(1)}` time, as
Theorem 21(a) says.  The six functions are arbitrary, so the statement is arithmetic only; it is not
applied to the bounds of the two reductions.

NOTE.  The hypothesis on `E₂` is what the time `n^{3/2+o(1)}` of Theorem 21(a) asks of the second
reduction. 

 #### Theorem 21(a): the reduction from 3SUM to Convolution-3SUM, after Chan and He

The first step towards Theorem 21(a), after [CH20, Theorem 5.1]: from n integers bounded by a power
of n, a deterministic reduction computes polylogarithmically many arrays of length Õ(n), whose
entries are again bounded by a power of n, in Õ(n^{3/2}) time; three of the integers sum to 0
exactly if one of the arrays is a yes-instance of Convolution-3SUM.

The namespace `ChanHe` defines a reduction of this kind, as a function from inputs to lists of
instances, in two versions: `ChanHe.reduction` for three sets and three arrays, and
`ChanHe.instances` for n numbers and one array.  Nothing is stated here about `ChanHe.reduction`.

Nothing here is about a machine. That the functions can be evaluated deterministically in n^(3/2)
polylog n time on a word RAM is not stated. Theorem 5.1 of [CH20] as printed is a statement about
running times, so it is not stated here. The easy converse reduction, from Convolution-3SUM to
3SUM, is not treated. 

### `Theorem_21a_threeSum_to_convolution`

 The reduction from 3SUM to Convolution-3SUM in the form needed for **Theorem 21(a)**.  The list
of instances may depend on the input, so a statement that such a list exists would be true for
trivial reasons.  The statement is therefore about the explicitly defined function
`ChanHe.instances`, and it is to be read together with the definitions of the namespace `ChanHe`.

What is stated: the input (`n ≥ 2` integers of absolute value at most `n^κ`, for a natural number
`κ`, the ν of Theorem 21, to which a real exponent can be rounded up; 3SUM asks for three numbers at
different positions), the number of instances, `(log n)^{O(1)}` (at most `ChanHe.numBound κ n`),
their length, `Õ(n)` (`ChanHe.lenOf κ n`, the common length), the absolute value of their numbers,
`n^{O(1)}` (at most `120 n^κ + 40`), and the one-array problem.

What is not stated: that the reduction is deterministic and takes `Õ(n^{3/2})` time.  This is about
a machine, and nothing here is about a machine.  In its place stands `ChanHe.scanPairs`, the number
of pairs (candidate prime, element) that the searches for the moduli go through.  It is a count that
we define, not a running time that we derive. It is at most `ChanHe.workBound κ n`, which is
`n^{3/2}` times a polylogarithm.

NOTE.
* `κ` is a natural number.
* Theorem 5.1 of [CH20] is a statement about running times, for 3SUM on three sets and
  Convolution-3SUM on three arrays.  The reduction stated here, with its count of instances, their
  length and the Õ(n^{3/2}), follows the proof of that theorem, and passes to `n` numbers and to one
  array by elementary devices; see `docs/REMARKS.md`, "Section 3: cited results". 

### `Theorem_21a_threeSum_to_exact`

 The two reductions of **Theorem 21(a)** composed.  For `n ≥ 2` put
`N = ChanHe.lenOf κ n`. There are `t ≤ √N + 1` and at most `2t` templates such that, for every input
`x` of `n` integers of absolute value at most `n^κ`: the list `ChanHe.instances n (n^κ) x` has at
most `ChanHe.numBound κ n` arrays; each template turns each array into an instance of Exact Triangle
on `t` vertices per part, with the filler weight `240 n^κ + 81` and all weights of absolute value at
most that; and three entries of `x` at different positions sum to 0 iff one of these instances has a
zero triangle.

So there are at most `2t · ChanHe.numBound κ n` triangle instances.  As above, `κ` is a natural
number; it is the paper's ν.

What is not stated.  The words "deterministically, in n^{3/2+o(1)} time" are about a machine, and
nothing here is about a machine. The forms `n^{1/2+o(1)}` of Theorem 21(a) for the number of
instances and for `t` are not part of this statement: they follow from the bounds on `numBound` and
`lenOf` in `theorem_21a_threeSum_to_convolution` by the arithmetic of `theorem_21a_compose`, but
this last step is not carried out here.  No lower bound on `t` is stated, so the weights are not
bounded by a power of the number of vertices, which is the form in which Theorem 19 takes them. 


## Section 4: definitions

Definitions used by the statements of Section 4, "The matrix theorem in general: a data structure".
They follow the paper's order and names, with three exceptions: `Cube.starsToP0`, from the proof of
Lemma 29, stands with the cubes of Section 4.2; `epsStar`, from Section 4.1, stands with `Rc`; and
the definitions for Table 2, which is printed in Section 4.1, come last. Every notion of Section 2
(terms, leaves, output strings, inner sets, private leaf, order, `α_d`, `β_d`, `Φ_τ`, `Ψ_τ`) is the
one defined for Section 2 and is not redefined.

Conventions, in addition to those of the definitions of Section 2.

* Table 1: `m` and `L` are natural-number variables, and `D = 4^m`, `N₀ = 3^{L-m}`,
  `K = binom(L, m)`, `M = K N₀²`, `α_d`, `β_d` are `D m`, `N0 L m`, `K L m`, `M L m`, `alpha m d`,
  `beta L m d` of Section 2. The remaining rows of Table 1: `ρ` is `rho L m`, and `γ`, `q`, `R_c(γ)`
  are `gammaOf c θ`, `qOf θ`, `Rc c γ`, all defined below; the switching order is a natural number
  `t`, and the ratio `c`, `ε` and `κ` are real numbers.
* "we say that level ℓ is lower than level ℓ' if ℓ < ℓ'" (Section 4): levels are compared in the
  order of `Fin L`.
* An output string is `η` in the Lean text; the paper writes w.
* The paper fixes `0 ≤ t ≤ m` (Section 4.2) and `L ≥ 10m` (Section 4). The definitions below make
  sense for all natural numbers; the statements carry `t ≤ m` and `10 * m ≤ L` as explicit
  hypotheses where they are needed. `m - t` is subtraction of natural numbers, which is the ordinary
  difference because `t ≤ m`.


 ### Notions from Section 2 

### `productAt`

 Section 4: "For a leaf τ of a tile with input arrays a and b, we call Φ_τ(a) Ψ_τ(b) the product
at τ." 

 ### 4.2 Boxes 

### `CubeSymbol`

 Section 4.2: the symbols of a cube, "each of which is one of the ten terms of Schönhage's
identity or a star ∗". 

### `Cube`

 Section 4.2: "A cube is a string π = π₁ ⋯ π_L of L symbols, each of which is one of the ten
terms of Schönhage's identity or a star ∗." 

### `Cube.HasLeaf`

 Section 4.2: "Its leaves are the leaves obtained by replacing each star by any of the ten
terms". So `τ` is a leaf of `π` if at every level `π` has a star or has the term of `τ`. 

### `Cube.leaves`

 Section 4.2: the set of the leaves of a cube. 

### `Cube.starLevels`

 The set of levels at which a cube has a star. 

### `Cube.P0Levels`

 The set of levels at which a cube has the symbol `P₀`. 

### `Cube.val`

 Section 4.2: "The value of a cube π is the sum of the products at its leaves,
val(π) := ∑_{τ a leaf of π} Φ_τ(a) Ψ_τ(b)." 

### `IsBox`

 Section 4.2: "A box is a cube π = π₁ ⋯ π_L such that (i) at most m - t of its symbols are P₀ or
stars, and (ii) every star is at a lower level than every P₀." 

### `lowest`

 The `k` lowest levels of `S` (Section 4.2 and Lemma 27: "the m - t - |Z| lowest levels of Q ∖
Z"): the levels of `S` with fewer than `k` levels of `S` below them. (All of `S` if `S` has at most
`k` levels.) 

### `Cube.starsToP0`

 Proof of Lemma 29: "the leaf we get by replacing its stars with P₀". 

### `Vof`

 Section 4.2: "V := Z ∪ {the m - t - |Z| lowest levels of Q ∖ Z} (Z padded from the bottom)". 

### `FV`

 Section 4.2: "F_V := {ℓ ∈ Q : ℓ < min(Q ∖ V)} (the levels that we have not reached)", and "We
define F_V by the same formula for every V ⊆ Q, with F_V := Q if V = Q." The condition "ℓ < min(Q ∖
V)" is written as "ℓ is below every level of Q ∖ V", which also gives the convention `F_V = Q` when
`Q ∖ V` is empty. (That this agrees with the paper's formula in both cases is the library's lemma
`FV_eq`.) 

### `BV`

 Section 4.2: "For V ⊆ Q with |V| = m - t, let 𝓑_V be the set of the 9^t cubes π with π_ℓ = ∗ if
ℓ ∈ F_V, P₀ if ℓ ∈ V ∖ F_V, one of the nine terms P_ij if ℓ ∈ Q ∖ V, the term P_ij with w_ℓ = z_ij
if ℓ ∉ Q", where `Q` is the inner set of the output string w, here `η`. The term of the last case is
the term of the private leaf of `η` (so the caption of Figure 10: "at every other level, they have
the term of the private leaf of w"). The boxes in these sets are "the boxes of w". 

### `Vsets`

 Lemma 28: the index set of the union and of the sum, "all V ⊆ Q with |V| = m - t". 

### `lowLeaves`

 Lemma 28: the leaves "τ contributing to w of order < t". 

### `querySum`

 The right-hand side of the equation of Lemma 28: "∑_{τ contributing to w, of order < t} Φ_τ(a)
Ψ_τ(b) + ∑_{V ⊆ Q, |V| = m - t} ∑_{π ∈ 𝓑_V} val(π)". It is what a query computes in its steps (2)
and (3) (Section 4.3): "Add up the products at the leaves of order below t contributing to w", "Add
to this the values of the α_t boxes of w". 

 ### 4.3 The data structure, in terms of the parameters 

### `boxes`

 The set of all boxes (of a tile), for the parameters `L`, `m`, `t`. 

### `boxesWithStars`

 "the boxes with e stars" (proof of Lemma 29, which computes "the values of the boxes in
increasing order of their number of stars"). 

### `Cube.replace`

 Proof of Lemma 29: "the ten strings π[ℓ ← λ] obtained by replacing that star by a term λ". 

### `dpValue`

 The dynamic program of Lemma 29 (proof, "The values"), which computes the value of a box with
`e` stars from the two encodings of the tile, `encA τ = Φ_τ(a)` and `encB τ = Ψ_τ(b)`: "The boxes
without stars are the leaves with at most m - t symbols P₀, and the value of each of them is the
product of its two numbers in the encodings. For a box π with e ≥ 1 stars, let ℓ be the highest
level at which π has a star. […] Hence we compute val(π) = ∑_λ val(π[ℓ ← λ]) with ten lookups in the
trie". A cube without stars is the leaf `Cube.starsToP0 π`. (The last case, a cube without stars
when `e ≥ 1`, does not occur for a box with `e` stars.) `dpValue` is the recurrence of this dynamic
program, not a program with a trie: where the paper looks a value up, `dpValue` computes it
again. 

### `rho`

 The decay rate of the `β_d` (Table 1, and Section 4.3): "ρ := 9m / (L - m + 1)". 

### `cost8`

 The expression inside the `O(·)` of (8) (preprocessing time and space of Theorem 30):
"L m ρ^t/(1 - ρ) N² + N · 10^L / (√K N₀)". 

### `costQuery`

 The expression inside the `O(·)` of the query time of Theorem 30:
"L ∑_{d=0}^{t} α_d". 

### `cost9`

 The expression inside the `O(·)` of (9), Theorem 30, for a set of `W` positions:
"L |W| ∑_{d=0}^{t} α_d + L m ρ^t/(1 - ρ) N² + N · 10^L / (√K N₀)". The paper labels the three terms
"queries", "boxes" and "encodings". 

 ### 4.4 Choosing the parameters 

### `padInnerCols`

 Proof of Corollary 26: "pad the inner dimension to 4^m < 4D with zero columns of X". The padded
matrix has `D'` columns. This is a padding if `D₀ ≤ D'`; for `D' < D₀` the function drops the last
columns. 

### `padInnerRows`

 Proof of Corollary 26: "and zero rows of Y".  The padded matrix has `D'` rows.  This is a
padding if `D₀ ≤ D'`; for `D' < D₀` the function drops the last rows. 

### `entropy`

 Section 4.4: "let H(x) := -x ln x - (1 - x) ln(1 - x) be the entropy function (with natural
logarithms)". (Lean's `Real.log 0 = 0` gives `H(0) = H(1) = 0`, the usual convention.) 

### `lnΛ`

 The denominator of equation (11), which the paper calls `ln Λ`:
`c ln 10 - (1/2) c H(1/c) - (c - 1) ln 3 + γ ln 4`, where "Λ := 10^c e^{-(1/2) c H(1/c)} 3^{-(c-1)}
4^γ" (Section 4.4). 

### `Rc`

 Equation (11): "R_c(γ) := ln 4 / ln Λ". 

### `epsStar`

 Section 4.1: "Let ε* := ln 4 / (5 ln 10)". 

### `rhoC`

 Corollary 31: "ρ_c := 9/(c - 1)". 

### `gammaOf`

 Corollary 31: "γ := θ ln(1/ρ_c) / ln 4". 

### `qOf`

 Corollary 31: "q := (H(θ) + θ ln 9) / ln 4". 

### `levelsOf`

 Table 1: "L and t are cm and θm rounded up to integers"; the proof of Corollary 31: "L := ⌈cm⌉".
(Only `L` gets a name here.) 

 #### Table 2 

### `ValidQueryEntry`

 What the caption of Table 2 claims for a number `γ₀` of the left half, in the row of `c` and `ε`
and the column of `q` ("a value γ for which Theorem 24 holds, meaning that after O(N² log² D/D^γ)
preprocessing, a query takes O(D^q log D) time", "whenever D ≤ N^ε"), as a consequence of Corollary
31: the corollary applies to `c`, some `θ ∈ (0, 0.9)` and `ε`, its `q` is at most the `q` of the
column, and its `γ` is at least `γ₀`. 

### `ValidDensityEntry`

 What the caption of Table 2 claims for a number `γ₀` of the right half, in the row of `c` and
`ε` and the column of `κ` ("a value γ for which Theorem 25 holds, meaning that any |W| ≤ N²/D^κ
wanted entries take O(N² log² D/D^γ) time"), as a consequence of Corollary 32: the corollary applies
to `c`, some `θ ∈ (0, 0.9)`, `ε` and `κ`, and its exponent `min{γ, κ - q}` is at least `γ₀`. 

### `Table2Query`

 How the left half of Table 2 is computed. Section 4.4, on Corollary 31: "which we use for the
left half of Table 2, with the c of the row and the θ that gives the q of the column"; the caption:
"We round all values down" (to four decimals); and the `ε` of the row is below `R_c(γ)`. 

### `Table2Ninth`

 How the column `q = 0.43` of Table 2 is computed: "(θ = 1/9 for q = 0.43)" (Section 4.4). As in
the other columns, the entry is rounded down to four decimals, and the `ε` of the row is below
`R_c(γ)`. 

### `Table2Density`

 How the right half of Table 2 is computed. Section 4.4, on the exponents of Corollary 32: "which
we use for the right half of Table 2, with the θ at which γ = κ - q". The entry is this `γ`, rounded
down to four decimals, and the `ε` of the row is below `R_c(γ)`. 

### `Table2Row`

 A row of Table 2.  The arguments stand in the order in which the row is printed: the
ratio `c`, the exponent `ε`, the six values of `γ` in the columns
`q = 0.10, 0.25, 0.43, 0.50, 0.75, 0.90` and the five values of `γ` in the columns
`κ = 0.10, 0.25, 0.50, 0.75, 1.00`.  Each entry is computed as Section 4.4 prescribes, is rounded
down to four decimals, and has `ε < R_c(γ)`. 

### `Table2Row.q043`

 The entry of the column `q = 0.43`, which uses `θ = 1/9`. 

### `Table2Row.eps`

 Section 4.4: "The ε of a row of the table is the smallest R_c(γ) over its entries." The
  caption: "We round all values down". The fields above give `ε < R_c(γ)` at every entry; this field
  gives the other half, that the smallest `R_c(γ)` of the row is below `ε + 0.001`, by exhibiting
  the entry of the column `q = 0.90` (which need not be the smallest: in the rows `c = 15, 12, 10.5`
  the smallest is in the column `κ = 1.00`). 


## Section 4: statements

The claims of Section 4 of the paper, "The matrix theorem in general: a data structure", that are
mathematics and not sentences about a machine. `docs/INDEX.md` says for each item of the paper what
is stated and what is not. The places where the Lean text differs from the wording of the paper are
collected in `docs/REMARKS.md`, "Section 4: differences".

The order is the paper's, with these exceptions. Figure 10 and `Lemma_28_boxes` come after Lemma 28.
`Eq_10`, from the proof of Corollary 31, stands with equation (10). `Sec4_epsStar_numeric` (Section
4.1) and `Sec4_Rc_lt_epsStar` (Table 1) stand with the clauses of Corollary 31 on ε*. The statements
on Table 2, `Table_1_section_2_column` and `Corollary_26_W` come at the end.

* Sentences about running time and space are sentences about a machine. Those of Theorems 24, 25 and
  30 and of Corollaries 26, 31 and 32 are stated about programs: `Items.Theorem_24` to
  `Items.Corollary_32`. The bound of the second sentence of Lemma 29 ("in O(L) time and space per
  box") has no statement; Theorem 30 about programs has its consequence, the first term of (8).
* Expressions (8) and (9) are the definitions `cost8` and `cost9`. Equation (11) is the definition
  `Rc`.
* Figure 9 draws the cube and the boxes of one output string in a small example (L = 3, t = 1).
  Nothing is stated for it.
* No statement says that q increases with θ on (0, 0.9), or that there is only one θ with
  γ = κ - q. So "the θ that gives the q of the column" and "the θ at which γ = κ - q" (Section 4.4)
  are rendered by "some θ with ..." in `Table2Query`, `Table2Density` and the field `eps` of
  `Table2Row`.
* The standing assumptions of the section, `0 ≤ t ≤ m` (Section 4.2) and `L ≥ 10m` (Section 4),
  appear as the explicit hypotheses `t ≤ m` and `10 * m ≤ L` in the statements that need them. "As
  in Section 2.4.3, all output strings in this section have inner sets of exactly m elements"
  (Section 4) is the hypothesis `(innerSetO η).card = m`.
* An output string is `η` in the Lean text; the paper writes w.
* `D m = 4 ^ m` is the paper's `D` after "from now on D = 4^m" (the proof of Corollary 26). The
  inner dimension of the given matrices, before it is padded to a power of four, is written `D₀`.
* Where a statement renders an `O(·)`, it has an explicit constant and an explicit order of
  quantifiers, and the docstring says how the sentence was read.


 ### 4.2 Boxes 

### `Lemma_27`

 **Lemma 27**. "Let Q be a set of m levels, and let 0 ≤ t ≤ m. For every Z ⊆ Q
with |Z| ≤ m - t, there is exactly one set V ⊆ Q with |V| = m - t and V ∖ F_V ⊆ Z ⊆ V, namely Z
together with the m - t - |Z| lowest levels of Q ∖ Z." This set is `Vof m t Q Z`. 

### `Lemma_28_leaves`

 **Lemma 28**, first sentence, first half. "Let w be an output string, with inner set
Q. The leaves of order at least t contributing to w are exactly the leaves of the boxes in ⋃_V 𝓑_V,
the union over all V ⊆ Q with |V| = m - t". 

### `Lemma_28_unique`

 **Lemma 28**, first sentence, second half: "and each of them is a leaf of exactly one
of these boxes." 

### `Lemma_28`

 **Lemma 28**, the displayed equation. "Hence (X_Q Y_Q)[w] = ∑_{τ contributing to w, of
order < t} Φ_τ(a) Ψ_τ(b) + ∑_{V ⊆ Q, |V| = m - t} ∑_{π ∈ 𝓑_V} val(π)", for the input arrays `a`, `b`
built from the matrices `X_Q`, `Y_Q` as in Section 2.3.3. The right-hand side is `querySum`. 

### `Lemma_28_counts`

 **Lemma 28**, last line: "a sum of ∑_{d=0}^{t-1} α_d products and α_t values of
boxes."  The third clause says that these α_t cubes are different, that is, that the sets 𝓑_V are
disjoint; Section 4.2 has it in the words "w has exactly α_t boxes". 

### `Lemma_28_boxes`

 Section 4.2, on the cubes of 𝓑_V, which Lemma 28 calls "the boxes in ⋃_V 𝓑_V": "Every cube in
𝓑_V is a box: it satisfies condition (i) of the definition because it has |V| = m - t symbols P₀ or
stars, and condition (ii) because its stars are below its symbols P₀, since F_V is an initial
segment of Q."  Moreover "a box of 𝓑_V has stars at the levels of F_V", so it is one of the boxes
with |F_V| stars (`boxesWithStars`). 

### `Figure_10_counts`

 Figure 10, for `m = 4` and `t = 2`: "these 6 · 81 = 486 = α₂ boxes contain each of the
α₂ + α₃ + α₄ = 9963 leaves of order at least 2". 

### `Figure_10_rows`

 Figure 10, the six rows, with the four levels `ℓ₁ < ℓ₂ < ℓ₃ < ℓ₄` of `Q` taken as
`0, 1, 2, 3`: the levels of `F_V`, which carry the stars; and the column "leaves per box" adds up,
over the 81 boxes of each row, to `81 · (10² + 10 + 10 + 1 + 1 + 1) = 9963`. (Here 81 and the powers
of ten are numerals.) 

### `Figure_10_Vof`

 Figure 10, column "sets Z of its leaves": the row `V` in which each set `Z` of at most
one level appears. (A set `Z` of two levels appears in the row `V = Z`; these six cases are not
written out.) 

 ### 4.3 The data structure, in terms of the parameters 

### `Lemma_29_count`

 **Lemma 29**, first sentence.  "There are at most (m+1) ∑_{d=t}^{m} β_d boxes." 

### `Lemma_29_values`

 **Lemma 29**, second sentence, correctness: "Given the two encodings of a tile, we can compute
the values of all these boxes". The recurrence of the dynamic program of the proof (`dpValue`), run
on the two encodings, returns `val(π)` for every box `π` with `e` stars. That the ten strings π[ℓ ←
λ] are boxes with `e - 1` stars, so that their values can be looked up, is `lemma_29_split`. (For
the time and space bound see `docs/REMARKS.md`, "Section 4: running times".) 

### `Lemma_29_split`

 Proof of **Lemma 29**, "The values": "For a box π with e ≥ 1 stars, let ℓ be the highest
level at which π has a star. [...] each of these strings is again a box, with e - 1 stars."  The
strings are the `π[ℓ ← λ]`, and `e + 1` stands for the paper's `e`. 

 #### The decay rate ρ and equation (7) 

### `Sec4_rho_lt_one`

 Section 4.3: `ρ = 9m/(L-m+1)` "is less than 1 since L ≥ 10m". 

### `Eq_7_ratio`

 Equation (7), first half: for `1 ≤ d ≤ m`,
`β_d / β_{d-1} = 9(m-d+1)/(L-m+d) ≤ 9m/(L-m+1) = ρ`. 

### `Eq_7`

 Equation (7), second half: "so β_d ≤ ρ^d M" (for `0 ≤ d ≤ m`). 

 ### 4.4 Choosing the parameters 

### `Eq_10_corollary_26`

 Equation (10), `D^γ · 10^L / (√K N₀) ≤ N`, where it is printed, in the proof of Corollary 26.
There `D = 4^m`, "L := 21m", "γ := ln(20/9)/(9 ln 4)", "K = binom(21m, m)", "N₀ = 3^{20m}", and "the
assumption N ≥ D^18 now reads N ≥ 4^{18(m-1)}". The inequality "holds whenever
1.63^m ≥ 4^18 √(21m+1), which is the case for all m ≥ 60". 

### `Eq_10`

 Equation (10), `D^γ · 10^L / (√K N₀) ≤ N`, with the parameters of Corollary 31, whose proof
says: "the inequality (10) thus holds once m exceeds a constant depending on c, θ, and ε". Here `D₀`
is the original inner dimension, `m = ⌈log_4 D₀⌉` (that is, `4^{m-1} < D₀ ≤ 4^m`), the `D` of (10)
is the padded `4^m`, `L = ⌈cm⌉`, `γ = θ ln(1/ρ_c)/ln 4`, and `D₀ ≤ N^ε` with `ε < R_c(γ)`. The
threshold `m₀` depends only on `c`, `θ`, `ε`. No hypothesis `ε > 0` is needed: for `ε ≤ 0` no
natural number `N` satisfies `2 ≤ D₀ ≤ N^ε`. 

### `Eq_11_iff`

 Equation (11) defines `R_c(γ) := ln 4/ln Λ` (the definition `Rc`, where `lnΛ c γ` is `ln Λ`).
The proof of Corollary 31 uses it in this form: "ε < R_c(γ) says that Λ < 4^{1/ε}".  Here `c ≥ 10`,
`γ ≥ 0`, and `ε > 0`, which the hypothesis 2 ≤ D ≤ N^ε of the corollary implies; for `ε ≤ 0`,
ε < R_c(γ) holds and Λ < 4^{1/ε} does not. 

 #### Corollary 31: the clauses that are not about time 

### `Corollary_31_gamma_pos`

 Corollary 31: "γ := θ ln(1/ρ_c)/ln 4 > 0". 

### `Sec4_Rc_strictAntiOn`

 Corollary 31: "R_c(0) increases [...] as c decreases to 10": the monotonicity.  It holds for
every fixed `γ ≥ 0`; the paper says it for `γ = 0` ("for γ = 0, ln Λ increases with c", proof of
Corollary 31). 

### `Sec4_Rc_zero_tendsto`

 Corollary 31: "Moreover, R_c(0) increases to ε* = ln 4/(5 ln 10) = 0.1204… as c decreases to
10": the limit. (The monotonicity is `sec4_Rc_strictAntiOn` at `γ = 0`.) 

### `Sec4_epsStar_numeric`

 Section 4.1: "Let ε* := ln 4/(5 ln 10) = 0.1204…". 

### `Sec4_Rc_lt_epsStar`

 Table 1, row `ε`: "R_c(γ) < 0.1204…", that is `R_c(γ) < ε*`, for `c > 10` and
`γ ≥ 0`. 

 #### Corollary 32 

### `Corollary_32_saving`

 Corollary 32: `N² log² D (D^{-γ} + D^{q-κ})` is "a saving of D^{min{γ, κ-q}}, up to logarithmic
factors, over the size N² of the product":
`D^{-min{γ,κ-q}} ≤ D^{-γ} + D^{q-κ} ≤ 2 D^{-min{γ,κ-q}}`. 

 #### Table 2, and the column of Table 1 on Section 2 

### `Table_2_query_valid`

 Caption of Table 2, left half: "the numerical entry is a value γ for which Theorem 24 holds,
meaning that after O(N² log² D/D^γ) preprocessing, a query takes O(D^q log D) time", "whenever
D ≤ N^ε". For an entry computed as Section 4.4 prescribes (`Table2Query`), Corollary 31 gives these
bounds (`ValidQueryEntry`). 

### `Table_2_ninth_valid`

 Caption of Table 2: "the column q = 0.43 uses the switching order t = m/9 of Section 2 (more
precisely, q = 0.4277…)". For an entry of this column, computed at `θ = 1/9` (`Table2Ninth`),
Corollary 31 gives the bounds of the caption with `q = 0.43`. 

### `Table_2_density_valid`

 Caption of Table 2, right half: "the numerical entry is a value γ for which Theorem 25 holds,
meaning that any |W| ≤ N²/D^κ wanted entries take O(N² log² D/D^γ) time". For an entry computed as
Section 4.4 prescribes (`Table2Density`), Corollary 32 gives this bound (`ValidDensityEntry`). 

 ##### The six rows of Table 2

Each statement has the numbers of a row in the order in which the paper prints them: the first line
has `c`, `ε` and the left half, the second line the right half. It says that every entry is computed
as Section 4.4 prescribes and is rounded down to four decimals, and that the `ε` of the row is below
`R_c(γ)` at every entry and is rounded down to three decimals. By `Table_2_query_valid`,
`Table_2_ninth_valid` and `Table_2_density_valid`, Corollary 31 or 32 then gives what the caption
claims for the entry. 

### `Table_2_c40`

 Table 2, the row `c = 40`. 

### `Table_2_c21`

 Table 2, the row `c = 21`. 

### `Table_2_c19`

 Table 2, the row `c = 19`. 

### `Table_2_c15`

 Table 2, the row `c = 15`. 

### `Table_2_c12`

 Table 2, the row `c = 12`. 

### `Table_2_c10_5`

 Table 2, the row `c = 10.5`. 

### `Table_2_larger_c`

 Caption of Table 2: "A larger c gives a larger γ but a smaller ε" (at a fixed `θ > 0`). A fixed
`θ` is a fixed column of the left half of the table: there `γ` increases with `c` and `R_c(γ)`
decreases. In the right half `θ` changes with `c`; for it the sentence is not stated. Nor is it
stated for the `ε` of a row, which is the smallest `R_c(γ)` over all entries of the row. 

### `Table_1_section_2_column`

 Table 1 (column "in Section 2"), Table 2's caption and Section 4.1: at `L = 19m` one has
"ρ < 1/2"; the bold entry `c = 19`, `θ = 1/9` is Theorem 5, "where γ = 1/18 = 0.0555…"; Theorem 5's
`ε = 1/18` is below `R_19(1/18)`; and "Theorem 5 is the entry c = 19, q = 0.43, applied to a set W
of N²/√D wanted entries (that is, κ = 1/2)", where the exponent `min{γ, κ - q}` of Corollary 32 is
still `1/18`. 

 #### Corollary 26 

### `Corollary_26_W`

 Corollary 26: `|W| D^{0.437} + N²/D^{0.063}` "is O(N²/D^{0.063}) whenever |W| ≤ N²/√D"
(with constant 2).

NOTE.  The paper states no lower bound on `D`; `D ≥ 1` is assumed, as in `Items.Corollary_26`. 


## Section 5: definitions

Definitions used by the statements about Section 5, in the paper's order. Only what the statements
need is defined: blocks of matrices (5.1, 5.2, 5.4), comparison counts, the two counting
problems, and the construction of Lemma 37 (5.2), and the three hinted matrix-vector problems with
the conjectures about them (5.4). The definitions of 5.4 are used by the statements about programs.
The weighted `k`-Clique problems of 5.3 are `EndStatement.ZeroWeightKClique`,
`WordRam.MinKClique` and `WordRam.MaxKClique`.

Conventions.

* The paper numbers indices from 1; Lean's `Fin n` starts at 0.
* The paper treats n^μ, n/d, n/t₂ as integers.  Here a matrix that is cut into `b` blocks of `m`
  consecutive rows has `b * m` rows, and row `i` of block `p` is row `p * m + i`, which is
  `finProdFinEquiv (p, i)`.  The arithmetic of Theorem 35 has `d = ⌊n^{1/40}⌋` and the real quotient
  `n/d`; nothing is stated about cutting into blocks of `d` when `d` does not divide `n`.
* Definitions shared with Section 3 (`TriangleInstance`, `IsMinPlusProduct`, ...) and Section 4
  (`epsStar`, `padInnerCols`, `padInnerRows`) stand with the definitions of these sections.


 ### Blocks of consecutive rows and columns (used in 5.1, 5.2 and 5.4) 

### `blockOfRows`

 Proof of Theorem 34: "Cut the n × n^μ matrix into n^{1-μ} blocks of n^μ consecutive
rows". Also the proof of Lemma 36 ("blocks B' ... of d consecutive rows") and the proof of Corollary
40 ("Cut the n rows of U into n/t₂ blocks of t₂ rows"). `blockOfRows A p` is block number `p`: its
row `i` is row `p * m + i` of `A`. 

### `blockOfCols`

 Proof of Theorem 34: "and the n^μ × n matrix into n^{1-μ} blocks of n^μ consecutive
columns". Also the proof of Lemma 36 ("cut A into n/d blocks A' ... of d consecutive columns").
`blockOfCols B q` is block number `q`: its column `j` is column `q * m + j` of `B`. 

 ### 5.2 Comparison counts 

### `Cmp`

 Lemma 36: "A comparison count may have ≤ in place of <."  `Cmp.lt` is the version with `<`,
`Cmp.le` the version with `≤`. 

### `Cmp.Holds`

 Lemma 36.  The comparison itself: `x < y`, or `x ≤ y`. 

### `Lists`

 Section 5.2, "Comparison counts": "We are given n row lists: for every r ∈ [n], a list R_r of at
most d real numbers x, where each x ∈ R_r has a color χ(x) ∈ [d] associated with it.  Similarly, we
are given n column lists: for every c ∈ [n], a list C_c of at most d real numbers y, each y ∈ C_c
again with a color χ(y) ∈ [d]". An entry of a list is the pair (number, color).  The bound "at most
d" is the separate predicate `Lists.Valid`.

NOTE.  The color belongs to the entry (the place in the list), not to the real number: the same
number may occur twice in a list, and the two occurrences are counted separately. 

### `Lists.row`

 the row lists R_r 

### `Lists.col`

 the column lists C_c 

### `Lists.Valid`

 Section 5.2: every list has "at most d" numbers. 

### `RowItem`

 Section 5.2.  A number of a row list: the row `r` and a place in the list R_r. 

### `ColItem`

 Section 5.2.  A number of a column list: the column `c` and a place in the list C_c. 

### `Item`

 Section 5.2.  A number of any of the lists. 

### `Item.val`

 Section 5.2.  The real number at an item. 

### `Item.color`

 Section 5.2.  The color χ of an item. 

### `Item.ofRow`

 Section 5.2.  A number of a row list, as a number of one of the lists. 

### `Item.ofCol`

 Section 5.2.  A number of a column list, as a number of one of the lists. 

### `rowItem`

 Section 5.2.  The number at place `i` of the row list R_r. 

### `colItem`

 Section 5.2.  The number at place `i` of the column list C_c. 

### `comparisonCount`

 Section 5.2: "γ(r,c) := |{(x,y) : x ∈ R_r, y ∈ C_c, χ(x) = χ(y), x < y}|" (with `≤` for
`Cmp.le`). The pairs are pairs of places in the two lists. 

 #### The objects in the proof of Lemma 36 

### `IsPredecessor`

 Proof of Lemma 36, [CVX22, Problem 3.2]: "find, for every (i,j), the predecessor and the
successor of C[i,j] among the d sums A'[i,k] + B'[k,j], where a sum equal to C[i,j] counts as its
predecessor". `IsPredecessor sums c v`: the value `v` is the predecessor of `c` among the numbers
`sums k`, that is, the largest of them that is at most `c`. 

### `IsSuccessor`

 Proof of Lemma 36, [CVX22, Problem 3.2], see `IsPredecessor`.  `IsSuccessor sums c v`: the value
`v` is the successor of `c` among the numbers `sums k`, that is, the smallest of them that is larger
than `c`. 

### `listOf`

 Proof of Lemma 36.  The elements of a subset `S ⊆ [d]`, listed in increasing order. 

### `count41`

 Proof of Lemma 36, the counting problem [CVX22, Problem 4.1]: "we are given a pivot k_ij ∈ [d]
for every (i,j) ∈ [n]² and a subset S ⊆ [d], and we must count, for every (i,j), the indices k' ∈ S
with A'[i,k'] + B'[k',j] < A'[i,k_ij] + B'[k_ij,j]; a call of the problem may also have ≤ in place
of <." 

### `pairs41`

 Proof of Lemma 36: "we group the pairs by their pivot, P_k := {(i,j) : k_ij = k}". 

### `lists41`

 Proof of Lemma 36: "For k ∈ [d], let the row list R_i consist of the numbers A'[i,k'] - A'[i,k],
k' ∈ S, each with color k', and let the column list C_j consist of the numbers B'[k,j] - B'[k',j],
k' ∈ S, again with color k'." 

### `count45`

 Proof of Lemma 36, the counting problem [CVX22, Problem 4.5]: "we must count, for every
(i,j,k,ℓ) ∈ Q, the pairs (k',ℓ') ∈ [d]² with A_i[k'] + B_j[ℓ'] < A_i[k] + B_j[ℓ]; again, a call may
have ≤ in place of <, and it may restrict k' and ℓ' to subsets of [d]."  Here `A i k` is A_i[k], the
k-th number of block A_i, and `K'`, `L'` are the subsets to which k' and ℓ' are restricted
(`Finset.univ` for no restriction), one pair of subsets for the whole call. 

### `lists45`

 Proof of Lemma 36: "the rows are the n pairs (i,k) and the columns are the n pairs (j,ℓ), the
row list R_(i,k) consists of the d numbers A_i[k'] - A_i[k], k' ∈ [d], the column list C_(j,ℓ) of
the d numbers B_j[ℓ] - B_j[ℓ'], ℓ' ∈ [d], all numbers have the same color ...  A restriction of k'
or of ℓ' deletes numbers from the lists." Here n = b * d, the pair (i,k) is row number
`finProdFinEquiv (i, k)`, and `χ₀` is the common color. 

 #### The construction of Lemma 37 

### `D''`

 Lemma 37: "D'' := ⌈2nd/s⌉ + d". 

### `numOfColor`

 Proof of Lemma 37.  The number of numbers of color `k` in all the lists. 

### `SortedOrder`

 Proof of Lemma 37: "For each color k, sort the numbers of color k of all the lists, and
break ties so that, among equal numbers, those from column lists precede those from row lists.  Let
pos(x) be the position of x in this order. ... (For ≤, we reverse the tie-breaking rule.)" The paper
does not say how the remaining ties (equal numbers from two row lists, or from two column lists) are
broken, so a `SortedOrder` is any outcome of such a sort.

NOTE.  Positions are counted from 0 within each color, so that "blk(x) := ⌊pos(x)/s⌋" gives "blocks
of s consecutive positions". 

### `SortedOrder.pos`

 pos(x), the position of x among the numbers of its color 

### `SortedOrder.pos_injective`

 two numbers of the same color have different positions 

### `SortedOrder.pos_lt`

 the positions of the numbers of color k are 0, 1, ..., (number of numbers of color k) - 1 

### `SortedOrder.sorted`

 the order is sorted 

### `SortedOrder.ties_lt`

 the tie-breaking rule for `<`: a number y of a column list precedes an equal number x of a row
  list 

### `SortedOrder.ties_le`

 the reversed tie-breaking rule for `≤`: a number x of a row list precedes an equal number y of
  a column list 

### `blk`

 Proof of Lemma 37: "Cut the order into blocks of s consecutive positions, and let blk(x) :=
⌊pos(x)/s⌋." 

### `blockPairs`

 Proof of Lemma 37: the "pairs (color, block)": all pairs (χ(x), blk(x)), x a number of one of
the lists. 

### `xCount`

 Proof of Lemma 37: "Let X[r,(k,β)] be the number of numbers of color k in R_r that lie in block
β". 

### `yCount`

 Proof of Lemma 37: "let Y[(k,β),c] be the number of numbers of color k in C_c that lie in a
block after β". 

### `matX`

 Proof of Lemma 37: "there are at most 2nd/s + d ≤ D'' pairs (color, block), and we index the
columns of X and the rows of Y by the pairs, padding with zeros if needed."  `idx` is the indexing;
the statements assume that it is injective on `blockPairs`. Column `j` of `X` is the column of the
pair (k,β) with `idx (k,β) = j`, and it is zero if there is no such pair. 

### `matY`

 Proof of Lemma 37.  The matrix `Y`, indexed like `matX`: row `j` of `Y` is the row of the pair
(k,β) with `idx (k,β) = j`, and it is zero if there is no such pair. 

### `blockRowItems`

 Proof of Lemma 37, "Same block": "For every color k and block β, let I be the numbers x of row
lists in the block, each with its row". 

### `blockColItems`

 Proof of Lemma 37: "and let J be the numbers y of column lists in the block, each with its
column". 

### `sameBlockCount`

 Proof of Lemma 37: "For every (x,y) ∈ I × J with pos(x) < pos(y) whose row and column form a
pair (r,c) ∈ P ... we add 1 to γ₂(r,c)."  The sum is over the pairs (color, block). 

### `enumeratedPairs`

 Proof of Lemma 37: the number of pairs (x,y) ∈ I × J that are enumerated, over all colors and
blocks. 

 #### The parameters of Corollary 38 and of the proof of Theorem 35 

### `blockLen`

 Proof of Corollary 38: "s := ⌈n^{1-1/440}/d⌉". 

### `Dstar`

 Proof of Corollary 38: "D* := ⌈3d²n^{1/440}⌉". 

### `listLen`

 Proof of Theorem 35: "Let d := ⌊n^{1/40}⌋". 

 ### 5.4 Three conjectures of van den Brand, Nanongkai, and Saranurak 

### `boolMul`

 Section 5.4: "All three are over the Boolean semiring".  The product of two Boolean matrices. 

### `toInt`

 Proof of Corollary 40: "We compute over ℤ with 0/1 matrices".  The 0/1 integer matrix
of a Boolean matrix. 

### `vHintedOutput`

 Section 5.4, v-hinted Mv (Definition 5.1 of [vdBNS19]): "Phase 1: an n × t matrix M.  Phase 2: a
t × n matrix V. Phase 3: an index i, after which the algorithm outputs MV_{[n],i}, the product of M
and column i of V." 

### `MvHintedOutput`

 Section 5.4, Mv-hinted Mv (Definition 5.6 of [vdBNS19]): "Phase 1: N ∈ {0,1}^{n×n} and V ∈
{0,1}^{t×n}.  Phase 2: a vector I ∈ [n]^t of column indices.  Phase 3: an index j, after which the
algorithm outputs N_{[n],I} V_{[t],j}, where N_{[n],I} is the n × t matrix whose k-th column is
column I_k of N." 

### `uMvHintedOutput`

 Section 5.4, uMv-hinted uMv (Definition 5.11 of [vdBNS19]): "Phase 1: U ∈ {0,1}^{n×t₁}, N ∈
{0,1}^{n×n}, and V ∈ {0,1}^{t₂×n}.  Phase 2: I ∈ [n]^{t₁}.  Phase 3: J ∈ [n]^{t₂}.  Phase 4: indices
i and j, after which the algorithm outputs (U N_{I,J} V)_{i,j}, where N_{I,J} is the t₁ × t₂
submatrix of N with the rows I and the columns J." 

### `Conjecture52`

 Section 5.4: "Each conjecture asserts that no algorithm simultaneously beats all of its listed
bounds, for any ε > 0." v-hinted Mv (Conjecture 5.2 of [vdBNS19]): "Bounds conjectured to be
impossible to achieve simultaneously: n^{ω(1,1,τ)-ε} for Phase 2 and n^{1+τ-ε} for Phase 3."

Running times are not defined here, so the conjecture is stated relative to a parameter:
`Achieves a₂ a₃` stands for "some algorithm solves the problem with t = n^τ, with polynomial time in
Phase 1, O(n^{a₂}) time in Phase 2 and O(n^{a₃}) time in Phase 3".  `ω` stands for the number
ω(1,1,τ).  For programs of the word RAM the parameter is `AchievesVHinted τ`.  The exponents of
rectangular matrix multiplication are not defined in Lean: `ω` is an arbitrary real number here, and
the definition says something only together with a condition on it. The statement that the
conjecture fails (`Items.Corollary_40_fail`) is made for every `ω ≥ 2`.

[vdBNS19] words the bounds as lower bounds Ω(n^{x-ε}) on the time of a phase.  That wording implies
the one used here, "not O(n^{x-ε})" (apply it with ε/2), so a refutation of the conjecture in this
form refutes it as worded there.  The same holds for `Conjecture57` and `Conjecture512`. 

### `Conjecture57`

 Section 5.4, Mv-hinted Mv (Conjecture 5.7 of [vdBNS19]): "n^{ω(1,τ,1)-ε} for Phase 2 and
n^{1+τ-ε} for Phase 3." `Achieves` is as in `Conjecture52`, for the Mv-hinted Mv problem
(`AchievesMvHinted τ`); `ω` stands for ω(1,τ,1). 

### `Conjecture512`

 Section 5.4, uMv-hinted uMv (Conjecture 5.12 of [vdBNS19]): "n^{ω(1,τ₁,1)-ε} for Phase 2,
n^{ω(τ₂,τ₁,1)-ε} for Phase 3, and n^{τ₁+τ₂-ε} for Phase 4."  `Achieves a₂ a₃ a₄` stands for "some
algorithm solves the problem with t₁ = n^{τ₁} and t₂ = n^{τ₂}, with polynomial time in Phase 1 and
O(n^{a₂}), O(n^{a₃}), O(n^{a₄}) time in Phases 2, 3, 4"; `ω₂` stands for ω(1,τ₁,1) and `ω₃` for
ω(τ₂,τ₁,1).  For programs of the word RAM the parameter is `AchievesUMvHinted τ₁ τ₂`. 


## Section 5: statements

The pieces of Sections 5.1 and 5.2 that the paper itself argues and that are mathematics:
correctness of the constructions, counts, and the arithmetic of the exponents, with the paper's
constants. `docs/INDEX.md` says for each item of the paper what is stated and what is not. Where a
statement differs from the printed sentence, `docs/REMARKS.md`, "Section 5 and the introduction:
differences", says why.

* The sentences of the form "can be solved in O(...) time" are not stated here. Those of Corollaries
  39 and 40 are stated about programs of the word RAM (`Items.Corollary_39_zero` to
  `Items.Corollary_40_fail`), and nothing else of Sections 5.3 and 5.4 is stated. Those of Theorem
  35 and of Corollary 38 are about randomized algorithms or real numbers, and the machine has
  neither random bits nor real numbers. That of Theorem 34 rests on Theorem 33, which the paper
  proves and which is not proved here, and on μ, which is defined through ω(1, μ, 1). Three lemmas
  of the library (the files that hold the proofs), `conditional_theorem_34`,
  `conditional_corollary_38` and `conditional_theorem_35`, say how each follows from the results
  that its proof uses, which are taken as hypotheses. The running time of Lemma 37 and Lemma 36 as a
  whole occur only as hypotheses of these lemmas. The list is in `docs/REMARKS.md`, "Section 5 and
  the introduction: running times".
* The theorems of other papers that Section 5 uses as black boxes are not stated (`docs/REMARKS.md`,
  "Section 5: cited results"). In particular the randomized reductions behind Lemma 36 are cited.
  Nothing of Theorem 33 and of its proof is stated.
* Of Lemma 36, the size O(n²/d) of the pair set of part (b) is not stated;
  `Theorem_35_three_sum_count` puts n²/d in its place. The last sentence of the lemma, on the
  operations applied to real numbers, is not stated.
* The other sentences inside proofs are lemmas of the library or are not formalized.
* The statements on blocks have n = b * d; the paper's proof treats n/d as an integer.
* "Õ(f)" is read as "O(f · (log n)^c) for some constant c".


 ### 5.1 Directed APSP with small integer weights 

### `Theorem_34_blocks`

 Proof of Theorem 34: "Cut the n × n^μ matrix into n^{1-μ} blocks of n^μ
consecutive rows, and the n^μ × n matrix into n^{1-μ} blocks of n^μ consecutive columns.  The
(min,+)-product then consists of n^{2-2μ} products of two n^μ × n^μ matrices, one for each pair of
blocks."  Here m = n^μ and b = n^{1-μ}, so that n = b * m. 

### `Theorem_34_entries`

 Proof of Theorem 34: "Their entries have absolute value Õ(n^{1-μ}) ≤ Õ(n^μ), because μ ≥ 1/2".
Stated is the inequality between the two powers, which is what `μ ≥ 1/2` gives; the logarithmic
factors are the same on both sides.  How Theorem 22 is applied to entries of this size is said at
the library's lemma `conditional_theorem_34`. 

### `Theorem_34_total`

 Proof of Theorem 34: "Theorem 22 computes each of them in Õ((n^μ)^{3-ε'/3}) time, and
all of them in Õ(n^{2+μ-με'/3}) time", with ε' = 0.00175. 

### `Theorem_34_absorb`

 Proof of Theorem 34: "This is O(n^{2+μ-ε₁}) for any constant ε₁ < με'/3". 

 ### 5.2 3SUM, APSP, and Exact Triangle with real inputs 

 #### Lemma 36(a): the parts argued in the paper 

### `Lemma_36a_exact_triangle`

 Proof of Lemma 36(a): "For Exact Triangle, A[i,k] := w(i,k), B[k,j] := w(k,j), and
C[i,j] := -w(i,j), and there is a triangle of weight zero if and only if, in some block, some C[i,j]
is its own predecessor." The instance has n = b * d vertices per part; A is cut into b blocks of d
consecutive columns and B into the corresponding blocks of d consecutive rows.  In the notation of
Section 3.2, i, k, j run over the parts A, B, C of the instance. 

### `Lemma_36a_min_plus_below`

 Proof of Lemma 36(a): "For the (min,+)-product of A and B, we take every C[i,j] smaller
than all the sums, for instance C[i,j] := min_k A[i,k] + min_k B[k,j] - 1."  `rowMin i` is min_k
A[i,k] and `colMin j` is min_k B[k,j]. 

### `Lemma_36a_min_plus_successor`

 Proof of Lemma 36(a): "Then the successor of C[i,j] in a block is the smallest sum of
the block". `sums` are the d sums of the block and `c` is a number smaller than all of them. 

### `Lemma_36a_min_plus_blocks`

 Proof of Lemma 36(a): "and the product is the entrywise minimum over the n/d blocks".
`M p` is the matrix of the smallest sums of block `p`, that is, the (min,+)-product of the p-th
blocks. 

 Proof of Lemma 36(a): "APSP with real weights and no negative cycles can be computed by
successive squaring of the weight matrix, performing ⌈log₂ n⌉ such products." This is
`Theorem_21b_repeated_squaring` (Theorem 21(b)), which is stated for weights in any linearly ordered
commutative group, in particular for real weights. 

### `Lemma_36a_count`

 Proof of Lemma 36(a): "By Fredman's trick, A'[i,k'] + B'[k',j] < A'[i,k] + B'[k,j] if
and only if A'[i,k'] - A'[i,k] < B'[k,j] - B'[k',j] ...  Thus the count of a pair (i,j) ∈ P_k is the
comparison count γ(i,j) of these lists with P := P_k."  Also with ≤. 

### `Lemma_36a_valid`

 Lemma 36(a): the comparison counts of a counting call have "n row lists and n column
lists of at most d numbers". 

### `Lemma_36a_colors`

 Lemma 36(a): "with at most one number of each color in a list". 

### `Lemma_36a_pairs`

 Lemma 36(a): "with pair sets P_1, …, P_d satisfying ∑_k |P_k| = n²". 

### `Lemma_36a_subtractions`

 Lemma 36(a): "forming its lists costs O(nd²) subtractions" (the proof of Lemma 36: "O(nd)
subtractions for each k").  Every number in a list is formed by one subtraction, so the number of
subtractions is the total length of the lists. 

 #### Lemma 36(b): the parts argued in the paper 

### `Lemma_36b_count`

 Proof of Lemma 36(b): "By Fredman's trick, the condition is A_i[k'] - A_i[k] < B_j[ℓ] -
B_j[ℓ'].  So a call is one comparison count: the rows are the n pairs (i,k) and the columns are the
n pairs (j,ℓ) ... and P := Q."  Also with ≤, and with k' and ℓ' restricted to subsets K' and L' of
[d]. 

### `Lemma_36b_lists`

 Lemma 36(b): the comparison counts have "n row lists and n column lists of at most d numbers,
all of the same color"; the proof of Lemma 36: "A restriction of k' or of ℓ' deletes numbers from
the lists." 

### `Lemma_36b_subtractions`

 Lemma 36(b): "forming the lists of a comparison count costs O(nd) subtractions", with
n = b * d. 

 #### Lemma 37

The lemma says "we can build matrices X [...] and Y [...] and compute integers γ₂(r,c), (r,c) ∈ P,
with" γ(r,c) = (XY)[r,c] + γ₂(r,c). Read as a bare existence statement this would be trivial (take
X = Y = 0), so the statements below are about the matrices and the integers that the proof
constructs: `matX`, `matY`, `sameBlockCount`, for an arbitrary outcome `o` of the sort and an
arbitrary indexing `idx` of the pairs (color, block). The running time of the lemma is a hypothesis
of the library's lemma `conditional_corollary_38`. 

### `Lemma_37_order_exists`

 Proof of Lemma 37: the sort can be carried out, that is, an order as described
exists. 

### `Lemma_37_index_exists`

 Proof of Lemma 37: "and we index the columns of X and the rows of Y by the pairs": an indexing
exists. 

### `Lemma_37`

 **Lemma 37** (after Matoušek), the part that is not a running time.  "Let s ≥ 1 be an
integer and D'' := ⌈2nd/s⌉ + d.  Given row lists R_r and column lists C_c as above and a set P ⊆
[n]², we can build matrices X ∈ {0,…,d}^{n×D''} and Y ∈ {0,…,d}^{D''×n} and compute integers
γ₂(r,c), (r,c) ∈ P, with γ(r,c) = (XY)[r,c] + γ₂(r,c) for every (r,c) ∈ P ...  The same holds with ≤
in place of < in the definition of γ." The matrices and the integers γ₂ depend on the real numbers
only through the positions `o.pos`, in accordance with "The only operations on real numbers are the
comparisons made when sorting the numbers of each color." 

### `Lemma_37_enumerated`

 Proof of Lemma 37: "Since |I||J| ≤ s²/4 and there are at most 2nd/s + d blocks, we
enumerate at most (2nd/s + d)s²/4 ≤ nds + ds² pairs (x,y)". 

 #### Corollary 38: correctness and parameter arithmetic 

### `Corollary_38_bound`

 Proof of Corollary 38: "Corollary 26 ... computes (XY)[r,c] for all (r,c) ∈ P
deterministically in O(|P|(D*)^{0.437} + n²/(D*)^{0.063}) time" and "the time of Lemma 37 itself is
O(nD* + (|P| + nds + ds²) log n) = O(|P| n^{0.0229} + n^{2-1/440} log n)"; together these are at
most a constant times the bound |P| n^{0.0229} + n²/d^{0.126} + n^{2-1/440} log n of the corollary.
`p` is |P|.  The hypothesis 1 ≤ d is the standing assumption of Section 5.2: "Throughout, d ∈ [n] is
a parameter".

NOTE. The time of Lemma 37 is taken as in the library's `Claim.Lemma_37`, so that this is the
arithmetic of `conditional_corollary_38`: it has `log n + 1` in place of `log n`, which makes the
statement stronger. 

### `Corollary_38_correct`

 Corollary 38, the part that is not a running time: the counts γ(r,c), (r,c) ∈ P, "with < or with
≤", are the wanted entries of a product with inner dimension D*, which satisfies the hypotheses of
Corollary 26 with N = n (second to fourth conjunct: (D*)^18 ≤ n, and entries of absolute value at
most n), plus the integers γ₂(r,c) of Lemma 37. The first conjunct, D'' ≤ D* (proof of Corollary 38:
"D'' ≤ 2d²n^{1/440} + d + 1 ≤ 3d²n^{1/440}"), says that "pad the product to the inner dimension D*"
only adds zero columns and zero rows: `padInnerCols` and `padInnerRows` would cut off a larger
matrix. `n₀` is the "suitable constant" of the corollary.  The hypothesis 1 ≤ d is the standing
assumption of Section 5.2: "Throughout, d ∈ [n] is a parameter". 

 #### Proof of Theorem 35: the arithmetic, with d := ⌊n^{1/40}⌋ 

### `Theorem_35_d`

 Proof of Theorem 35: "Let d := ⌊n^{1/40}⌋, apply Lemma 36 with this d, and answer every
comparison count by Corollary 38." This d satisfies the hypotheses 1 ≤ d ≤ n of Lemma 36 and d ≤
n^{1/40} of Corollary 38. 

### `Theorem_35_counting_call`

 Proof of Theorem 35: "the d comparison counts of a counting call cost ∑_{k ∈ [d]} O(|P_k|
n^{0.0229} + n²/d^{0.126} + n^{2-1/440} log n) = O(n^{2.0229} log n), since ∑_k |P_k| = n²". `p k`
is |P_k|. 

### `Theorem_35_forming_lists`

 Proof of Theorem 35: "forming the lists costs O(nd²) = O(n^{1.05})". 

### `Theorem_35_min_plus_total`

 Proof of Theorem 35: "So the Õ(n/d) counting calls of Lemma 36(a) cost Õ((n/d) n^{2.0229}) =
Õ(n^{3-1/40+0.0229}) ≤ O(n^{2.998})". 

### `Theorem_35_further_time`

 Proof of Theorem 35: "and its additional time is Õ(n³/d) = Õ(n^{2.975})" (which is
O(n^{2.998})). 

### `Theorem_35_three_sum_count`

 Proof of Theorem 35, 3SUM: "a comparison count of Lemma 36(b) costs O((n²/d) n^{0.0229} +
n²/d^{0.126} + n^{2-1/440} log n) = O(n^{2-1/40+0.0229} log n) = O(n^{1.9979} log n)". 

### `Theorem_35_three_sum_total`

 Proof of Theorem 35, 3SUM: "so 3SUM can also be solved in Õ(n^{1.9979}) ≤ O(n^{1.998}) expected
time"; the further time Õ(n²/d) of Lemma 36(b) is within the same bound. 

### `Theorem_35_one_run`

 Proof of Theorem 35, "Las Vegas, and high probability": "we stop a run that exceeds twice the
bound on its expected time".  By Markov's inequality such a run is stopped with probability at most
1/2.  `T` is the running time of a run and `B` the bound on its expectation. 

### `Theorem_35_restarts`

 Proof of Theorem 35: "and start again, and c log₂ n runs all fail with probability at most
n^{-c}".  `T i` is the running time of the i-th run; the runs are independent, and there are m ≥ c
log₂ n of them. (The m runs take 2Bm time in all, a factor O(log n) more than B; the bounds of
Theorem 35 still hold because `theorem_35_min_plus_total` and `theorem_35_three_sum_total` hold for
every power of the logarithm.) 


## The word RAM: problems

First comes what it means that a program of the machine of `EndStatement.lean` solves a problem
within a time bound.  Then come the problems: which number lies in which cell at the start, and
what a right answer is.  No sentence of the paper is stated here; the sentences are the item
statements `Items.Theorem_5`, …, in the terms that are defined here.  `docs/MACHINE.md`, Part 1,
goes through the definitions at length and compares the machine with the standard word RAM point by
point.

**What a reader of the statements about programs can skip.**  Of the definitions of Sections 2 to 5
the statements `wordRam_theorem_5`, … use only these 28:
* Section 2: `N0`, `K`, `alpha`;
* Section 3: `LopInstance`, `LopInstance.commonNeighbors`, `LopInstance.InTriangle`,
  `LopInstance.numTriangles`, `LopInstance.ofMatrices`, `GraphHasZeroTriangle`;
* Section 4: `rho`, `cost8`, `costQuery`, `cost9`, `entropy`, `rhoC`, `gammaOf`, `qOf`, `lnΛ`, `Rc`,
  `epsStar`;
* Section 5, namespace `HintedMv`: `boolMul`, `toInt`, `vHintedOutput`, `MvHintedOutput`,
  `uMvHintedOutput`, `Conjecture52`, `Conjecture57`, `Conjecture512`.

NOTE.  Eight notions are defined twice: in `EndStatement.lean`, and with Mathlib for the statements
on the reductions and about programs.  For each of them a statement, named in brackets, says that
the two definitions agree (a further form of `O(n^a)`, the bound `Within` on the steps of a phase,
is not compared):
* "a program solves a problem": there `Problem`, `Problem.SolvedBy` and the word sizes of
  `Problem.SolvedInTime`, for one size `n`; here `Problem`, `Admissible`, `output` and `Solves`, for
  several sizes (`Agreement_solves`);
* `O(n^r)`: there `BigO`, for a rational exponent and from `n = 2` on; in Section 3 `IsBigOPow`, for
  a real exponent and all large `n` (`Agreement_bigO`, for `r ≥ 0`);
* "solved in time": there `Problem.SolvedInTime` and `BigO`, with a rational exponent and a bound
  `T(n)` that is `O(n^r)` from `n = 2` on; here `SolvesWithin`, `SolvedInTimeAt` and `SolvedInTime`,
  with a real exponent and the bound `C (n^a (log n)^e + 1)` at every size
  (`Agreement_solvedInTime`, for a rational exponent `r ≥ 0` and `e = 0`); both are stated through
  `Problem.SolvedBy`;
* Exact Triangle: `EndStatement.ExactTriangle` and `TriangleInstance.HasZeroTriangle`
  (`Agreement_exactTriangle`);
* the (min,+)-product: `EndStatement.MinPlusProduct` and `IsMinPlusProduct`
  (`Agreement_minPlusProduct`);
* APSP: `EndStatement.Path` and `EndStatement.APSP`, where a missing edge is `none`, and
  `walkWeight`, `NoNegativeCycle` and `IsDistanceMatrix`, where it is `⊤`
  (`Agreement_apsp_noNegativeCycle`, `Agreement_apsp_output`);
* a matrix written row by row: `EndStatement.rowByRow` and `rowMajor` (`Agreement_rowByRow`);
* the weight of a `k`-clique: the sum in `EndStatement.ZeroWeightKClique` and `cliqueWeight`
  (`Agreement_cliqueWeight`).

**The machine** is defined in `EndStatement.lean` and nowhere else: `Instr`, `exec` and
`loadWords`.  The paper works "in the standard word RAM model with O(log N)-bit words", and so
counts "operations on O(log N)-bit integers" (Section 2).  There is no division, no shift, no
bitwise operation and no constant but 1: in its instructions the machine is weaker than the standard
word RAM.

NOTE.  On four points the machine is generous; none of them changes an exponent:
* Every cell outside the input, with a positive or a negative name, holds 0 at the start, and
  `Solves`, `SolvesWithin` and `RunsPhases` charge no space, so a table that is addressed directly
  by a number costs nothing to set up (on a machine without this, lazy initialisation costs a
  constant factor).
* The finitely many cells that a program names in its text need not be addressable by a word.
* The slope `b` of the word size is chosen after the exponent `κ` of the magnitude of the numbers.
* The inputs of phases and the queries arrive at no cost. 

 ### What it means to solve a problem

**The order of the choices.**  In every statement the order is: the constants of the problem (the
exponent `κ` of the magnitude of the numbers, the `k` of `k`-Clique); then the program, the slope
`b` of the word size and the constant `C` of the time bound; then the instance; then the word size,
any number of bits that is admissible for the slope.  So the program cannot depend on the instance
or on its size, and it cannot rely on long words. 

 #### The word size and the output cells 

### `Admissible`

 The word size `W` is admissible against the slope `b` for an input with the parameters `params`
(its sizes): `W` is at least `b · (⌊log₂ p₁⌋ + ⌊log₂ p₂⌋ + … + 1)`.  If every parameter is at most a
fixed power of the size `n`, the smallest admissible word size is a constant times `log n`: "O(log
n)-bit words".  A statement fixes only the slope `b`, together with the program, and the program has
to work, within the same bound on the number of steps, at every admissible word size. 

### `output`

 The output of a function problem: the cells right after the input, read as signed words.
`output c len i` is the number in the `i`-th cell of the memory `c` after an input of `len`
cells. 

 #### Problems, and solving a problem within a time bound 

### `Problem`

 A computational problem on the word RAM. 

### `Problem.Inst`

 The instances. 

### `Problem.params`

 The parameters of an instance on which the word size depends: its sizes. 

### `Problem.input`

 The input: the numbers written into the cells 0, 1, 2, … 

### `Problem.IsAnswer`

 `IsAnswer x verdict out`: the verdict, and the numbers `out 0, out 1, …` in the cells right
  after the input, are a correct answer to the instance `x`. 

### `Solves`

 **Solving a problem within a time bound.**  The program `P` with slope `b` solves the problem on
the instances in `dom` within time `T`: on every such instance `x` and at every admissible word size
`bits`, the run from the first instruction on the starting memory (input in the cells 0, 1, 2, …,
zeros elsewhere) gives a verdict after at most `T x` steps, and the verdict and the output are a
correct answer. 

 #### Time bounds in one size `n`, for the problems of `EndStatement.lean` 

### `SolvesWithin`

 The program `P` with slope `b` solves the problem `Q` within `T(n)` steps when all numbers are
integers of absolute value at most `n^κ`.  This is what `EndStatement.Problem.SolvedInTime` asks of
the runs of `P`, for a real bound `T`: on every such instance, of any size `n`, and at every word
size of at least `b (⌊log₂ n⌋ + 1)` bits, `P` halts within `T(n)` steps with the right verdict and
output (`EndStatement.Problem.SolvedBy`).

NOTE.  As in `EndStatement.Problem.SolvedInTime`, the bound speaks of every number of the input
list.  Where the input contains an adjacency matrix, its entries 1 count too; `n^κ` is at least 1 as
soon as there is a vertex. 

### `SolvedInTimeAt`

 The problem `Q`, a value of `EndStatement.Problem`, is solved by a deterministic algorithm in
`O(n^a (log n)^e)` time when all numbers are integers of absolute value at most `n^κ`: there are a
program, a slope and a constant `C` such that the program solves `Q` within `C (n^a (log n)^e + 1)`
steps.  (For `a ≥ 0` the `+ 1` matters only at `n ≤ 1`, where `n^a (log n)^e` may be 0.) 

### `SolvedInTime`

 The same for every constant `κ`: "all numbers in the input are integers of absolute value
n^{O(1)}" (Theorem 2).  The program, the slope and the constant may depend on `κ`.

NOTE.  `κ` is the paper's ν.  Where the paper has ν ≥ 1 (Theorem 19, Corollary 39), `κ = 0` is
included here. 

### `SolvedInPolylogTime`

 The same in `O(n^a (log n)^{O(1)})` time, which Theorem 22 writes Õ(n^a).

NOTE.  The exponent of the logarithm may depend on `κ` too: this is the weaker reading of the
Õ of Theorem 22. 

### `SolvedInLittleOTime`

 The problem `Q` is solved by a deterministic algorithm in `n^{a+o(1)}` time when all numbers are
integers of absolute value at most `n^κ`, for every constant `κ`: as `SolvedInTime`, with the bound
`C (n^{a+o(n)} + 1)` for a function `o` that tends to 0.  The program, the slope, the constant and
the function may depend on `κ`.  (The constant is needed at `n ≤ 1`, where `n^{a+o(n)}` is 0 or 1;
the `+ 1` keeps the form of `SolvedInTimeAt`.  For `a < 0` the bound means `O(1)`.) 

 #### A query program that serves one query after the other 

### `withQuery`

 The memory on which a query starts: the memory `c`, left behind by the preprocessing or by the
previous query, with the row `I` and the column `J` written into the two query cells `qI` and
`qJ`. 

### `Serves`

 The query program `Q` serves the queries of the list one after the other, starting from the
memory `c`: each run starts at the first instruction, accepts within `tq` steps and leaves the right
entry in the cell `qOut`; the next query starts from the memory that this run leaves. 

 #### Programs that receive their input in phases

A problem in phases has one program for each phase.  The inputs of the phases are laid
out one after the other in the cells 0, 1, 2, …, but the input of a phase is written into its cells
only when the phase starts.  Each program starts at its first instruction on the memory that the
previous phase has left; the first one starts on a memory of zeros.  So a phase cannot see the input
of a later phase, and nothing is reset between phases.  The output is read from the cells after the
last input.  Receiving an input takes no steps, and the inputs of earlier phases stay in memory
unless a program overwrites them.  What an earlier phase has left in the cells of a later input is
lost; the earlier phase knows which cells these are, since all sizes are given in Phase 1.  (In the
running times of Corollary 40 the bound of a phase is at least the length of its input, if the
exponent `γ` of `Items.Corollary_40_general_times` is at most 1; so they do not depend on inputs
being free.) 

### `withInput`

 The memory on which a phase starts: the memory `c` with the list `ws` written into the cells
`off, off + 1, …`. 

### `RunsPhases`

 The phases of the list, each given by its program, its input and a number of steps, run one
after the other from the memory `c`: every phase starts at its first instruction and accepts within
its number of steps, the inputs are written one after the other from the cell `off` on, and the last
memory, with the address of the first cell after the last input, satisfies `good`.


### `Within`

 A number `s` of steps is `O(n^a)` with the constant `C`: `s ≤ C (n^a + 1)`.  For `n ≥ 1` and
`a ≥ 0` the `+ 1` only changes the constant; for `a < 0` the bound means `O(1)`. 

 ### The problems of the paper, their inputs and their answers

**Layout.**  Matrices are written row by row, one number per cell, as signed words.  Booleans are
written as 0 and 1, and indices and vertices count from 0.  The first cells hold the sizes.  The
bound on the absolute values of the numbers is not written into memory.  For the matrix problems it
is a number `U` that is part of the instance as a mathematical object (`ThinPair`); for the problems
in the form of `EndStatement.Problem` it is a hypothesis of `SolvesWithin`.  In the statements it is
a fixed power of the size, with an exponent that is fixed before the program (and 1 for the 0/1
matrices of the lopsided triangle problems).  A program for a problem with an output has to accept,
and to leave the output in the cells right after the input. 

 #### How matrices and Booleans are written 

### `rowMajor`

 A matrix written row by row. 

### `bit`

 A Boolean as a number. 

 #### The wanted entries of a thin matrix product (Theorems 1, 5, 25 and 30, Corollaries 26 and
32) 

### `ThinPair`

 Two matrices `X ∈ ℤ^{N×D}` and `Y ∈ ℤ^{D×N}` with entries of absolute value at most `U`. 

### `ThinPair.N`

 The long side. 

### `ThinPair.D`

 The short side. 

### `ThinPair.U`

 The bound on the absolute values of the entries. 

### `ThinPair.X`

 The first matrix. 

### `ThinPair.Y`

 The second matrix. 

### `ThinPair.boundX`

 The entries of `X` are bounded. 

### `ThinPair.boundY`

 The entries of `Y` are bounded. 

### `ThinInstance`

 Theorem 5: two such matrices and "a set W of [...] positions of an N × N matrix".

NOTE.  The paper does not say how a set is given.  Here it is a list without repetitions, in any
order. 

### `ThinInstance.W`

 The wanted positions. 

### `ThinInstance.nodup`

 No position is listed twice. 

### `ThinInstance.input`

 The input of the matrix problems: `N`, `D`, `|W|`, then further parameters `extra` (none, except
in Theorem 30), then `X`, then `Y`, then the rows `I` of the wanted positions, then their columns
`J`. 

### `thinProduct`

 **The wanted entries of a thin matrix product** (Theorem 5): accept, and leave `(XY)[I,J]` for
the `i`-th wanted position `(I,J)` in the `i`-th output cell. 

 #### The two-stage data structure for a thin matrix product (Section 4) 

### `ThinPair.input`

 The input of the preprocessing: `N`, `D`, further parameters `extra` (none, except in
Theorem 30), then `X`, then `Y`.  The list `extra` is fixed before the instance. 

### `IsDataStructure`

 **A data structure for the entries of a thin matrix product** (Theorem 30, Corollary 26): "After
preprocessing X and Y [...], the data structure answers a query for any single entry of XY, not
known in advance" (Section 4).

`P` is the preprocessing program, `Q` the query program, `qI`, `qJ`, `qOut` the three cells through
which queries are put and answered; all of them, and the slope `b`, are fixed before the instance.
On every instance in `dom` and at every admissible word size:

* time: the preprocessing accepts within `Tp x` steps;
* space: it leaves unchanged every cell `a` with `a < -Sp x` or `a > len + Sp x`, where the input
  occupies the cells 0 to `len - 1` (so the cells of the input are not counted);
* queries: then every sequence of queries `(I, J)` with `I, J < N` is served, each query within
  `Tq x` steps.  A query starts on the memory left behind; nothing is reset for it.

NOTE.  The paper says "time and space" and does not define space.  Here space is the extent of the
memory in which the preprocessing leaves the data structure, not the number of cells written, which
is at most the time anyway; a structure that is scattered over a large range of addresses does not
count as small.  Cells that the preprocessing restores, and cells that the queries write, are not
constrained. 

 #### The lopsided triangle problems (Definitions 13 and 14) 

### `ThinInstance.ZeroOne`

 The entries of both matrices are 0 or 1: the two biadjacency matrices of an instance of
Lop-AE-SparseTri(N, D) (Section 3.1). 

### `ThinInstance.lop`

 The instance of the lopsided triangle problems that two 0/1 matrices and a list of query pairs
describe.

NOTE.  Definition 13 has "a middle part M of at most D vertices"; here the middle part has exactly
`D` vertices, the columns of `X`.  A smaller middle part is written with zero columns of `X` and
zero rows of `Y`: vertices without edges, which lie in no triangle. 

### `lopCount`

 **#Lop-AE-SparseTri** (Definition 14), with the graph given by its two biadjacency matrices: the
`i`-th output cell holds the number of triangles through the `i`-th query pair. 

### `lopDetect`

 **Lop-AE-SparseTri** (Definition 13): the `i`-th output cell holds 1 if the `i`-th query pair
lies in a triangle, and 0 if not. 

 #### Exact Triangle, 3SUM, the (min,+)-product and APSP

These four are the problems `ExactTriangle`, `ThreeSum`, `MinPlusProduct` and `APSP` of
`EndStatement.lean`. 

 #### Exact Triangle on `n`-vertex graphs 

### `WeightedGraph`

 A graph on `n` vertices with integer edge weights: an instance of Exact Triangle "on an
arbitrary n-vertex graph" (Section 3.2); Theorem 2 has "Exact Triangle on n-vertex graphs". 

### `WeightedGraph.G`

 The graph. 

### `WeightedGraph.w`

 The weight of the edge `{u, v}`. 

### `WeightedGraph.symm`

 The graph is undirected. 

### `GraphExactTriangle`

 **Exact Triangle on `n`-vertex graphs**, stated as the problems of `EndStatement.lean` are: the
input is the adjacency matrix (1 for an edge, 0 for none), then the matrix of the weights (0 where
there is no edge); accept exactly if three pairwise adjacent vertices have edge weights that sum to
zero. 

 #### Zero-Weight, Min-Weight and Max-Weight `k`-Clique (Corollary 39)

Zero-Weight `k`-Clique is the problem `ZeroWeightKClique k` of `EndStatement.lean`.  The other two
have its input: for each ordered pair of parts `(p, q)`, in row-major order, an `n × n` block of
numbers, where `w p q u v` is the weight between vertex `u` of part `p` and vertex `v` of part `q`.

NOTE.  All `k²` blocks are input, but only the blocks with `p < q` count; the others may hold
anything within the bound on the numbers of the input.  The paper does not fix a layout. 

### `cliqueWeight`

 The total edge weight of the `k`-clique that has the vertex `v p` in part `p` (Corollary 39):
the sum, over the pairs of parts `p < q`, of the weight between `v p` and `v q`. 

### `MinKClique`

 **Min-Weight `k`-Clique** (Corollary 39): accept, and leave in the `p`-th of the `k`
output cells (`p = 0, …, k − 1`) the number, below `n`, of the vertex chosen in part `p`, so that
the `k` vertices form a `k`-clique of minimum total edge weight.  Every such clique is accepted.

NOTE.  The parts have at least one vertex: at `n = 0` there is no clique to output. 

### `MaxKClique`

 **Max-Weight `k`-Clique** (Corollary 39): the same with maximum total edge weight. 

 #### The three hinted matrix-vector problems of [vdBNS19] (Corollary 40) 

### `hintSize`

 Section 5.4: the hint dimension "t = n^τ".

NOTE.  The paper treats `n^τ` as an integer; here it is rounded down, which keeps what the proof of
Corollary 40 needs, for `n ≥ 1`: `t ≥ 1` if `τ ≥ 0`, and `t^18 ≤ n` if `0 ≤ τ ≤ 1/18`.  The number
`t` is given to the programs in Phase 1, after `n`; they need not compute it. 

### `AchievesVHinted`

 **v-hinted Mv** (Section 5.4; Definition 5.1 of [vdBNS19]) with `t = n^τ` is solved with
polynomial time in Phase 1, `O(n^{a₂})` time in Phase 2 and `O(n^{a₃})` time in Phase 3.  Phase 1
receives `n`, `t` and the `n × t` matrix `M`; Phase 2 the `t × n` matrix `V`; Phase 3 the index `i`;
the output is the `n` entries of the Boolean product of `M` and column `i` of `V`. 

### `AchievesMvHinted`

 **Mv-hinted Mv** (Section 5.4; Definition 5.6 of [vdBNS19]) with `t = n^τ`, in the same sense.
Phase 1 receives `n`, `t`, the `n × n` matrix `N` and the `t × n` matrix `V`; Phase 2 the `t` column
indices `I`; Phase 3 the index `j`; the output is the `n` entries of `N_{[n],I} V_{[t],j}`. 

### `AchievesUMvHinted`

 **uMv-hinted uMv** (Section 5.4; Definition 5.11 of [vdBNS19]) with `t₁ = n^{τ₁}` and `t₂ =
n^{τ₂}` is solved with polynomial time in Phase 1 and `O(n^{a₂})`, `O(n^{a₃})`, `O(n^{a₄})` time in
Phases 2, 3, 4.  Phase 1 receives `n`, `t₁`, `t₂` and the matrices `U` (`n × t₁`), `N` (`n × n`),
`V` (`t₂ × n`); Phase 2 the `t₁` row indices `I`; Phase 3 the `t₂` column indices `J`; Phase 4 the
indices `i` and `j`; the output is the one entry `(U N_{I,J} V)_{i,j}`. 


## Agreement with the definitions of EndStatement.lean

Eight notions have two definitions each.  `EndStatement.lean` defines them for the five claims, with
Lean's core library only, for integers and square matrices.  The statements on the reductions and
the statements about programs use definitions with Mathlib: the paper needs Exact Triangle and the
(min,+)-product also over the real numbers, matrices that are not square, problems with several
sizes, and time bounds with real exponents and logarithmic factors.  The statements below say that
the two definitions of each notion agree.  APSP has two statements, one for the promise and one for
the output.


### `Agreement_exactTriangle`

 Exact Triangle: `EndStatement.ExactTriangle`, on the three matrices of weights of `T`, asks
whether `T` has a zero triangle. 

### `Agreement_minPlusProduct`

 The (min,+)-product: the output cells are right for `EndStatement.MinPlusProduct` exactly if,
read row by row as a matrix, they are the (min,+)-product in the sense of `IsMinPlusProduct`. 

### `Agreement_apsp_noNegativeCycle`

 APSP, the promise.  A missing edge is `none` in `EndStatement.APSP` and `⊤` in
`NoNegativeCycle`.  No closed `EndStatement.Path` has negative weight exactly if `NoNegativeCycle`
holds. 

### `Agreement_apsp_output`

 APSP, the output.  The output cells are right for `EndStatement.APSP` exactly if the first cell
of every pair of vertices holds 0 or 1, and the matrix that has the second cell where the first
holds 1, and `⊤` elsewhere, is the distance matrix in the sense of `IsDistanceMatrix`. 

### `Agreement_rowByRow`

 A square matrix written row by row: `EndStatement.rowByRow` and `rowMajor` give the same
list. 

### `Agreement_cliqueWeight`

 The weight of a `k`-clique: the sum in `EndStatement.ZeroWeightKClique` is `cliqueWeight`, for
every choice `v` of one vertex in each part.  So that problem asks whether some clique has
`cliqueWeight` 0. 

### `Agreement_solves`

 "A program solves a problem".  `Problem`, `Admissible`, `output` and `Solves` are the form for
problems with several sizes.  Write a problem `Q` of `EndStatement.lean` in this form: the instances
are those whose numbers have absolute value at most `n^κ`, the size is the one parameter of the word
size and stands in front of the input, and a right answer is a right verdict and a right output.
Then `Solves` says the same as `SolvesWithin`, which is stated through
`EndStatement.Problem.SolvedBy`. 

### `Agreement_bigO`

 `T(n) = O(n^r)`, for a rational exponent `r ≥ 0`: `EndStatement.BigO` says the same as
`IsBigOPow`. 

### `Agreement_solvedInTime`

 "Solved in time `O(n^r)`", for a rational exponent `r ≥ 0`: `EndStatement.Problem.SolvedInTime`
says the same as `SolvedInTime` with the real exponent `r` and no logarithmic factor. 


## The word RAM: running times

An item statement is a running-time sentence of the paper, written as a proposition about programs
of the machine of `EndStatement.lean` and named after its item, such as `Items.Theorem_5` or
`Items.Corollary_26`.  Its docstring quotes the sentence.  The notions of solving are `Solves`,
`IsDataStructure`, `SolvesWithin` and `RunsPhases`, and the forms derived from them (`SolvedInTime`,
`AchievesVHinted`, …); the layouts of the inputs and the order of the choices are explained with
them.  The definitions only say what the sentences mean.  That they hold is stated by the theorems
`wordRam_theorem_5`, `wordRam_corollary_26`, ….  The five claims of `EndStatement.lean` are five of
the bounds of `Theorem_19`, `Theorem_22_second` and `Corollary_39_zero`.

* **Order.**  Sections 2 to 5 in the paper's order, then the introduction.  Its Theorems 1 to 4
  restate and combine the later items (here Theorem 3 is stated through Corollary 26, and Theorem 4
  through Corollary 40), so they stand last.
* **Items and propositions.**  Some items have several propositions, for instance `Corollary_26` for
  the data structure and `Corollary_26_wanted` for the entries at a given set of positions; and some
  propositions hold several bounds of their item, joined by "and", for instance `Theorem_19`.
* **Definitions that are not items.**  `thinDom`, `HasDataStructure` and `theorem30Dom` abbreviate
  hypotheses or sentences that occur in more than one proposition.  `DataStructureBelow` and
  `WantedBelow` state the last sentences of Theorems 3 and 1 ("More generally, …") with a bound `ε₀`
  in the place of 0.1204.
* **Departures.**  Where a proposition departs from the printed sentence, for instance by a lower
  bound `D ≥ 1` that the paper leaves out, its docstring, or that of the definition through which it
  is stated, says so, mostly in a paragraph that begins with NOTE.
* **Real parameters.**  Corollaries 31 and 32 have real parameters `c` and `θ`.  The statements do
  not mention the numbers `⌈cm⌉` and `⌈θm⌉` of the proof; they only say that programs with certain
  time bounds exist.  So they make sense, and are stated, for all real `c` and `θ`, although a
  program is a finite text: a proof may use rational parameters close to `c` and `θ`, which the
  strict inequality `ε < R_c(γ)` leaves room for.
* **Not stated about programs.**  The other sentences of the paper about running time are not stated
  about programs.  The machine has neither random bits nor real numbers: Theorem 35 (with the half
  of Theorem 2 on real inputs) needs both, and Corollary 38 needs real numbers.  Theorem 34 rests on
  Theorem 33, which the paper proves and which is not proved here, and on μ, which is defined
  through ω(1, μ, 1). For these three items see the library's lemmas `conditional_theorem_34`,
  `conditional_corollary_38` and `conditional_theorem_35`, where Theorem 33 and Lemmas 36 and 37 are
  hypotheses.  Theorems 17 and 21 speak of an arbitrary solver, while each item statement is about
  one fixed program.  The time bound of Lemma 29 enters the bound (8) of Theorem 30. 

 ### Section 2: Theorem 5 

### `Theorem_5`

 **Theorem 5**: "Let D ≥ 4 be a power of four and N ≥ D^18.  Given as input matrices X ∈
ℤ^{N×D} and Y ∈ ℤ^{D×N}, whose entries are integers of absolute value at most N^{O(1)}, as well as a
set W of at most N²/√D positions of an N × N matrix, the entries (XY)[I,J], (I,J) ∈ W, can be
computed deterministically in time O(N² log² D/D^{1/18})."  `c` is the exponent hidden in
`N^{O(1)}`.  (As a statement about the existence of programs, this follows from
`Corollary_26_wanted`, whose bound is smaller on these inputs: a statement of this kind cannot say
by which algorithm a bound is reached.) 

 ### Section 3: Corollaries 15 and 16, Theorems 19 and 22 

### `Corollary_15`

 **Corollary 15**: "Let D ≥ 4 be a power of four with n ≥ D^18, and consider an instance
of #Lop-AE-SparseTri(n,D) or of Lop-AE-SparseTri(n,D) with |W| query pairs.  If |W| ≤ n²/√D, then
the instance can be solved deterministically in O(n² log² D/D^{1/18}) time.  In general, [...] in
time O((n² + |W|√D) log² D/D^{1/18})." The general bound contains the first one, since
`|W|√D ≤ n²` there.  (As a statement about the existence of programs, this follows from
`Corollary_16`, whose bound is smaller; see the remark at `Theorem_5`.) 

### `Corollary_16`

 **Corollary 16**: "Let n ≥ D^18, and consider an instance of #Lop-AE-SparseTri(n,D) or
of Lop-AE-SparseTri(n,D) with |W| query pairs.  It can be solved deterministically in O(|W|
D^{0.437} + n²/D^{0.063}) time."

NOTE.  The paper states no lower bound on `D`; `D ≥ 1` is assumed, as in `Corollary_26` below. 

### `Theorem_19`

 **Theorem 19**: "For every constant ν ≥ 1, Exact Triangle on n vertices per part with
integer weights of absolute value at most n^ν can be solved by a deterministic algorithm in
O(n^{3−1/648} log² n) time [...], and in O(n^{3−ε'} log n) ≤ O(n^{3−ε_T}) time", with `ε' = 0.00175`
and `ε_T = 0.0017`.  (The paper reaches the first bound using Theorem 5 and the second using
Corollary 26.  This cannot be said by "there is a program": as statements about the existence of
programs, the first and the third bound follow from the second, which is smaller.) 

### `Theorem_22_first`

 **Theorem 22**, the bounds "Using Theorem 5": 3SUM in `O(n^{1.99923})` time, "and the
(min,+)-product [...] as well as APSP [...] in Õ(n^{3−1/1944}) ≤ O(n^{2.99949}) time".  (The
intermediate form `n^{2−1/1296+o(1)}` for 3SUM is `Theorem_22_threeSum` below.  "Using Theorem 5"
cannot be said by "there is a program": as statements about the existence of programs, all five
bounds follow from those of `Theorem_22_second`, which are smaller.) 

### `Theorem_22_second`

 **Theorem 22**, the bounds "Using Corollary 26 instead": 3SUM in `O(n^{1.9992})` time,
the (min,+)-product and APSP in "Õ(n^{3−ε'/3}) ≤ O(n^{2.99942})" time, with
`ε' = 0.00175`.  (The intermediate form `n^{2−ε'/2+o(1)}` for 3SUM is `Theorem_22_threeSum`
below.) 

### `Theorem_22_threeSum`

 **Theorem 22**, the two bounds for 3SUM before rounding: "Using Theorem 5 (through
Theorem 19), deterministic algorithms solve 3SUM on n integers of absolute value at most n^ν in
n^{2−1/1296+o(1)} ≤ O(n^{1.99923}) time [...].  Using Corollary 26 instead, the times are
n^{2−ε'/2+o(1)} ≤ O(n^{1.9992}) [...]", with `ε' = 0.00175`. The rounded bounds are in
`Theorem_22_first` and `Theorem_22_second`.  (As a statement about the existence of programs, the
first bound follows from the second, which is smaller.) 

 ### Section 4: Theorems 24 and 25, Corollary 26, Theorem 30, Corollaries 31 and 32 

### `thinDom`

 The hypotheses on the input in Corollaries 31 and 32 and Theorems 24 and 25: "where 2 ≤ D ≤
N^ε", with entries "of absolute value at most N^{O(1)}".  `lo` is the lower bound on `D`, which is 2
there.  (`N ≥ 1` follows if `lo = 2`; for `lo = 1` it excludes `N = 0`, `D = 1`, `ε = 0`, where the
bounds with the factor `N²` would be 0.) 

### `HasDataStructure`

 The conclusion of Theorem 24 and Corollary 31: there is a data structure for the inputs with
`2 ≤ D ≤ N^ε` with preprocessing in `O(N² log² D/D^γ)` time and space and queries in
`O(D^q log D)` time. 

### `Theorem_24`

 **Theorem 24**: "For every ε < ε*, and every q > 0, there is a γ > 0 such that the
following holds. Given as input matrices X ∈ ℤ^{N×D} and Y ∈ ℤ^{D×N}, where 2 ≤ D ≤ N^ε, whose
entries are integers of absolute value at most N^{O(1)}, we can preprocess them deterministically in
O(N² log² D/D^γ) time and space, after which any single entry (XY)[I,J] can be computed
deterministically in O(D^q log D) time." 

### `Theorem_25`

 **Theorem 25**: "For every ε < ε* and every κ > 0 there is a γ > 0 such that the
following holds. Given as input matrices [...], where 2 ≤ D ≤ N^ε, [...] as well as a set W of at
most N²/D^κ positions of an N × N matrix, the entries (XY)[I,J], (I,J) ∈ W, can be computed
deterministically in time O(N² log² D/D^γ)." 

### `Corollary_26`

 **Corollary 26**, first two sentences: "Let N ≥ D^18, and let X ∈ ℤ^{N×D} and Y ∈ ℤ^{D×N}
have entries of absolute value at most N^{O(1)}.  We can preprocess them deterministically in
O(N²/D^{0.063}) time and space, after which any single entry (XY)[I,J] can be computed
deterministically in O(D^{0.437}) time."

NOTE.  The paper states no lower bound on `D`; `D ≥ 1` is assumed (for `D = 0` the bound
`O(D^{0.437})` would be 0 steps). 

### `Corollary_26_wanted`

 **Corollary 26**, last sentence: "Hence, for every set W of positions of an N × N
matrix, the entries (XY)[I,J], (I,J) ∈ W, can be computed deterministically in O(|W| D^{0.437} +
N²/D^{0.063}) time".  (With `D ≥ 1`, as in `Corollary_26`.) 

### `theorem30Dom`

 The hypotheses of **Theorem 30**: "Let m ≥ 1, D = 4^m, L ≥ 10m, 0 ≤ t ≤ m, and N ≥ √K
N₀", with entries "of absolute value at most N^{O(1)}". 

### `Theorem_30`

 **Theorem 30**: "we can preprocess them deterministically in time and space" (8).  "After
this, any single entry (XY)[I,J] can be computed deterministically in O(L ∑_{d=0}^{t}
α_d) time."  "The constants hidden in the O(·) depend only on the exponent in N^{O(1)}": the
constant `C` is chosen after the exponent `c` and before `m`, `L`, `t`.  These parameters are given
to the preprocessing after `N` and `D`; the two programs do not depend on them. 

### `Theorem_30_wanted`

 **Theorem 30**, the offline form (9): "In particular, for every set W of positions of
an N × N matrix, the entries (XY)[I,J], (I,J) ∈ W, can be computed deterministically in time O(L |W|
∑_{d=0}^{t} α_d + L m ρ^t/(1 − ρ) N² + N·10^L/(√K N₀))." 

### `Corollary_31`

 **Corollary 31**: "Let c > 10 and 0 < θ < 0.9, let ρ_c := 9/(c−1), and let γ := θ
ln(1/ρ_c)/ln 4 > 0 and q := (H(θ) + θ ln 9)/ln 4.  Given as input matrices X ∈ ℤ^{N×D} and Y ∈
ℤ^{D×N} whose entries are integers of absolute value at most N^{O(1)}, where 2 ≤ D ≤ N^ε and ε <
R_c(γ), with R_c as in (11), we can preprocess them deterministically in O(N² log² D/D^γ) time and
space, after which any single entry (XY)[I,J] can be computed deterministically in O(D^q log D)
time.  The constants hidden in the O(·) depend on c, θ, and ε." 

### `DataStructureBelow`

 For every `ε < ε₀` and every `q > 0` there is a `γ > 0` such that, whenever `D ≤ N^ε`, the pair
can be preprocessed in `O(N²/D^γ)` time (and space), after which any single entry can be computed in
`O(D^q)` time.  The paper has this sentence with `ε₀ = 0.1204` (Theorem 3).

NOTE.  The paper states no lower bound on `D` and `N` here, and speaks of time only; `D ≥ 1` and
`N ≥ 1` are assumed, and the space is bounded like the time.  Theorem 24 has logarithmic factors and
assumes `D ≥ 2`; on the step from there Section 4.1 says: "The logarithmic factors in both theorems
can be removed by halving γ and applying Theorem 24 with q/2 in place of q; for D = 1 the bounds are
trivial." 

### `Corollary_32`

 **Corollary 32**: "Let c, θ, γ, q, X, Y, D, and ε be as in Corollary 31, and let κ > 0.
For every set W of at most N²/D^κ positions of an N × N matrix, the entries (XY)[I,J], (I,J) ∈ W,
can be computed deterministically in time O(N² log² D (D^{−γ} + D^{q−κ}))". 

### `WantedBelow`

 For every `ε < ε₀` and every `κ > 0` there is a `γ > 0` such that, whenever `D ≤ N^ε`, the
entries at any set of at most `N²/D^κ` positions can be computed in `O(N²/D^γ)` time.  The paper has
this sentence with `ε₀ = 0.1204` (Theorem 1).

NOTE.  The paper states no lower bound on `D` and `N` here; `D ≥ 1` and `N ≥ 1` are assumed.  On the
case `D = 1`, which Theorem 25 and Corollary 32 exclude, see the NOTE at `DataStructureBelow`. 

 ### Section 5: Corollaries 39 and 40 

### `Corollary_39_zero`

 **Corollary 39**, the case of Zero-Weight k-Clique.  The paper: "Let k ≥ 3 and ν ≥ 1 be
constants.  Given a complete k-partite graph with parts of n vertices and integer edge weights of
absolute value at most n^ν, deterministic algorithms decide in O(n^{k−ε_T⌊k/3⌋}) time whether some
k-clique, with one vertex in each part, has total edge weight zero". 

### `Corollary_39_min_max`

 **Corollary 39**, the other two cases: "deterministic algorithms [...] in
O(n^{k−ε_T⌊k/3⌋}) time [...] find a k-clique of minimum, or of maximum, total edge weight."  The
hypotheses are those of `Corollary_39_zero`; `ε_T = 0.0017` (Theorem 19).  That the time bound
covers finding, and not only deciding, is confirmed by the end of the paper's proof. 

### `Corollary_40_times`

 **Corollary 40**, the running times of its first paragraph (also in **Theorem 4**): for
Conjectures 5.2 and 5.7 and "every 0 < τ < 1/18: Phase 2 takes O(n^{2−0.063τ}) time and Phase 3
takes O(n^{1+0.437τ}) time"; for Conjecture 5.12 and "every 0 < τ₁ < τ₂/18: Phase 3 takes
O(n^{1+τ₂−0.063τ₁}) time and Phase 4 takes O(n^{τ₂+0.437τ₁}) time, with polynomial Phase 1 and a
Phase 2 that only stores I".  (Theorem 4 prints the first two bounds only.)

NOTE.  `τ₂ < 1` is assumed: it is the standing assumption of Section 5.4 ("for constants τ, τ_i ∈
(0,1)").  The words "only stores I" are read as `O(n^{τ₁})` time. 

### `Corollary_40_general_times`

 **The proof of Corollary 40**, paragraph "General τ": the running times.  (For this range the
corollary itself says only that the conjectures fail: `Corollary_40_fail`.)  For every `0 < τ < ε*`
there is a `γ > 0` with "Phase 2 in O(n²/D^γ) = O(n^{2−γτ}) time and Phase 3 in O(n D^{1/2}) =
O(n^{1+τ/2}) time"; and for every `0 < τ₁ < ε* τ₂` (and `τ₂ < 1`) there is a `γ > 0` with Phase 2 in
`O(n^{τ₁})`, Phase 3 in `O(n^{1+τ₂−γτ₁})` and Phase 4 in `O(n^{τ₂+τ₁/2})` time.

NOTE.  For Conjecture 5.12 ("we use the same blocks") the three bounds are those that the argument
gives, with `D^γ` and `D^{1/2}` in place of `D^{0.063}` and `D^{0.437}`.  On `τ₂ < 1` see the NOTE
at `Corollary_40_times`. 

### `Corollary_40_fail`

 **Corollary 40** (also **Theorem 4**), "fail": Conjectures 5.2 and 5.7 of
[vdBNS19], read as statements about programs of this machine, fail for every `0 < τ < τ₀`, and
Conjecture 5.12 fails for every `0 < τ₁ < τ₀ τ₂` (with `τ₂ < 1`), "whatever the value of ω".

The exponents of rectangular matrix multiplication are not defined here.  `ω`, `ω₂`, `ω₃` stand for
`ω(1,1,τ) = ω(1,τ,1)`, `ω(1,τ₁,1)`, `ω(τ₂,τ₁,1)`, and the statement is made for all real numbers
that satisfy the lower bounds of Corollary 40, "ω(1,1,τ) = ω(1,τ,1) ≥ 2 and ω(τ₂,τ₁,1) ≥ 1 + τ₂
because of the input and output sizes"; the bound `2 ≤ ω₂` is the first of these at `τ = τ₁`.  That
the true exponents satisfy these bounds is not proved here. The paper has `τ₀ = 1/18` in the first
paragraph, `ε*` in the second, and `0.1204` in Theorem 4.

NOTE.  `τ₂ < 1` is assumed; see the NOTE at `Corollary_40_times`. 

 ### Section 1, the introduction: Theorems 1 to 4 

### `Theorem_1`

 **Theorem 1**: "Let N ≥ D^18, let X ∈ ℤ^{N×D} and Y ∈ ℤ^{D×N} have entries of absolute
value N^{O(1)}, and let W be any set of |W| ≤ N²/√D positions.  The entries (XY)[I,J], (I,J) ∈ W,
can be computed deterministically in O(N²/D^{0.063}) operations on O(log N)-bit integers.  More
generally, for every ε < 0.1204 and every κ > 0 there is a γ > 0 such that, whenever D ≤ N^ε
and |W| ≤ N²/D^κ, the task takes O(N²/D^γ) operations."

NOTE.  The paper states no lower bound on `D`; `D ≥ 1` is assumed, and in the last sentence also
`N ≥ 1` (see `WantedBelow`). 

### `Theorem_2`

 **Theorem 2**, the deterministic half: "On a word RAM with O(log n)-bit words,
deterministic algorithms solve the following problems, where all numbers in the input are integers
of absolute value n^{O(1)}: Exact Triangle on n-vertex graphs in O(n^{2.9983}) time, APSP on
directed n-vertex graphs with no negative cycles in O(n^{2.9995}) time, the (min,+)-product of two
n × n matrices in O(n^{2.9995}) time, and 3SUM on n numbers in O(n^{1.9992}) time."  (For APSP and
the (min,+)-product, Theorem 22 prints the smaller exponent 2.99942: `Theorem_22_second`.)

NOTE.  Here Exact Triangle has the tripartite form of Section 3.2, with `n` vertices per part; for
`n`-vertex graphs see `Theorem_2_graphs`. 

### `Theorem_2_graphs`

 **Theorem 2**, first line, as printed: "Exact Triangle on n-vertex graphs in
O(n^{2.9983}) time". 

### `Theorem_3`

 **Theorem 3**: "Let N ≥ D^18, and let X ∈ ℤ^{N×D}, Y ∈ ℤ^{D×N} have entries of absolute
value N^{O(1)}. The pair (X,Y) can be preprocessed deterministically in O(N²/D^{0.063}) time [...].
After this, any single entry (XY)[I,J] can be computed deterministically in O(D^{0.437}) time [...].
More generally, for every ε < 0.1204 and every q > 0 there is a γ > 0 such that, whenever D ≤ N^ε,
the pair can be preprocessed in O(N²/D^γ) time, after which any single entry can be computed in
O(D^q) time."  The first part is `Corollary_26`.

NOTE.  The departures are those of the two definitions: `D ≥ 1` in the first part; `D ≥ 1` and
`N ≥ 1` in the second; and in both the space is bounded like the time, while the theorem speaks of
time only. 

### `Theorem_4`

 **Theorem 4**: "The v-hinted Mv, Mv-hinted Mv, and uMv-hinted uMv conjectures of
[vdBNS19] [...] are refuted in the regime of thin hints.  For hint dimension t = n^τ with 0 < τ <
1/18, the phase after the hint takes O(n^{2−0.063τ}) time and the phase after the vector
O(n^{1+0.437τ}) time [...]. Correspondingly, the uMv version [...] fails for τ₁ < τ₂/18.  All three
fail, with smaller savings, for every τ < 0.1204 (for the uMv version, τ₁ < 0.1204 τ₂)."  The three
parts follow the sentences of the theorem.  (The first contains also the running times of the uMv
version, which are printed in Corollary 40 only; the second follows from the third.)

NOTE.  For the uMv version `τ₂ < 1` is assumed; see the NOTE at `Corollary_40_times`. 
