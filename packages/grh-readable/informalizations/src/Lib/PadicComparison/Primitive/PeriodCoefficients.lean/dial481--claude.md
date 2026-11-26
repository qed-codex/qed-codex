---
{
  "module": "src/Lib/PadicComparison/Primitive/PeriodCoefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Primitive/PeriodCoefficients.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Primitive/PeriodCoefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tilts and period coefficients of p-adic tests: products, comparisons, theories

This file treats the `p`-adic side of the comparison of cohomologies. A `p`-adic test `c`
(`New.Variety.PadicTest`) has a ring `R = c.ProdRing`, a generic ring `R[1/p] = c.GenericRing` and a
tilt `R♭` (`New.Variety.PadicTest.tilt`), an algebra over `O♭ = OFlat`. Here `^` denotes `p`-adic
completion. `S` is an `A_inf`-algebra and `K` is an `S`-algebra.

## Main definitions and results

* `New.Variety.bijective_prod_tilt`: bijectivity of `x ↦ (f x, g x)`, which recognises a product,
  passes from the rings of `p`-adic tests to their tilts.
* `New.Variety.IsPeriodRingPair`: `S` is `p`-torsion-free and `p`-complete, `p` divides the image of
  `ξ`, and `τ` is a unit in `K`.
* `New.Variety.hasPartitions_periodAlg`: a functor `Ψ` with an isomorphism `θ` from the period
  coefficients `asModules (tilt ⋙ periodAlg S) ⋙ tensorWith K K` turns a product of two tests into a
  product (`New.Variety.HasPartitions`).
* `New.Variety.CoeffCompBijective.periodAlg_of_almostCoeff`: for an `A_inf`-algebra `S` with
  `IsPeriodRingPair p S K` and `Flat S K`, under base-change hypotheses on `N` and `N'` and with
  `ψ`, `ψ'` perfect and torsion-free, bijectivity of a comparison of cohomology groups
  (`New.Variety.CoeffCompBijective`) passes from the coefficients `b ↦ b ⊗ (O♭ ⊗ S) ⊗ 𝔪`
  (`New.Variety.almostCoeff`) to the coefficients `b ↦ K ⊗ (S ⊗ W(b))^` (`New.Variety.periodAlg`).
  The bridge is the ideal `W(𝔪)` of `A_inf` (`New.Lift.wittOfMaxIdeal`). It reduces to `𝔪` modulo
  `p` and contains `τ` (`New.Period.tau`).
* `New.Variety.primitiveMap`: the `O♭`-algebra map `O♭ ⊗_{𝔽_p} LC(Spec R[1/p]) → R♭` that extends
  `New.Variety.locConstToTilt`, where `LC` denotes locally constant functions.
* `New.Variety.tiltTheory`: with coefficients `R ↦ R♭ ⊗_{O♭} M`, a theory (`New.Variety.Theory`)
  along `New.Variety.genericTestOver`.

Notions from other files:
* `New.Period.OFlat`: the ring `O♭`, the inverse limit of `O_C / p` along `x ↦ x ^ p`.
* `New.Variety.IsPerfectTorsionFree b`: the `O♭`-algebra `b` is perfect, and `pFlat`, the class of
  `ξ` modulo `p`, is a non-zero-divisor on it.
* `New.Variety.CoeffCompBijective β α F`: the comparison of cohomology groups along `β` and `α` is
  bijective in every degree for the coefficients `F`.
* `New.Variety.moduleCoeff F`: a functor `F` to modules, read as a functor to abelian groups, to
  serve as coefficients of cohomology.

## Relation to the literature

Known; see `Lib.PadicComparison.Descent.TestCovers` and `Lib.PadicComparison.HodgeTate.PeriodMap`
for sources.



## Products of p-adic tests under tilting and product-preserving functors

A product of two objects is recognised here by the map `x ↦ (f x, g x)` being bijective.


### `_root_.Function.Bijective.map_prod`

 If `x ↦ (f x, g x)` is bijective for linear maps `f : X ⟶ Y` and `g : X ⟶ Z`, then so is
`x ↦ (U.map f x, U.map g x)` for every functor `U` from modules to types that preserves finite
products. 

### `bijective_prod_tilt`

 Tilting keeps the product of two tests: if maps of `p`-adic tests `f : c ⟶ d` and `g : c ⟶ d'`
present the ring of `c` as the product of the rings of `d` and `d'`, then the induced maps present
the tilt of `c`, read as an `O♭`-module (`asModules tilt`), as the product of the tilts of `d` and
`d'`. 


## Period ring pairs and additivity of period coefficients

Let `S` be an `A_inf`-algebra and `K` an `S`-algebra. The period coefficient sends a `p`-adic test
with ring `R` to `K ⊗ (S ⊗ W(R♭))^`, where `^` is `p`-adic completion. `Ψ` is any functor
isomorphic to it.


### `IsPeriodRingPair`

 The `A_inf`-algebra `S` is `p`-torsion-free and `p`-adically complete, `p` divides the image of
`ξ` in `S`, and the image of `τ` in the `S`-algebra `K` is a unit. 

### `IsPeriodRingPair.dvd_xi`

 The prime `p` divides the image of `ξ` in `S`. 

### `IsPeriodRingPair.isUnit_tau`

 The image of `τ` in `K` is a unit. 

### `isPeriodRingPair_OC`

 `O_C` and `ℂ_p` form a period ring pair: `O_C` is `p`-torsion-free and `p`-complete, `θ ξ = 0`
for `θ = theta`, the structure map `A_inf → O_C`, and `θ τ ≠ 0` is a unit of the field `ℂ_p`. 

### `hasPartitions_periodAlg`

 Let `Ψ` be isomorphic (by `θ`) to the period coefficient `c ↦ K ⊗ (S ⊗ W(R♭))^`. Then `Ψ` has
partitions: tests can be cut along idempotents, and `Ψ` sends a product of two tests to the
product of its values. 

### `IsPeriodRingPair.pFlat_smul_eq_zero`

 For a period ring pair, `pFlat`, the class of `ξ` modulo `p`, kills `O♭ ⊗ S`. 

 ## Passing bijectivity from almost coefficients to period coefficients 

### `mem_wittOfMaxIdeal_of_natCast_mul_mem`

 If `p * y` lies in `W(𝔪) = wittOfMaxIdeal`, for `𝔪` the maximal ideal of `O♭`, so does `y`:
`W(𝔪)` is the kernel of the map to the Witt vectors of the residue field, a domain in which
`p ≠ 0`. 

### `exists_isReductionMod_wittOfMaxIdeal`

 There is a linear map `W(𝔪) → 𝔪` that is onto with kernel `p W(𝔪)`: the zeroth coordinate.
Here `𝔪` is the maximal ideal of `O♭` and `W(𝔪) = wittOfMaxIdeal`. 

### `exists_comp_eq_tau_smul_id`

 There are `S`-linear maps between `S ⊗ W(𝔪)` and `S`, with `W(𝔪) = wittOfMaxIdeal`, that compose
to `τ` in both orders: `s ⊗ w ↦ w s` and `s ↦ s ⊗ τ`. 

### `CoeffCompBijective.completion_wittOfMaxIdeal_of_almostCoeff`

 The completed step of `CoeffCompBijective.periodAlg_of_almostCoeff`. Let `ψ`, `ψ'` be functors
to `O♭`-algebras with perfect values on which `pFlat` is regular, compared by `β` along `φ`, and let
`S` be a `p`-torsion-free `A_inf`-algebra; `α : N' ⟶ φ ⋙ N` compares `N` and `N'`, the functors on
`C` and `C'` whose cohomology is taken. If the comparison is bijective for the coefficients
`b ↦ b ⊗ (O♭ ⊗ S) ⊗ 𝔪`, then it is bijective for the coefficients `b ↦ ((S ⊗ W(𝔪)) ⊗ W(b))^`. Here
`𝔪` is the maximal ideal of `O♭`, `W(𝔪) = wittOfMaxIdeal`, and `^` is the `p`-adic completion. 

### `nonempty_completion_wittOfMaxIdeal_iso`

 After `p`-adic completion and `K ⊗ –`, the functors `b ↦ (S ⊗ W(𝔪)) ⊗ W(b)` and
`b ↦ S ⊗ W(b)` are isomorphic, for a period ring pair `(S, K)`: tensored with `W(b)`, the maps of
`exists_comp_eq_tau_smul_id` compose to `τ`, a unit of `K`. Here `W(𝔪) = wittOfMaxIdeal`, for `𝔪`
the maximal ideal of `O♭`. 

### `CoeffCompBijective.periodAlg_of_almostCoeff`

 Let `ψ`, `ψ'` be functors to `O♭`-algebras with perfect values on which `pFlat` is regular,
compared by `β` along `φ`, and let `α : N' ⟶ φ ⋙ N`. Let `S` be an `A_inf`-algebra and `K` a flat
`S`-algebra that form a `New.Variety.IsPeriodRingPair`. Suppose that the cohomology of `N` commutes
with flat extension of coefficients. Suppose also that the cohomology of `N'` commutes with `K ⊗ –`
for coefficients that factor through `ψ'`. If the comparison is bijective for the coefficients
`b ↦ b ⊗ (O♭ ⊗ S) ⊗ 𝔪`, `𝔪` the maximal ideal of `O♭`, then it is bijective for the
coefficients `b ↦ K ⊗ (S ⊗ W(b))^`, with `^` the `p`-adic completion. 


## Near-zero submodules and the generic fibre of a p-adic test

* `New.Variety.PadicTest.nearZeros`: the submodule of near-zero elements.
* `New.Variety.PadicTest.bijective_locConstAlg_map_algebraMap`: locally constant functions on
  `Spec R` and on `Spec R[1/p]` correspond.
* `New.Variety.genericTestOver`: the functor `c ↦ R[1/p]` to tests over `Ω`.


### `instance (F : ModuleCat S ⥤ ModuleCat S) [F.Additive] : (moduleCoeff F).Additive`

 For an additive functor `F` of modules, `moduleCoeff F` is additive. 

### `PadicTest.nearZeros`

 Near-zero elements. Let `κ f` be submodules of `X` indexed by maps of tests `f : c ⟶ d`, and
let `I` be an ideal of `R[1/p] = c.GenericRing`. This is the submodule of the `y` for which some
`a ∈ I` has `y ∈ κ f` whenever `f` makes `1 - a` a unit. 

### `PadicTest.bijective_locConstAlg_map_algebraMap`

 Every locally constant function on `Spec R[1/p]` with values in `ZMod p` extends uniquely to
`Spec R`, for the ring `R = c.ProdRing` of a `p`-adic test. 

### `genericTestOver`

 The functor sending a `p`-adic test with ring `R` to `R[1/p]`, a test over `Ω` with algebra
structure through `Ω → ℂ_p`. 


## Locally constant functions into the tilt and the theory R♭ ⊗ M

Take an ideal `I` of `R[1/p]`. The maps of tests that kill `I` are those whose tilt factors through
the perfect quotient of `R♭` by the ideal `New.Variety.PadicTest.tiltNearZeros`.


### `PadicTest.tiltNearZeros`

 The ideal of the tilt `R♭` of `c` of the elements `y` for which some `a ∈ I` has `g♭ y = 0`
for every map of tests `g` that makes `1 - a` a unit, `g♭` the map of tilts: the near-zero
elements (`PadicTest.nearZeros`) for the kernels of the maps of tilts. 

### `locConstToTilt`

 For a `p`-adic test `c` with ring `R = c.ProdRing`, the natural map of `𝔽_p`-algebras from the
locally constant functions `Spec R[1/p] → 𝔽_p` to the tilt `R♭`. A function is extended to
`Spec R`, restricted to `Spec (R/p)` and read as the element `x` of `R/p` whose germ at each prime
is the value there. It goes to the constant sequence `(x, x, …)`, which lies in `R♭` because
`t ^ p = t` in `𝔽_p`. 

### `oFlatLocConst`

 The functor from test rings to `O♭`-algebras sending `A` to `O♭ ⊗_{𝔽_p} LC(A)`, where `LC(A)` is
the ring of locally constant functions `Spec A → 𝔽_p`. 

### `primitiveMap`

 The natural map of `O♭`-algebras `O♭ ⊗_{𝔽_p} LC(Spec R[1/p]) → R♭` for `p`-adic tests with
ring `R`, where `LC` denotes the locally constant `𝔽_p`-valued functions. It is the extension of
`locConstToTilt` to `O♭`-algebras, its transpose under base change to `O♭`. 

### `PadicTest.le_ker_of_tiltNearZeros_le_ker`

 Let `f : c ⟶ d` be a map of `p`-adic tests and `I` an ideal of the generic ring `R[1/p]` of `c`.
Suppose the map of tilts `f♭` kills the ideal `PadicTest.tiltNearZeros c I`, which consists of the
elements `y` of the tilt `R♭` for which some `a ∈ I` has `g♭ y = 0` for every map of tests `g` out
of `c` that makes `1 - a` a unit. Then the induced map `mapGeneric f` of generic rings kills `I`. 

### `PadicTest.perfectRing_quotient_tiltNearZeros`

 For an ideal `I` of the generic ring `R[1/p]` of `c`, the quotient of the tilt `R♭` by the
ideal `PadicTest.tiltNearZeros c I` is perfect. 

### `PadicTest.mem_nearZeros_of_rTensor_eq_zero`

 Let `M` be an `O♭`-module and `J = PadicTest.tiltNearZeros c I`. Let `x ∈ R♭ ⊗_{O♭} M` have
image zero in `(R♭ ⧸ J) ⊗ M`. Then the same holds for `x` and the maps `g♭ ⊗ M`, `g♭` the map of
tilts: for some `a ∈ I`, `(g♭ ⊗ M) x = 0` for every map of tests `g` that makes `1 - a` a unit. 

### `tiltTheory`

 The theory (`New.Variety.Theory`, for the prime `ℓ = p`) on `p`-adic tests along `R ↦ R[1/p]`
(`New.Variety.genericTestOver`), with coefficients `R ↦ R♭ ⊗_{O♭} M`. It needs `p` invertible in
`Ω`, and every perfect `O♭`-algebra acyclic for these coefficients (`ac`,
`New.Variety.IsAcyclicOnPerfect`). For an ideal `I` of `R[1/p]`, the maps of tests that kill `I` are
those whose tilt factors, uniquely, through the perfect quotient `R♭ ⧸ J`, with
`J = PadicTest.tiltNearZeros c I`. Besides `p` killing the coefficients and Zariski descent (tilting
and `· ⊗ M` keep products), this gives the two other properties of a theory: restriction of
cohomology to these maps is onto, and a section that dies along them vanishes near every maximal
ideal containing `I`. 
