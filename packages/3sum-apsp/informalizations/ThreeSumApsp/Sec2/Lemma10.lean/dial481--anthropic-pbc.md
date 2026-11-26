---
{
  "module": "ThreeSumApsp/Sec2/Lemma10.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma10.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma10.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sections 2.4.1 and 2.4.2: the encodings, the recursion `Pruned`, and Lemma 10

The encoding of an array is computed by `Full` with the other array left out (`computeEncoding_phi`,
`computeEncoding_psi`).  `Pruned(S)` is `Full` without that phase, and each call computes only the
outputs in the set `S` that is passed to it.  Lemma 10 (`lemma_10`) has three claims.

* Values.  One induction gives a closed form (`Pruned_eq_restrictTo_sum`): at a string of `S`,
  `Pruned` returns the sum, over the leaves contributing to the string, of the product of the two
  numbers looked up at the leaf.  With the encodings of `a` and `b` this sum is `Mult(a, b)` by
  definition (`Lemma10.values`), which is what `Full` returns by Lemma 7
  (`Pruned_eq_restrictTo_Full`).  The paper compares `Pruned` with `Full` level by level instead.
* Leaves visited.  A vertex below the root is called exactly if it contributes to a string of `U`
  (`Pruned.called_iff_root_or`, `Pruned.called_iff`; the step of the induction is
  `Pruned.called_succ`).  For leaves this is `Lemma10.leaves_visited`.  The set passed to a vertex
  consists of the suffixes of these strings (`Pruned.mem_passed_iff`; no later proof uses this).
* Total size.  A set of strings is no larger than its set of leaves, because a string is determined
  by its private leaf (`card_le_card_Leaves`), and the leaves of `Leaves(S)` that begin with
  `λ` are the leaves of `Leaves(S_λ)` with `λ` put in front (`card_Leaves_succ`).  So the
  sets passed at one depth have total size at most `|Leaves(U)|` (`Pruned.sum_card_passed_le`), and
  there are `L + 1` depths (`Lemma10.total_size`).

Which calls `Pruned` makes depends only on the set passed to it, so the second and the third claim
are proved for any two arrays in place of the two encodings.


 ### Section 2.4.1: the encodings 

### `computeEncoding`

 Section 2.4.1, the procedure that computes the encoding of `a`: "we run Full with b left out and
without step (4): […] the left number at the leaf τ is Φ_τ(a), and the leaf stores it." What is left
of `Full` is step (2) for `a`, the recursive calls of step (3), and at depth `L` the number that has
been reached. "The encoding of b […] is computed in the same way", so the procedure is written once,
for the coefficients `c` of any family of linear forms: `c = φ` for `a`, and `c = ψ` for `b`. 

### `computeEncoding_eq_encodeWith`

 At the leaf `τ` the procedure of Section 2.4.1 stores `∑_u a[u] ∏_ℓ c_{τ_ℓ}(u_ℓ)`. 

### `computeEncoding_phi`

 The procedure of Section 2.4.1 computes the encoding of `a`. 

### `computeEncoding_psi`

 The procedure of Section 2.4.1 computes the encoding of `b`. 

 ### Section 2.4.2: the sets `S_λ` of step (2) 

### `mem_sliceSet`

 Membership in a slice of a set of output strings. 

### `childSet_P`

 Section 2.4.2, step (2): "i.e., S_{P_ij} := S_{z_ij} ∪ S_{z₀}". 

### `childSet_P0`

 Section 2.4.2, step (2): "and S_{P₀} := S_{z₀}". 

### `sliceSet_subset_childSet`

 Section 2.4.2, step (4): "These restrictions make sense, since S_{z_ij} ⊆ S_{P_ij} and S_{z₀} ⊆
S_λ for every λ, by step (2)": `S_z ⊆ S_λ` whenever `λ` contributes to `z`. 

### `mem_childSet`

 In the proof of Lemma 10: "S_λ consists of the last L-k-1 variables of each string in S
such that λ contributes to the first variable of that string." 

 ### Lemma 10, first claim: the values 

### `restrictTo_of_mem`

 At a string of `S`, an array restricted to `S` has its own entry. 

### `restrictTo_empty`

 An array restricted to the empty set is the zero array. 

### `Pruned.childResult`

 The array `C_λ` of step (3) of `Pruned`; it is the zero array if `S_λ = ∅`. 

### `Pruned_succ`

 Steps (2) to (4) of `Pruned`, written out. 

### `Pruned_succ_apply`

 Step (4) of `Pruned` at one string: the entry at `w ∈ S` is the sum of the `C_λ`, at the rest of
`w`, over the terms `λ` that contribute to the first variable of `w`. 

### `Pruned_eq_restrictTo_sum`

 What `Pruned` returns, for arbitrary arrays in place of the two encodings: at each string of
`S`, the sum, over the leaves contributing to it, of the product of the two numbers looked up at the
leaf in step (1). 

### `Lemma10.values`

 **Lemma 10**, first claim.  "Let a and b be input arrays, and let U be a set of output
strings of length L. Called at the root, Pruned(U) returns Mult(a, b) restricted to U." 

### `Pruned_eq_restrictTo_Full`

 Section 2.4.2, the specification of `Pruned`: it "returns the array returned by the vertex
τ₁⋯τ_k of Full, restricted to the strings in S".  Here `a` and `b` are the input arrays of that
vertex: by `Phi_cons` and `Psi_cons`, applied once for each level, the parts of the two encodings
below a vertex are the encodings of its input arrays. 

 ### Lemma 10, second claim: the calls that are made and the sets passed to them 

### `Vertex.Contributes`

 Section 2.3.2: "a vertex τ₁ ⋯ τ_k contributes to an output string w if τ_ℓ contributes to w_ℓ at
every level ℓ ≤ k."  Only `k ≤ L` occurs; the hypothesis `h` is there so that `w_ℓ` makes sense. 

### `Vertex.contributes_iff_leaf`

 Section 2.3.2: for a vertex at depth `L`, that is, a leaf, "contributes to" means that `τ_ℓ`
contributes to `w_ℓ` at every level. 

### `Vertex.contributes_cons`

 The vertex `λ τ₁⋯τ_k` contributes to `w` if and only if `λ` contributes to the first variable of
`w` and `τ₁⋯τ_k` contributes to the rest of `w`. 

### `Pruned.childCalls`

 The calls made by the child `λ` of `Pruned(S)`: none if `S_λ = ∅`. 

### `Pruned.calls_succ`

 The calls made by `Pruned(S)`: the call itself, and the calls made by the children `λ` with
`S_λ ≠ ∅`. 

### `Pruned.mem_calls_succ`

 The calls of `Pruned(S)`, one level unfolded (steps (2) and (3)): the call itself, and for each
term `λ` with `S_λ ≠ ∅` the calls of `Pruned_λ(S_λ)`. 

### `PrunedCall.vertex_under_eq_iff`

 A call below the child `λ` is at the vertex `τ` of depth `k + 1` exactly if `λ` is the first
term of `τ` and, seen from the child, the call is at the rest of `τ`. 

### `Pruned.Called`

 `Pruned(U)`, called at the root, calls the vertex `τ`.  For a leaf this is `Pruned.Visits`. 

### `Pruned.called_root`

 The root is called. 

### `Pruned.called_succ`

 Step (3): a vertex `λ τ'` below the root is called exactly if `S_λ ≠ ∅` and the child `λ` calls
`τ'`. 

### `exists_contributes_childSet`

 The vertex `λ τ'` contributes to a string of `S` exactly if `τ'` contributes to a string of
`S_λ`. 

### `Pruned.called_iff_root_or`

 A vertex at depth `k ≤ L` is called by `Pruned(U)` if and only if it is the root or it
contributes to some string of `U` (proof of Lemma 10).  The induction follows the
recursion: the vertex `λ τ'` is called by `Pruned(U)` exactly if `τ'` is called by `Pruned(U_λ)`. 

### `Pruned.called_iff`

 In the proof of Lemma 10: "the vertex is called if and only if this set is nonempty",
that is, if and only if the vertex contributes to some string of `U`.

NOTE.  As printed this fails for the root when `U = ∅` (the root is always called).  The hypothesis
`hk` excludes only that case.  `hkL` says that `τ` is a vertex of the recursion tree, whose depth is
at most `L` (Section 2.3.1); the type `Vertex k` exists for every `k`. 

### `Pruned.depth_add_length`

 A call at depth `k` is passed strings of length `L - k`. 

### `IsSuffixFrom`

 `w'` is the suffix of `w` that is left when the first `k` variables are removed. 

### `isSuffixFrom_zero`

 Removing no variable leaves the string as it is. 

### `isSuffixFrom_succ`

 Removing `k + 1` variables is removing the first variable and then `k` more. 

### `mem_iff_root`

 The set passed to the root is `U`, and the root contributes to every string. 

### `Pruned.mem_passed_iff`

 Proof of Lemma 10 (announced in Section 2.4.2): "the set passed to the vertex τ₁⋯τ_k
consists of the suffixes w_{k+1}⋯w_L of the strings w of U to which the vertex contributes".  For a
call `c`, `c.vertex.1` is the depth `k`, `c.vertex.2` the vertex, `c.passed.1` the length `L - k` of
the strings passed, and `c.passed.2` the set passed. 

### `Lemma10.leaves_visited`

 **Lemma 10**, second claim.  "The leaves it visits are exactly those of Leaves(U)".  The
hypothesis `0 < L ∨ U.Nonempty` is explained at `lemma_10`. 

 ### Lemma 10, third claim: the total size of the sets passed 

### `mem_Leaves_succ`

 The leaf `λ τ'` is in `Leaves(S)` if and only if `τ'` is in `Leaves(S_λ)`. 

### `card_Leaves_succ`

 `Leaves(S)` is the disjoint union, over the terms `λ`, of the leaves `λ τ'` with `τ'` in
`Leaves(S_λ)`. 

### `privateLeaf_injective`

 Different output strings have different private leaves. 

### `card_le_card_Leaves`

 The map of the proof of Lemma 10, at the root: an output string goes to the leaf that
picks `P_ij` where the string has `z_ij` and `P₀` where it has `z₀`.  The leaf contributes to the
string and determines it, so a set of output strings is no larger than its set of leaves. 

### `sizeAt`

 The total size of the sets passed to the calls at depth `k` in a list of calls. 

### `sizeAt_cons`

 The size at depth `k` of a list of calls with one more call. 

### `sizeAt_bind`

 The size at depth `k` of the lists of calls of the ten children together. 

### `sizeAt_under_succ`

 Seen from one level higher, the calls at depth `k` are at depth `k + 1`. 

### `sizeAt_under_zero`

 Seen from one level higher, no call is at depth `0`. 

### `sum_sizeAt`

 The total size of the sets passed is the sum, over the depths, of the sizes at each depth. 

### `Pruned.sum_card_passed_le`

 End of the proof of Lemma 10: "the sets passed to the vertices at each of the L+1
depths have total size at most |Leaves(U)|." 

### `Lemma10.total_size`

 **Lemma 10**, third claim.  "the sets passed to the calls it makes have total size at
most (L+1) |Leaves(U)|." 

### `lemma_10`

 **Lemma 10**, its three claims together.  "Let a and b be input arrays, and let U be a
set of output strings of length L. Called at the root, Pruned(U) returns Mult(a, b) restricted to U.
The leaves it visits are exactly those of Leaves(U), and the sets passed to the calls it makes have
total size at most (L+1) |Leaves(U)|."

NOTE.  The hypothesis `0 < L ∨ U.Nonempty` of the second claim is not in the paper.  It excludes
only the case `L = 0`, `U = ∅`, in which the root is itself a leaf, so that the call at the root
visits it, while `Leaves(∅)` is empty.  In the paper `L ≥ m ≥ 1`, and `Pruned` is run only on
nonempty sets (Section 2.4.4). 
