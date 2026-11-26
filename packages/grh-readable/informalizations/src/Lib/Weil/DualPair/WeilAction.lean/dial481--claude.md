---
{
  "module": "src/Lib/Weil/DualPair/WeilAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/WeilAction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/WeilAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Laws of the Weil action of a pair: translations, real points, levels, rational maps

Let `S`, `T` be hermitian spaces (`New.Space`). A pair `p = (g, h)` of adelic points of their
unitary groups acts on `Hom(S, T)` by `x ↦ h x g⁻¹` (`New.G.onHom`). It acts on the Weil
representation of `Hom(S, T)` by `New.pairWeil S T a b p`, the Weil operator times
`New.pairChar a b p = a (det h) / b (det g)`. The file proves that this action preserves the inner
product. It also describes the action of the real points `(x, y)` of the two unitary groups of signs
`s`, `s'` on the Fock space. It then writes maps, the Heisenberg cocycle and the Heisenberg
operators of `Hom(V, V')` in rational coordinates and defines theta lifts.

## Main definitions and results

* `New.pairWeil_of_mem_Gamma`: rational points (`New.Space.Γ`) act by `f ↦ f (h⁻¹ · g)`.
* `New.pairTheta_mul`, `New.continuous_pairTheta`: the theta kernel `New.pairTheta` satisfies
  `pairTheta S T a b f (p * q) = pairTheta S T a b (pairWeil S T a b q f) p`, and it is continuous.
* `New.realPairWeil γ γ'`: the representation on the Fock space `New.PairFock E s s'` of
  `Hom(S, T)`. It is the oscillator operator of `z ↦ y z x⁻¹` times `det y ^ γ * det x ^ (-γ')` at
  each place.
* `New.pairWeil_integrated`, `New.pairWeil_integrated_all`: on `New.Space.integrated _ v f`, the
  vector `f` with its real vacuum replaced by `v`, real points act on `v` by `New.realPairWeil` and
  finite points act on `f`.
* `New.exists_level_pairWeil`: a datum in the finite part `New.Space.finitePart` of `Hom(S, T)` (the
  span of finite Heisenberg translates of the vacuum) is fixed under `New.pairWeil` by a product of
  open subgroups of the two finite adelic unitary groups.
* `New.Space.IsThetaLift`: a family of maps between spaces of forms computes the theta integrals
  between standard positive spaces.

Notions from other files:
* `New.G`: The adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the
  identity matrix at the finite places.
* `New.GInf E s`: the real points, one complex unitary group `U(diag s)` for each infinite place;
  `New.homSigns s s'` is the sign vector `(i, j) ↦ s' i * s j` of `Hom(S, T)`, and `New.realSigns`
  repeats a sign vector at every infinite place.
* `New.Fock.realWeil`: The Weil representation of U(ε) on the Fock space `𝓕 ε`; its multiplier
  `New.Fock.realMultiplier u` is the conjugate of the determinant of the negative block of u.
* `New.blockDiagAlg ε`: the complex matrices that commute with `diag ε`, that is, the block
  diagonal matrices for the partition of the indices by sign; `New.principalMinor y p` is the
  determinant of the block of `y` on the indices that satisfy `p`.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places; `New.Space.Γ` is the group
  of rational points of its unitary group, inside `New.G`.
* `New.AutChar E`: the continuous characters of the norm-one adeles `U(1)(𝔸)` that are trivial on
  rational points; `a`, `b` are such characters.
* `New.Space.hom`: The space `Hom(S, T)` of `n' × n` matrices, indexed by pairs (row, column);
  `New.matrixToVec` reads a matrix as a vector on these pairs.

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence`, `Lib.Weil.Fock.OscillatorPair`,
`Lib.Weil.CompactLift.DefiniteThetaLift` and `Lib.Weil.Periods.Unfolding` for sources.



## Basic laws, translation law and continuity of theta kernels

* `New.G.onHom_mulVec`, `New.G.det_onHom`, `New.G.onHom_mem_Gamma`: matrix, determinant and
  rationality of `New.G.onHom p`.


 ### Matrices as vectors on pairs of indices 

### `star_matrixToVec_dotProduct_matrixToVec`

 For matrices x and y, the dot product of the conjugate of the vector of x with the vector of y
is tr(xᴴy). 

### `kronecker_mulVec_eq_matrixToVec`

 On vectors indexed by pairs, `A ⊗ₖ Bᵀ` is the map `x ↦ A x B`. 

 ### The homomorphism to the group of Hom(S, T), and determinants 

### `G.onHom_mulVec`

 The image of a pair (g, h) in the unitary group of Hom(S,T) acts on an adelic vector x, read
as an n′ × n matrix, by x ↦ hxg⁻¹. 

### `G.onHom_eq`

 The real components of `onHom p` are `Fock.pairHom`, the finite one is `U.kroneckerHom`. Here
`p.1.1 w`, `p.2.1 w` are the components of `g` and `h` at the infinite place `w`, and `p.1.2`,
`p.2.2` their finite components. 

### `G.onHom_snd`

 The finite component of `onHom (g, h)` is `h_f ⊗ₖ (g_f⁻¹)ᵀ`. 

### `G.onHom_fin`

 For finite points `g`, `h`, the image of the pair `((1, g), (1, h))` under `onHom` has
infinite component `1`. 

### `G.det_onHom`

 For (g, h) in the unitary groups of ranks n and n', the determinant of x ↦ hxg⁻¹ on
Hom(S,T) is (det h)^n (det g)^(−n'). 

### `det_fst`

 The infinite component of `det g` is, at each infinite place `w`, the determinant of the
component of `g` at `w`. 

### `det_atPlace`

 The component of `det g` at a finite place `w` is the determinant of the component of `g`
at `w`. 

### `Space.vecAtPoint_hom`

 For a rational n′ × n matrix x, the adelic vector attached to it in the space Hom(S,T) is
the matrix x_T⁻¹ x x_S, with x_S, x_T the points of S and T. 

### `G.onHom_mem_Gamma`

 If `g` and `h` are rational points of the unitary groups of `S` and `T`, then the point of the
unitary group of `Hom(S, T)` given by `x ↦ h x g⁻¹` is rational. 

### `AutChar.apply_det_ratEmbed`

 A character of `[U(1)]` is trivial on the determinants of rational points. 

 ### The Weil action of the pair and the theta kernel 

### `pairWeil_apply`

 For p = (g, h) in G(s) × G(s′), `New.pairWeil S T a b p` is the Weil representation ω of
`S.hom T` at the element x ↦ hxg⁻¹ (`New.G.onHom p`), multiplied by the scalar
`pairChar a b p` = a(det h) b(det g)⁻¹. 

### `dataInner_pairWeil`

 The Weil action `pairWeil S T a b p` of a pair preserves the inner product `dataInner` on data
for `Hom(S, T)`. 

### `pairWeil_of_mem_Gamma`

 Let `S` and `T` be spaces over the CM field `E` (with Weil data) and `a`, `b` characters of its
norm-one adeles. Rational points `g` of `U(S)` and `h` of `U(T)` act by substitution: the value of
`pairWeil S T a b (g, h) f` at `x` is `f (h⁻¹ x g)`. Here `x` is a matrix read as a vector on pairs
of indices, on which `x ↦ h⁻¹ x g` is multiplication by the Kronecker product `h⁻¹ ⊗ₖ gᵀ`. 

### `pairTheta_mul`

 The translation law of the theta kernel: translating the point by `q` on the right is acting
on the datum by `q`. 

### `continuous_pairTheta`

 For a CM field `E` with Weil data, pointed hermitian spaces `S` and `T` over `E`, and
automorphic characters `a`, `b` of U(1)(𝔸), consider the theta kernel
(f, (g, h)) ↦ θ(ω_{a,b}(g,h)f). Here f is a Schwartz function in 𝒮(Hom(S,T)), g lies in `G E s`,
h lies in `G E s'`, ω_{a,b} is the Weil representation attached to `a` and `b`, and θ is the theta
functional of Hom(S,T). This kernel is jointly continuous in the datum f and the point (g, h). 


## The real Weil action of a pair and the kernel property

Real points `(x, y)` of a pair of unitary groups of signs `s`, `s'` act on the Fock space of
`Hom(S, T)`.

* `New.realPairWeil_polyVector`: block diagonal points (`New.blockDiagAlg`) act on the vector
  `New.Fock.polyVector _ P` of a polynomial `P` by a substitution and a character.
* `New.realPairWeil_vacVector`: they act on the vacuum by that character.


### `PairFock`

 The Fock space for the signs s′_i s_j of Hom(S,T), repeated at every infinite place. 

### `pairHomInf`

 The homomorphism sending real points (x, y) to the action z ↦ y_w z x_w⁻¹ on matrices at each
infinite place w, as one block diagonal unitary matrix (`blockU`), in `USign` for the signs of
`Hom(S, T)` repeated at every infinite place. 

### `realPairWeil`

 The real Weil representation of the pair with weights γ, γ′: (x, y) acts by
∏_w (det y_w)^{γ_w} (det x_w)^{−γ′_w} times the Fock operator of z ↦ y z x⁻¹. 

### `continuous_realPairWeil`

 The real Weil action `New.realPairWeil γ γ'` is jointly continuous in the real point and the
Fock vector. 

### `principalMinor_eq_det_toSquareBlock`

 The principal minor of `y` on the indices of sign `σ` is the determinant of the diagonal block
of `y` for `σ` in the partition of the indices by sign. 

### `det_eq_prod_principalMinor`

 Let the isometry `u` of signs `s` be block diagonal for the partition of the indices by sign
(it lies in `New.blockDiagAlg s`, the matrices that commute with the sign matrix). Then its
determinant is the product, over the signs `σ`, of its principal minors on the indices of
sign `σ`. 

### `Fock.realMultiplier_of_mem_blockDiagAlg`

 For a block diagonal isometry `u = diag(γ, z)` of the form with signs `ε` (`z` is the block on
the negative coordinates), the multiplier of the real Weil representation is `det z⁻¹`. 

### `Fock.realVac_mulVec_of_mem_blockDiagAlg`

 A block diagonal isometry is a unitary matrix, so it preserves the Gaussian `realVac`, which
depends on `y` only through `star y ⬝ᵥ y`. 

### `vacuumFn_mulVec_of_mem_maxCompact`

 An element `k` of the maximal compact subgroup (unitary matrices at the infinite places,
integral at the finite places) preserves the vacuum function. 

### `weilMultiplier_mul_of_mem_maxCompact`

 The multiplier `Δ` of the Weil representation (`New.weilMultiplier`) is multiplicative for
factors from the maximal compact subgroup: `Δ(k g k') = Δ(k) Δ(g) Δ(k')` for `k`, `k'` in it. 

### `Space.dataInner_omega_of_mem_maxCompact`

 The maximal compact subgroup acts on data by substitution: for `k` in it, the coefficient
`⟨ϱ(x) vac, ω(k) f⟩` is the multiplier of `k` times the coefficient `⟨ϱ(k⁻¹ x) vac, f⟩`. These
coefficients are the values at `x` and `k⁻¹ x` of the functions underlying `ω(k) f` and `f`. 

### `Fock.realWeil_polyVector_of_mem_blockDiagAlg`

 Let `u = diag(γ, z)` be a block diagonal isometry of the form with signs `ε`, with `γ` on the
positive and `z` on the negative coordinates. The real Weil representation of `u` acts on the Fock
vector `polyVector ε P` of a polynomial `P` by `det z⁻¹` times the substitution
`X i ↦ ∑ j, γ j i • X j` on the positive and `X i ↦ ∑ j, z⁻¹ i j • X j` on the negative variables.
This is the standard action of the maximal compact subgroup of `U(p, q)` in the Fock model (Folland,
*Harmonic Analysis in Phase Space*). 

### `kronecker_mem_blockDiagAlg`

 The Kronecker product of matrices that are block diagonal for the signs `s'` and `s` is block
diagonal for the product signs `New.homSigns s s'`. 

### `realPairWeil_polyVector`

 The maximal compact subgroups act by a substitution and the character of the vacuum. Let `x`,
`y` be block diagonal for the signs `s`, `s'` of signatures `(p, q)`, `(p', q')`. The scalar
is the product over the places of
`(det y⁺) ^ (γ - q) (det y⁻) ^ (γ - p) (det x⁺) ^ (q' - γ') (det x⁻) ^ (p' - γ')`.
At each place, the variable `X a b` goes to `∑ y i a * x⁻¹ b j * X i j` if `s' a = s b`, and to
`∑ y⁻¹ a i * x j b * X i j` otherwise, with the sums over the variables of that place.

A special case of the standard action of the maximal compact subgroup in the Bargmann–Fock model,
for a unitary dual pair. 

### `realPairWeil_vacVector`

 Block diagonal points `x` of the source (signs `s`) and `y` of the target (signs `s'`) act on
the real vacuum by a character. At the place `w`, the determinant of the block of sign `σ` of `y`
has the exponent `γ w` minus the number of signs `-σ` in `s`; that of `x` has the number of signs
`-σ` in `s'` minus `γ' w`. This is the case `P = 1` of `New.realPairWeil_polyVector`. 

### `pairThetaKer`

 The theta kernel of the pair: the action `New.pairWeil S T a b` with the theta functional. It is
continuous and left invariant under the rational points of both groups. 

### `pairWeil_integrated`

 Let `a` have weight `γ` and `b` weight `γ'` (`HasWeight`, tame parts `ψ`, `ψ'`): at a real point
`z` of U(1), `a z = ∏_w z_w ^ γ w`, and likewise `b` with `γ'`. For a Fock vector `v` and `f` in
𝒮(`S.hom T`), write v ⊗ f = ∫ v(y) ϱ(y)f dy for the integrated Heisenberg action
(`New.Space.integrated`). Then for archimedean points x ∈ G_∞(s), y ∈ G_∞(s′), taken as adelic
elements with trivial finite part, ω_{a,b}(x,y)(v ⊗ f) = (Ω(x,y)v) ⊗ f, where ω_{a,b} is
`New.pairWeil S T a b` and Ω is `New.realPairWeil γ γ'`. 

### `pairWeil_integrated_fin`

 Finite points `(k, k')` act on `v ⊗ f` (`New.Space.integrated`, `v` a vector of the Fock space
`New.PairFock E s s'`) through `f`. 

### `pairWeil_integrated_right`

 Let the character `a` have weight `γ` (with tame part `ψ`). For a Fock vector `v` and `f` in
𝒮(`S.hom T`), let v ⊗ f = ∫ v(y) ϱ(y)f dy be the integrated Heisenberg action
(`New.Space.integrated`). For an archimedean point h ∈ G_∞(s′), taken with trivial finite part and
paired with 1 in the first group, `New.pairWeil S T a b` sends v ⊗ f to (Ω(1,h)v) ⊗ f with
Ω = `New.realPairWeil γ 0`; no weight of `b` is needed. 

### `pairWeil_integrated_all`

 On `v ⊗ f`, for spaces `S`, `T` and characters `a`, `b` of weights `γ`, `γ'` (with tame parts
`ψ`, `ψ'`), the real part `(x, y)` of a pair acts on the Fock vector `v` by
`New.realPairWeil γ γ'`, and the finite part `(k, k')` acts on `f`. 

 ## Open levels fixing finite data 

### `exists_level_pairWeil`

 Let `E` be a CM field with Weil data, `S`, `T` hermitian spaces with points, and `a`, `b`
characters of U(1)(𝔸) trivial on its rational (norm-one) points. Suppose `f` lies in the finite
part of 𝒮(Hom(S, T)), which is the span of the translates of the vacuum under the finite Heisenberg
operators. Then there are open subgroups `K`, `K'` of the finite adelic unitary groups `Gf E n`,
`Gf E n'` such that `pairWeil S T a b` fixes `f` at every `((1, k), 1, k')` with `k ∈ K` and
`k' ∈ K'` (these elements are trivial at the infinite places). 


## Maps in rational coordinates, Heisenberg cocycle and theta lifts

A space (`New.Space`) has a Gram matrix `J` over `E` and an adelic point `x`. The Weil
representation of `Hom(V, V')` is written in the adelic coordinates that the points give.

* `New.Space.homAtPoint`: passes from a matrix `w` in rational coordinates to `x'⁻¹ w x`.
* `New.Space.homBicharacter_eq`: the Heisenberg bicharacter in rational coordinates is the
  standard character of a trace.
* `New.Space.homHeisenbergOp`: the Heisenberg operator of a matrix in rational coordinates.


### `homAtPoint`

 The additive map sending an adelic matrix w : V → V' in rational coordinates to x'⁻¹wx, its
vector in the adelic coordinates of Hom(V,V'); here x = `V.x` and x' = `V'.x` are the points. 

### `homBicharacter`

 The Heisenberg bicharacter β of Hom(V,V') evaluated at two adelic matrices x, y given in
rational coordinates. 

### `twistedPairWeil`

 The representation `New.pairWeil` of U(V) × U(V′) on 𝒮(Hom(V, V′)) with the characters `a ι` and
`a ι′`, where ι, ι′ index the bases of V, V′. 

### `homBicharacter_eq`

 The Heisenberg bicharacter of `Hom(V, V')` at two adelic matrices `x`, `y` in rational
coordinates is the standard additive character of `ȷ / 2` times the trace of `y^* x`. Here `y^*`
(`New.Space.formAdjoint`) is the adjoint of `y` for the hermitian forms of `V` and `V'`, and `ȷ`
is the element of the Weil data. 

### `finCoord_homAtPoint`

 The finite coordinates (`New.finCoord`) of `New.Space.homAtPoint` of `x` form the matrix
`α⁻¹ x'_f⁻¹ x_fin x_f`. Here `x_fin` is the finite part of `x`, `x_f` and `x'_f` are the finite
parts of the points of `V` and `V'` (`New.Space.xFin`), and `α` is the finite idele of the Weil
data. 

### `homHeisenbergOp`

 The Heisenberg operator ϱ on 𝒮(Hom(V, V′)) at `New.Space.homAtPoint` of an adelic matrix x :
V → V′ given in rational coordinates. 

### `IsThetaLift`

 A family of maps `k`, indexed by `O`, computes the theta lifts between the standard positive
spaces on ι and ι′. For every polynomial `P` and every linear functional `t` on `WeylIndex ι κ → ℂ`,
there is a linear functional `t'` on `WeylIndex ι' κ → ℂ` with the following property. For every
`o`, `Φ`, `φ` and `h`, take the integral over `g` of θ of `twistedPairWeil (a o) (g, h)` applied to
`P` tensored with `Φ`, times the coefficient of `φ` at `g` taken with `t`. This integral is the
coefficient of `k o Φ φ` at `h` taken with `t'`. 
