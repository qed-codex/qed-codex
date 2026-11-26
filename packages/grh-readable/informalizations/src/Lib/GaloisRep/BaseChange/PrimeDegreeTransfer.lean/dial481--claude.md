---
{
  "module": "src/Lib/GaloisRep/BaseChange/PrimeDegreeTransfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/PrimeDegreeTransfer.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/PrimeDegreeTransfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Base change in prime degree for definite U(n): a weak base change eigenform

Base change of algebraic modular forms on the definite unitary group along a step E'/E of prime
degree (`New.IsStep`), from the twisted trace identity `New.twisted_trace_identity`.

* `New.IsWeakBaseChange`: f' is a weak base change of f off a finite set of places.
* `New.IsLocalMatching`: matching test functions over E and E' above a finite set Z of places.
* `New.exists_isWeakBaseChange_of_matching`: an eigenform over E' that is a weak base change of f
  and has prescribed eigenvalues for the local operators.

Notions from other files that the statements use:
* `New.IsStep E' μ`: `E` contains a primitive 5040th root of unity, `E'` is a CM field, Galois of
  prime degree over `E`, with an integer of trace `1`, and `μ` is a character of the finite ideles
  of `E` with open kernel, trivial on `E^×`, such that `μ (z z̄) = 1` exactly when `z` is an element
  of `E^×` times the norm of a finite idele of `E'`.
* `Z.conjClosure` is `Z ∪ Z̄`, and `New.placesAbove E' Z` is the set of places of `E'` above it.
* `New.sphericalAt π w`: the vectors fixed by the integral elements supported at `w` and `w̄`.
  `New.HasHeckePolyAt f w hw P`: `f` is spherical at `w` and an eigenvector of each `New.heckeSplit`
  there, and `P` is built from the eigenvalues and the norm of `w`.
* `New.IsMatchingPairAbove σ μ Z K f φ`: `(f, φ)` is a matching pair of test functions for the
  twisted trace identity at the places above `Z`, at level `K`.
* `New.heckeFun ρ L F` is the Hecke operator `∑_{g ∈ G/L} F g • ρ g`, `New.levelSpace ρ L` is the
  `L`-fixed space, and `New.Weight.baseChange` is the weight pulled back to `E'`.

## Relation to the literature

Known result: Cyclic base change of prime degree for definite unitary groups (weak lift, local
matching). Here the lift goes from U(n) over E to U(n) over E' rather than to GL_n, with E'/E tame
and E containing enough roots of unity, and only existence is proved. Hecke polynomials match where
the place splits completely and an auxiliary character is trivial, tame types are kept, and class
sums are compared directly, without stabilisation. Source: J.-P. Labesse, Changement de base CM et
séries discrètes, in On the stabilization of the trace formula, 2011, Cor. 5.3, and Cohomologie,
stabilisation et changement de base, Astérisque 257, 1999; J. Arthur and L. Clozel, Simple algebras,
base change, and the advanced theory of the trace formula, Ann. Math. Studies 120, 1989; local
matching after P. Scholze, The Langlands-Kottwitz approach for some simple Shimura varieties, 2013,
Prop. 2.1 (norms inverted inside O[γ]) and J.-P. Labesse, Fonctions élémentaires et lemme
fondamental pour le changement de base stable, Duke Math. J. 61, 1990.


### `IsWeakBaseChange`

 `f'` is a weak base change of `f` off the set `Z` of places of `E`: `Z` is finite, and for every
place `w` of `E` outside `Z ∪ Z̄` and every place `u` of `E'` above `w`,
* if `w` is unramified in the step (`New.IsStepUnramifiedAt`) and `f` is spherical at `w`, then
`f'` is spherical at `u`;
* if `w` is matched (`New.IsMatched`: `μ` is trivial on `E_w^×`, and each place above `w` has the
  norm of `w` and is moved by every `σ ≠ 1`) and split, then for every Hecke polynomial `P` of `f`
  at `w` (`New.HasHeckePolyAt`) the place `u` is split and `P` is a Hecke polynomial of `f'` at
  `u`. 

### `IsLocalMatching`

 Matching local data above a set `Z` of places of `E`, for groups `G`, `G'` mapped into the
finite adelic unitary groups over `E` and `E'` by `a`, `a'`. There are `σ ≠ 1` in `Gal(E'/E)` and
retractions `r`, `r'` (`New.IsLocalRetraction`: `a` lands in the elements supported on `Z ∪ Z̄`,
`r ∘ a = id`, and the kernel of `r` is the elements trivial on `Z`; likewise for `a'`, `r'` and the
places of `E'` above `Z`) such that
* each `F j` is bi-invariant under `L`, and each `F' j` under `L'`;
* `Z` is finite, and `L'` is stable under `σ` (through `r'`);
* the preimage of `L'` in `Gf E' n` is open, and its preimage under base change is the preimage
  of `L` in `Gf E n`;
* some level `K` between the preimage of `L'` and the integral level above `Z` has split
  `σ`-cocycles (`New.CocyclesSplit`), and for `j ∈ P` the pair `(F j ∘ r, F' j ∘ r')` matches above
  `Z` at level `K`. 

### `isLocalMatching_empty`

 For the empty set of places and trivial local groups, the constant functions 1 are matching
local data (`New.IsLocalMatching`). 

### `exists_mem_inf_galoisGf_eq_inv_mul_of_cocyclesSplit`

 Let `S` be a `σ`-stable set of places of `E'`. Suppose that `K` contains the elements trivial on
`S` and that its `σ`-cocycles split on `S` (`New.CocyclesSplit`: each `s ∈ K` of twisted norm
`s · σ s ⋯ σ^{q-1} s = 1` has some `t ∈ K` that is `1` off `S` with `t⁻¹ * s * σ t = 1` on `S`), and
that `N` does the same with `S` and `Sᶜ` exchanged. Then every `s ∈ K ⊓ N` of twisted norm `1` is a
coboundary: `σ t = s⁻¹ * t` for some `t ∈ K ⊓ N`. 

### `map_heckeSplit_comap`

 Let `t` be a linear map with `t (π g x) = π (σ g) (t x)`, and let `u` and `u.comap σ` be split.
On a vector `x` such that `t x` is spherical at `u`, `t` carries the Hecke operator `T_j` at
`u.comap σ` (`New.heckeSplit`) to the one at `u`. 

### `heckeGenEigenspace`

 The `L`-fixed vectors that are generalised eigenvectors of the Hecke operator of `F i` for
the eigenvalue `θ i`, for every `i`. 

### `HasNonzeroTraceAround`

 `T` has non-zero trace on `Y ⊓ W` for every subrepresentation `W` containing `f` such that
`Y ⊓ W` is finite-dimensional and preserved by `T`. 

### `IsHeckeEigenvector`

 `g` is fixed by `L`, and the Hecke operator of each `F i` multiplies it by `θ i`. The vector
`g` may be zero. 

### `IsHeckeEigenvector.mem_levelSpace`

 `g` is fixed by `L`. 

### `IsHeckeEigenvector.heckeFun_apply`

 The operator of `F i` multiplies `g` by `θ i`. 

### `localFormTranslation`

 A group `G` with a map `a` to the finite adelic unitary group acts on the forms of weight `κ`
by right translation through `a`. 

### `inf_supportedOn_le_inf_localLevel`

 Let `w` be a place of `E` off `Z ∪ Z̄`, let `M` contain the elements trivial above `Z ∪ Z̄`, and
let the local level `m u` be the maximal compact subgroup `localIntGL n u` at each place `u` above
`w` or `w̄`. Then the integral elements supported on a set `S` of such places lie in `M` and in the
level given by `m` at the places not above `Z ∪ Z̄`. 

### `exists_isEigenform_of_hasHeckePolyAt`

 A non-zero function `f` is an eigenform (`New.IsEigenform`) as soon as it has a Hecke polynomial
at every split place `w` outside `S` at which the open subgroup `H` contains the maximal compact
subgroup, provided almost all places are outside `S`. 

### `baseChangeGf_mem_localLevel_univ`

 Let `g` be trivial on `Z`. If its image over `E'` lies in the level `m` at the places not above
`Z`, it lies in the level `m` at all places, since its components above `Z ∪ Z̄` are `1`. 

### `IsMatchingPairAbove.mul_mul`

 Let `(f₁, φ₁)`, `(f₂, φ₂)`, `(f₃, φ₃)` be matching pairs above `Z`, `X`, `Y` at levels `K`, `B`,
`C`. If the places of `E'` above `X` and above `Y` are disjoint and together are the places not
above `Z` (said with their idempotents), the products form a matching pair at all places, at level
`K ⊓ (B ⊓ C)`. 

### `IsMatched.isStepUnramifiedAt`

 A matched place (`New.IsMatched`) is unramified in the step (`New.IsStepUnramifiedAt`): some
`σ ≠ 1` moves each place above it, so it is not in the inertia group, and `μ` is trivial on
`E_w^×`. 

### `FinPlace.induction_on_comap`

 In prime degree, let `σ ≠ 1` be in the Galois group and let `p` be a property of places of
`E'` that passes from each place `u` to `u.comap σ`. Then `p` passes from `v` to every place `u`
above the same place of `E`. 

### `trace_restrict_heckeFamily_ne_zero_of_hasNonzeroTraceAround`

 Let the operators of the `F j` and the spherical operators at the places `u x` commute on the
finite-dimensional `L`-fixed vectors (`New.IsCommutingHeckeFamily`); let `f` be fixed by
`trivialOn n S ⊓ L`, with eigenvalue `ev y` for the spherical operator `op y`; and inside every
subrepresentation through `f` let the operator of `F j₀` have non-zero trace on the generalised
`θ`-eigenspace of the `F (o i)` (`New.HasNonzeroTraceAround`). Then it has non-zero trace on the
`L`-fixed joint generalised eigenspace for `θ` on the `F (o i)` and `ev` on the `op y`. 

### `mem_levelSpace_formTranslation_iff`

 A form is fixed by `K` under the translation of forms iff its underlying function is fixed by
`K` under right translation of functions. 

### `isWeakBaseChange_of_forall_heckeSplit_eq_smul`

 Let `f` be a form of weight `κ` over `E`, `g` a form of weight `κ.baseChange` over `E'`, and
`Z` a finite set of places of `E`. Suppose that for every place `w ∉ Z ∪ Z̄` at which `f` is
spherical: if `w` is unramified in the step, `g` is spherical at every place above `w`
(`h_spherical`); and if `w` is split and matched and `f` has eigenvalue `t i` for the `i`-th
spherical operator at `w`, then `g` has eigenvalue `t i` for the `i`-th spherical operator at
every split place above `w` (`h_eigen`). Then `g` is a weak base change of `f` off `Z`. 

### `IsBaseChangeLevel.eq_localIntGL_of_mem_sphericalAt`

 Let `m` be a base change level below the stabiliser of the form `f` (`New.IsBaseChangeLevel`).
For a place `w` that is unramified in the step and at which `f` is spherical, each `m u` with `u`
above `w` or `w̄` is the maximal compact subgroup `localIntGL n u`. 

### `IsTransferLevel`

 Facts about a level `𝓛` over `E'` used in the proof of
`New.exists_isWeakBaseChange_of_matching`, for a form `f` over `E` and sets `Z`, `X` of places of
`E`. The level `𝓛` is `L₁` intersected with the maximal level above the split matched places of
`X` and with a subgroup `C` for the remaining places, and `𝓛 ≤ K₁ ≤ New.stdLevel E' n`; matching
pairs above `Z` have level `K`. 

### `IsTransferLevel.le_stdLevel`

 `K₁` consists of integral elements. 

### `IsTransferLevel.le`

 `𝓛` lies in `K₁`. 

### `IsTransferLevel.isOpen`

 `𝓛` is open. 

### `IsTransferLevel.comap_galoisGf`

 `𝓛` is stable under `σ`. 

### `IsTransferLevel.exists_coboundary`

 The elements of `K₁` of twisted norm `1` are coboundaries in `K₁`. 

### `IsTransferLevel.eq_inf`

 `𝓛` is `L₁`, intersected with the maximal level above `X` and with `C`. 

### `IsTransferLevel.supportedOn_le`

 Elements supported above `Z ∪ Z̄` lie in the maximal level above `X` and in `C`. 

### `IsTransferLevel.supportedOn_placesAbove_le`

 Elements supported above `X ∪ X̄` lie in `C`. 

### `IsTransferLevel.isSplit`

 The places of `X` are split. 

### `IsTransferLevel.isMatched`

 The places of `X` are matched. 

### `IsTransferLevel.notMem_conjClosure`

 The places of `X` lie off `Z ∪ Z̄`. 

### `IsTransferLevel.kf_inf_supportedOn_le`

 For `w ∈ X`, `𝓛` contains the integral elements supported above `w` and `w̄`. 

### `IsTransferLevel.isMatchingPair_mul`

 A product of a matching pair above `Z` of level `K`, a matching pair above `X` of maximal
  level and the indicator function of `C` is a matching pair of level `K₁`. 

### `IsTransferLevel.mem_levelSpace`

 `f` is fixed by the elements of `𝓛` over `E` that are trivial on `Z`. 

### `IsTransferLevel.kf_inf_supportedOn_le_of_mem_sphericalAt`

 For a place `w` off `Z ∪ Z̄` that is unramified in the step and at which `f` is spherical,
  `𝓛` contains the integral elements supported above `w` and `w̄`. 

### `IsTransferLevel.mem_of_isMatched`

 A split matched place off `Z ∪ Z̄` at which `f` is spherical lies in `X`. 

### `exists_isTransferLevel`

 Let `σ ≠ 1`, let `f` be a form of weight `κ` over `E`, and let `Z` be a set of places of `E`.
Let `L₁` be an open `σ`-stable subgroup over `E'` that contains the elements trivial above
`Z ∪ Z̄`, and let `K ⊇ L₁` consist of elements integral above `Z ∪ Z̄`, with `σ`-cocycles that
split above `Z ∪ Z̄`. Then there is a level `𝓛` with the properties of `IsTransferLevel`. 

### `IsTransferLevel.isSplit_of_below_mem`

 A place of `E'` above a place of `X` is split. 

### `IsTransferLevel.maxCompactAt_le_of_below_mem`

 At a place of `E'` above a place of `X`, `𝓛` contains the maximal compact subgroup. 

### `IsTransferLevel.supportedOn_le_comap`

 The elements over `E` supported at a place of `X` and its conjugate map into `C`. 

### `IsTransferLevel.supportedOn_le_of_below_mem`

 The elements supported at a place of `E'` above `X` and at its conjugate lie in `C`. 

### `IsTransferLevel.exists_isCommutingHeckeFamily_comap`

 Let `G` be a retract at `Z` whose level `L` has preimage the pull-back of `L₁` to `E`, and let
`F j` be `L`-bi-invariant functions with commuting operators. At the pull-back of `𝓛` to `E`, the
operators of the `F j` and the spherical operators at the places of `X` form a commuting family
with a relation to functions, as in `New.exists_isHeckeFunctionRelation`. 

### `apply_eq_of_twist_heckeSplit`

 In prime degree, let `σ ≠ 1`, and let `t` preserve the `L`-fixed vectors and turn the action of
`g` into that of `σ g`. Let all places above `w` be split with `L` maximal there, and let `A u` be
the `i`-th spherical operator at `u` on the `L`-fixed vectors. If `Θ u = Θ v` whenever
`t * A u = A v * t`, then `Θ` takes the same value at all places above `w`. 

### `exists_eigenvector_of_isTransferLevel`

 The eigenvector step of `New.exists_isWeakBaseChange_of_matching`, for local data as in
`New.IsLocalMatching` (`hF`: each `F j` is `L`- and each `F' j` is `L'`-bi-invariant; `h_comm`: the
operators of the `F j` commute, and so do those of the `F' j`) and a level `𝓛` as in
`IsTransferLevel`. There is a form `g ≠ 0` over `E'` fixed by `𝓛` and `L'`: a `θ`-eigenvector of the
`F' (o i)` in the image of `F' j₀`, a spherical eigenvector at split places off `Z ∪ Z̄` where `𝓛`
is maximal, and with the eigenvalues of `f` at `w` at every split place above a place `w ∈ X`. 

### `exists_isWeakBaseChange_of_matching`

 Base change in prime degree for definite U(n) along the step `E'/E` (`New.IsStep`), with `E'`
containing a primitive 5040th root of unity. Let `f` be a form of weight `κ` over `E`, and `F`, `F'`
matching local data above `Z` with levels `L`, `L'` (`New.IsLocalMatching`), acting on forms by
right translation through `a` and `a'`, that is through `New.localFormTranslation`; let `o : ι → J`,
`θ : ι → ℂ`, `j₀ ∈ P`. Suppose the operators of the `F j` commute, and so do those of the `F' j`
(`h_comm`); for `j ∈ P` the operator of `F (o i)` times that of `F j` is that of some `F k` with
`k ∈ P`, the same `k` serving for `F'` (`h_stable`); and (`h_trace`) the operator of `F j₀` has
nonzero trace on `Y ⊓ W`, where `Y` is the `L`-fixed generalised eigenvectors of each `F (o i)` for
`θ i`, for every subrepresentation `W ∋ f` with `Y ⊓ W` finite-dimensional and stable. Then some
form `g` over `E'` of weight `κ.baseChange` is an eigenform with Hecke polynomials `H` (`g ≠ 0`, and
at almost all places `u` of prime norm, `u` is split and `H u` is a Hecke polynomial of `g` at `u`),
a weak base change of `f` off `Z` (`New.IsWeakBaseChange`), fixed by `L'` with eigenvalue `θ i` for
`F' (o i)`, and the image under the operator of `F' j₀` of a vector fixed by `L'`. 
