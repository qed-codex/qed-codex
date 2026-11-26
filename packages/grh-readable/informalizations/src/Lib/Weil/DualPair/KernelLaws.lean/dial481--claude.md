---
{
  "module": "src/Lib/Weil/DualPair/KernelLaws.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/KernelLaws.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/KernelLaws.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta kernels of unitary pairs modulo an ideal: formal laws and seesaw identities

This file proves the formal laws of the theta kernel θ^{S,T}_{a,b}[Ψ,P](g,h) =
`New.modKernel` S T a b 𝔪 Ψ P g h. Here S and T are spaces of ranks n and n′, and a and b are
characters of [U(1)]. Ψ is a function on n′ × n matrices over O_E/𝔪, and P is a polynomial whose
variables are indexed by an infinite place and a matrix position (row, column). The kernel is
`New.pairTheta` of the datum `New.modDatum`; the laws cover bilinearity, twisting, integral
translations, seesaw identities, negation, passing to a smaller ideal and relabelling.

## Main definitions and results

* `New.exists_conj_modKernel_eq_mul_modKernel_neg`, `New.exists_stdKernel_neg_left`: the complex
  conjugate of a kernel is a kernel for the negated first space, up to a factor of modulus one.
* `New.modKernel_mul_stdLevel_left`, `New.modKernel_mul_stdLevel_right`: right translation by the
  lattice stabiliser `New.stdLevel` acts on Ψ through its reduction `New.Modulus.reductionGL`, up to
  a scalar; `New.modDatum_factor`, `New.modKernel_factor`: passing to a smaller ideal.
* `New.modKernel_block_right`, `New.modKernel_sum_right`, `New.modKernel_sum_left`,
  `New.Rows.modKernelStdSpace_block`: seesaw identities, the kernel of a direct sum at block
  diagonal elements is a product; `New.stdKernel_sum_right`, `New.stdKernel_sum_left`: the same with
  standard characters; `New.stdKernel` S T 𝔪 is `New.modKernel` S T (stdChar s) (stdChar s') 𝔪, with
  s, s′ the signs of S, T.

Notions from other files:
* `New.pairWeil`: The representation ω_{a,b}(g, h) = a(det h) b(det g)⁻¹ ω(`onHom` (g, h)); the
  scalar is `New.pairChar a b (g, h)`.
* `New.Modulus`: a nonzero ideal of O_E prime to its complex conjugate, that is, never divisible by
  both w and w̄; `𝔪.ResidueRing` is O_E/𝔪 and `𝔪.places` the set of primes dividing 𝔪.
* `New.Space.boxProd`: the product f₁ ⊠ f₂ of data on two blocks of coordinates.
* `New.negSource` (`Lib.Weil.DualPair.FiniteAction`): the change of coordinates x ↦ (1, u⁻¹) x from
  Hom(S⁻,T) to Hom(S,T); `negSource.map` pulls data on Hom(S,T) back to data on Hom(S⁻,T).

## Relation to the literature

Known; see `Lib.Weil.DualPair.GaloisLaw` for sources.

See also `Lib.Weil.DualPair.ThetaLiftConvergence`.


### `Modulus.reductionGL`

 Reduction modulo 𝔪, as a homomorphism from the stabiliser of Ô^n in the finite adelic
unitary group to GL_n(O_E/𝔪). 

### `modKernelStdSpace`

 The theta kernel θ^{S,I}_{a,b}[Ψ, P](g, (1, h)), where I is the standard space I_{n′} of rank n′
and h lies in its finite adelic unitary group. 

### `vacuumDatum`

 The datum on Hom(S, T) with the function Ψ on matrices modulo 𝔪 at the places dividing 𝔪 and the
vacuum at the other finite places, as an element of the finite part of the space of data. 

### `renameRowsCols`

 For maps e, f of row and column indices, the ℂ-algebra map of polynomial rings sending the
variable X_(i,r,c) to X_(i,e(r),f(c)). 

 ### Bilinearity, twisting, integral translations and seesaw identities 

### `modKernelBilin`

 The value θ^{S,T}_{a,b}[Ψ, P](g, h) of the theta kernel as a complex bilinear form in the
function Ψ modulo 𝔪 and the polynomial P. 

### `pairWeil_twist`

 Multiplying the characters `a`, `b` of the Weil representation of a pair by characters `μ`, `μ'`
of `[U(1)]` multiplies the operator `ω_{a,b}(g, h)` by `μ (det h) / μ' (det g)`. 

### `pairTheta_twist`

 For hermitian spaces `S` and `T`, characters `a`, `b`, `μ`, `μ'` in `AutChar E`, a test
function `f` in `𝒮 (S.hom T)`, and unitary group elements `g : G E s` and `h : G E s'`:
replacing the characters `a`, `b` of the theta kernel `pairTheta S T a b f` by `a * μ` and `b * μ'`
multiplies its value at `(g, h)` by `μ (det h) / μ' (det g)`. 

### `modKernel_twist`

 Twisting the characters: for characters μ, μ′ of [U(1)], θ_{aμ,bμ′}[Ψ,P](g,h) = μ(det h)
μ′(det g)⁻¹ θ_{a,b}[Ψ,P](g,h), for all Ψ modulo 𝔪, polynomials P, and g, h. 

### `pairWeil_modDatum_stdLevel`

 For integral finite k in U(S) and k′ in U(T), ω_{a,b}(k, k′) sends the datum `New.modDatum` of
Ψ mod 𝔪 and a real Fock vector v to a(det k′) b(det k)⁻¹ times the datum of x ↦ Ψ(k′⁻¹xk) and v,
with k, k′ reduced modulo 𝔪 and `New.detFin` the finite determinant. 

### `modKernel_mul_stdLevel_left`

 Let `modKernel S T a b 𝔪 Ψ P` be the theta kernel (g, h) ↦ θ(ω_{a,b}(g, h) f) on the adelic
unitary groups of `S` and `T`, where the datum f is built from a function `Ψ` on n′ × n matrices
modulo `𝔪` and the Fock vector of the polynomial `P`. For `k` in the stabiliser of Ô^n in the finite
unitary group, the kernel at (g·(1, k), h) equals the kernel at (g, h) with `Ψ` replaced by
x ↦ b(det k)⁻¹ Ψ(x k̄). Here k̄ is the reduction of `k` modulo `𝔪`. 

### `modKernel_mul_stdLevel_right`

 Let `modKernel S T a b 𝔪 Ψ P` be the theta kernel (g, h) ↦ θ(ω_{a,b}(g, h) f) on the adelic
unitary groups of `S` and `T`, where the datum f is built from a function `Ψ` on n′ × n matrices
modulo `𝔪` and the Fock vector of the polynomial `P`. For `k` in the stabiliser of Ô^{n′} in the
finite unitary group, the kernel at (g, (x, h k)) equals the kernel at (g, (x, h)) with `Ψ` replaced
by y ↦ a(det k) Ψ(k̄⁻¹ y). Here k̄ is the reduction of `k` modulo `𝔪`. 

### `Modulus.liftFn_mul_blocks`

 Along a splitting `e` of the coordinates, the lift `liftFn` to finite adelic vectors (Φ of the
reduction mod 𝔪 of the components at the places dividing 𝔪 if these are integral, 0 otherwise) of a
product of functions modulo `𝔪` of the two blocks is the product of their lifts. 

### `boxProd_integrated_schrodingerOp_liftFn`

 Let `e` split the coordinates of `S` into those of `V₁` and `V₂`, compatibly with the signs.
Take on each `Vᵢ` the datum given by the Fock vector of a polynomial `Pᵢ`, a function `Φᵢ` modulo
`𝔪` at the primes dividing `𝔪`, and the vacuum elsewhere. The product `boxProd` of these data is
the datum on `S` given by `P₁ P₂` and `Φ₁ Φ₂`, read on the two blocks of coordinates. 

### `modKernel_block_right`

 Seesaw identity in the second space, along a sign-compatible splitting `e` of the coordinates
of `T` into those of `V₁` and `V₂`. Let the point of `T` be block diagonal with blocks the points
of `V₁` and `V₂`, and let `h` be block diagonal with blocks `h₁` and `h₂`. With Ψ₁, P₁ and Ψ₂, P₂
read on the two blocks of rows, θ^{S,T}_{a,bb′}[Ψ₁Ψ₂, P₁P₂](g, h) is
θ^{S,V₁}_{a,b}[Ψ₁,P₁](g,h₁) · θ^{S,V₂}_{a,b′}[Ψ₂,P₂](g,h₂). 

### `modKernel_sum_right`

 Seesaw identity in the second space: the kernel of (S, T ⊕ V) for characters a, bb′, the product
ΨΨ′ on the two row blocks and PP′ (P, P′ read in the variables of the two row blocks), at (g, h ⊕
h′), is θ^{S,T}_{a,b}[Ψ,P](g,h) · θ^{S,V}_{a,b′}[Ψ′,P′](g,h′). 

### `modKernel_sum_left`

 For a modulus 𝔪, a function Ψ on `n' × n` matrices over O_E/𝔪 and a polynomial P in variables
indexed by (infinite place, row, column), the theta kernel θ^{S,T}_{a,b}[Ψ,P](g,h) = θ(ω_{a,b}(g,h)
f) (`modKernel`) is built from the datum f given by Ψ and the Fock vector of P. Seesaw identity in
the first space: the kernel of (S ⊕ V, T) for characters aa′, b, the product ΨΨ′ on the two column
blocks and PP′ (P, P′ read in the variables of the two column blocks), at (g ⊕ g′, h), is
θ^{S,T}_{a,b}[Ψ,P](g,h) · θ^{V,T}_{a′,b}[Ψ′,P′](g′,h). 

### `stdKernel_sum_right`

 Sums in the second space, with standard characters (`New.stdKernel`): the kernel of (S, T ⊕ V)
for the product ΨΨ′ on the two row blocks and PP′, at (g, h ⊕ h′), is
θ^{S,T}[Ψ,P](g,h) · θ^{S,V}[Ψ′,P′](g,h′). This is a special case of `New.modKernel_sum_right`. 

### `stdKernel_sum_left`

 Sums in the first space, with standard characters (`New.stdKernel`): the kernel of (S ⊕ V, T)
for the product ΨΨ′ on the two column blocks and PP′, at (g ⊕ g′, h), is
θ^{S,T}[Ψ,P](g,h) · θ^{V,T}[Ψ′,P′](g′,h). This is a special case of `New.modKernel_sum_left`. 

 ### Negation 

### `Modulus.normNegOne`

 The unit of O_E/𝔪 that is the reduction of the chosen element of norm −1 of Ô. 

### `map_negSource_modDatum`

 Let Ψ be a function on n′ × n matrices over O_E/𝔪 and P a complex polynomial. The antilinear map
`negSource.map`, from data on Hom(S,T) to data on Hom(S⁻,T), sends the datum `modDatum` of v_P and Ψ
to the datum of v_{P̄} and x ↦ conj(Ψ(u⁻¹x)). Here P̄ is P with conjugated coefficients, the
polynomial vectors use the signs s′s and s′(−s) respectively, and u = `𝔪.normNegOne` is the unit of
O_E/𝔪 obtained by reducing the chosen ε ∈ Ô with εε̄ = −1. 

### `exists_conj_modKernel_eq_mul_modKernel_neg`

 Negating S conjugates theta kernels: for some c of modulus one depending only on S and T, the
conjugate of θ^{S,T}_{a,b}[Ψ,P](g,h) (`New.modKernel`, the theta kernel of the datum built from Ψ on
matrices mod 𝔪 and the Fock vector of P, with a, b twisting the action) is c
θ^{S⁻,T}_{a⁻¹υⁿ,b⁻¹υ^{n′}}[Ψ′,P̄](g,h) for all a, b, 𝔪, Ψ, P, g, h, where n, n′ are the sizes. Here
S⁻ is `New.Space.neg` S, and Ψ′(x) is the conjugate of Ψ(u⁻¹x), with u the unit of O_E/𝔪 reducing
the chosen element of norm −1 of Ô. P̄ has the conjugate coefficients, and υ is the splitting
character of the Weil data restricted to the norm-one ideles. On the right, `New.G.neg` moves g to
the group of S⁻. 

### `exists_stdKernel_neg_left`

 Negating S conjugates kernels with standard characters (`New.stdKernel`): for some c of modulus
one depending only on S and T, the complex conjugate of θ^{S,T}[Ψ,P](g,h) is c υ(det g)^{−(n₊ − n₋)}
θ^{S⁻,T}[Ψ′,P̄](g,h) for all 𝔪, Ψ, P, g, h. Here υ is `New.WeilData.upsilonU1`, the splitting
character of the Weil data restricted to the norm-one ideles (a character of U(1)(𝔸) trivial on
U(1)(E)). n₊ = `negCount (-s')` and n₋ = `negCount s'` count the signs 1 and −1 of T, so that
n₊ − n₋ is its signature. S⁻ is `New.Space.neg` S, and Ψ′(x) is the conjugate of Ψ(u⁻¹x), where
u = `New.Modulus.normNegOne` is the reduction mod 𝔪 of the chosen ε in Ô with ε̄ε = −1. P̄ has the
conjugate coefficients. On the right, `New.G.neg` moves g to the group of S⁻. This is a corollary of
`New.exists_conj_modKernel_eq_mul_modKernel_neg`. 

 ### Passing to a smaller ideal 

### `modDatum_factor`

 If the ideal 𝔪′ is contained in 𝔪, the datum modulo 𝔪′ given by the pullback of Ψ under
reduction to O_E/𝔪 and by the real Fock vector v equals the datum modulo 𝔪 given by Ψ and v. 

### `modKernel_factor`

 Change of modulus: if the ideal 𝔪′ is contained in 𝔪, a function Ψ on matrices modulo 𝔪, read
modulo 𝔪′ through the reduction O_E/𝔪′ → O_E/𝔪, has the same theta kernel as Ψ, for all characters
a, b of [U(1)], polynomials P and points g, h. 

 ### Relabelling, and the seesaw identity for a standard space split into blocks 

### `modKernel_reindex`

 The theta kernel θ[Ψ, P](g, h) is unchanged when the coordinates of S and T are relabelled
by sign-compatible bijections e, e′ and Ψ, P, g, h are relabelled accordingly. 

### `Rows.modKernelStdSpace_block`

 Seesaw identity for the standard space I_n = `New.stdSpace E n`, split as I_{n₁} ⊕ I_{n₂} along
a bijection ε, with `U.block ε` the block diagonal embedding of the unitary groups. Here
`New.modKernelStdSpace` is the theta kernel with a standard second space and finite second argument.
With Ψ, P read on the n₁ rows and Ψ′, P′ on the n₂ rows, θ^{T,I_n}_{a,bb′}[ΨΨ′, PP′](g, h ⊕ h′) =
θ^{T,I_{n₁}}_{a,b}[Ψ,P](g,h) · θ^{T,I_{n₂}}_{a,b′}[Ψ′,P′](g,h′) for finite adelic h, h′. The
polynomials are read on the blocks by `renameRowsCols`, which renames the rows of the variables. 
