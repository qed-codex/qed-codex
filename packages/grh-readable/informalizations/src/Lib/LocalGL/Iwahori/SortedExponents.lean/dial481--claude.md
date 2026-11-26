---
{
  "module": "src/Lib/LocalGL/Iwahori/SortedExponents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/SortedExponents.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/SortedExponents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sorted exponents at pro-p Iwahori level

Let `ρ` be a smooth representation of `GL_N(F)`, where `F` has compact ring of integers and a
uniformiser `ϖ` with `v ϖ = exp (-1)`. An exponent is sorted when the absolute values `‖θ i ϖ‖` of
its characters do not increase. This file shows that the characters of an exponent that is nonzero
on a suitable pro-p Iwahori fixed vector (see `New.IsExponent.exists_sorted`) can be reordered so
that it is sorted, and that for unitary `ρ` an eigenvector in a span of translates with
finite-dimensional pro-p Iwahori fixed part gives an exponent. Let `ρ` be unitary, and let the
vectors fixed by `New.proIwahori` in the span of the translates of any vector form a
finite-dimensional space. For such `ρ`, this file constructs eigenvectors with sorted characters. It
does so from a vector of parahoric type and from a vector with a nonzero projection along characters
of determinants.

## Main definitions and results

* `New.IsExponent.exists_sorted`: the characters of an exponent nonzero on a pro-p Iwahori fixed
  `τ`-eigenvector `x` of the integral torus, which permutations preserving `τ` scale, can be
  reordered so that the absolute values `‖θ i ϖ‖` do not increase.
* `New.IsIwahoriEigen.exists_isExponent`: in the unitary case an eigenvector in a span of translates
  with finite-dimensional pro-p Iwahori fixed part gives an exponent.
* `New.exists_sorted_isIwahoriEigen_of_diagGL_smul`, `New.exists_sorted_of_detChar`: eigenvectors
  with sorted characters, from a vector of parahoric type and from a vector with a nonzero
  projection along characters of determinants.

Notions from other files:
* `New.proIwahori`: The pro-p Iwahori subgroup I₁ of GL_n(𝒪): matrices that are upper triangular
  with ones on the diagonal modulo the maximal ideal.
* `New.dominantTorus`: Dominant elements of the diagonal torus: the `t` with `v (t i) ≤ v (t j)` for
  `i ≤ j`.
* `New.IsExponent`: `l (ρ(t) (mean of x over proIwahori)) = ξ(t) l(x)` for all dominant diagonal `t`
  and all `x`.
* `New.IsIwahoriEigen`: x is a nonzero vector fixed by the pro-p Iwahori subgroup I₁ with
  `U_t x = ξ(t) x` for all dominant t, where `U_t` is `ρ(t)` followed by the mean over I₁.
* `New.torusChar`: For characters θ_i of Fˣ, the character t ↦ ∏ θ_i(t_i) |t_i|^(N-1-i) of the
  diagonal torus.

## Relation to the literature

Known; see `Lib.LocalGL.Iwahori.SphericalExponents` for sources.



## Sorting exponents, and sorted exponents from a parahoric type

The vector `x` is fixed by `New.proIwahori`, and the integral torus acts on it by `τ`. Every
permutation matrix whose permutation preserves the values of `τ` on units at each index acts on `x`
by a scalar. By the roots of an exponent for `torusChar θ` we mean the values `θ i ϖ`.

* `New.IsExponent.exists_sorted`: an exponent that is nonzero at `x` can be moved, along a
  permutation, to one whose roots `θ i ϖ` do not increase in absolute value.
* `New.IsIwahoriEigen.exists_isExponent`: for unitary `ρ`, an eigenvector of the operators
  `iwahoriHeckeHom ρ t` gives an exponent.
* `New.exists_sorted_isIwahoriEigen_of_diagGL_smul`: let `ρ` be unitary, and let the
  `New.proIwahori`-invariants in the span of the translates of `x` have finite dimension. Then a
  nonzero such `x` gives an exponent, and an eigenvector for a reordering of its characters sorted
  by the absolute values `‖θ i ϖ‖`.


### `_root_.Fin.rev_val_eq_rev_val_add_one_of_covBy`

 If `j` is the successor of `i` in `Fin n`, then `i.rev` is the successor of `j.rev`. 

### `torusChar_comp_swap`

 Exchanging two neighbouring components of `θ` in `torusChar θ` amounts to exchanging the entries
of the argument, up to the factor `normAbsChar (t i / t j)`. Here `normAbsChar` is the absolute
value `|·|` whose powers occur in `torusChar θ t = ∏ i, θ i (t i) * |t i| ^ (N - 1 - i)`. 

### `transvectionGL_apply_diagGL_compactMean`

 A transvection moves past a diagonal matrix with its entry rescaled; if the rescaled
transvection lies in `proIwahori`, it is absorbed by the mean. 

### `IsExponent.apply_permGL_swap_diagGL_compactMean`

 After the exchange of two neighbours `i`, `j`, an exponent still satisfies its defining
identity, for the exchanged character, at the dominant `t` with `t i / t j` of order at most `1`. 

### `stepTorus`

 The torus element with `ϖ` at the indices before `j` and `1` from `j` on. 

### `stepTorus_mem_dominantTorus`

 For a uniformiser `ϖ`, `stepTorus ϖ j` is dominant: the order of its entries drops by one
from `j - 1` to `j` and nowhere else. 

### `stepTorus_comp_swap`

 For `i < j`, exchanging the entries `i` and `j` of `stepTorus ϖ j` moves one factor `ϖ`
from the index `i` to the index `j`. 

### `div_stepTorus_mem_dominantTorus`

 Let `ϖ` be a uniformiser, `j = i + 1`, and `t` dominant with `v (t i) < v (t j)`. Then
`t / stepTorus ϖ j` is still dominant. 

### `IsExponent.apply_permGL_swap_compactMean_of_forall_transvectionGL`

 Let `l` be an exponent and `j = i + 1`. On a vector `z` fixed by the transvections `1 + a E_ij`
with `a` integral, the form `l ∘ ρ (swap i j)` does not see the mean over `New.proIwahori`. 

### `IsExponent.quadratic_relation_stepTorus`

 The quadratic relation at the vector `U_w z`, for `w = stepTorus ϖ j` and `j = i + 1`. Here
`U_w` is the mean over `New.proIwahori` followed by `ρ (diagGL w)`, and `q` is the order of the
residue field. Let `l` be an exponent for `ξ` that takes the value `κ` at the translates of `U_w z`
by the diagonal `d` with `-u⁻¹` at `i`, `u` at `j` and `1` elsewhere, for units `u`. Then
`q l (s (mean of U_w z)) = ξ (w ∘ swap i j) l (s (mean of z)) + (q - 1) κ`, with `s = ρ (swap i j)`.


### `IsExponent.swap_compactMean_apply_diagGL_of_apply_eq_zero`

 Let `l` be an exponent for `torusChar θ`, let `j = i + 1` and let `z` lie in the kernel of
`l`. Then the form `l ∘ ρ (swap i j) ∘ (mean over New.proIwahori)` is an eigenform at `z` of
the operator `U_t` (the mean followed by `ρ (diagGL t)`) for dominant `t`, with the exchanged
character `torusChar (θ ∘ swap i j)`. 

### `IsExponent.apply_mulSingle_eq_or_apply_permGL_inv_eq_zero`

 Let `l` be an exponent for `ξ`, and let each integral diagonal matrix `diagGL t` act on `x` by
the scalar `τ t`. For an index `b`, a unit `ε` and a permutation `σ'`, either `ξ` at `mulSingle b ε`
equals `τ` at `mulSingle (σ' b) ε`, or `l` vanishes at `ρ (permGL σ'⁻¹) x`. 

### `IsExponent.apply_permGL_swap_compactMean_ne_zero`

 Let `l` be an exponent for `ξ`, let `j = i + 1`, let `x` be fixed by `New.proIwahori`, and put
`y = ρ (permGL (σ * swap i j)⁻¹) x`. If `l` vanishes at `y` but not at `ρ (swap i j) y`, then
`l ∘ ρ (swap i j)` does not vanish at the mean of `y` over `New.proIwahori`. 

### `IsExponent.exists_sorted`

 Sorting an exponent. Let `ϖ` be a uniformiser, let `x` be fixed by `New.proIwahori` (`hx`), let
the integral torus act on `x` by `τ` (`hτ`), and let every permutation matrix whose permutation
preserves `τ` on units act on `x` by a scalar (`hP`). Let `l` be an exponent for `torusChar θ` with
`l x ≠ 0`. Here an exponent (`IsExponent`) for `ξ` is a form with
`l (ρ t (mean of y over I₁)) = ξ t * l y` for dominant diagonal `t`, and `torusChar θ t = ∏ i, θ i
(t i) * |t i| ^ (N - 1 - i)`. Then there is a permutation `σ` such that (a) some exponent for
`torusChar (θ ∘ σ)` is nonzero at `ρ (permGL σ⁻¹) x`, and (b) `‖θ (σ i) ϖ‖` does not increase in
`i`.

A special case of the Bernstein–Zelevinsky results on cuspidal exponents: a torus exponent nonzero
on a pro-p-Iwahori-fixed vector with a type can be permuted so that |θ_i(ϖ)| is non-increasing. 

### `IsExponent.eventually_apply_diagGL_pow_eq_zero`

 Let `x` be fixed by `New.proIwahori`, let `l` be an exponent for `torusChar θ` that vanishes at
every permuted vector `ρ (permGL σ) x`, and let `s` be strictly dominant. Then for every `z` in the
span of the translates of `x`, `l` vanishes at `ρ (diagGL (s ^ n)) z` for all large `n`. 

### `exists_mul_powers_eq_of_strictMono`

 Let `s` be strictly dominant. Every torus element `t` becomes dominant when multiplied by a
power of `s`: `t * s ^ k` is dominant for some `k`, in the form that
`MonoidHom.toLocalizationMap` asks for. 

### `IsIwahoriEigen.exists_isExponent`

 An eigenvector gives an exponent. Let `ρ` be a smooth representation of `GL_N(F)` with a
positive definite invariant form `B` (`hB`), and suppose the I₁-invariants (`New.proIwahori`) in the
span of the translates of `x` are finite-dimensional. If this span contains a non-zero I₁-fixed `y`
with `U_t y = ξ(t) y` for all dominant `t` (`U_t` = mean over I₁ after `ρ (diagGL t)`), then it
contains a `w` with `B w w ≠ 0` such that `B w` is an exponent for `ξ`, i.e.
`B w (ρ(t) (mean of z over I₁)) = ξ(t) B w z` for all `z` and dominant `t`; as `B` is positive
definite, `B w w ≠ 0` says `w ≠ 0`. 

### `exists_sorted_isIwahoriEigen_of_diagGL_smul`

 Let `ρ` be unitary (`hB`), `ϖ` a uniformiser, and `x ≠ 0` fixed by `New.proIwahori`, where the
span of the translates of `x` has finite-dimensional `proIwahori`-invariants. Let the integral torus
act on `x` by `τ` (`hτ`), and let each permutation matrix whose permutation preserves `τ` on units
act on `x` by a scalar (`hP`). Then some `θ` has (a) an exponent for `torusChar θ` nonzero at `x`,
that is, a form `l` with `l (ρ t (mean of y over I₁)) = torusChar θ t * l y` for dominant diagonal
`t`; (b) `θ i ε = τ (mulSingle i ε)` for units `ε`; (c) a `σ` with `‖θ (σ i) ϖ‖` not increasing, and
a nonzero `I₁`-fixed `y` in the span of translates of `x` with
`(mean over I₁) (ρ t y) = torusChar (θ ∘ σ) t • y` for dominant `t`. 


## Sorted exponents from distinct characters of determinants

Let `x` be a vector of a smooth unitary representation of `GL_N(F)` that is fixed by the principal
congruence subgroup, so that `GL_N` of the residue field acts on the span of its translates by
`GL_N` of the valuation ring. If `x` has a nonzero projection along a product, in the sense of
parabolic induction (`New.Hall`), of distinct characters of determinants (`New.detChar`), then the
span of its translates contains a sorted eigenvector for the pro-`p` Iwahori operators, provided
that the pro-`p` Iwahori invariants of every cyclic subrepresentation have finite dimension
(`New.exists_sorted_of_detChar`). The proof passes to a vector on which a parahoric subgroup acts by
a character and applies `New.exists_sorted_isIwahoriEigen_of_diagGL_smul`.


### `New.exists_monovary_card_fiber`

 An index set ordered by `e` can be cut into consecutive blocks of prescribed sizes `m a`: there
is a map `b` to the blocks that grows with `e` (`Monovary e b`) and whose fibre over `a` has `m a`
elements. 

### `New.reindexGL_symm_mem_intGL`

 Reading a matrix of `GL (Fin N)` of the valuation ring along `e : n ≃ Fin N` gives a matrix of
`GL n` of the valuation ring. 

### `New.exists_reindexGL_apply_eq_smul_of_finsum_ne_zero`

 Let `x` be fixed by the integral matrices that reduce to `1`, and `s` a lift of `GL n` of the
residue field to the valuation ring. Let the sum in `h_sum_ne`, against the product of the
characters `χ a ∘ det` in the sizes of the fibres of `b` (`rankPart k` takes the part on `GL_k`,
`evalGL g` the value at `g`), be nonzero. Then the span of the translates of `x` contains a nonzero
`y` on which each integral `g` whose reduction lies in `parabolic b` acts by the product of the
`χ a` of the determinants of its diagonal blocks. 

### `New.blockTriangular_intGL_map_reindexGL_symm_of_valuation_lt_one`

 Let `g` be a matrix of `GL (Fin N)` of the valuation ring whose entry `(i, j)` has valuation
less than `1` whenever `c (e⁻¹ j) < c (e⁻¹ i)`. Then `g`, read as a matrix indexed by `n` and
reduced modulo the maximal ideal, is block upper triangular for `c`. 

### `New.reindexGL_apply_eq_prod_smul_of_blockTriangular`

 Let `b` grow with the order `e` (`Monovary e b`), and let each integral `g` whose reduction
lies in `parabolic b` act on `y` by the product of the `χ a` of the determinants of its diagonal
blocks. Then each integral `g` whose reduction is upper triangular for the order `e` acts on `y` by
the product of the `χ (b i)` of the diagonal entries of its reduction. 

### `New.mem_levelSpace_proIwahori_of_forall_apply_eq_prod_smul`

 Let every integral `g` that is upper triangular modulo the maximal ideal act on `y` by the
product of the `f i` of the residues of its diagonal entries, where `R : F → 𝓀[F]` extends the
residue map. Then `y` is fixed by `New.proIwahori`. 

### `New.apply_eq_prod_smul_of_valuation_lt_one`

 Let `R : F → 𝓀[F]` extend the residue map, let `b` grow with the order `e`, and let each
integral `g : intGL n 𝒪[F]` whose reduction lies in `parabolic b` act on `y` by the product of the
`χ a` of the determinants of its diagonal blocks. Then each `g` in `GL (Fin N)` of the valuation
ring that is upper triangular modulo the maximal ideal acts on `y` by the product of the
`χ (b (e⁻¹ i))` of the residues `R (g i i)` of its diagonal entries. 

### `New.eq_of_forall_mulChar_residue_eq`

 If `χ` is injective and the characters `χ a` and `χ a'` of the residue field agree at the
residue of every unit of the valuation ring, then `a = a'`. 

### `Polynomial.prod_X_sub_C_eq_prod_pow_of_card_fiber`

 If `f i = g (c i)` for every `i` and the fibre of `c` over `a` has `m a` elements, then the
monic polynomial with the roots `f i` is `∏ a, (X - g a) ^ m a`. 

### `New.exists_sorted_of_detChar`

 Let `ρ` be smooth and unitary (`B` is an invariant scalar product), with finite-dimensional
`New.proIwahori`-invariants in each cyclic subrepresentation, and let `ϖ` be a uniformiser. Let the
characters `χ a` of the residue field be distinct and `∑ m a = N`, and let `Y` be the Hall-algebra
(`New.Hall`) product of the class functions `χ a ∘ det` on matrices of size `m a`. Let `x` be fixed
by the integral matrices that reduce to `1`, let `s` be a section of the reduction map, and suppose
`∑ conj (Y g) • ρ (s g) x ≠ 0`; here matrices are indexed by `n` and moved to `Fin N` along `e`.
Then the span of the translates of `x` contains a nonzero `New.proIwahori`-fixed `y` with
`(mean over I₁) (ρ t y) = torusChar θ t • y` for all dominant diagonal `t` (`New.IsIwahoriEigen`),
where `torusChar θ t = ∏ i, θ i (t i) * |t i| ^ (N - 1 - i)`, and `‖θ i ϖ‖` does not increase with
`i`. There is also a labelling `c` of the indices, taking each label `a` exactly `m a` times, such
that `θ i t` is `χ (c i)` of the residue of `t` for every unit `t`. 
