---
{
  "module": "src/Lib/Weil/MixedModel/NamedData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/NamedData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/NamedData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Data named by Schwartz–Bruhat functions: Heisenberg laws, transport, Weil action

Let S be a set of finite places disjoint from its conjugate S̄. A Schwartz–Bruhat function Ψ above S
names an operator `V.schrodingerOp S Ψ` on 𝒮(V). The box function names the projection P^S =
`New.Space.projOn` S. Its translates name Heisenberg translates ϱ(αy₊) P^S of it, with α the finite
idele of `New.WeilData`. Naming is compatible with products of data. For general g, Ψ is composed
with g_f⁻¹ and the vector also changes.

## Main definitions and results

* `New.Space.schrodingerOp`: sends ∑ c_y (translate of the indicator by y) to the operator ∑ c_y
  ϱ(αy₊) P^S, with y₊ the part of y above S ∪ S̄ and P^S = `New.Space.projOn` S.
* `New.Space.rho_schrodingerOp`: naming is equivariant for the Heisenberg operators of the parts of
  vectors above S ∪ S̄.
* `New.Space.dataInner_schrodingerOp`: the inner product of two named vectors factors.
* `New.Space.schrodingerOp_union`: for disjoint `S`, `T` with `S ∪ T` disjoint from its conjugate, a
  product of functions names the composite.
* `New.Space.omega_schrodingerOp`: for any `g`, `ω g (schrodingerOp Ψ f) = schrodingerOp (Ψ ∘ g_f⁻¹)
  u`, where `u` is `ω g` applied to the name of the box function composed with `g_f`, and `u` is
  fixed by `V.projOn S`.
* `New.Space.omega_schrodingerOp_of_mem_supportedOn`: `g` supported on `S ∪ S̄` acts by
  `Ψ ↦ Ψ ∘ g⁻¹`, times the conjugate of `New.chiAdelic` at the `S`-part of `det g`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with
  xᴴJx equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.Space.ϱ`: the Heisenberg operator of an adelic vector `y` on `𝒮 V`.
* `New.Space.projOn`: the operator P^S on 𝒮(V), the mean over y in Ô^n of the finite Heisenberg
  operators `New.Space.finHeisenbergOp` at the part of y above S ∪ S̄ (`S.conjClosure`).
* `New.localInner`: the integral of conj(Ψ) Ψ′ over the finite adelic vectors integral off S,
  normalised so that Ô^n has mass one.
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.



## Naming vectors by Schwartz–Bruhat functions at split places

Transfer from the Schrödinger model at a set S of finite places to the space 𝒮(V) of the Weil
representation. The Heisenberg group acts on functions above S by `New.schrodingerAct`. For S
disjoint from its conjugate, a Schwartz–Bruhat function above S (`New.IsSchwartzBruhat`) is a
combination of translates of the indicator `New.boxIndicator` of the vectors integral on S.

`New.idem` S is the idempotent of S in the finite adeles. `New.finVec` y is the adelic vector with
finite part αy and zero real part.


### `heisenbergCombination`

 The linear map sending finitely supported coefficients c_y to the operator ∑ c_y ϱ(αy₊) P^S
on 𝒮(V), y₊ the part of y above S ∪ S̄. 

### `schrodingerOp`

 The linear map Ψ ↦ Ψ⊗ from functions on finite adelic vectors to operators on 𝒮(V):
`New.Space.heisenbergCombination` of chosen coefficients c, with `New.schrodingerCombination` c = Ψ
when such exist. 

### `commute_schrodingerOp`

 `V.schrodingerOp S Ψ` is the operator `Ψ⊗` on `𝒮 V`: a combination of Heisenberg operators
composed with the projection `V.projOn S`, with chosen coefficients whose Schrödinger combination is
`Ψ`, when such coefficients exist. It commutes with every bounded operator `A` on `𝒮 V` that
commutes with `V.ϱ y` for all adelic vectors `y` with zero real part whose finite part is zero off
`S` and its conjugate. 

### `integrated_schrodingerOp`

 For v in the Fock space and f in 𝒮(V), v⊗(Ψ⊗f) = Ψ⊗(v⊗f): the operators `New.Space.integrated` v
and `New.Space.schrodingerOp` S Ψ commute. 

### `commute_rho_schrodingerOp`

 For any function `Ψ` on finite adelic vectors, the operator Ψ⊗ = `V.schrodingerOp S Ψ` on 𝒮(V)
commutes with the Heisenberg operator `V.ϱ z` of any adelic vector `z` whose finite components
vanish at the places of S ∪ S̄. 

### `schrodingerOp_projOn`

 Naming ignores the projection P^S = `New.Space.projOn` S: `V.schrodingerOp S Ψ` takes the same
value at `P^S f` as at `f`. 

### `finVec_idem_smul_snd_eq_zero_of_disjoint`

 The translation vector `finVec (idem U.conjClosure • y)` vanishes at every place of `T` and of
its conjugate when `U ∪ Ū` is disjoint from `T`: there the idempotent of `U ∪ Ū` is `0`. 

### `projOn_schrodingerOp_vacElem`

 If the set T of finite places is disjoint from S ∪ S̄, then Ψ ⊗ vac, named at S, with
vac = `V.vacElem` the vacuum vector of 𝒮(V), is fixed by the projection P^T. 

### `localInner_boxIndicator_mulVec`

 For g ∈ GL_n(𝔸_f), take `localInner S` (∫ conj(Ψ) Ψ′ over the finite adelic vectors integral off
S, for the Haar measure giving Ô^n mass one) of the indicator of vectors integral at S against its
transform x ↦ indicator(g x). This equals `‖Δ_f(g_S)‖⁻²`, where `g_S` (`cutGL`) is `g` above `S` and
`1` elsewhere. Here `Δ_f` (`New.glMultiplier`) is χ_f(det u) for the chosen u with uÔ^n = Ô^n ∩
g_S⁻¹Ô^n. 

### `fourier_boxIndicator`

 Over the vectors x integral off S, the integral of F x = 1(x+m) χ(z*(x+m)_S) c 1(z), with 1 the
indicator of integrality on S and χ = `New.stdLattice.selfDualAddChar`, is c if z is integral on S ∪
S̄ and 0 otherwise. The integrand `F` is given by the equation `h`. 

 ### Naming is well defined when `S` is disjoint from its conjugate 

### `dataInner_heisenbergCombination`

 Let S be disjoint from its conjugate, let c, c′ be finitely supported coefficients indexed by
finite adelic vectors y, and let f, f′ ∈ 𝒮(V). Set A_c = `V.heisenbergCombination S c`, the operator
∑ c_y ϱ(αy₊) P^S on 𝒮(V) with y₊ the part of y above S ∪ S̄, and Ψ_c = `schrodingerCombination S c`,
the function ∑ c_y (`New.schrodingerAct` S y applied to the indicator of vectors integral on S),
where `schrodingerAct S y Φ` is x ↦ `selfDualAddChar E` (½ y*(2x + y)_S) · Φ(x + y). Then
`dataInner` (the pairing ∫ f̄ f′) gives ⟨A_c f, A_{c′} f′⟩ = `localInner S` Ψ_c Ψ_{c′} · ⟨P^S f, P^S
f′⟩, where `localInner S` is ∫ conj(Ψ) Ψ′ over the finite adelic vectors integral off S (Ô^n having
mass one), and P^S = `V.projOn S` is the mean over y ∈ Ô^n of the finite Heisenberg operators at the
part of y above S ∪ S̄. 

### `schrodingerOp_schrodingerCombination`

 The name does not depend on the choice of coefficients: for `S` disjoint from its conjugate,
the combination of translates of the indicator with coefficients `c` names
`V.heisenbergCombination S c`. 

### `schrodingerOp_schrodingerAct_boxIndicator`

 Let `S` be disjoint from its conjugate. Then `schrodingerOp S` of the Schrödinger translate
`schrodingerAct S y` of the indicator `boxIndicator n S` sends `f` to `V.ϱ (finVec y₊)` applied to
P^S f = `V.projOn S f`, where y₊ = `idem S.conjClosure • y` is the part of `y` at S ∪ S̄.
Multiplying by `semichar y₊` gives the same rule for `finHeisenbergOp y₊`, with the phase of
`New.semichar_smul_schrodingerAct` on the left. 

### `schrodingerOp_boxIndicator`

 For a set S of finite places disjoint from its conjugate, the indicator of the vectors
integral at all places of S names the operator P^S = `New.Space.projOn` S. 

### `rho_schrodingerOp`

 Let `S` be disjoint from its conjugate and `Ψ` Schwartz–Bruhat above `S`, and write Ψ⊗ for the
operator `V.schrodingerOp S Ψ` on 𝒮(V). For a finite adelic vector `y`, let y' be `y` kept at S ∪ S̄
and set to 0 elsewhere. Then applying the Heisenberg operator `V.ϱ` of `finVec` y' (zero archimedean
part, finite part αy') to Ψ⊗f gives (`schrodingerAct S y Ψ`)⊗f, where `schrodingerAct S y Ψ` is
x ↦ `selfDualAddChar E` (½ y*(2x + y)_S) · Ψ(x + y). 

### `dataInner_schrodingerOp`

 Let `S` be disjoint from its conjugate and `Ψ`, `Ψ'` Schwartz–Bruhat above `S`, and write Ψ ⊗ f
for `V.schrodingerOp S Ψ f`. Then ⟨Ψ ⊗ f, Ψ′ ⊗ f′⟩ (the pairing `dataInner`, ∫ f̄ f′ on 𝒮(V)) equals
`localInner S Ψ Ψ'` times ⟨P^S f, P^S f′⟩. Here `localInner S Ψ Ψ'` is ∫ conj(Ψ) Ψ′ over the finite
adelic vectors integral off `S`, with Haar measure giving Ô^n mass one. P^S = `V.projOn S` is the
mean over y ∈ Ô^n of `finHeisenbergOp` at the part of y above S ∪ S̄. 


## Names under changes of coordinates and products of data

Names on the vacuum are transported by a change of coordinates
(`New.CoordChange.map_schrodingerOp`).


### `CoordChange.map_schrodingerOp`

 Names are transported by a change of coordinates `D`. Let `S` and `S'` be disjoint from their
conjugates. Let the finite part `D.finEquiv` carry parts at `S'` to parts at `S`, and parts at
`S'.conjClosure` to parts at `S.conjClosure` (the sets with their conjugates). For `Ψ`
Schwartz–Bruhat above `S`, `D.map` sends the vector named by `Ψ` on the vacuum of `V₁` to the vector
named by `σ ∘ Ψ ∘ D.finEquiv`, at `S'`, on the vacuum of `V`. 

### `Space.boxProd_projOn`

 The projection P^S commutes with products of data: the product `V.boxProd hs` (the product of
the underlying functions, for a splitting `e : n₁ ⊕ n₂ ≃ n` of the coordinates compatible with the
signs, `hs`) of the projected vectors of `V₁` and `V₂` is the projection of their product. 

### `Space.schrodingerOp_mem_finitePart_of_mem`

 For any set `S` of finite places and any function `Ψ`, the operator `V.schrodingerOp S Ψ` maps
the finite part `V.finitePart` (the span of the finite Heisenberg translates of the vacuum) into
itself: if `f` lies in `V.finitePart`, so does `V.schrodingerOp S Ψ f`. 

### `Space.schrodingerOp_mem_finitePart`

 `New.Space.schrodingerOp_mem_finitePart_of_mem`, with the membership of `f` in `V.finitePart` as
a default argument proved by `simp`. 

### `Space.boxProd_schrodingerOp`

 Let `S` be disjoint from its conjugate, `Ψ`, `Ψ'` Schwartz–Bruhat above `S`, and
`e : n₁ ⊕ n₂ ≃ n` a splitting of the coordinates compatible with the signs (`hs`); write Ψ⊗ for the
operator `schrodingerOp S Ψ` and vac for the vacuum `vacElem`. Then `V.boxProd hs` (the product of
the underlying functions) of Ψ⊗vac in 𝒮(V₁) and Ψ'⊗vac in 𝒮(V₂) equals Θ⊗vac in 𝒮(V). Here
`Θ x = Ψ x₁ * Ψ' x₂`, with x₁, x₂ the two blocks of coordinates of `x` given by `e`. 

 ## The Weil action on names and names over disjoint sets of places 

### `schrodingerOp_union`

 Let S, T be disjoint sets of finite places with S ∪ T disjoint from its conjugate, let Ψ be
Schwartz–Bruhat above S and Ψ′ above T, and let f ∈ 𝒮(V). Then `V.schrodingerOp (S ∪ T) (Ψ * Ψ')`
f = `V.schrodingerOp S Ψ` (`V.schrodingerOp T Ψ'` f). Here `schrodingerOp S Ψ` is the operator Ψ⊗ on
𝒮(V) given by the combination ∑ c_y ϱ(αy₊) P^S (`heisenbergCombination`) for coefficients c whose
matching function `schrodingerCombination S c` equals Ψ. 

### `map_snd_adeleMatrix`

 The finite parts of the entries of `g.adeleMatrix` are the entries of the finite component
`g.snd`. 

### `omega_schrodingerOp`

 Let S be disjoint from its conjugate, Ψ be Schwartz–Bruhat above S, g ∈ `G E s` with finite
component g_f = `g.snd`, and f ∈ 𝒮(V), and write Φ⊗ = `V.schrodingerOp S Φ` for the operator ∑ c_y
ϱ(αy₊) P^S (`heisenbergCombination`) whose matching function `schrodingerCombination S c` is Φ. Let
u = `V.ω g` (B⊗ f), where B(x) = `boxIndicator n S` (g_f x) is the indicator of the x with g_f x
integral at every place of S. Then u is fixed by P^S = `V.projOn S` (the mean over y ∈ Ô^n of the
finite Heisenberg operators above S ∪ S̄), and `V.ω g` (Ψ⊗ f) = Ψ′⊗ u with Ψ′(x) = Ψ(g_f⁻¹ x). 

### `omega_schrodingerOp_of_mem_supportedOn`

 Let `S` be disjoint from its conjugate, `Ψ` Schwartz–Bruhat above `S`, and `g` in the finite
adelic unitary group (gᴴg = 1) supported on S ∪ S̄. Then `V.ω g` sends `V.schrodingerOp S Ψ f`, the
operator Ψ⊗ on 𝒮(V) applied to `f`, to `V.schrodingerOp S` of x ↦ Ψ(g⁻¹x) applied to `f`, times a
scalar. The scalar is the complex conjugate of `chiAdelic` (x ↦ υ(x)|x|^(−1/2), with υ the splitting
character) at the idele `detOn S g`, which equals det g at the places of `S` and 1 elsewhere. 
