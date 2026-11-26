---
{
  "module": "src/Lib/Weil/DualPair/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Defs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hom(S,T), the Weil representation and theta kernel of a pair, and data modulo an ideal

For hermitian spaces `S`, `T` (`New.Space`) of ranks `n`, `n'`, the `n' × n` matrices form a space
`Hom(S, T)`. The pair `(g, h)` acts on it by `x ↦ h x g⁻¹`. The Weil representation `New.Space.ω` of
that space restricts to the pair. Theta kernels are also built from a polynomial at the real places
and a function modulo an ideal at the finite places.

## Main definitions and results

* `New.Space.hom`, `New.G.onHom`: the space `Hom(S, T)` and the map `U(S) × U(T) → U(Hom(S, T))`.
* `New.pairWeil S T a b`: the representation of the pair, twisted by `a (det h) * b (det g)⁻¹`
  (`New.pairChar`), for characters `a, b` of `[U(1)]` (`New.AutChar`).
* `New.pairTheta`: the theta kernel, the theta functional `New.Space.θ` of
  `pairWeil S T a b (g, h) f`.
* `New.Modulus`: a non-zero ideal `𝔪` of `𝓞 E` such that no prime `w` divides it together with the
  complex conjugate of `w`; `New.Modulus.ResidueRing` is the finite ring `𝓞 E ⧸ 𝔪`,
  `New.Modulus.places` the set of primes dividing `𝔪` and `New.Modulus.reduction` a reduction map
  from `New.Ô E`.
* `New.modDatum`: the vector in the data space of `New.Space.hom S T` with real part `v`, with `Ψ`
  at the primes dividing `𝔪` (`New.Space.schrodingerOp`) and the vacuum elsewhere.
* `New.modKernel`: its theta kernel `New.pairTheta`, for `v` the Fock vector of a polynomial;
  `New.stdKernel`: this kernel for the standard characters `New.stdChar` of `S` and `T`.

Notions from other files:
* `New.Space`: a hermitian space over a CM field E with `CMType E` (a chosen embedding at each
  infinite place; it contains `NumberField E` and `IsCMField E`), with a point, given by a matrix J
  over E and x in GL_n(𝔸) with xᴴJx equal to diag(s), for a sign vector s, at the infinite places
  and 1 at the finite places; `𝒮 V` is the data space of such a space V, on which the Weil
  representation acts.
* `New.WeilData`: the fixed choices that the Weil representation needs, among them a splitting
  character `υ` of the ideles of E.
* `New.AutChar`: a continuous circle-valued character of U(1)(𝔸), the norm-one adeles of E, that is
  trivial on the elements coming from E.
* `New.Fock.polyVector`: the vector P(ζ(x)) exp(−|x|²/2) of the Fock space, for a polynomial P in
  the Fock coordinates ζ(x) of a real vector x.
* `New.Space.integrated`: the bilinear map (v, f) ↦ v ⊗ f = ∫ v(y) ϱ(y)f dy over real vectors y, for
  v in the Fock space and f in 𝒮(V), with ϱ the Heisenberg representation on 𝒮(V).

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence`, `Lib.Weil.MixedModel.ZeroTerm` and
`Lib.Adelic.Unitary.WeakApproximation` for sources.



## The Weil representation and theta kernel of a pair of hermitian spaces

* `New.AutChar.spaceChar`: for a character `a` of `[U(1)]` and a rank `k`, the base change of `a`
  divided by the `k`-th power of the fixed splitting character `υ` of `New.WeilData`.
* `New.rankTwist`: the product of `a` with the `⌊n/2⌋`-th power of `υ` on norm-one ideles, for an
  index type of size `n`.
* `New.stdChar`: the standard character of a space, the power of `υ` on `[U(1)]` by the number
  of negative signs.


 ### The space of homomorphisms 

### `homSigns`

 For sign vectors s on n and s′ on n′, the sign vector on n′ × n given by the products
s′(i)s(j). 

### `matrixToVec`

 A matrix x read as the function (i, j) ↦ x_{ij} on pairs (row, column). 

### `vecToMatrix`

 A vector on pairs (row, column) as a matrix; inverse to `New.matrixToVec`. 

### `stdForm_homSigns`

 Over the adeles of the field E, let `stdForm E s` be the diagonal matrix that is diag(s) at the
infinite places and the identity at the finite ones. The standard form of the product signs on
n′ × n is the Kronecker product of that of s′ and the transpose of that of s. 

### `G.onHom`

 The homomorphism from G(s) × G(s′) to the adelic unitary group of the product signs sending
(g, h) to x ↦ hxg⁻¹ on n′ × n matrices. 

### `G.det`

 The determinant, as a homomorphism from the adelic unitary group of signs s to the group of
adeles x of E with x x̄ = 1 (the determinant of the standard form is a unit). 

### `detFin`

 For g in the finite adelic unitary group, the determinant of the element (1, g) of G, as an
adele of norm one. 

### `Space.hom`

 The space `Hom(S, T)` of `n' × n` matrices, indexed by pairs (row, column): its Gram matrix is
the Kronecker product `J_T ⊗ (J_S⁻¹)ᵀ`, its point is `x_T ⊗ (x_S⁻¹)ᵀ` (with inverse
`x_T⁻¹ ⊗ x_Sᵀ`), and the coordinate `(i, j)` has the sign `s' i * s j`. 

 ### Characters, the action of the pair and the theta kernel 

### `WeilData.upsilonU1`

 The restriction of υ to the norm-one ideles, as a character of U(1)(𝔸) trivial on the elements
coming from E. 

### `WeilData.upsilonU1_apply`

 For u in the norm-one adeles U(1)(𝔸) of the CM field E, the character `upsilonU1` takes the
value υ(u). Here υ is the splitting character contained in the Weil data on E, and u is viewed as an
idele. 

### `AutChar.spaceChar`

 The Hecke character `x ↦ a (x / x̄) * υ x ^ (-k)` of `E`, for a character `a` of `[U(1)]` and a
natural number `k`: the base change `a.baseChange` divided by the `k`-th power of the splitting
character `υ`. It is the character attached to a space of rank `k` in a dual pair. 

### `rankTwist`

 For a character a of [U(1)] and a finite index set of size n, the character a·υ^⌊n/2⌋ of [U(1)],
where υ is restricted to the norm-one ideles (`upsilonU1`). 

### `stdChar`

 The standard character of a space with signs s: the character υ^{n₋} of [U(1)], where υ is
restricted to the norm-one ideles (`upsilonU1`) and n₋ is the number of signs −1. Its Hecke
character `spaceChar` at the rank n₊ + n₋ of the space is υ^{−(n₊ − n₋)}, the power of υ by minus
the signature (`New.AutChar.spaceChar_stdChar`). 

### `stdChar_sum`

 The standard character of a sum of spaces is the product of their standard characters. 

### `stdChar_neg`

 The standard character of the negated space is the inverse of the standard character times
υⁿ, where υ is restricted to the norm-one ideles (`upsilonU1`) and n is the rank: negation
exchanges the numbers of signs 1 and −1, which add up to n. 

### `pairChar`

 For characters a, b of [U(1)], the complex character (g, h) ↦ a(det h) b(det g)⁻¹ of
G(s) × G(s′). 

### `pairWeil`

 The representation (g, h) ↦ a(det h) b(det g)⁻¹ ω(x ↦ hxg⁻¹) of the product of the two adelic
unitary groups on the data space of Hom(S, T). 

### `pairTheta`

 The theta kernel θ^{S,T}_{a,b}(f)(g, h) = θ(ω_{a,b}(g,h)f), for f in 𝒮(Hom(S,T)) and θ the
theta functional of Hom(S,T). 


## Moduli prime to their conjugates and data modulo an ideal

* `New.Modulus.liftFn`: a function of vectors modulo `𝔪` read on finite adelic vectors.


### `Modulus`

 A modulus: a nonzero ideal of O_E prime to its complex conjugate, that is, no prime w divides
it together with its conjugate w̄. 

### `Modulus.ideal`

 The ideal `𝔪` of the ring of integers of `E`. 

### `Modulus.ne_bot`

 The ideal is not zero. 

### `Modulus.not_le_star`

 No prime `w` divides the ideal together with its complex conjugate `star w`. 

### `ResidueRing`

 The residue ring O_E/𝔪 of the modulus 𝔪. 

### `instance : Fintype 𝔪.ResidueRing`

 The residue ring of a modulus is finite, as the ideal is nonzero. 

### `places`

 The set of finite places of E that divide 𝔪. 

### `instance : Finite 𝔪.places`

 Only finitely many primes divide a modulus. 

### `reduction`

 A chosen ring homomorphism Ô → O_E/𝔪, on the integral finite adeles Ô, extending reduction on
O_E, with kernel tÔ for an integral idele t equal to 1 off 𝔪. 

### `liftFn`

 A function `Ψ` of vectors modulo `𝔪`, read on finite adelic vectors `x`. Multiplying by
`idem 𝔪.places` keeps the components at the primes dividing `𝔪` and sets the others to `0`. If the
result is integral, the value is `Ψ` of its reduction modulo `𝔪`; otherwise it is `0`. 

### `modDatum`

 The datum v ⊗ Ψ ⊗ vac on Hom(S,T), for a vector v of the real Heisenberg model of Hom(S,T) and
a function Ψ on matrices modulo 𝔪: its real part is v, the lift of Ψ is put in at the places
dividing 𝔪 by `New.Space.schrodingerOp` (the operator attached to a function of finite adelic
vectors), and it is the vacuum elsewhere. 

### `modKernel`

 The theta kernel `(g, h) ↦ θ (ω_{a,b} (g, h) f)` on the product of the adelic unitary groups
of `S` and `T`, for the datum `f = modDatum S T 𝔪 Ψ v` given by a function `Ψ` on matrices modulo
`𝔪` and the Fock vector `v` of the polynomial `P`; `a` and `b` are the characters that twist
the action. 

### `stdKernel`

 The theta kernel θ^{S,T}[Ψ, P]: the kernel `New.modKernel` of a function Ψ on n′ × n matrices
modulo 𝔪 and a polynomial P, for the standard characters (`New.stdChar`) of S and T. 


## Lifts of functions modulo an ideal and the primitive character

For a modulus `𝔪`, a function `Ψ` on `n → 𝔪.ResidueRing` has a lift `𝔪.liftFn Ψ` to finite adelic
vectors.

* `New.Modulus.isSchwartzBruhat_liftFn`: the lift is Schwartz–Bruhat above `𝔪.places`
  (`New.IsSchwartzBruhat`).


 ### Reduction modulo `𝔪` and the generator of its kernel 

### `IsGenerator`

 The finite idele `t` generates the modulus `𝔪` in the integral finite adeles `Ô E`, and it is
`1` away from `𝔪`. 

### `IsGenerator.mem`

 The idele `t` is integral. 

### `IsGenerator.apply_of_notMem`

 The component of `t` at a place not dividing `𝔪` is `1`. 

### `IsGenerator.reduction_eq_zero_iff`

 The kernel of `𝔪.reduction` consists of the multiples of `t` in `Ô E`. 

### `IsGenerator.valued_apply`

 The order of `t` at every place `w` is the multiplicity of `w` in `𝔪`. 

### `IsGenerator.forall_smul_mem_iff`

 For a finite adele `y`, `𝔪 y ⊆ Ô E` if and only if `t y ∈ Ô E`. 

### `exists_generator`

 Every modulus `𝔪` is generated in `Ô E` by a finite idele that is `1` away from `𝔪`. 

### `generator`

 A finite idele `t` generating `𝔪` in `Ô E`, chosen from `exists_generator`. It is integral,
and equal to `1` at the places not dividing `𝔪`. The kernel of `𝔪.reduction` consists of the
multiples of `t` in `Ô E`. See `generator_mem`, `generator_apply_of_notMem`,
`reduction_eq_zero_iff_generator_inv_mul_mem` and `valued_generator`. 

### `isConjDisjoint_places`

 The set of primes dividing a modulus is disjoint from its complex conjugate. 

### `reduction_algebraMap`

 On global integers, `𝔪.reduction` is the usual reduction `𝓞 E → 𝓞 E ⧸ 𝔪`. 

### `isValuationPair_residueRing`

 For any a, b in O_E/𝔪 there is an idempotent e of O_E/𝔪 such that a and b both lie in the
principal ideal generated by (1 − e)a + eb; this is what `IsValuationPair` says for `⊤`. 

### `generator_spec`

 The idele `t = 𝔪.generator` is integral, has component `1` at every place not dividing `𝔪`,
and an element `x` of `Ô E` reduces to `0` modulo `𝔪` exactly when `t⁻¹ x` is integral. 

### `valued_generator`

 The idele `t = 𝔪.generator` has order equal to the multiplicity of `w` in `𝔪` at every finite
place `w`. 

### `reduction_eq_zero_iff`

 An element of `Ô E` reduces to `0` modulo `𝔪` exactly when it lies in the ideal of `Ô E`
generated by `𝔪`. 

### `reduction_congr`

 Two elements of `Ô E` with the same components at the primes dividing `𝔪` have the same
reduction modulo `𝔪`. 

### `reduction_idem_mul`

 Setting the components outside the primes dividing `𝔪` to `0` does not change the reduction
modulo `𝔪`. 

 ### Lifting functions modulo `𝔪` 

### `liftFn_one`

 The lift of the constant function `1` is the indicator of the vectors that are integral at the
primes dividing `𝔪`. 

### `liftFn_single`

 For an integral vector `x₀`, the lift `𝔪.liftFn` of the point mass at its class is the
indicator `cosetIndicator` of the vectors `x` such that `t⁻¹ (x - x₀)` is integral at the primes
dividing `𝔪`, where `t = 𝔪.generator`. 

### `liftFn_reduction_add`

 Translating a function modulo `𝔪` by the class of an integral vector `z` translates its lift
by `z`. 

### `apply_reduction_eq_of_algebraMap`

 Let `f` and `g` be ring homomorphisms to `S` from `𝓞 E ⧸ 𝔪` and from `Ô E`. If they agree on
every global integer, then `f (𝔪.reduction x) = g x` for every `x` in `Ô E`. 

### `factor_reduction`

 If `𝔪` divides `𝔫`, reduction modulo `𝔫` followed by `𝔫.ResidueRing → 𝔪.ResidueRing` is
reduction modulo `𝔪`. 

### `isSchwartzBruhat_liftFn`

 The lift of any function Ψ on (O_E/𝔪)^n to finite adelic vectors is Schwartz–Bruhat on the
places dividing 𝔪: it depends only on the components at these places, it is locally constant, and
those components stay in a compact set on its support. 

### `localInner_liftFn`

 For a modulus `𝔪` (a nonzero ideal of O_E prime to its conjugate), `𝔪.liftFn Ψ` reads a function
`Ψ` of vectors modulo `𝔪` on finite adelic vectors `x`: it keeps the components of `x` at the primes
dividing `𝔪`, and takes `Ψ` of the reduction if the result is integral and `0` otherwise. The
theorem says that `localInner 𝔪.places` of two such lifts is the mean of `conj (Ψ y) * Ψ' y` over
all vectors `y` modulo `𝔪`. Here `localInner 𝔪.places` is `∫ conj(Φ) Φ'` over the finite adelic
vectors integral off `𝔪.places`, for the Haar measure giving `Ô^n` mass one. 

 ### The primitive character modulo `𝔪` 

### `exists_isPrimitive_addChar`

 Let 𝔪 be a modulus of the CM field E, where E carries Weil data. There is a primitive additive
character ψ′ of the residue ring `𝔪.ResidueRing` = O_E/𝔪 with ψ′(x mod 𝔪) = ψ₀(t⁻¹x) for all `x` in
`Ô E`. Here `t = 𝔪.generator` is the chosen finite idele generating 𝔪 in `Ô E`, and ψ₀ is the
character `selfDualAddChar E` of the finite adeles, z ↦ ψ_f(ȷαᾱz), built from the Weil data, for
which `Ô E` is self-dual. 

### `primAddChar`

 The character ψ′ of `𝔪.ResidueRing` with ψ′(x mod 𝔪) = ψ₀(t⁻¹x) for `x` in `Ô E`, where
`t = 𝔪.generator` (`New.Modulus.primAddChar_reduction`). It is primitive
(`New.Modulus.isPrimitive_primAddChar`) because `Ô E` is self-dual for ψ₀
(`forall_selfDualAddChar_mul_eq_one_iff`). 

### `primAddChar_reduction`

 For a modulus 𝔪 of the CM field E with Weil data, the character ψ′ = `𝔪.primAddChar` of O_E/𝔪
satisfies ψ′(x mod 𝔪) = ψ₀(t⁻¹x) for `x` in `Ô E`. Here `t = 𝔪.generator` is the chosen finite idele
generating 𝔪 in `Ô E`, and ψ₀ = `selfDualAddChar E` is the character z ↦ ψ_f(ȷαᾱz) of the finite
adeles given by the Weil data. 

### `isPrimitive_primAddChar`

 The additive character ψ′ = `New.Modulus.primAddChar` of O_E/𝔪 is primitive: for every nonzero a
in O_E/𝔪, the character x ↦ ψ′(ax) is nontrivial. 

### `rho_star_idem_smul_projOn`

 Let `V` be a space, `f` a vector of `𝒮 V` and `y` a finite adelic vector. Translate the mean
`V.projOn 𝔪.places f` of `f` over integral translations by the part of `y` above the conjugates of
the primes dividing `𝔪`, using the Heisenberg operator `V.ϱ`. The result is `V.schrodingerOp`
applied to `f` with the function x ↦ ψ₀(y* x)·1(x). Here ψ₀ is `selfDualAddChar E` and 1
(`boxIndicator`) is the indicator of the vectors integral at every prime dividing `𝔪`. Only the part
`idem 𝔪.places • x` of `x` above those primes enters. 

### `schrodingerOp_char_eq_translate_projOn`

 Let `u` be an integral vector, and let `Ψ x = ψ′(x ⬝ᵥ (u mod 𝔪))`, where ψ′(x mod 𝔪) = ψ₀(t⁻¹x)
is `𝔪.primAddChar` and `t = 𝔪.generator`. Then the operator `V.schrodingerOp` on 𝒮(V) attached to
the lift `𝔪.liftFn Ψ` sends `f` to `V.ϱ` applied to `V.projOn 𝔪.places f`. Here `V.ϱ` is taken at
the adelic vector with zero real part and finite part α times the conjugate of the part of `t⁻¹ u`
at the primes dividing `𝔪`. The map `𝔪.liftFn Ψ` is `Ψ` of the reduction of the part at those primes
when integral and `0` otherwise, and `projOn` is the mean of the finite Heisenberg operators over
integral vectors supported at the primes dividing `𝔪` and their conjugates. 

### `schrodingerOp_single_eq_mean_translate_projOn`

 The operator named by the indicator of a class `a` modulo `𝔪` is a weighted mean of translates.
Choose for every class `b` of vectors modulo `𝔪` an integral vector `u b` in it, and let `y b` be
the conjugate of the part of `t⁻¹ u b` at the places dividing `𝔪`, where `t = 𝔪.generator`. Then the
operator `V.schrodingerOp` attached to the lift of the point mass at `a` sends `f` to the mean over
`b` of `ψ′(-a ⬝ b)` times the translate of `V.projOn 𝔪.places f` by the finite Heisenberg operator
`V.finHeisenbergOp (y b)`, which equals `V.ϱ (finVec (y b))` because `y b` has norm zero. Here ψ′ is
`New.Modulus.primAddChar`, and `V.projOn 𝔪.places f` is the mean of `f` over integral translations
at those places and their conjugates. 


## Kronecker products of rational matrices in the coordinates of Hom(V,T)

`New.Space.hom_point_inv_mul_kronecker` reads a Kronecker product A ⊗ Bᵀ of rational matrices in the
adelic coordinates of Hom(V,T): it is (x_T⁻¹A) ⊗ (Bx_V)ᵀ, x_V and x_T being the points of V and T.


### `hom_point_inv_mul_kronecker`

 Let `E` be a CM number field with a chosen embedding at each infinite place (`CMType E` contains
`NumberField E` and `IsCMField E`), and `V`, `T` hermitian spaces over `E` with points x_V, x_T
(the adelic matrices `V.x`, `T.x`). For matrices A, B over E, read adelically by `toAdele`, the
inverse of the point of Hom(V,T) times A ⊗ Bᵀ is (x_T⁻¹A) ⊗ (Bx_V)ᵀ. 

### `noncomputable instance : Invertible V.J`

 The Gram matrix of a hermitian space is invertible. 
