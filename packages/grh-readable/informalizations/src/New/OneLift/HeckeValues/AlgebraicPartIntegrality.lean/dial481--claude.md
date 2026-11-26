---
{
  "module": "src/New/OneLift/HeckeValues/AlgebraicPartIntegrality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartIntegrality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartIntegrality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The lift of a character: denominators, and one group ring element for all twists

Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `ϑ` be a tame character with set of places
(modulus) `Q`, and let `New.Data.CriticalPair.trivialLift` be the lift of `ν ϑ`, a normalised theta
lift from `U(1)` to `U(2 z)`. The number `New.Data.CriticalPair.integralAlgebraicPart` is an integer
multiple of its normalised squared norm `New.Data.CriticalPair.algPart`.

* `New.Data.CriticalPair.trivialLift_apply`: the lift as a finite sum of values of the kernel
  `New.Data.CriticalPair.pointKernel`.
* `New.Data.CriticalPair.weylGauge_denomBound_smul_pointKernel_le_one`:
  `New.Data.CriticalPair.denomBound` times each kernel value is integral at primes prime to the norm
  of `Q`, in terms of the gauge `New.weylGauge`.
* `New.Data.CriticalPair.denomBound_smul_trivialLift_mem_integralForms`,
  `New.Data.CriticalPair.integralAlgebraicPart_mem_integralAway`: so
  `New.Data.CriticalPair.denomBound` times the lift is an integral form away from `Q`, and
  `New.Data.CriticalPair.integralAlgebraicPart` is an integral number away from `Q`.
* `New.Data.CriticalPair.norm_sq_trivialLift_eq_sum`: the squared norm of the lift as a double sum
  of values of the tame character times pairings `New.Data.CriticalPair.kernelPairing` that depend
  on `Q` only.
* `New.Data.TameChar.IsIntegralMeasure`: functions of `ϑ` given, on the tame characters with set
  `Q`, by one element of the group ring of `U(1)(𝔸)` that is integral away from `Q`.
* `New.Data.CriticalPair.isIntegralMeasure_integralAlgebraicPart`: the multiple
  `New.Data.CriticalPair.integralAlgebraicPart` is such a function.

Notions from other files:
* `New.Data.TameChar`: a character of `U(1)(𝔸)` of weight 0 with tame part supported on a finite set
  `Q` of places of norm prime to `D.M * D.N`, `Q` disjoint from its conjugate.
* `New.Data.CriticalPair`: a critical pair, that is, an integer `1 ≤ z ≤ t` and a character `ν` of
  `U(1)(𝔸)` of weight `-c`, with `z ≤ c(v) ≤ 4b` and tame part supported on the chosen places.
* `New.Data.CriticalPair.HasLiftRank`: the index set `n` has `2 z` elements and `z ≥ 2`, for the
  pair `p = (ν, z)`.

## Relation to the literature

This file proves, for this data, versions of known results: integral group-ring elements that
interpolate twisted values of Hecke L-functions (see `New.Congruences.Selmer.ClassSums`), which are
squared norms of theta lifts from U(1) (see `Lib.SiegelWeil.RallisInner.SharpData`). Here only the
side of the squared norms is treated.


### `TameChar.IsIntegralMeasure`

 `F` is an integral measure at the modulus `Q` of `ϑ`, that is, evaluation on a group ring
element that is integral away from `Q`: there are finitely many points `u a` of `U(1)(𝔸)` and
complex numbers `c a` such that (a) `‖j (c a)‖ ≤ 1` for every prime `l` prime to the norms of the
places in `Q` and every ring map `j : ℂ →+* ℂ_[l]`, and (b) `F ϑ' = ∑ a, c a * ϑ' (u a)` for all
tame `ϑ'` of modulus `Q`. 

### `TameChar.IsIntegralMeasure.norm_sq`

 If `F` is an integral measure at the modulus `Q` of the tame character `ϑ`, that is, given on
the characters of modulus `Q` by an element of the group ring of `U(1)(𝔸)` that is integral away
from `Q`, then so is `ϑ' ↦ ‖F ϑ'‖ ^ 2`. Its element is the product of that of `F` and the image of
it under the conjugate-linear map with `[u] ↦ [u⁻¹]`. 

### `instance {l : ℝ} [D.HasLogUpper D.t l] : D.HasLogUpper p.z l`

 For a critical pair `p = (ν, z)`, a bound `D.t ≤ exp l` on the number `D.t`, which bounds `z`,
is also the bound `z ≤ exp l`. 

 ### The lift as a sum of kernel values, and its integrality 

### `pointDatum`

 The point datum of the pair `p` at the modulus `Q` of `ϑ`, a Schwartz function on the finite
adelic points of `Hom(E, E^n)`. It is the vacuum off the chosen places (the places of the two level
primes of `D`) and the places of `Q`; at these places it is the indicator `identityBlockIndicator`,
taken modulo `levelModulus 1` (the product of all of them), of the columns that reduce to one fixed
basis vector at the chosen places and have the entry `1` in that position at the places of `Q`. The
factor `P.vacuumScale D.towerExp ^ card n` makes the vacuum integral; here `lValueData H ϑ` is the
lift data of `p` twisted by `ϑ`. 

### `pointKernel`

 The kernel of the pair `p` twisted by `ϑ`: for finite points `g` of `U(1)` and `h` of `U(2 z)`,
the vector of derivatives at zero (jet) of the theta function of `pointDatum H ϑ` at `(g, h)`, in
the weight `κ` of the lift, with one coordinate for each index in the basis `WeylIndexFamily` of
that weight. The variables are scaled by `star D.piMBar * P.jetScale D.towerExp`: the period scale
of the Taylor series at the exponent `D.towerExp` that picks the field `D.E` in its tower, times the
conjugate of `D.piMBar`, an integer of `P.K` of norm the product of the two level primes. 

### `smul_kernelForm_apply`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
let `ϑ` be a tame character, and let `g`, `h` be finite adelic points of `U(1)` and `U(n)` over
`D.E`. For `X = lValueData H ϑ`, the lift data of `ν ϑ`, the form `X.kernelForm g` on `U(n)` is the
theta kernel at `g` of the block datum `X.descentPair.blockDatum`, with unscaled derivatives. Its
value at `h`, times the normalising factor, is the sum of the values of the scaled theta kernel
`pointKernel H ϑ` at `(g * twistResidueLift A, h)`. Here `A` runs over the families of units of the
residue fields at the modulus of `ϑ`, and `twistResidueLift A` is an integral lift of `A⁻¹`.

The factor is `a ^ card n * b ^ p.rowLengthSum`. The number `a = P.vacuumScale D.towerExp` makes the
vacuum Schwartz function of rank one integral. The number `b` scales the variables of the Taylor
series: it is the period scale `P.jetScale D.towerExp` times the conjugate of `D.piMBar`, an integer
of `P.K` of norm `D.M`. 

### `trivialLift_apply`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
and let `ϑ` be a tame character. The form `trivialLift H ϑ` is the normalised theta lift of `ν ϑ`
from `U(1)` to `U(n)`; the character is part of the Weil action, so that the function lifted is the
constant `1`. Its value at a finite adelic point `h` of `U(n)` is the sum of the values of the theta
kernel `pointKernel H ϑ` at `(c.1.out * twistResidueLift c.2, h)`. Here `c.1` runs over the double
cosets of the finite adelic `U(1)` by its rational points and `D.chosenLevel`, `c.1.out` is a
representative, `c.2` runs over the families of units of the residue fields at the modulus of `ϑ`,
and `twistResidueLift c.2` is an integral lift of the inverse family. 

### `weylGauge_denomBound_smul_pointKernel_le_one`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
let `ϑ` be a tame character, `l` a prime that does not divide the norm of the modulus of `ϑ`, `j` an
embedding of `ℂ` into `ℂ_[l]`, and `g`, `h` finite adelic points of `U(1)` and `U(n)`. Let `M = D.M`
be the product of the two level primes, `f = D.f` the number of infinite places of `D.E`, and
`d = P.d` the prime with `P.K = ℚ(√-d)`. Then `p.denomBound = M ^ (4 f z) * (M d) ^ p.rowLengthSum`
times the value at `(g, h)` of the theta kernel `pointKernel H ϑ` has gauge at most `1` at the point
`h` with respect to `j`: the inverse of `h`, acting in the highest weight of the lift with no power
of the determinant, moves it to a vector whose coordinates have absolute value at most `1`. 

### `denomBound_smul_trivialLift_mem_integralForms`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
let `ϑ` be a tame character, `l` a prime that does not divide the norm of the modulus of `ϑ`, and
`j` an embedding of `ℂ` into `ℂ_[l]`. Then the theta lift `trivialLift H ϑ` of `ν ϑ` to `U(n)`,
times the natural number `p.denomBound`, is a form integral at `j`. 

### `integralAlgebraicPart_mem_integralAway`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
and let `ϑ` be a tame character whose modulus has norm `N = ϑ.normQ`. The number
`integralAlgebraicPart H ϑ = D.chosenGroupOrder * p.denomBound ^ 2 * ‖φ‖ ^ 2 / N ^ (2 z - 1)`, where
`φ = trivialLift H ϑ` is the normalised theta lift of `ν ϑ` to `U(n)`, is integral at every prime
that does not divide `N`. 

### `norm_integralAlgebraicPart_one_le_one`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
and let `φ = trivialLift H TameChar.one` be the normalised theta lift of `ν` to `U(n)`, with no
twist. The number `integralAlgebraicPart H TameChar.one`, the squared norm `‖φ‖ ^ 2` times the
natural number `D.chosenGroupOrder * p.denomBound ^ 2`, is integral at every prime `l`: its image
under every field isomorphism `ι : ℂ ≃+* PadicAlgCl l` has norm at most one. 

 ### One group ring element for all twists 

### `TrivialLiftIndex`

 The index set of the sum in `trivialLift_apply`: pairs of a class of `U(1)` at the principal
level at the chosen places and a family of units of the residue fields at the modulus of `ϑ`. 

### `liftPoint`

 The finite point of `U(1)` attached to an index: the representative of the class times
`twistResidueLift` of the family of units, a lift of the inverse family. 

### `trivialLift_apply_eq_sum_smul`

 Let `p = (ν, z)` be a pair with `z ≥ 2`, let `n` have `2 z` elements, and let `ϑ`, `ϑ'` be tame
characters with the same modulus. The value of the lift of `ν ϑ'` at a finite point `h` of `U(n)` is
the sum over `a` of `ϑ'(det (1, g))⁻¹` times the value at `(g, h)` of the theta kernel of `p`
twisted by `ϑ.pow 0`, the trivial character regarded as tame of modulus `ϑ.Q`. Here `a` is a class
of `U(1)` at the principal level at the chosen places with a family of units of the residue fields
at the modulus, `g = liftPoint ϑ a` is the finite point of `U(1)` attached to `a`, and `(1, g)` is
the adelic point with component `1` at the infinite places and finite part `g`. 

### `kernelPairing`

 The class sum over `U(2 z)`, at the level of the lift, of the Gram pairing of the values at
`liftPoint ϑ b` and `liftPoint ϑ a` of the kernel of the trivial character of modulus `ϑ.Q`. A
single term of the lift need not have this level; the sum is taken at fixed representatives of the
classes. 

### `norm_sq_trivialLift_eq_sum`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
and let `ϑ`, `ϑ'` be tame characters with the same modulus. The squared norm of the theta lift
`trivialLift H ϑ'` of `ν ϑ'` to `U(n)` (the class sum, at the level of the lift, of the Gram
pairings of its values with themselves) is the sum of the numbers
`ϑ'(det (g b / g a)) * kernelPairing H ϑ a b`, where `g a` is the adelic point of `U(1)` with
component `1` at the infinite places and finite part `liftPoint ϑ a`. Here `a`, `b` run over
`TrivialLiftIndex ϑ`, and `kernelPairing H ϑ a b` is the same class sum for the kernels of `p`
twisted by the trivial character of that modulus, taken at `g b` and `g a`. 

### `mul_kernelPairing_mem_embValRing`

 The number `kernelPairing H ϑ a b` is the class sum over the unitary group `U(n)` of the pairing
of the kernel values at `liftPoint ϑ b` and `liftPoint ϑ a`. Times
`D.chosenGroupOrder * p.denomBound ^ 2` it is integral at every prime `l` that does not divide the
norm of the modulus: its image under an embedding `j` of `ℂ` into `ℂ_[l]` has norm at most `1`. 

### `isIntegralMeasure_integralAlgebraicPart`

 Let `p = (ν, z)` be a critical pair with `z ≥ 2`, let `n` have `2 z` elements (hypothesis `H`),
and let `ϑ` be a tame character of modulus `Q`. For a tame character `ϑ'`, the number
`integralAlgebraicPart H ϑ'` is
`D.chosenGroupOrder * p.denomBound ^ 2 * ‖trivialLift H ϑ'‖ ^ 2 / ϑ'.normQ ^ (2 z - 1)`: the squared
norm of the theta lift of `ν ϑ'` to `U(n)`, divided by a power of the norm of the modulus and
multiplied by a natural number that does not depend on `ϑ'`. This function of `ϑ'` is an integral
measure at `Q`: there are finitely many points `u a` of `U(1)(𝔸)` and numbers `c a`, integral at the
primes that do not divide the norm of `Q`, such that its value at every `ϑ'` of modulus `Q` is
`∑ a, c a * ϑ' (u a)`. 
