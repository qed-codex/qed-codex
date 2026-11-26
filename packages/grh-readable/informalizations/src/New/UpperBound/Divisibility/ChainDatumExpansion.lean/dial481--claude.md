---
{
  "module": "src/New/UpperBound/Divisibility/ChainDatumExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainDatumExpansion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainDatumExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Two invariant sums of translates attached to a chain datum

A chain datum `Ψ` has a plain tensor `φ♭` and a glued tensor `Glue φ♭`, and the latter is jointly
invariant. Expanding the gluing writes `Glue φ♭` as a double sum of translates of the vacuum
(`IsChainDatum.gluedTensor_eq_sum_translates`), and collecting its terms gives a weak chain datum
(`IsChainDatum.exists_isWeakChainDatum_compositeLift_eq`); this serves for sums of norms and for the
primes `p ≠ N`. The projection on vacua above `N` takes `Glue φ♭` to `φ♭`, so `φ♭` is jointly
invariant too (`IsChainDatum.isWeakChainDatum`); this serves for `p = N`.

Notions from other files:
* `D : Data P`: a CM field `E` with `f` infinite places, spaces `X_0, …, X_m` over it in a chain of
  `m` theta lifts, `X_j` of rank `n_j`, and a prime level `N = π π̄` with `π = D.piN`.
* `D.piNPlaces`: the places `w ∣ π`.
* `D.X j = D.InitIndex j ⊕ Unit`: the basis indices of `X_j`; the last one is the `Unit` summand.
* A tuple of translations `t`: a finite adelic matrix `t j` for each `j`, with rows indexed by
  `X_{j+1}` and columns by `X_j`. It is admissible for `q` if each `t j`, times the conjugate of
  `D.piM`, is integral at the places prime to `q`.
* `D.translateDatum t j`: the integral vacuum of `Hom(X_j, X_{j+1})` translated by the matrix `t j`.
* `D.gluedDoubleLiftDatum v i`: the gluing, the sum over `y` modulo `N` of the translates of
  `v (2 i) ⊗ v (2 i + 1)` by the last column `-y / N` and the last row `-ȳ / N`.
* `plainTensor Ψ`, `gluedTensor Ψ`: the tensors `φ♭ = ∑ x, Ψ x • ⊗ⱼ translateDatum x j` and
  `Glue φ♭`.
* `IsAdmissibleCombination v A q d p B z`: `z = ∑ x, r x • v x` with `r` supported in `A`, each
  `d * r x` integral away from `q` and, if `p` holds, all conjugates of `r` of `ℓ¹`-norm at most
  `B`.
* `IsChainDatum ϑ Ψ`, `IsWeakChainDatum ϑ Ψ`: admissible coefficients whose glued, respectively
  plain, tensor is jointly invariant under the levels `D.levelX j`; the conditions on support and
  sum of norms are weaker for a weak chain datum.

## Relation to the literature

See `New.UpperBound.Divisibility.LocalDivisibility` for related work.


### `TameChar.normQ_notMem_of_N_mem`

 A place `w` above the level `N` does not divide `ϑ.normQ`, the product of the norms of the
places in the finite set `ϑ.Q` of the tame character `ϑ`. 

### `vacuumProjFinPart_translateDatum`

 Let `ϑ` be a tame character and `ϑ.normQ = q` the product of the norms of the places in its
finite set `ϑ.Q`. Let the tuple of translations `t` be admissible for `q`: each matrix `t j`, times
the conjugate of `D.piM`, is integral at the places prime to `q`. Then the projection on the vacuum
at the places of `D.piNPlaces` and their conjugates fixes the translate `D.translateDatum t j` of
the integral vacuum by `t j`. 

### `eq_zero_of_poleColumn_mem_integralBox`

 Let `y` be a vector on `X_{j+1}` of classes modulo `N` at each `w ∣ π`, and suppose that the
adelic matrix `poleColumn`, with last column `-y / N` at these places and all other entries `0`, is
integral at these places and their conjugates. Then `y = 0`. 

### `vacuumProjFinPart_gluedDoubleLiftDatum`

 Let `t` be a tuple of translations that is admissible for `ϑ.normQ`, the product of the norms of
the places in the set of the tame character `ϑ`. Gluing the `i`-th double lift means summing, over
the vectors `y` on `X_{2i+1}` of classes modulo `N` at each place `w ∣ π`, the translates of
`translateDatum t (2 i) ⊗ translateDatum t (2 i + 1)` by the last column `-y / N` and the last row
`-ȳ / N`. The projection on the vacuum at the places above `N`, applied to both factors of this sum
`D.gluedDoubleLiftDatum`, keeps only the term `y = 0`, so it undoes the gluing. 

### `heisenbergFinPart_translateDatum_of_disjoint`

 Let the tuple of translations `t` vanish at the places above `N` and let the matrix `z` vanish
at all other places, that is, outside `D.piNPlaces` and its conjugate. Then translating the integral
vacuum by `t j` and then by `z` is translating it by `z + t j`: as the supports are disjoint, there
is no phase. 

### `gluedDoubleLiftDatum_translateDatum`

 Let the translations `t` vanish at the places above `N`. Then `D.gluedDoubleLiftDatum` is a sum
over the vectors `y` on `X_{2i+1}` of classes modulo `N` at each place `w ∣ π` (`D.piNPlaces`). Its
term is the tensor of the translates of the integral vacuum by `t (2 i)` plus `poleColumn`, the
matrix with last column `-y / N` at the `w ∣ π`, and by `t (2 i + 1)` plus `poleRow`, the matrix
with last row `-ȳ / N` at their conjugates. 

### `GluingClasses`

 The index set of the gluing: for each of the `ϱ + 1 = m / 2` double lifts, a vector on the
middle space `X_{2 i + 1}` modulo `N` at each place `w ∣ π`. 

### `gluingTuple`

 The tuple of translations `z` attached to the classes `y`: in the `i`-th double lift, `z (2 i)`
has last column `-y i / N` and the last row of `z (2 i + 1)` is its conjugate; all other entries
are `0`. 

### `gluingTuple_mem_supportedTranslations`

 For each class `y` in `D.GluingClasses`, the tuple of translations `gluingTuple y` lies in
`D.supportedTranslations D.N`: it vanishes at all places prime to `N`. 

### `card_gluingClasses_le`

 A class of the gluing assigns a residue modulo `N` to each double lift `i`, basis index of
`X_{2i+1}` and place `w ∣ π`. There are at most `N ^ (f m n_m / 2)` of them. 

### `ungluedVacuum`

 The tensor `⊗ⱼ translateDatum t j` of the translates of the integral vacuum by `t`, grouped by
double lifts and not glued. 

### `plainTensor_eq_sum_ungluedVacuum`

 The plain tensor of `Ψ` is `∑ x, Ψ x • D.ungluedVacuum x`. 

### `gluedVacuum_eq_sum_translates`

 If the translations `t` vanish at the places above `N`, the glued tensor `D.gluedVacuum t` is
the sum, over the classes `y` of the gluing, of `D.ungluedVacuum (t + gluingTuple y)`: the tensors,
not glued, of the translates of the integral vacuum by `t + gluingTuple y`. 

### `add_mem_admissibleTranslations_mul_N`

 Adding a tuple `z` that vanishes at the places not above `N` to a tuple that is admissible for
`q` gives a tuple that is admissible for `q N`. 

### `isAdmissibleCombination_sum_ungluedVacuum`

 A class `y` of the gluing gives a residue modulo `N` for each double lift, middle basis index
and place `w ∣ π`, and `gluingTuple y` puts `-y / N` in the corresponding last columns and its
conjugate in the last rows. `D.ungluedVacuum t` is the tensor product over `j` of the translates of
the integral vacuum by `t j`.

Let the tuple `t` be admissible for `q`: each `t j`, times the conjugate of `D.piM`, is integral at
the places prime to `q`. Then the sum of `D.ungluedVacuum (t + gluingTuple y)` over all classes `y`
equals `∑ x, r x • D.ungluedVacuum x` with `r` supported on tuples admissible for `q N`. The values
of `r` are integral away from `q` with denominator `1`, and all conjugates of `r` have `ℓ¹`-norm at
most `N ^ (f m n_m)`. The norm bound is only asked when `boundRequired` holds. 

### `isJointlyInvariant_of_plainTensor`

 Suppose that the plain tensor `∑ x, Ψ x • ⊗ⱼ translateDatum x j`, with the factors grouped in
pairs `2 i, 2 i + 1` (the double lifts), is fixed by every tuple `b j ∈ D.levelX j` with `b m = 1`.
Then the same sum, with `m` single factors, is jointly invariant: for every tuple `b` with `b j = 1`
for all `j ≥ m` and every linear map from the `m`-fold tensor product to the functions on the Weyl
indices of `X_m`, the sum before and after the action of `b` has the same image. 

### `TameChar.M_mul_normQ_notMem_of_N_mem`

 A place `w` above the level `N` divides neither the principal level `D.M` nor `ϑ.normQ`, the
product of the norms of the places in the finite set `ϑ.Q` of the tame character `ϑ`. 

### `IsChainDatum.gluedTensor_eq_sum_translates`

 **Expanding the gluing.** Fix admissible data `D`: a CM field `E` with `f` infinite places, a
chain of `m` theta lifts `X_0 → ⋯ → X_m` with `X_j` of rank `n_j`, and a prime level `N = π π̄`. A
twist `ϑ` is a character of `U(1)(𝔸)` of weight `0` with tame part non-trivial exactly at a finite
set of places of norm prime to `N`. A tuple of translations (`D.Translations`) is a finite adelic
matrix for each lift. A chain datum `Ψ` for `ϑ` is a finitely supported coefficient function on such
tuples, with bounded support and size, whose glued tensor `gluedTensor Ψ` (its tensor, glued in each
double lift) is invariant.

Then `gluedTensor Ψ` is the double sum, over `x` and over the classes `y` in `D.GluingClasses` (a
residue modulo `N` for each double lift, middle basis index and place above `π`), of `Ψ x` times
`D.ungluedVacuum (x + gluingTuple y)`, the tensor product over the lifts of the integral vacuum (a
fixed scalar multiple of the vacuum vector of `Hom(X_j, X_{j+1})`) translated by
`x + gluingTuple y`. There are at most `N ^ (f m n_m / 2)` classes `y`, and the tuples
`gluingTuple y` vanish at the places not above `N`. 

### `IsChainDatum.exists_isWeakChainDatum_compositeLift_eq`

 Every chain datum `Ψ` has a weak chain datum `Ψ'`, obtained by expanding the gluing, such that
on every source form `φ` (a form on `X_0` of level `D.levelX 0`) the two composite lifts agree:
`compositeLift ϑ Ψ φ`, which lifts `φ` through the double lifts with the glued tensor of `Ψ` as data
and restricts the result from `X_m` to its subspace `Y_m`, equals `restrictedChain ϑ Ψ' φ`, the
combination `Ψ'` of chains of `m` single lifts, restricted in the same way. 

### `IsChainDatum.isInvariant_plainTensor`

 Let `ϑ` be a twist and `Ψ` a chain datum for `ϑ`: coefficients on tuples `x` of translation
matrices whose glued tensor is invariant. Then the plain tensor
`φ♭ = ∑ x, Ψ x • ⊗ⱼ translateDatum x j` of the translated integral vacua is invariant too: under the
Weil actions of the theta kernels `D.liftKernel ϑ`, every tuple `b j ∈ D.levelX j` with `b m = 1`
fixes it. 

### `IsChainDatum.isWeakChainDatum`

 Here `D` is admissible data with scale `x = D.x` and prime level `N`. `ϑ` is a twist: a
weight-`0` character whose tame part is non-trivial exactly at the places of the finite set `ϑ.Q`.
Also `q = ϑ.normQ`, the product of their norms. A chain datum `Ψ` for `ϑ` is a weak chain datum.
That is: the tuples of translations in its support are admissible for `q N`, its values are integral
away from `q`, their conjugates have `ℓ¹`-norm at most `exp (x ^ 60)` if `ϑ.Q` is empty, and its
plain tensor `∑ x, Ψ x • ⊗ⱼ translateDatum x j`, with no gluing, is invariant under all the levels
`D.levelX j` at once. 
