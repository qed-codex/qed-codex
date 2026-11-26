---
{
  "module": "src/Lib/LocalGL/Iwahori/QuadraticRelation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/QuadraticRelation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/QuadraticRelation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quadratic relation and injectivity of U_t at pro-p Iwahori level

Let `ρ` be a smooth representation of `GL_N(F)`, where `F` has compact ring of integers and a
uniformiser `ϖ`. This file shows that conjugation by a monomial matrix carries one parahoric
subgroup into another. With this it proves the quadratic relation for a simple transposition.
It shows that some operator `U_t` with `t` strictly dominant is injective on the vectors fixed by
`New.proIwahori`. For an exponent, it shows that the mean over `New.proIwahori` in the defining
identity can be dropped at diagonal matrices of units and at certain monomial translates.

## Main definitions and results

* `New.quadratic_relation`: the quadratic relation for a simple transposition.
* `New.exists_iwahoriHeckeHom_injective`: some operator `U_t` with `t` strictly dominant is
  injective on the vectors fixed by `New.proIwahori`. Here `U_t = New.iwahoriHeckeHom ρ t` sends
  such a vector `x` to the mean over `New.proIwahori` of `ρ(diag t) x`.

Notions from other files:
* `New.proIwahori`: The pro-p Iwahori subgroup I₁ of GL_n(𝒪): matrices that are upper triangular
  with ones on the diagonal modulo the maximal ideal.
* `New.dominantTorus`: Dominant elements of the diagonal torus: the `t` with `v (t i) ≤ v (t j)` for
  `i ≤ j`.
* `New.IsExponent`: `l (ρ(t) (mean of x over proIwahori)) = ξ(t) l(x)` for all dominant diagonal `t`
  and all `x`.

## Relation to the literature

Known; see `Lib.LocalGL.Iwahori.SphericalExponents` for sources.



## Monomial matrices and the quadratic relation

Conjugation by a monomial matrix carries one parahoric subgroup into another
(`New.conj_monomial_mem_blockParahoric`); with it the file proves the quadratic relation for a
simple transposition.


### `mem_blockParahoric`

 An element `g` lies in `New.blockParahoric c` iff it lies in `GL_N` of the valuation ring and
its entry `g i j` has valuation less than 1 whenever `c j < c i`. 

### `mem_proIwahori_iff_blockParahoric`

 An element lies in `New.proIwahori` iff it lies in the parahoric `New.blockParahoric id` and
every diagonal entry is congruent to 1 modulo the maximal ideal. 

### `conj_monomial_mem_blockParahoric_of_mem`

 Let `c` and `d` be level functions `ℕ → ℕ` (see `New.blockParahoric`), and let `g` lie in the
parahoric of level function `d`. Let `m = σ diag(t)`, with `σ` a permutation matrix. Suppose that
for all `a`, `b` either `g_{σa,σb} = 0` or
`log v(t_b) + [c(b) < c(a)] ≤ log v(t_a) + [d(σb) < d(σa)]`, where `log` gives the integer exponent
of a valuation. Then `m⁻¹ g m` lies in the parahoric of level function `c`. 

### `conj_monomial_apply_self_mem`

 The diagonal entries of `m⁻¹ g m`, for `m = σ diag(t)`, are those of `g`, permuted by `σ`; so
they lie in every set `S` that holds the diagonal entries of `g`. 

### `conj_monomial_mem_blockParahoric`

 Let `g` lie in the parahoric of level function `d`, with diagonal entries in `S`, and let
`m = σ diag(t)` satisfy the condition of `New.conj_monomial_mem_blockParahoric_of_mem`. Then
`m⁻¹ g m` lies in the parahoric of level function `c`, with diagonal entries in `S`. 

### `transvectionGL_apply_permGL_inv`

 If `x` is fixed by `New.proIwahori` and `σ a < σ b`, then `ρ(σ⁻¹) x` is fixed by `1 + c E_ab`
for integral `c`. 

### `proIwahori_le_blockParahoric`

 If `c j < c i` forces `j < i`, as it does for monotone `c`, then the pro-`p` Iwahori subgroup
lies in the parahoric subgroup for the blocks of `c`. 

 ### The quadratic relation 

### `swap_mul_transvectionGL`

 The factorisation `s (1 + u E_ab) = (1 + u⁻¹ E_ab) d (1 + u⁻¹ E_ba)`, for `s` the transposition
of `a` and `b` and `d` diagonal with `-u⁻¹` at `a`, `u` at `b` and `1` elsewhere. 

### `exists_swap_conj_mem_proIwahori`

 For adjacent indices (`h : a ⋖ b`, that is `b = a + 1`) and `g` in `New.proIwahori` there is an
integral `c` such that the transposition of `a` and `b` conjugates `g (1 + c E_ab)` into
`New.proIwahori`. 

### `v_mulSingle_neg_inv_mul_mulSingle_eq_one`

 If `v u = 1`, every entry of the diagonal torus element with `-u⁻¹` at `a`, `u` at `b` and `1`
elsewhere has valuation `1`. 

### `quadratic_relation`

 The quadratic relation. Let `b = a + 1`, let `s` be the transposition of `a` and `b`, `q` the
order of the residue field, and `φ` a linear map invariant under `New.proIwahori`. Let `x` be fixed
by all `1 + r E_ba` with `r` integral. Let `φ (ρ(d) x) = c` for every diagonal `d` with `-u⁻¹` at
`a`, `u` at `b` and `1` elsewhere, where `v u = 1`. Then
`q φ (s (mean of x over New.proIwahori)) = φ (s x) + (q - 1) c`. 


## Injectivity of some U_t, and invariance properties of exponents

Some `U_t` with `t` strictly dominant is injective. For an exponent, the mean over `New.proIwahori`
in its defining identity can be dropped in two cases: at diagonal matrices of units
(`New.IsExponent.apply_diagGL_unit`) and at certain monomial translates
(`New.IsExponent.apply_diagGL_apply_diagGL_mul_permGL`).


### `diagGL_conj_mem_proIwahori_of_v_eq_one`

 A diagonal matrix whose entries are units of the ring of integers conjugates every element of
`New.proIwahori` into `New.proIwahori`. 

### `exists_iwahoriHeckeHom_injective`

 Let `F` have a uniformiser `ϖ` (`v ϖ = exp (-1)`) and let `ρ` be a smooth representation of
`GL_N(F)`. For dominant diagonal `t`, `U_t = iwahoriHeckeHom ρ t` acts on the vectors fixed by the
pro-`p` Iwahori subgroup `New.proIwahori`: it applies `ρ (diagGL t)` and then takes the mean
`compactMean` over `proIwahori`. There is a strictly dominant `t` (the valuations `v (t i)`, written
multiplicatively, strictly increase) such that `U_t` is injective. It is a case of the Moy–Prasad
and Morris injectivity of fixed vectors into the Jacquet module. 

 ### Exponents 

### `IsExponent.apply_compactMean`

 An exponent `l` (with character `ξ`) does not change under the mean over `New.proIwahori`:
this is its defining identity at `t = 1`. 

### `IsExponent.apply_proIwahori`

 An exponent `l` (with character `ξ`) is invariant under `New.proIwahori`:
`l (ρ k z) = l z` for `k` in `New.proIwahori`. 

### `IsExponent.apply_diagGL_unit`

 Let `l` be an exponent with character `ξ`, and let `t` be a diagonal element all of whose
entries are units of the ring of integers. Then `l (ρ(diag t) z) = ξ(t) · l z` for every vector `z`,
so the mean over `New.proIwahori` can be dropped. 

### `IsExponent.apply_diagGL_apply_diagGL_mul_permGL`

 Let `ρ` be a smooth complex representation of `GL_N(F)`, and let `l` be an exponent with
character `ξ`: `l (ρ(t) (mean of z over New.proIwahori)) = ξ(t) l z` for all vectors `z` and all
dominant diagonal `t`. Let `y` be fixed by a subgroup `K` containing every `g` of
`blockParahoric c` (entries `g i j` in the maximal ideal whenever `c j < c i`) whose diagonal
entries are `≡ 1` mod the maximal ideal; let `σ` be a permutation, `s` a diagonal torus element
and `d` dominant, and suppose that for `σ b < σ a` either `v s_{σ b} ≤ v s_{σ a}`, or `c a ≤ c b`
and `v s_{σ b} ≤ v s_{σ a} · exp 1`. Then at `x = ρ(diagGL s · permGL σ) y` the mean over
`New.proIwahori` can be dropped: `l (ρ(diagGL d) x) = ξ(d) l x`. 

### `IsExponent.apply_monomial_translate`

 The value of an exponent `l` of character `ξ` on monomial translates. Let `y` be fixed by a
subgroup `K` that contains the elements of the parahoric of level function `c` (integral `g` with
`v (g i j) < 1` whenever `c j < c i`) with diagonal entries `≡ 1`. Suppose that for `σ b < σ a`
either `v t_{σ b} ≤ v t_{σ a}`, or `c a ≤ c b` and `v t_{σ b} ≤ v t_{σ a} · exp 1`. Then
`l (ρ(t) ρ(σ) y) = ξ(t) l (ρ(σ) y)`. Here `ϖ` is a uniformiser (`hϖ`). 
