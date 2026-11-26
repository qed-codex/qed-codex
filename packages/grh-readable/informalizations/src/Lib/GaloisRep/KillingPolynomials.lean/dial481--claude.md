---
{
  "module": "src/Lib/GaloisRep/KillingPolynomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/KillingPolynomials.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/KillingPolynomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Free cocharacter weights force rank n and identify killing polynomials

A Galois representation that is only known to be killed, for most Frobenius elements (the filter
`New.mostFrobenii`), by monic polynomials of degree `n` is shown to have rank `n`, given that the
span of its image contains the diagonal matrices and that a one-parameter torus with `n` free
weights (`New.HasNoSmallRelations`) lies in the Zariski closure of a conjugate of the image of every
neighbourhood of `1`.

* `New.powMinor y m a`: a minor of order `m` of the matrix whose column `j < m` lists the entries of
  `y ^ j`. Over a field all of them vanish exactly when `1, y, …, y ^ (m - 1)` are linearly
  dependent.
* `New.exists_factor_charpoly`: over an integrally closed domain, if these minors all vanish, a
  factor of degree less than `m` of the characteristic polynomial of `y` kills `y`.
* `New.HasNoSmallRelations.inv_scalar_on_blocks`: if these minors vanish, with `m ≤ n + 1` and `c`
  surjective, for `diagonal (T ∘ e ∘ c) * x` over the Laurent polynomials, then `n < m` and on each
  fibre of `c` the block of `x⁻¹` is a scalar matrix.
* `New.card_eq_and_charpoly_eq`: the rank is `n` and the polynomials are the characteristic
  polynomials.

Notions from other files:
* `New.Ω`: the field `Ω` is an algebraic closure of `ℚ`: it has characteristic zero, is
  algebraically closed and is algebraic over `ℚ`.
* `New.HasNoSmallRelations e`: for `e : Fin n → ℤ`, distinct exponent vectors `α` of the same total
  degree at most `(n + 1) ^ 2` have distinct weights `∑ i, α i * e i`.
* `New.FrobeniusDatum E`: a place of degree one of `E` with a Frobenius element `frob` above it.
* `New.mostFrobenii E`: the filter of sets of such data that, inside every nonempty open set of
  `Gal(Ω/E)`, contain all data at almost all places whose Frobenius lies in a smaller nonempty open
  set.
* `T i`: the monomial of degree `i` in the Laurent polynomials `k[T;T⁻¹]`.

## Relation to the literature

Known result: Rank n and characteristic polynomials from Frobenius polynomial relations. Let a
continuous representation have image spanning the diagonal matrices, and let monic degree-n
polynomials kill it at most Frobenius elements. If a cocharacter with free (very different)
exponents constrains it, then its rank is n and the polynomials are its characteristic polynomials
at most Frobenius elements. This is one step inside the known construction of Galois representations
for definite unitary groups. In the literature, Frobenius polynomial relations on a dense set
determine a representation when the n-dimensional one is known and large. Related work:
Boston–Lenstra–Ribet 1991; Nekovář, Eichler–Shimura relations and semisimplicity, 2018;
Fayad–Nekovář 2019; Harris–Taylor 2001, VII.1.8.

See also `Lib.GaloisRep.Main.OddRank`.


### `powMinor`

 The minor of order `m`, at the rows `a 0, …, a (m - 1)`, of the matrix with rows indexed by
`N × N` whose column `j < m` lists the entries of the square matrix `y ^ j`: its entry at `(i, j)`
is the entry of `y ^ j` at the place `a i`. 

### `exists_factor_charpoly`

 Let `y` be a square matrix over an integrally closed domain `R`. If all minors `powMinor y m a`
of its first `m` powers vanish, then `y.charpoly = p * q` with `p` of degree less than `m` and
`p(y) = 0`. 

### `powMinor_diagonal_X_mul_eq_zero`

 Let the weights `e : Fin n → ℤ` be free (`HasNoSmallRelations e`: distinct exponent vectors of
one total degree at most `(n + 1) ^ 2` have distinct weights `∑ i, α i * e i`), let `c : N → Fin n`,
let `x` be an invertible matrix over `k` and let `m ≤ n + 1`. If all minors `powMinor` of order `m`
of the product of the diagonal matrix with entries `T (e (c a))` and `x` over `k[T;T⁻¹]` vanish,
then so do those of the product of the diagonal matrix with entries `X (c a)` and `x` over the
polynomials in the variables `X i`. 

### `HasNoSmallRelations.inv_scalar_on_blocks`

 Let the weights `e : Fin n → ℤ` be free (`HasNoSmallRelations e`: distinct exponent vectors of
one total degree at most `(n + 1) ^ 2` have distinct weights `∑ i, α i * e i`), let `c : N → Fin n`
be onto, let `x` be an invertible matrix over `k`, let `m ≤ n + 1`, and let `y` be the product, over
the Laurent polynomials `k[T;T⁻¹]`, of the diagonal matrix with entries `T (e (c a))` and `x`.
Suppose every `powMinor y m a` vanishes, where `powMinor y m a` is the `m × m` minor at rows
`a 0, …, a (m - 1)` of the matrix with rows indexed by `N × N` whose column `j < m` lists the
entries of `y ^ j`. Then `n < m`, and for `a ≠ b` with `c a = c b` the inverse `x⁻¹` has entry `0`
at `(a, b)` and equal entries at `(a, a)` and `(b, b)`. 

### `HasNoSmallRelations.lt_of_powMinor_eq_zero`

 Let the weights `e : Fin n → ℤ` be free, let `c : N → Fin n` be onto, let `x` be an invertible
matrix over `k` and let `m ≤ n + 1`. If all minors `powMinor` of order `m` of the product of the
diagonal matrix with entries `T (e (c a))` and `x` over `k[T;T⁻¹]` vanish, then `n < m`. 

### `HasNoSmallRelations.inv_apply_eq_zero_and_eq_of_powMinor_eq_zero`

 Let the weights `e : Fin n → ℤ` be free, let `c : N → Fin n` be onto, let `x` be an invertible
matrix over `k` and let `m ≤ n + 1`. If all minors `powMinor` of order `m` of the product of the
diagonal matrix with entries `T (e (c a))` and `x` over `k[T;T⁻¹]` vanish, then for `a ≠ b` with
`c a = c b` the inverse `x⁻¹` has entry `0` at `(a, b)` and equal entries at `(a, a)` and `(b, b)`.


### `powMinor_eq_zero_of_aeval_eq_zero`

 If a nonzero polynomial `p` of degree less than `m` kills the matrix `M` over `K`, then all
minors `powMinor (φ M) m a` vanish, for any `K`-algebra map `φ` into the matrices over `k`. 

### `charpoly_eq_of_powMinor_ne_zero`

 Let `N` have `n ≥ 1` elements and let a monic polynomial `P` of degree `n` kill the matrix `M`
over `K`. If some minor `powMinor (φ M) n a` is nonzero, for a `K`-algebra map `φ` into the
matrices over `k`, then `P` is the characteristic polynomial of `M`: otherwise `M.charpoly - P`
would be a nonzero polynomial of degree less than `n` that kills `M`. 

### `HasNoSmallRelations.injective`

 Free weights `e : Fin n → ℤ` are pairwise distinct: apply freeness to the exponent vectors of
degree one. 

### `exists_eq_of_powMinor_diagonal_eq_zero`

 Let `e : Fin n → ℤ` be injective, `κ : N → ℤ` and `l : Fin n → N` with `κ (l i) = e i`. If all
minors of order `n + 1` of the first `n + 1` powers of the diagonal matrix with entries `T (κ j)`
vanish, then every `κ j` is one of the `e i`: otherwise the minor at the diagonal places
`j, l 0, …, l (n - 1)` would be a Vandermonde determinant of distinct monomials. 

### `not_forall_conj_entries_of_diagonal_mem`

 Let `Q` be an invertible matrix over `k`, let `φ` send a matrix `M` over `K` to `Q * M * Q⁻¹`
over `k`, and let the `K`-subspace `V` contain every diagonal matrix. Then the matrices `φ x`,
`x ∈ V`, do not all have entry `0` at `(a, b)` and equal entries at `(a, a)` and `(b, b)`: for the
diagonal units `Eₜₜ` this would make each `Q a t * Q⁻¹ t a` zero, while their sum over `t` is
`1`. 

### `eventually_mostFrobenii_of_open`

 Let `E` be a number field inside `Ω` (`EmbeddedNumberField E`), and let `p` be a property of the
elements of `Gal(Ω/E)`. If every nonempty open set `V` contains a nonempty open set on which `p`
holds, then `p` holds at the Frobenius elements of most Frobenius data. 

### `exists_surjective_comp_eq_of_powMinor_diagonal_eq_zero`

 Let `e : Fin n → ℤ` be injective and let every `e i` be a value of `κ : N → ℤ`. If all minors
of order `n + 1` of the powers of `diagonal (T ∘ κ)` vanish, then `κ = e ∘ c` for an onto `c`. 

### `mvPolynomialX_map_eval_uncurry`

 The matrix of variables `X (i, j)`, evaluated at the entries of a matrix `M` over `k`, is
`M`. 

### `mvPolynomialX_map_aeval_uncurry`

 The matrix of variables `X (i, j)`, evaluated at the entries of a matrix `M` over a
`k`-algebra `S`, is `M`. 

### `card_eq_and_charpoly_eq`

 Let `E` be a number field inside `Ω`, a fixed algebraic closure of `ℚ`, let `r` be a continuous
representation of `Gal(Ω/E)` on `K ^ N`, and let `k` be a normed field over `K`. Suppose:
* the span of the image of `r` contains every diagonal matrix;
* for most Frobenius data `v` (the filter `mostFrobenii E`) the polynomial `P v` is monic of degree
  `n ≥ 1` and kills `r v.frob`;
* the free integers `e i` (`HasNoSmallRelations e`: distinct exponent vectors of one total degree at
  most `(n + 1) ^ 2` have distinct weights) all occur among the integers `κ j`;
* for an invertible matrix `Q` over `k`, every polynomial in the entries that vanishes at `Q * r g`
  for all `g` near `1` also vanishes at `diagonal (T ∘ κ) * Q` over `k[T;T⁻¹]`.

Then `N` has `n` elements and `P v` is the characteristic polynomial of `r v.frob` for most
Frobenius data `v`. 
