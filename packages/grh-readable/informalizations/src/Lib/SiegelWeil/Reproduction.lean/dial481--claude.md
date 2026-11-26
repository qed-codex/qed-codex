---
{
  "module": "src/Lib/SiegelWeil/Reproduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Reproduction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Reproduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Holomorphic Fock vectors and a reproducing formula by theta lifts

Polynomial vectors in the Fock model of a pair of unitary groups with signs `s` and `s'`: their
coefficients, their weights and the span of their translates. Then the reproducing formula, whose
hypotheses these facts supply.

* `New.Rows.linSubst_variableMinor`, `New.Rows.polyMatrixCoeff_eq_holMinorsPi_mul_conj`: a minor of
  variables is scaled by a principal minor of the group element. For a polynomial in the variables
  of sign `1` that is scaled in this way, the coefficient at `(u, 1)` is its value at `(1, 1)` times
  a function `holMinorsPi` times the conjugate of another.
* `New.Rows.prod_variableMinor_mem_holomorphicData`,
  `New.Rows.letterPoly_highestVector_mem_holomorphicData`: two families of nonzero holomorphic
  vectors.
* `New.Rows.realPairWeil_mem_span_pairedDetProd`: the definite second group moves a power of a minor
  into the span of the products of minors of Y times the matrix of variables, for any invertible
  matrix Y over E.
* `New.Rows.reproducing_formula_modKernel`: at each point, convolution with `holMinorsPi s u` is a
  finite combination of values of theta lifts to a definite group of rank above `2 * card n`.

Notions from other files:
* `New.PairFock E s s'`: the Fock space of `n' × n` matrices at every infinite place, with the signs
  `New.homSigns s s'`, that is `s'(i) s(j)`, repeated at every place by `New.realSigns`.
* `New.Fock.polyVector`: the linear map P ↦ v_P from complex polynomials to the Fock space,
  v_P(x) = P(ζ(x))exp(−|x|²/2), where ζ(x)_i is x̄_i at positive and x_i at negative coordinates.
* `New.realPairWeil γ e`: the real Weil representation of the pair of unitary groups, twisted by
  `det ^ (-e)` on the first group and `det ^ γ` on the second.
* `New.Rows.holomorphicData s s' O u γ e`: the Fock vectors all of whose coefficients are
  holomorphic of weight `u` on the first group, for the order `O` of its coordinates.
* `New.holMinorsPi s u`: the product over the infinite places of the quotients of minors of weight
  `u`, a function on the product of the unitary groups of signs `s`.

## Relation to the literature

Known result: Basis problem in the stable range, as a reproducing formula. This is a unitary version
at a fixed level, in which pairing with a holomorphic discrete series coefficient is, at each point,
a finite combination, the same for all functions of that level, of values of theta lifts to a large
definite group. It is deduced from injectivity by linear duality. Source: S. Böcherer, Über die
Fourier-Jacobi-Entwicklung Siegelscher Eisensteinreihen, Math. Z. 183 (1983); J.-S. Li, Crelle 428
(1992).

See also `Lib.Weil.Fock.OscillatorPair` and `Lib.Weil.DualPair.HolomorphicData`.


 ### The coefficient of a product of minors 

### `linSubst_variableMinor`

 Let the rows `i a` all have sign `κ` for `s'` and let `c` enumerate the indices of sign `κ`
for `s`. The linear substitution of the matrix variables `X (τ, r, k)` by which `(u⁻¹, 1)` acts
multiplies `variableMinor τ i c`, the minor of the variables at the place `τ` in rows `i` and
columns `c`, by the principal minor of `u τ` on the indices of sign `κ`. 

### `principalMinor_pairHomInf_neg`

 The principal minor of the action of `(u, 1)` on matrices of variables, on the variables of sign
`-1` for `homSigns s s'`, is the product over the places `w` and the rows `r` of the minor of `u w`
of sign `s' r` over `det (u w)`. 

### `polyMatrixCoeff_eq_holMinorsPi_mul_conj`

 Let `P` be a polynomial in the variables of sign `1` for `homSigns s s'`, those `(w, r, k)` with
`s' r * s k = 1`, that the substitution attached to `u⁻¹` multiplies by the powers `ν`, `c` of the
two principal minors of `u`. Its coefficient `polyMatrixCoeff` (the pairing of its Fock vector with
the translate by `(u, 1)`) is the value at `(1, 1)` times `holMinorsPi s v u` times the conjugate of
`holMinorsPi s k u`, for `v = (-ν; r₊) + r₋ - e` and `k = (0; c + r₋)`. Here `r₋ = negCount s'`
and `r₊ = card n' - r₋` count the signs of `s'`, `(a; b)` has entries `a` where `s = 1` and `b`
elsewhere, and `e` is the weight of the character on the first group (`e = r₋` for the standard
splitting). 

 ### Holomorphic products of minors and their translates 

### `prod_variableMinor_mem_holomorphicData`

 For signs `+1` on `p` and `-1` on `q`, an order `O` that puts `p` first and a definite second
space of coordinates `n'`, let `Q` be the product over the infinite places of the `d`-th power of
the minor (`variableMinor`) in rows `i` and all the positive columns. Then `Q ≠ 0` and its Fock
vector is holomorphic (`holomorphicData`) of weight `-d` on `p` and `card n'` on `q`, for the
character weights `γ` and `0`. 

### `realPairWeil_mem_span_pairedDetProd`

 For signs `+1` on `p` and `-1` on `q`, let `Y` be an invertible matrix over `E`. An element `y`
of the definite second group maps, under `realPairWeil`, the Fock vector of the product over the
places `w` of the `d`-th power of the minor in rows `i` and the columns of sign `+1` into the span
of the Fock vectors of `pairedDetProd`: for a choice `I` of rows, the product over `w` and `k` of
the determinants of the rows `I w k` of `Φ w Y` times the positive columns of variables, `Φ w`
being the chosen embedding of `E` at `w`. 

### `letterPoly_highestVector_mem_holomorphicData`

 Let the order `O` put the sign `+1` first. (a) Within each sign the parameter `l` increases
along `O`, and `l` is injective. (b) `o a` counts the indices `b` of the sign of `a`
with `s a * l a < s a * l b`. (c) The column multiplicities `κ τ i` vanish for `i` above the
number of indices of sign `c`. Let `Q` be the polynomial `letterPoly` of the highest vector of
weight `κ`: the product over the places `τ` and the sizes `i < card n'` of the `κ τ i`-th powers
of minors of size `i` of the variables, on the rows where `equivFin n'` takes its `i` largest
values and the columns `a` of sign `c` with `o a < i`. Then `Q` is nonzero and its Fock vector is
holomorphic (`holomorphicData`), for the character weights `γ` and `w`, of weight `staircaseWeight`:
at each column the vacuum weight shifted by `-w τ`, minus the sign times the number of these minors
that contain the column. 

 ### The reproducing formula 

### `realConv_holMinorsPi_eq_zero_of_lift_eq_zero`

 Let `S` have signs `s` and let the order `O` put the sign `+1` first. Let `u` be `K`-dominant
for `O`, with `holMinorsPi s u` integrable; this is the function on the real points `h` given by the
product over the infinite places `τ` of the quotients of minors of weight `u τ` at `h τ`. Let
`Q₀ ≠ 0` have a holomorphic Fock vector of weight `u` for the character weights `γ'`, `γ`. Let `c`
and `b` be the characters of the theta kernel of `S` and the standard definite space of rank
`card n'`, with `b` of weight `γ` and trivial tame part (`b.HasWeight γ 1`). Let `𝔪 = (N)` have a
prime divisor and let `card n'` exceed twice `card n`. If `ψ` is rapidly decreasing of level `N` and
its lift by the datum (`modDatum`) of `Q₀` and of the indicator of the matrix of `e : n ↪ n'` modulo
`𝔪` vanishes, then `realConv (holMinorsPi s u) ψ`, the convolution of `ψ` with it over the real
points, vanishes. 

### `lift_modDatum_eq_zero_of_mem_span`

 Let the characters `c` and `b` define the theta kernel of a hermitian space `S` of signs `s` and
the standard definite space of rank `card n'`, let `c` have weight `γ'` and trivial tame part
(`c.HasWeight γ' 1`), let `𝔪 = (N)`, and let `ψ` be a rapidly decreasing automorphic function for
`S` (`ψ ∈ S.rapidFunctions`). For each class `p` of level `N` of the definite unitary group, let the
span of the Fock vectors of the `Q p i` contain the translates of the vector of `Q₀` by the real
points of that group. If, at each class `p`, the theta lift of `ψ` by each `Q p i`, taken with the
indicator of the matrix of the inclusion `e` modulo `𝔪` (the datum `modDatum`: the Fock vector
paired by `integrated` with the Schrödinger operator of that indicator on the vacuum), vanishes,
then the lift by `Q₀` vanishes everywhere. 

### `reproducing_formula_modKernel`

 Reproducing formula. Let the order `O` put the sign `+1` first, and let `S` be a hermitian space
over `E` of signs `s`. Assume: (a) `𝔪 = (N)` has a prime divisor, and the characters `c` and `b`
have weights `γ'` and `γ` and trivial tame part; (b) `u` is `K`-dominant for `O` and
`holMinorsPi s u` (the product over infinite places `w` of the quotients of minors `holMinors` of
weight `u w`) is integrable; (c) the definite space `New.stdSpace` of rank `card n'` has more than
twice the rank of `S`; (d) `Q₀ ≠ 0` and its Fock vector is holomorphic of weight `u` for the
character weights `γ'` and `γ`; (e) for each class `p` of level `N` of the unitary group of this
definite space, the span of the Fock vectors of the `Q p i` contains the translates of that of `Q₀`
by the real points of that group. Then for each point `x` there are constants `a` such that, for all
`ψ` in `rapidOfLevel S N` (rapidly decreasing, automorphic and of level `N`), the integral
`∫ ψ(x (h, 1)) holMinorsPi s u h dh` over `h` in the archimedean group `∏_w U(diag s)` is the sum of
`a (p, i)` times the integral of `ψ` against the theta kernel `modKernelStdSpace` at the class `p`
(the kernel of the lift by `pairThetaKer S (stdSpace E n') c b` with the datum `modDatum`), taken
with polynomial `Q p i` and, modulo `𝔪`, the indicator of the matrix of the inclusion `e`. 
