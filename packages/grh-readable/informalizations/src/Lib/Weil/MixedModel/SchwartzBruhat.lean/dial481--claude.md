---
{
  "module": "src/Lib/Weil/MixedModel/SchwartzBruhat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/SchwartzBruhat.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/SchwartzBruhat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Schwartz–Bruhat functions on a set of places and the Schrödinger model there

Functions on finite adelic vectors that only see the components at a set `S` of finite places, and
the action of the Heisenberg group on them when `S` is disjoint from its conjugate.

* `New.IsSchwartzBruhat S Ψ`: `Ψ` is Schwartz–Bruhat above `S`. Examples are the indicator
  `New.boxIndicator` of the vectors integral on `S` and the coset functions `New.cosetIndicator`.
* `New.IsSchwartzBruhat.eq_sum_cosetIndicator`, `New.IsSchwartzBruhat.mem_of_cosets`: such a
  function is a finite linear combination of coset functions.
* `New.schrodingerAct`: the Schrödinger model, with the Heisenberg law
  `New.schrodingerAct_schrodingerAct`. `New.semichar_smul_schrodingerAct` gives its form in the
  normalisation that represents the lattice, and its vacuum is the box function
  (`New.schrodingerAct_boxIndicator`).
* `New.Space.mem_range_schrodingerCombination`: every Schwartz–Bruhat function above `S` is a finite
  combination of Heisenberg translates of the box function.

Notions from other files:
* `New.idem S`: the finite adele with component 1 at the places of `S` and 0 elsewhere, so that
  `idem S • x` is the part of `x` at `S`.
* `New.stdLattice.selfDualAddChar`: a character of the finite adeles for which `Ô^n` is its own dual
  under the pairing `selfDualAddChar E (y* x)`.
* `Set.conjClosure`: the set `S ∪ S̄` of the places in `S` and their complex conjugates;
  `Set.IsConjDisjoint S` says that `S` and `S̄` are disjoint.
* `New.stdLattice.half` is `1 / 2`, `New.stdLattice.traceOneAdele` an integer `c₀` with
  `c₀ + c̄₀ = 1`, and `New.stdLattice.semichar x` is `selfDualAddChar E (c₀ / 2 * x* x)`.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.


 ### The box, coset functions and the partial determinant 

### `integralBox`

 The additive group of finite adelic n-vectors that are integral at every place of S. 

### `boxIndicator`

 The complex-valued indicator function of the finite adelic n-vectors that are integral at
every place of S. 

### `IsSchwartzBruhat`

 Ψ is Schwartz–Bruhat above S: it depends only on the components at S, is locally constant,
and the S-parts of its support lie in a compact set. 

### `IsSchwartzBruhat.idem_smul`

 `Ψ x` depends only on the components of `x` at the places of `S`. 

### `IsSchwartzBruhat.locally_constant`

 `Ψ` is locally constant. 

### `IsSchwartzBruhat.compact_support`

 On the support of `Ψ`, the part of `x` at the places of `S` stays in a compact set. 

### `detOn`

 The homomorphism sending g in GL_n of the finite adeles to the idele equal to det g at the
places of S and 1 elsewhere. 

### `cosetIndicator`

 The indicator function of the finite adelic vectors x such that t⁻¹(x − z) is integral at
every place of S. 

### `detOn_apply`

 The component of the idele `detOn S g` (`g` a finite adelic unitary point) at a finite place
`w`: `det g_w` if `w ∈ S`, and `1` otherwise. 

### `detOn_eq_prod`

 For a finite adelic unitary point g (`g : Gf E n`) and a finite set T of finite places, the
idele det g_T is the product over w ∈ T of the ideles with component det g_w at w and 1
elsewhere. 

 ### The Schrödinger model 

### `schrodingerAct`

 The Schrödinger model at the places of `S`: the vector `y` acts on functions by
`Ψ ↦ (x ↦ selfDualAddChar E (½ y* (2 x + y)_S) * Ψ (x + y))`, where `z_S = idem S • z` is the part
of `z` at `S`. 

### `schrodingerAct_apply`

 The value of the Schrödinger operator of `y` on `f` at `x`. 

### `schrodingerCombination`

 The linear map sending finitely supported coefficients c_y to the function ∑ c_y
`New.schrodingerAct` S y applied to the indicator of vectors integral on S. 

### `localInner`

 The inner product ∫ conj(Ψ) Ψ′ over the finite adelic vectors integral off S, for the Haar
measure giving Ô^n mass one. 

### `integralBox_compl_inter`

 A vector integral off `S` and integral on `S` is integral everywhere. 

### `isSchwartzBruhat_boxIndicator`

 The indicator of the vectors integral at every place of `S` is Schwartz–Bruhat above `S`. 

### `comp`

 Let `Ψ` be Schwartz–Bruhat above `S` (instance `hΨ`), `A` a matrix with a left inverse `B`
(`B A y = y` for all `y`), and `y` a vector. Then `x ↦ Ψ (A x + y)` is
Schwartz–Bruhat above `S`. 

### `comp_add`

 A translate of a Schwartz–Bruhat function above `S` is Schwartz–Bruhat above `S`. 

### `comp_mulVec`

 The composite of a Schwartz–Bruhat function above `S` with an invertible matrix over the finite
adeles is Schwartz–Bruhat above `S`. 

### `eq_sum_cosetIndicator`

 Let Ψ be Schwartz–Bruhat above S (instance `hΨ`) and t a finite idele, with Ψ(y) = Ψ(x) when
Ψ(x) ≠ 0 and t⁻¹(y − x) is integral on S. Then there is a finite set A of vectors q with Ψ(q) ≠ 0
such that Ψ = ∑_{q ∈ A} Ψ(q) · `cosetIndicator S t q`. 

### `integrableOn_mul`

 For `Ψ` Schwartz–Bruhat above `S` (instance `hΨ`) and a continuous `F`, the product `F Ψ` is
integrable on the vectors integral off `S`, for the measure `New.latticeMeasure` that gives `Ô^n`
mass one. 

### `mem_of_cosets`

 A Schwartz–Bruhat function Ψ above S (instance `hΨ`) lies in a subspace P if each y with
Ψ(y) ≠ 0 has a neighbourhood U such that P contains every coset function `cosetIndicator S t z`,
t an integral idele, whose coset has S-parts in U. 

### `instance (t : (𝔸f E)ˣ) (z : n → 𝔸f E) : IsSchwartzBruhat S fun x : n → 𝔸f E ↦ cosetIndicator S t z x`

 The coset functions are Schwartz–Bruhat above `S`. 

### `idem_mul_star`

 For `S` disjoint from its conjugate (hypothesis `hS`), the idempotents of `S` and of `S̄` have
product zero. 

### `idem_conjClosure_eq_add_star`

 For `S` disjoint from its conjugate (hypothesis `hS`), the idempotent of `S ∪ S̄` is the sum of
those of `S` and of `S̄`. 

### `schrodingerAct_schrodingerAct`

 The Heisenberg law, for `S` disjoint from its conjugate (hypothesis `hS`): the operators compose
up to the bicharacter `β` of `New.stdLattice.finHeisenberg` at the parts of `y` and `y'` at
`S ∪ S̄`. 

### `semichar_smul_schrodingerAct`

 For `S` disjoint from its conjugate (hypothesis `hS`), the operator of `y`, corrected by the
semicharacter `semichar` of the part of `y` at `S ∪ S̄`, sends `Ψ` to
`x ↦ selfDualAddChar E (y* (x + c₀ y)_S) * Ψ (x + y)`, where `c₀ = traceOneAdele` and
`z_S = idem S • z`. 

### `schrodingerAct_boxIndicator`

 For `S` disjoint from its conjugate (hypothesis `hS`) and `y` integral on `S ∪ S̄`, the operator
of `y`, corrected by the semicharacter `semichar` of the part of `y` at `S ∪ S̄`, fixes the box
function. 

### `schrodingerAct_idem`

 For `S` disjoint from its conjugate (hypothesis `hS`) and `Ψ` Schwartz–Bruhat above `S`
(instance `hΨ`), a vector supported on `S` acts on `Ψ` by translation. 

### `schrodingerAct_star_idem_smul`

 Let `E` be a CM number field with Weil data (instances `CMType E`, `WeilData E`; they fix the
character `selfDualAddChar E`), `n` a finite index type and `S` a set of finite places disjoint
from its conjugate (hypothesis `hS`), and let `Ψ` be Schwartz–Bruhat above `S` (instance `hΨ`).
Then a vector supported on the conjugate of `S` acts on `Ψ` by multiplication with a character. 

### `instance (y : n → 𝔸f E) : IsSchwartzBruhat S (schrodingerAct S y Ψ)`

 The Schrödinger operators keep the Schwartz–Bruhat functions above `S`. 

 ### Translates of the box function span 

### `_root_.New.Space.mem_range_schrodingerCombination`

 Let `E` be a CM number field with Weil data (instances `CMType E`, `WeilData E`; they fix the
character in `schrodingerAct`), `n` a finite index type and `S` a set of finite places of `E`
disjoint from its complex conjugate. Let `Φ` be a function on finite adelic `n`-vectors that is
Schwartz–Bruhat above `S`: locally constant, depending only on the components at `S`, and with
compact support there. Then `Φ` is a finite combination of Heisenberg translates of the box
function: there are finitely supported coefficients `c` with
`Φ = ∑ c y • schrodingerAct S y (boxIndicator n S)`, which is `schrodingerCombination S c`. Here
`boxIndicator n S` is the indicator of the vectors integral at every place of `S`. 
