---
{
  "module": "src/New/OneLift/ComparisonOperator/OneExchange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One exchange, and class sums at the level of a row stabilizer

The exchange identity compares class sums of theta kernels on a definite space `E^n` with integrals
over `[U(V')]`. For `W = E^b ⊕ W'` and an invariant datum it confines the twist to the kernel of
`(V', E^b)`, two spaces of equal rank. (`E^b` is the standard definite space with basis indexed by
`b`.) If `F` is invariant under a row stabilizer, the datum is a product for `z` in the stabilizer,
and the class sum at full level unfolds to the class sum of this product at the level of the
stabilizer.

## Main definitions and results

* `New.Rows.rowStabilizer`: the invertible A with the columns of 1 off e and w · φ(A) = w.
* `New.Rows.columnDatum`: the factor that depends only on the columns e.
* `New.Rows.columnDatum_mul_ite_eq_ite_mem_rowStabilizer`: for F left invariant under
  `New.Rows.rowStabilizer`, the function χ(det z) F(z⁻¹ y), cut down to z in the stabilizer, is a
  product.
* `New.Rows.integrable_and_mul_stdClassSum_eq_integral_mul`: from the exchange identity for matched
  data on `E^b ⊕ W'`, with the constant `c`: for an invariant datum `Ψ'`, `c` times the class sum
  of the kernel of `χ (det x'') Ψ' (x''⁻¹ x')` is the integral of the kernel of `(V', E^b)` with
  datum `χ ∘ det` times the kernel of `(V', W')` with datum `Ψ'`.
  `New.Rows.mul_stdClassSum_eq_integral_mul_modKernel` sums this over the classes of `U(E^b)`.
* `New.Rows.stdClassSum_rowStabilizer_eq`: a class sum at full level equals a class sum at the level
  of a row stabilizer, with a datum supported on matrices of a special shape.

Notions from other files:
* `New.AutChar`: an automorphic circle-valued character of U(1)(𝔸). `HasWeight` e ψ gives its
  exponents e at the infinite places and its tame parts ψ at the finite places.
* `New.modKernelStdSpace` W α β 𝔪 Ψ P g h: the theta kernel of the pair of W and the standard
  definite space, with the twisting characters α and β, the datum Ψ modulo 𝔪 and the polynomial P,
  at the adelic point g and at the point with real part 1 and finite part h.
* `New.stdLevel`: the level K₀, the stabilizer of the standard lattice.
* `New.Fock.polyVector` ε P: the Fock vector P(ζ(x)) exp(-|x|²/2), where ζ conjugates the
  coordinates of positive sign. For a pair with signs s and t, `homSigns` s t gives the products of
  the signs as those of the coordinates, and `realSigns` repeats them at every infinite place.
* `New.Modulus`: a modulus, a nonzero ideal 𝔪 of O_E prime to its complex conjugate, that is, never
  divisible by both w and w̄; `New.Modulus.ResidueRing` is the residue ring O_E/𝔪.
* `New.Exchange.IsTameFor`: `IsTameFor 𝔪 ν e χ` says that 𝔪 ≠ (1), that ν has weight e and that its
  tame part is ramified exactly at the places dividing 𝔪 and gives the character χ modulo 𝔪.
* `New.Rows.liftMod`: a chosen lift of g ∈ GL_n(O_E/𝔪) to K₀, with component 1 outside the places
  dividing 𝔪 and their conjugates.
* `New.Space` E n s: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸)
  with xᴴJx equal to diag(s) at the infinite places and 1 at the finite places.
* `New.G` E s: the adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the
  identity matrix at the finite places; `New.Gf` E n is G_f.

## Relation to the literature

See `New.OneLift.ComparisonOperator.FirstFactors`, `New.OneLift.ComparisonOperator.GluingMaps`
and `New.Determinant.Exchange.ExplicitMatching` for related work.



## The function χ(det z) F(z⁻¹ y) on a row stabilizer as a product

`New.inclMatrix R e` is the N × r matrix whose column j is the unit vector e j.


### `FixesColsOff`

 The columns of the square matrix z outside the image of e are those of the identity matrix. 

### `rowStabilizer`

 The subgroup of the A in GL_N(R) such that (a) the columns of A outside the image of e are those
of 1, and (b) w · φ(A) = w. Condition (a) says that A fixes the projection
`1 - inclMatrix R e * (inclMatrix R e)ᵀ` under left multiplication. Condition (b) says that φ(A)
fixes w under right multiplication, hence the passage through the opposite group. 

### `columnDatum`

 The function of an N×r matrix σ equal to χ(det of the rows e of σ) if
`w * σ.map φ = w * inclMatrix S e`, and 0 otherwise. 

### `columnDatum_mul_ite_eq_ite_mem_rowStabilizer`

 Let H = `rowStabilizer φ w e` be the group of the invertible A that have the columns of 1 off
the image of e and satisfy w · φ(A) = w, let F be left invariant under H, and let z be an N × N
matrix. Then `columnDatum` of the columns e of z, times F(y) if z has the columns of 1 off e and 0
otherwise, equals χ(det z) F(z⁻¹ y) if z lies in H, and 0 otherwise. 


## Rapid decay of kernels, one exchange, and class sums at row stabilizers

`New.modKernel S T a b 𝔪 Ψ P` is the theta kernel of the pair `(S, T)` for a function `Ψ` on
matrices modulo `𝔪` and a polynomial `P`; `New.stdClassSum K` is the class sum of level `K` on the
standard definite space `stdSpace`.


### `isRapid_modKernel`

 Let `S` and `V` be hermitian spaces with signs `s` and `t` at the infinite places. If some place
divides the modulus `𝔪` and the function `Ψ` on matrices modulo `𝔪` is supported on matrices with a
left inverse, the theta kernel `modKernel` of `(S, V)` for `Ψ`, the polynomial `P` and the twisting
characters `a`, `β` has rapid decay in the adelic point `g` of `U(S)`: its product with any power of
the height is bounded. 

### `hasLeftInv_of_isUnit_det_toRows₁`

 A matrix `y` with rows indexed by `m ⊕ k` whose top block `y.toRows₁` (the rows in `m`) has unit
determinant has a left inverse (`HasLeftInv`), namely `(y.toRows₁⁻¹ 0)`. 

### `areMatched_det_mul`

 Let `Ψ'` be a function on matrices modulo `𝔪` that is invariant under right multiplication by
invertible matrices. Then the functions `Φ x = χ (det x'') Ψ' (x''⁻¹ x')` of `x = (x' x'')` and
`Ψ y = χ (det y') Ψ' (y'')` of `y = (y'; y'')` are matched for `χ⁻¹` (`AreMatched`). 

### `integrable_and_mul_stdClassSum_eq_integral_mul`

 One exchange. Let `V'` and `W'` be hermitian spaces with bases indexed by `b` and `n` and signs
`t` and `s` at the infinite places, with adelic unitary groups `G E t` and `G E s`. Let `E^b` be the
standard definite space (`stdSpace`), `W = E^b ⊕ W'`, and let `.sum ((1, h'), g)` be the point of
`U(W)` with blocks `h'` and `g`. Let `𝔪 ≠ (1)` be a modulus and `χ` a character of `𝒪 / 𝔪`. For a
function `Φ` on matrices modulo `𝔪`, `K Φ` is a function on the finite points of `U(E^n)`. We assume
the exchange identity: for matched `Φ`, `Ψ` (`AreMatched`), `c` times the class sum of `K Φ` at full
level is the integral over the automorphic quotient of `U(V')` of the theta kernel of `(V', W)` with
datum `Ψ` and the polynomial `P` in the variables of `W'`. Let `Ψ'` be invariant under right
multiplication by `GL_b (𝒪 / 𝔪)`. Then the product of the kernel of `(V', E^b)` at `h'` and the
kernel of `(V', W')` at `g` is integrable, and its integral is `c` times the class sum of `K Φ` for
`Φ (x' x'') = χ (det x'') Ψ' (x''⁻¹ x')`. 

### `mul_stdClassSum_eq_integral_mul_modKernel`

 One exchange, summed over the classes of `U(E^b)`. Let `V'` and `W'` be hermitian spaces with
bases indexed by `b` and `n` and signs `t` and `s` at the infinite places, with adelic unitary
groups `G E t` and `G E s`; let `E^b` be the standard definite space, `𝔪 ≠ (1)` a modulus and `χ` a
character of `𝒪 / 𝔪`. Suppose that `c₀` times the class sum over the finite points `h'` of `U(E^b)`
of `coef h'` times the theta kernel of `(V', E^b)` at `(x, h')` is `F x`. Suppose that the functions
`K Φ h'` on the finite points of `U(E^n)` satisfy the exchange identity: for matched data `Φ`, `Ψ`
modulo `𝔪` (`AreMatched`), `c` times the class sum of `K Φ h'` is the integral over the automorphic
quotient of `U(V')` of the kernel of `(V', E^b ⊕ W')` with datum `Ψ` and the polynomial `P` in the
variables of `W'`, at the point `.sum ((1, h'), g)` with blocks `h'` (real part `1`) and `g`. Let
`Ψ'` be invariant under right multiplication by `GL_b (𝒪 / 𝔪)`. Then `c c₀` times the class sum over
`h'` of `coef h'` times the class sum of `K Φ h'`, for `Φ (x' x'') = χ (det x'') Ψ' (x''⁻¹ x')`, is
the integral of `F` times the kernel of `(V', W')` at `g` with datum `Ψ'` and polynomial `P`. 

### `integral_mul_modKernel_sum_translates`

 Let `V'` and `W'` be hermitian spaces, and let `F` on the adelic unitary group of `V'` be
automorphic, rapidly decreasing (`rapidFunctions`) and right invariant under the full level
`stdLevel`. Let `β'`, the character that twists the action of `U(V')` in the theta kernel of
`(V', W')`, have weight `wt` and trivial tame part (`HasWeight wt 1`); `a` is the other twist. In
the integral of `F` against the kernel over the quotient by rational points (`quotMeasure`), all
right translates `ψ (· γ)` of a datum `ψ` modulo `𝔪` by `γ` in `GL (𝒪 / 𝔪)` give the same value. So
their sum, read modulo a multiple `𝔪'` of `𝔪`, gives the number of the `γ` times the integral for
`ψ`. 

### `stdClassSum_tower`

 The tower property of class sums. Let `f₀` be left invariant under the rational points `Γf` and
right invariant (`rightStabilizer`) under `levelOfSubgroup H`, the elements of the full level
`stdLevel` that reduce modulo `𝔪` into the subgroup `H`, and let `f`, of full level, be the sum of
the right translates of `f₀` by lifts of coset representatives of `H`. Then the class sum of `f₀` at
that level is the class sum of `f` at full level. 

### `signedRowSubst`

 The substitution `x_τ ↦ c_τᵀ x_τ` in the columns `j` with `s j = 1` and `x_τ ↦ d_τ x_τ` in the
other columns, on complex polynomials in the entries of `b × n` matrices `x_τ`, one for each
infinite place `τ`. 

### `realPairWeil_ratEmbed_inv_polyVector`

 Let `δ` be a rational point of the unitary group of the standard definite space `E^b`, paired
with a space of signs `s`. Let `polyVector` of a polynomial `P` be its Fock vector
`P (ζ x) exp (-|x|²/2)` for the signs of the pair. The real part of `δ⁻¹` acts on it (by
`realPairWeil γ 0`, the real Weil action twisted by `det ^ γ`) as the substitution
`x_τ ↦ (δ⁻¹)ᵀ x_τ` in the columns of sign `1` and `x_τ ↦ δ x_τ` in those of sign `-1`, times
`∏ τ, (det δ) ^ (q - γ τ)`, where `q` (`negCount s`) is the number of signs `-1`. At the place `τ`,
`δ` is read in the complex embedding `Φ τ` that the CM type chooses. 

### `modKernelStdSpace_stdEmbFin_mul`

 Let `W` be a hermitian space with signs `s`, definite or not. The kernel of `(W, E^b)` is that
of a function `Ψ` on matrices modulo the ideal `𝔪` and a polynomial `P`; the automorphic characters
`α` and `β` twist the actions of `U(E^b)` and `U(W)`. Let `α` have exponents `γ` at the infinite
places, and let `δ` be a rational point of `U(E^b)`. The kernel at the adelic point `g` and the
finite point `δ h` is `∏ τ, (det δ) ^ (q - γ τ)`, with `q` the number of signs `-1`, times the
kernel at `(g, h)` of the polynomial obtained from `P` by `x_τ ↦ (δ⁻¹)ᵀ x_τ` in the columns of sign
`1` and `x_τ ↦ δ x_τ` in those of sign `-1`. 

### `fixesLeft_modKernelStdSpace`

 Consider the theta kernel `modKernelStdSpace` of a hermitian space `W` and the standard definite
space `E^b`, for a function `Ψ` on matrices modulo the ideal `𝔪`, a polynomial `P` and automorphic
characters `α`, `β` that twist the actions of `U(E^b)` and `U(W)`, at an adelic point `g` of `U(W)`.
Let `α` be tame for `𝔪` (`IsTameFor`): `𝔪 ≠ (1)`, `α` has exponents `γ` at the infinite places, and
its residue characters are nontrivial exactly at the primes dividing `𝔪`, with product `χ` on
`𝒪 / 𝔪`. Let the Fock vector of `P` be fixed by the real group of `E^b`. Then the kernel, as a
function of the finite point of `U(E^b)`, is left invariant under the rational points. 

### `stdClassSum_rowStabilizer_eq`

 Let the automorphic character `α` be tame for the ideal `𝔪` (`IsTameFor`): `𝔪 ≠ (1)`, `α` has
exponents `γ` at the infinite places, and its residue characters are nontrivial exactly at the
primes dividing `𝔪`, with product `χ` on `𝒪 / 𝔪`. Let `β` be the second twisting character, and let
the Fock vector of the polynomial `P` be fixed by the real group of the standard definite space
`E^b`. Let `F` be left invariant under the group `H` (`rowStabilizer`) of the invertible `A` modulo
`𝔪` with `w · φ(A) = w` and the columns of `1` off `e`. Write `x = (x′ | x″)`. Then the class sum at
full level of the kernel with datum `χ (det x″) F (x″⁻¹ x′)` equals the class sum, at the level
`levelOfSubgroup H` of the elements that reduce modulo `𝔪` into `H`, of the kernel with this datum
restricted to `x″` in `H`. With `σ` the columns `e` of `x″`, the restricted datum is
`columnDatum χ φ w e σ` times `F x′` if `x″` has the columns of `1` off `e`; else it is 0. 
