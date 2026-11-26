---
{
  "module": "src/Lib/Weil/Fock/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Fock model of the Weil representation of U(ε) at a real place

For signs ε : ι → {±1}, this file builds the Fock model of the Weil representation of the unitary
group U(ε) = `New.USign` ε. The polynomial vectors v_P(x) = P(ζ(x)) exp(−|x|²/2), where ζ =
`New.Fock.holomorphicCoord` ε conjugates the positive coordinates, lie in the Fock space. Products
along splittings of the coordinates and over real places are compatible with polynomial vectors.

## Main definitions and results

* `New.Fock.realMultiplier`, `New.Fock.norm_realMultiplier_le`: the multiplier of the Weil
  representation, the conjugate of the negative minor, is bounded by ‖u‖^{|ι|}.
* `New.Fock.realAction`: the unitary group `U(ε)` acts on the datum in the sense of
  `New.Heisenberg.MultiplierAction`, with multiplier `New.Fock.realMultiplier` (the conjugate
  determinant of the negative block) and cocycle `1`.
* `New.Fock.fockSpace`, `New.Fock.realWeil`, `New.Fock.realHeisenbergOp`, `New.Fock.vacVector`,
  `New.Fock.fockInner`: the space, the Weil representation of U(ε), the Heisenberg action, the
  vacuum, the inner product.
* `New.Fock.polyVector`: the vector v_P(x) = P(ζ(x)) exp(−|x|²/2) of a polynomial P. It lies in the
  Fock space because derivatives of the Heisenberg action on the vacuum produce all polynomials.
* `New.Fock.polyVector_injective`: P ↦ v_P is injective.
* `New.Fock.piTensor`: the product of a family indexed by `T` (the real places), a vector on
  `T × ι`; it is compatible with polynomials and inner products.
* `New.Fock.blockU`, `New.Fock.realWeil_piTensor`: block diagonal unitary matrices act factor by
  factor.

Notions from other files:
* `New.Heisenberg`: A continuous function β on W × W, W a topological abelian group, with values of
  modulus one, multiplicative in each variable, and β(x,x) = 1.
* `New.Fock.normalizedVolume`: Lebesgue measure on `ι → ℂ` divided by `π ^ card ι`.
* `New.principalMinor`: the determinant of the block of a square matrix on the indices that
  satisfy a condition.
* `New.Heisenberg.IsVacuum.modelSubmodule`: The complex subspace of integrable functions v on W
  satisfying the reproducing identity v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y) for every x, where β is the
  bicharacter, e the vacuum and μ the measure.

## Relation to the literature

Known; see `Lib.Weil.Fock.OscillatorPair` for sources.



## The real Heisenberg datum and creation and annihilation operators

* `New.Fock.realHeisenberg`, `New.Fock.realVac`: the bicharacter β(x,y) = exp(i Im y*εx) on ℂ^ι and
  the Gaussian exp(−|x|²/2).
* `New.Fock.posProj`, `New.Fock.holomorphicCoord`: the projection on the coordinates of sign +1, and
  the map that conjugates these coordinates.
* `New.Fock.raiseOp`, `New.Fock.lowerOp`, `New.Fock.glOp`: the operators A_a, B_b on polynomials
  (one multiplies by the variable, the other differentiates, according to the sign) and A_a B_b.


### `realHeisenberg`

 For signs ε, the Heisenberg datum on ℂ^ι given by the continuous unit-modulus bicharacter
β(x,y) = exp((y*εx − x*εy)/2) = exp(i Im y*εx). 

### `realVac`

 The function on ℂ^ι sending x to exp(−|x|²/2). 

### `posProj`

 The diagonal complex matrix P₊ with entry 1 where ε_i = 1 and 0 elsewhere; for −ε it is the
projection P₋ on the negative coordinates. 

### `holomorphicCoord`

 For signs ε and x in ℂ^ι, the vector whose i-th coordinate is the conjugate of xᵢ if εᵢ = 1
and xᵢ otherwise. 

### `raiseOp`

 For signs ε and index a, the linear operator on complex polynomials: multiplication by X_a
if ε_a = 1, otherwise −∂/∂X_a. 

### `lowerOp`

 For signs ε and index a, the linear operator on complex polynomials: ∂/∂X_a if ε_a = 1,
otherwise multiplication by X_a. 

### `glOp`

 For signs ε and indices a, b, the composite A_a∘B_b on polynomials, with A_a = X_a or −∂_a and
B_b = ∂_b or X_b according as the sign is positive or negative. 

### `weilDeriv`

 For signs ε, the complex-linear map from ι×ι matrices to operators on polynomials, u ↦
Σ_{a,b} u_{ab} A_a B_b. It is the derivative of the Weil representation on polynomial vectors
(`New.Fock.hasDerivAt_realWeil`). 

### `heisenbergDeriv`

 For signs ε and x in ℂ^ι, the operator Σᵢ (conj(ζᵢ(x))·Xᵢ − ζᵢ(x)·∂/∂Xᵢ) on complex
polynomials, where ζ = `holomorphicCoord ε`, written through `raiseOp` and `lowerOp`. It is the
derivative dρ(x) of the Heisenberg action on polynomial vectors
(`New.Fock.hasDerivAt_realHeisenbergOp`). 


## Positive and negative projections and the real multiplier

Matrix facts for the unitary group U(ε) = `New.USign` ε of the diagonal matrix of signs ε.
P₊ = `New.Fock.posProj` ε is the projection on the positive coordinates, and P₋ = 1 − P₊ the
projection on the negative coordinates.

* `New.Fock.signMatrix_eq_posProj_sub`: the matrix of signs is P₊ − P₋.
* `New.Fock.principalMinor_sign_eq_det`: the minor on the negative indices is det(P₊ + P₋u).
* `New.Fock.norm_realMultiplier_le`: the multiplier, the conjugate of that minor, is at most
  ‖u‖^{|ι|}.


### `posProj_mul_self`

 The projection P₊ is idempotent and Hermitian, and the matrix of signs is Hermitian: the three
facts `posProj_mul_posProj`, `conjTranspose_posProj` and `conjTranspose_signMatrix` together. 

### `principalMinor_sign_eq_det`

 The principal minor of a matrix u on the indices of sign −1 is det(P₊ + P₋u), where
P₋ = 1 − P₊. 

### `realMultiplier`

 For u in the unitary group U(ε), the complex conjugate of the determinant of the block of u on
the indices of sign −1. 

### `norm_realMultiplier_le`

 For u in the unitary group U(ε), the multiplier `realMultiplier u` has modulus at most
‖u‖^{|ι|}, where ‖u‖ is the operator norm of the matrix of u. 


## The Gaussian vacuum

* `New.Fock.beta_mul_realVac`: the translated Gaussian is the reproducing kernel `exp (ζ(y)* ζ(x))`
  times two Gaussians, where `ζ = New.Fock.holomorphicCoord ε` conjugates the positive coordinates.
* `New.Fock.integral_exp_holomorphicCoord`: the reproducing formula for exponentials, a Gaussian
  integral.
* `New.Fock.isVacuum_realVac`: the Gaussian is a vacuum, by these two formulas.


### `beta_mul_realVac`

 For the Gaussian e and the real bicharacter β of signs ε, β(y,x) e(x − y) = e(x) e(y)
exp(conj ζ(y) · ζ(x)), with ζ = `New.Fock.holomorphicCoord` ε the holomorphic coordinates. 

### `integrable_exp_mul_realVac`

 For every real C, the function u ↦ exp(C‖u‖) exp(−|u|²/2) on ℂ^ι, with ‖u‖ the maximum norm
and |u| the Euclidean norm, is integrable for the normalised Lebesgue measure
`New.Fock.normalizedVolume`. 

### `integral_exp_holomorphicCoord`

 The reproducing formula of Fock space for an exponential. With ζ = `New.Fock.holomorphicCoord` ε
z and F(ζ) = exp(c · ζ), the integral of F(ζ) exp(conj ζ · ζ₀) exp(−|z|²) over z in ℂ^ι, for the
normalised Lebesgue measure `New.Fock.normalizedVolume`, is F(ζ₀). A case of Bargmann's reproducing
formula for entire functions (Folland, *Harmonic Analysis in Phase Space*). 

### `isVacuum_realVac`

 The Gaussian `New.Fock.realVac` is a vacuum for the Heisenberg datum `New.Fock.realHeisenberg ε`
and the normalised measure `New.Fock.normalizedVolume`. 

### `exists_norm_eval_le_exp`

 A complex polynomial P in the variables ι grows at most exponentially: there are k in ℕ and C
in ℝ with ‖P(l)‖ ≤ |C| exp(k ‖l‖) for every l in ℂ^ι, where ‖l‖ is the maximum norm. 


## Unitary action on the real Heisenberg datum and sums of data

* `New.Fock.realCoordSum`: a splitting of the index set splits the datum and the Gaussian.
* `New.Fock.realAction`: the unitary group U(ε) acts on the datum, with multiplier
  `New.Fock.realMultiplier` and trivial cocycle; the cocycle identity is
  `New.Fock.realMultiplier_mul_integral_eq_one`, a Gaussian integral on ℂ^ι × ℂ^ι.


### `realCoordSum`

 For a bijection e : ι₁ ⊕ ι₂ ≃ ι with ε ∘ e = ε₁ ⊕ᵥ ε₂ (hypothesis he), the isomorphism
ℂ^ι₁ × ℂ^ι₂ ≅ ℂ^ι under which β of ε and the Gaussian are the products of those of ε₁, ε₂, packaged
as the structure `(realHeisenberg ε).OrthogonalSum`. 

### `det_fromBlocks_mul_fromBlocks_eq_realMultiplier_mul`

 For g and h in U(ε), with k = g h, P₊ = `posProj ε` and T a function with
T(x) = P₊ + (1 − P₊) x, the product of the block matrices (T(h), 1 − P₊; 0, T(k⁻¹) k)ᴴ,
(P₊, P₊ − 1; 1, 1) and (1, 1; −T(h), −T(h) + T(g⁻¹) k) has determinant
`realMultiplier g * realMultiplier h * realMultiplier k⁻¹`. 

### `realMultiplier_mul_integral_eq_one`

 The cocycle identity for the multiplier `realMultiplier`: for g and h in U(ε), the product
`realMultiplier g * realMultiplier h * realMultiplier (g * h)⁻¹` times the double integral
∫∫ e(h x) e(g h y) β(x, y) e(x + y) dx dy is 1. Here e is the Gaussian `New.Fock.realVac`, β the
bicharacter of `New.Fock.realHeisenberg` ε, and both integrals are for `New.Fock.normalizedVolume`;
the double integral is a Gaussian integral on `ℂ^ι × ℂ^ι`. 

### `realAction`

 The linear action of the unitary group `U(ε)` on `ℂ^ι` preserves the bicharacter of
`New.Fock.realHeisenberg ε` and the measure. Its multiplier is `New.Fock.realMultiplier g`, the
conjugate of the determinant of the negative block of `g`, and its cocycle is trivial. 


## Fock space and polynomial vectors

* `New.Fock.fockSpace`, `New.Fock.realWeil`, `New.Fock.realHeisenbergOp`, `New.Fock.vacVector`,
  `New.Fock.fockInner`: the Fock space, the Weil representation of U(ε) and the Heisenberg action
  on it, the vacuum, the inner product.
* `New.Fock.polyVector`, `New.Fock.polyVector_injective`: the vector v_P of a polynomial P, and
  P ↦ v_P is injective.
* `New.Fock.hasDerivAt_realHeisenbergOp`: the derivative of t ↦ `New.Fock.realHeisenbergOp`(tv)v_P
  at 0 is v_Q, where Q is `New.Fock.heisenbergDeriv` ε v P.


 ### The Fock space and its operators 

### `fockSpace`

 The Fock space: integrable functions c on ℂ^ι with c(x) = ∫ c(y)β(y,x)e(x−y) dy, under the L¹
norm. Here β is the bicharacter of `New.Fock.realHeisenberg` ε and e is the Gaussian
exp(−|x|²/2). 

### `realWeil`

 The Weil representation of U(ε) on the Fock space 𝓕: u sends c to Δ(u) ∫ c(y) ρ(uy) e dy, where
ρ is the Heisenberg action `New.Fock.realHeisenbergOp`, e is the Gaussian and Δ is the multiplier of
`New.Fock.realAction`. 

### `realHeisenbergOp`

 For x in ℂ^ι, the Heisenberg operator on the Fock space 𝓕 sending c to z ↦ β(x,z) c(z − x),
where β is the bicharacter of `New.Fock.realHeisenberg` ε. 

### `vacVector`

 The Gaussian exp(−|x|²/2) regarded as an element of the Fock space. 

### `fockInner`

 The bounded sesquilinear form on the Fock space, conjugate-linear in the first variable:
(c, c′) ↦ ∫ c̄ c′ for the measure `New.Fock.normalizedVolume`. 

 ### Differentiating the Heisenberg action 

### `differentiableAt_integral_smul_realHeisenbergOp`

 Let f(z, y) = (f₁, f₂) in ℂ^ι × ℂ be jointly continuous in z in the finite-dimensional space E
and y = (s, x) in ℂ × ℂ^ι, holomorphic in z, with f₁ and f₂ homogeneous in y of degrees 1 and 2 for
real scalars, and let a in E satisfy f(a, (s, x)) = (ζ(x), −|x|²/2), ζ = `New.Fock.holomorphicCoord`
ε. Then the Fock-space-valued integral ∫ P(f₁) exp(f₂) `New.Fock.realHeisenbergOp`(x)
`New.Fock.vacVector` dx, with f at (z, (1, x)) and for `New.Fock.normalizedVolume` (Lebesgue measure
divided by π^card ι), is complex differentiable in z at a. 

### `eval_heisenbergDeriv`

 For v and l in ℂ^ι and ζ = `New.Fock.holomorphicCoord` ε, the value at l of the polynomial
`New.Fock.heisenbergDeriv` ε v P is (conj ζ(v) · l) P(l) − ∑_i ζ_i(v) (∂_i P)(l). 

### `exists_hasDerivAt_realHeisenbergOp`

 If v_P(x) = P(ζ(x))exp(−|x|²/2), ζ = `New.Fock.holomorphicCoord` ε, lies in the Fock space, then
for v in ℂ^ι so does v_Q, Q = ∑_i (conj(ζ_i(v)) X_i − ζ_i(v) ∂_i)P, and v_Q is the derivative at t =
0 of t ↦ `New.Fock.realHeisenbergOp`(tv)v_P, t real. Here `hP_mem` and `h_mem` are the memberships
of v_P and v_Q in `New.Heisenberg.IsVacuum.modelSubmodule`, the subspace that is the Fock space. 

 ### The polynomial vectors 

### `polyVector`

 The linear map P ↦ v_P from complex polynomials to the Fock space, v_P(x) = P(ζ(x))exp(−|x|²/2),
where ζ(x)_i is x̄_i at positive and x_i at negative coordinates. 

### `polyVector_apply`

 The Fock vector v_P = `polyVector ε P` of a complex polynomial P in the variables ι is the
function x ↦ P(ζ(x))·exp(−|x|²/2) on ℂ^ι, where ζ(x) = `holomorphicCoord ε x` has i-th coordinate
x̄ᵢ if εᵢ = 1 and xᵢ otherwise, and exp(−|x|²/2) is `realVac x`. 

### `hasDerivAt_realHeisenbergOp`

 For v in ℂ^ι and a polynomial P with Fock vector v_P = `New.Fock.polyVector` ε P, the curve
t ↦ `New.Fock.realHeisenbergOp`(tv)v_P (t real) has derivative at t = 0 equal to the Fock vector of
the polynomial `New.Fock.heisenbergDeriv` ε v P = Σᵢ (conj(ζᵢ(v))·XᵢP − ζᵢ(v)·∂P/∂Xᵢ), where
ζ = `holomorphicCoord ε`. Here `realHeisenbergOp x` is the Heisenberg operator on the Fock space
sending c to z ↦ β(x,z)c(z − x), with β the bicharacter of `realHeisenberg ε`. 

### `polyVector_injective`

 The map P ↦ v_P = `New.Fock.polyVector` ε P from polynomials to the Fock space is injective. 


## Tensor products over coordinate splittings and real places

* `New.Fock.realBoxProd`: the product of two vectors along a splitting `ι₁ ⊕ ι₂ ≃ ι` of the
  coordinates; on polynomial vectors it multiplies the polynomials
  (`New.Fock.realBoxProd_polyVector`).
* `New.Fock.piTensor`: the product of a family of Fock vectors indexed by a finite type `T`, a
  vector on `T × ι`; `New.Fock.blockU` and `New.Fock.realWeil_piTensor`: block diagonal unitary
  matrices act on such products factor by factor.


### `realBoxProd`

 For signs ε : ι → ℤˣ and coordinates split by a bijection e : ι₁ ⊕ ι₂ ≃ ι under which ε becomes
the signs ε₁ : ι₁ → ℤˣ on ι₁ and ε₂ : ι₂ → ℤˣ on ι₂ (`he`), the bounded bilinear map sending two
Fock vectors c₁, c₂ to their external product x ↦ c₁(x ∘ e ∘ inl) c₂(x ∘ e ∘ inr) in the Fock
space of ε. 

### `_root_.MeasurableEquiv.curry_apply_eq`

 Currying x : α × β → γ and evaluating at a gives the function b ↦ x (a, b). 

### `pi_normalizedVolume`

 The product over T of copies of the measure `New.Fock.normalizedVolume` on ℂ^ι is the image of
`New.Fock.normalizedVolume` on ℂ^(T × ι) under currying. 

### `piTensor`

 The continuous multilinear map sending (for signs ε : ι → ℤˣ) a T-indexed family of Fock vectors
v_τ to the product function x ↦ ∏ v_τ(x_τ) in the Fock space on T × ι. 

### `piTensor_polyVector`

 The product of the Fock vectors of the `P τ` is the Fock vector of their product, `P τ` being
written in the variables of the block `τ`. 

### `blockMatrix`

 The ring homomorphism sending a T-indexed family of complex ι × ι matrices to the block
diagonal matrix with rows and columns indexed by T × ι. 

### `blockMatrix_preserves_signMatrix`

 For a family u of elements of the unitary group U(ε) (matrices g with gᴴ diag(ε) g = diag(ε)),
the block diagonal matrix B with blocks u_τ satisfies Bᴴ J B = J for the diagonal sign matrix J
with entry ε_i at (τ, i). 

### `blockU`

 The homomorphism from U(ε)^T to the unitary group of the signs (τ, i) ↦ ε_i on T × ι, by
block diagonal matrices. 

### `realWeil_piTensor`

 The Weil representation of the block diagonal matrix `New.Fock.blockU` u acts on a product
`New.Fock.piTensor` v factor by factor: each v_τ is sent to `New.Fock.realWeil` (u_τ) v_τ. 

### `realBoxProd_polyVector`

 For the splitting e : ι₁ ⊕ ι₂ ≃ ι and signs ε : ι → ℤˣ, ε₁ : ι₁ → ℤˣ, ε₂ : ι₂ → ℤˣ with ε ∘
e = ε₁ ⊕ᵥ ε₂ (`he`), `New.Fock.realBoxProd` sends the Fock vectors of a polynomial P in the
variables ι₁ and a polynomial Q in the variables ι₂ to the Fock vector of the product of P and Q,
each renamed into the variables ι along e. 
