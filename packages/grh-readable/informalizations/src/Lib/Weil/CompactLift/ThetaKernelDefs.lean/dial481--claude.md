---
{
  "module": "src/Lib/Weil/CompactLift/ThetaKernelDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/CompactLift/ThetaKernelDefs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/CompactLift/ThetaKernelDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The jet matrix of a definite pair is a kernel for algebraic forms

An abstract theta kernel is an action of `G × G'` on a space of data, with a jet matrix for each
datum that is equivariant for the rational points. Such a kernel lifts algebraic forms from rank `n`
to rank `n'`.

* `New.IsLiftWeight`: the condition on ranks and weights under which the lift exists.
* `New.Kernel`: the abstract theta kernel.
* `New.Kernel.lift`, `New.Kernel.lift_equivariant`: the theta lift of a kernel and its equivariance
  under `G × G'`.
* `New.schurCoeffPoly`: the polynomial `Aᵀ S(z) ξ`, with `S = schur κ`.
  `New.dotProduct_schurJet_mulVec` writes the entries of the jet matrix as jets along it.
  `New.realPairWeil_schurCoeffPoly` gives the action of the real points on it, and
  `New.theta_pairWeil_schurCoeffPoly` its theta function as a coefficient of the jet matrix.
* `New.thetaKernel`: the kernel of the definite pair, which sends `f` to
  `schurJet κ (jetSeries _ c f)`.

Notions from other files:
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Space.finitePart`: The finite part 𝒮_f: the subspace of 𝒮(V) spanned by the translates of the
  vacuum under the finite Heisenberg operators `New.Space.finHeisenbergOp`.
* `New.rightStabilizer`: The subgroup of k in G with f(gk) = f(g) for all g.
* `New.AlgForm`: Smooth algebraic forms of weight (κ, e): functions φ on G_f with values in vectors
  indexed by `New.WeylIndex n κ`, with φ(γg) = ρ(γ)φ(g) for rational γ and an open stabiliser.
* `New.schurJet`: The matrix of jets of a power series along the entries of `schur κ`.

## Relation to the literature

Known; see `Lib.Weil.CompactLift.DefiniteThetaLift` for sources.


### `coeff_aeval_smul_X`

 Scaling the variables of a complex polynomial by `t` scales the coefficient of a monomial
by `t` to the power of its degree. 

### `isHomogeneous_iff_aeval_smul_X`

 A complex polynomial is homogeneous of degree `d` exactly when multiplying the variables by
any `t ≠ 0` multiplies it by `t ^ d`. 

### `IsLiftWeight`

 The weight `(κ, e)` of rank `n` goes up to rank `n'` along the exponent `eb`. Here `κ τ h` is
the number of columns of height `h` at the place `τ`. There are three conditions: no column has
height strictly between `card n` and `card n'`, and `card n ≤ card n'` (`New.FitsRanks`); the
rank grows, `card n < card n'`; and `e τ = eb τ + κ τ (card n)`, since in rank `n` the columns of
height `card n` give a power of the determinant, whose exponent is added to `eb τ`. 

 ### The Fock polynomial and the finite Weil representation 

### `schurCoeffPoly`

 For a covector A and a vector ξ, the polynomial Aᵀ S_κ(z) ξ in the entries of the n′ × n
matrices z_τ, one for each infinite place τ, where S_κ = `schur κ`. S_κ(z) has rows indexed by
`WeylIndex n' κ` and columns by `WeylIndex n κ`, and its entries are polynomials in the z_τ. 

### `Space.heisenbergFinPart`

 The finite Heisenberg operator `New.Space.finHeisenbergOp` of a vector x over the finite adeles,
restricted to the finite part 𝒮_f of 𝒮(V). 

### `pairWeilFinite`

 The Weil representation `pairWeil V T a b` at the finite points, restricted to the finite part
of 𝒮(Hom(V, T)). 

### `Kernel`

 An abstract theta kernel with data in S. It consists of a representation ω of G_f × G'_f on S,
and a linear map `jetMap` from S to linear maps from functions on `WeylIndex n κ` to functions on
`WeylIndex n' κ`, equivariant for the rational points Γ × Γ' in weight e on the source and ea on
the target; every datum has an open stabiliser. The subgroup K does not enter the fields: it is the
level at which `New.Kernel.lift` integrates. 

### `Kernel.ω`

 The action of the finite points `G_f × G'_f` on the data. 

### `Kernel.jetMap`

 The jet map of a datum, a linear map from vectors of rank `n` to vectors of rank `n'`. 

### `Kernel.equivariant`

 The jet map is equivariant for the rational points `Γ × Γ'`:
  `jetMap (ω (γ, δ) Φ) (weightRep κ e γ v) = weightRep κ ea δ (jetMap Φ v)`. 

### `Kernel.isOpen_stabilizer`

 Every datum Φ has an open stabiliser: `g ↦ ω g Φ` is invariant under an open subgroup. 

### `Kernel.integrand_mem_smoothInvariants`

 Let `k` be an abstract theta kernel (`New.Kernel`) over a CM field `E`, with a representation
`ω` of `G_f × G'_f` on the data `S` and a jet map `jetMap` from data to linear maps from functions
on `WeylIndex n κ` to functions on `WeylIndex n' κ`. For a datum `Φ`, an algebraic form `φ` of
weight `(κ, e)` and `h ∈ G'_f`, the integrand `g ↦ jetMap(ω(g, h)Φ)(φ(g))` of the theta lift lies in
`New.smoothInvariants stdRatPoints`. In words, it is left invariant under the rational points
`U_n(E)`, and its stabiliser under right translation is open. 

### `Kernel.lift`

 The theta lift with datum Φ. An algebraic form φ of weight (κ, e) goes to the algebraic form
h ↦ ∫ jetMap(ω(g,h)Φ)(φ(g)) dg of weight (κ, ea). The integral is over Γ\G_f, Γ the rational
points, for the Haar measure with vol K = 1 (`New.classIntegral`). 

### `Kernel.lift_equivariant`

 Equivariance of the theta lift: the lift with datum ω(a,b)Φ of the right translate of φ by a
is the right translate by b of the lift of φ with datum Φ. 

### `dotProduct_schurJet_mulVec`

 For a covector A, a vector ξ and a power series F, A paired with the Schur jet matrix of F
applied to ξ is the jet of F along the polynomial Aᵀ S_κ(z) ξ. 

### `map_schurJet`

 Assume `IsLiftWeight n n' κ eb e`, i.e. the weight `(κ, e)` of rank `n` goes up to rank `n'`
along `eb`. Then applying a ring homomorphism `φ` to an entry of the Schur jet matrix of a power
series `F` gives the same entry of the Schur jet matrix of the power series obtained by applying `φ`
to the coefficients of `F`. 

### `eval_schurCoeffPoly`

 Under `IsLiftWeight n n' κ eb e`, evaluating `schurCoeffPoly A ξ` at z gives Aᵀ S_κ(z) ξ, for
the matrices z_τ with entries z(τ, b, c). 

### `realPairWeil_schurCoeffPoly`

 Let `E` be a CM field, and assume `IsLiftWeight n n' κ eb e`: `card n < card n'`,
no column has height strictly between them, and `e τ = eb τ + κ τ (card n)`. For real points `x` of
U(n) and `y` of U(n') (signs `1`), the real Weil representation `realPairWeil ea eb` acts by
`∏_w (det y_w)^{ea_w} (det x_w)^{−eb_w}` times the Fock operator of `z ↦ y z x⁻¹`, and it sends
`schurCoeffPoly A ξ = Aᵀ S_κ(z) ξ` to `schurCoeffPoly (A ᵥ* conjWeylMatrix κ ea y⁻¹) (conjWeylRep κ
e x ξ)`. That is, `y⁻¹` acts on the covector `A` and `x` acts on the vector `ξ` by the conjugate
Weyl representations of weights `(κ, ea)` and `(κ, e)`. 

### `aeval_smul_X_schur`

 If the ranks fit `κ` (`New.FitsRanks`), scaling the entries of the variable matrices `z τ` by
`c` multiplies each entry of `schur κ z` by `c` to the number of boxes in the columns of height
below `card n'`. 

### `isHomogeneous_schur`

 If the ranks fit `κ` (`New.FitsRanks`), the entries of `schur κ z` are homogeneous polynomials
in the entries of the variable matrices `z τ`. The degree is the number of boxes in the columns of
height below `card n'`. 

### `schurJet_jetSeries_eq_smul`

 Assume `IsLiftWeight n n' κ eb e`. Scaling the variables of the Taylor series of f by `c`
multiplies its Schur jet matrix by `c` to the number of boxes in the columns of height below
`card n'`. 

### `theta_pairWeil_schurCoeffPoly`

 The theta function of a Schur coefficient is a matrix coefficient of the jet matrix. Assume
`IsLiftWeight n n' κ eb e`, and let the characters `a`, `b` have weights `ea`, `eb`, with ψ, ψ' the
attached characters of the residue fields at the finite places. Let `v` be the Fock vector of
`schurCoeffPoly A ξ`, and move `v ⊗ f` by the adelic points `(x, g)` and `(y, h)`. The theta
functional of the result, times `c` to the number of boxes, is `Aᵀ y⁻¹ k x ξ`. Here `k` is the jet
matrix at the scale `c` of the translate of `f` by the finite parts `(g, h)`, and the real parts
`x`, `y` act in the weights `(κ, e)`, `(κ, ea)`. 

### `thetaKernel`

 The theta kernel of the definite pair `stdSpace E n`, `stdSpace E n'`, for characters `a`, `b`
of weights `ea`, `eb` and a subgroup `K` of the finite points. The data are the finite part of
𝒮(Hom), with the action `pairWeilFinite (stdSpace E n) (stdSpace E n') a b` of the finite points. A
datum `f` gives a linear map from vectors of weight `(κ, e)` in rank `n` to those of weight
`(κ, ea)` in rank `n'`. Its matrix is `schurJet κ (jetSeries _ c f)`: the jets along `schur κ` of
the Taylor series of the theta function of `f`, with derivatives scaled by `c`. 
