---
{
  "module": "src/Lib/Weil/Construction/ProductsAndTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ProductsAndTransport.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ProductsAndTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products of data along a splitting of coordinates, and changes of coordinates

This file forms the product f₁ ⊠ f₂ = `New.Space.boxProd` of data along a splitting of the
coordinates that is compatible with the signs. It also defines the block diagonal embedding
`New.G.blockEmb` of the two unitary groups. It shows that the product is compatible with the
Heisenberg operators, the vacua, the inner products, the insertion of real Fock vectors and the
Weil representation of block diagonal elements. It defines the changes of coordinates
`New.CoordChange` that keep the vacuum, and the transport `New.CoordChange.map` of data along them.
It shows that the transport preserves norms and respects the Heisenberg operators, the vacuum,
the insertion of a real vector, and the Weil representation up to a scalar.

## Main definitions and results

* `New.Space.rho_boxProd`, `New.Space.boxProd_vacElem`, `New.Space.dataInner_boxProd`,
  `New.Space.omega_boxProd`, `New.Space.boxProd_integrated`: the product respects the Heisenberg
  operators, the vacua, the inner products, the Weil representation of block diagonal elements and
  the insertion of real Fock vectors.
* `New.CoordChange.map_rho`, `New.CoordChange.map_vacElem`, `New.CoordChange.map_omega`,
  `New.CoordChange.map_integrated`: transport respects the Heisenberg operators, the vacuum, the
  Weil representation (up to a scalar) and the insertion of a real vector.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Space.vacElem`: The vacuum: the function e (Gaussian times twisted lattice indicator) as an
  element of 𝒮(V).

## Relation to the literature

Known; see `Lib.Weil.Construction.VacuumProjections` for sources.



## Products of data along a splitting of the coordinates

The coordinates split by a bijection e : n₁ ⊕ n₂ ≃ n under which the signs `s` become `s₁` followed
by `s₂`.

* `New.G.blockEmb`: the block diagonal embedding of the two unitary groups; it is a closed embedding
  and, for the definite spaces `New.stdSpace`, detects rational points.
* `New.Space.boxProd`: the bounded bilinear product f₁ ⊠ f₂ of data, the product of the underlying
  functions. It respects the Heisenberg operators, the vacua, the inner products, the insertion of
  real Fock vectors and the Weil representation of block diagonal elements. A renaming of the
  coordinates is the case of an empty second summand.
* `New.weilMultiplier_fromBlocks`: the multiplier `New.weilMultiplier` of the Weil representation is
  multiplicative on block diagonal elements.

Throughout, the hypothesis `hs : s ∘ e = s₁ ⊕ᵥ s₂` says that e carries the signs s to s₁ followed by
s₂, and V, V₁, V₂ are spaces with the signs s, s₁, s₂.


 ### Block diagonal elements 

### `G.blockEmb`

 The homomorphism sending a pair of elements of the adelic unitary groups of signs s₁, s₂ to
their block-diagonal matrix, reindexed into the unitary group of signs s. 

### `SiegelWeil.blockEmb_mem_Gamma_iff`

 For the definite spaces `stdSpace` (all signs `1`; `hs` records that `e` keeps these signs), the
block diagonal element `blockEmb hs g` of a pair `g` lies in the rational points `Γ` of
`stdSpace E n` exactly when `g.fst` and `g.snd` lie in those of `stdSpace E n₁` and
`stdSpace E n₂`. 

### `G.isClosedEmbedding_blockEmb`

 The block diagonal embedding `blockEmb hs` of `G E s₁ × G E s₂` into `G E s` is a closed
embedding. 

 ### The product of data 

### `realSigns_comp_split`

 The splitting of the coordinates induces a sign-compatible splitting of the real coordinates,
which are indexed by pairs (infinite place, coordinate). 

### `boxProd`

 For a sign-compatible splitting of the coordinates, the bounded bilinear map 𝒮(V₁) × 𝒮(V₂) →
𝒮(V), c₁ ⊠ c₂ = ∬ c₁(y₁)c₂(y₂) ϱ(y₁,0)ϱ(0,y₂)vac dy₁dy₂, where ϱ(y)c(x) = β(y,x)c(x−y). It is the
product of the underlying functions, see `New.Space.boxProd_val`. 

### `boxProd_val`

 On the underlying integrable functions, (f₁ ⊠ f₂)(x) = f₁(x₁) f₂(x₂), where x₁ and x₂ are the
two parts of the vector x. 

### `rho_boxProd`

 Let the coordinates of V split along e : n₁ ⊕ n₂ ≃ n into those of V₁ and V₂, with compatible
signs (`hs`), and let f₁ ⊠ f₂ be the box product 𝒮(V₁) × 𝒮(V₂) → 𝒮(V). For an adelic vector x, the
Heisenberg operator satisfies ϱ(x)(f₁ ⊠ f₂) = ϱ(x₁)f₁ ⊠ ϱ(x₂)f₂, where x₁ = x ∘ e ∘ inl and x₂ = x ∘
e ∘ inr are the two parts of x. 

### `boxProd_rho`

 When the coordinates and signs of V split into those of V₁ and V₂, ϱ(y₁)f₁ ⊠ ϱ(y₂)f₂ = ϱ(y)(f₁ ⊠
f₂), where y is the vector with parts y₁ and y₂. 

### `boxProd_vacElem`

 Let `e` split the coordinates of `V` into those of `V₁` and `V₂`, compatibly with the signs
(`hs`). The bilinear map `boxProd hs` : 𝒮(V₁) × 𝒮(V₂) → 𝒮(V) is the product of the underlying
functions. It sends the pair of vacua of `V₁` and `V₂` (each a Gaussian times a twisted lattice
indicator) to the vacuum `V.vacElem` of `V`. 

### `dataInner_boxProd`

 For a splitting of the coordinates of V into those of V₁ and V₂ compatible with the signs,
the product of data is multiplicative for the inner products:
⟨f₁ ⊠ f₂, f₁′ ⊠ f₂′⟩ = ⟨f₁, f₁′⟩ ⟨f₂, f₂′⟩. 

### `boxProd_integrated`

 The product respects the insertion of real vectors:
(v₁ ⊗ f₁) ⊠ (v₂ ⊗ f₂) = (v₁ ⊠ v₂) ⊗ (f₁ ⊠ f₂). Here v ⊗ f = `New.Space.integrated` v f inserts a
vector v of the Fock space of the real coordinates, and v₁ ⊠ v₂ = `New.Fock.realBoxProd` is the
product of Fock vectors along the splitting of the real coordinates given by
`realSigns_comp_split`. 

### `_root_.New.weilMultiplier_fromBlocks`

 If the matrix of g is block diagonal with blocks g₁, g₂ along a sign-compatible splitting e of
the coordinates (`h_blocks`: relabelling rows and columns of `g.adeleMatrix` by `e` gives
`fromBlocks g₁.adeleMatrix 0 0 g₂.adeleMatrix`), then Δ(g) = Δ(g₁)Δ(g₂) for Δ =
`New.weilMultiplier`. 

### `omega_boxProd`

 If the matrix of g is block diagonal with blocks g₁, g₂ for a sign-compatible splitting of
the coordinates (`h_blocks`, as in `New.weilMultiplier_fromBlocks`), then
ω(g)(f₁ ⊠ f₂) = ω(g₁)f₁ ⊠ ω(g₂)f₂. When `n₂` is empty, e is a renaming of the coordinates, and this
is the rule that a renaming carries ω(g₁) to ω of the renamed element g. 


## Changes of coordinates that keep the vacuum

A change of coordinates `New.CoordChange` is a map φ = A × B of adelic vectors whose finite part B
keeps the standard lattice and turns x*x into −x*x, that keeps the vacuum and keeps the bicharacter
β up to an isometric ring endomorphism σ of ℂ (in the uses, the identity or conjugation). The
examples negate a space or move it to the other side of a dual pair. A plain renaming of the
coordinates keeps x*x; it is covered by `New.Space.boxProd`.

* `New.CoordChange.map`, `New.CoordChange.realMap`: the σ-semilinear transport of data and of real
  Fock vectors.


### `CoordChange`

 For signs `s` on `n` and `s₁` on `n₁` and a ring endomorphism `σ` of ℂ, a change of adelic
coordinates φ = A × B keeping the adelic bicharacter β of the Heisenberg group up to σ, where the
real part A keeps the Gaussian and the finite part B keeps Ô^n and turns x*x into −x*x. 

### `CoordChange.φ`

 The change of coordinates: a bicontinuous additive bijection of adelic vectors. 

### `CoordChange.realEquiv`

 The real part `A`, acting on complex coordinates indexed by (infinite place, coordinate). 

### `CoordChange.finEquiv`

 The finite part `B`, acting on finite adelic vectors. 

### `CoordChange.apply_adelicSum`

 In the coordinates `adelicSum`, the map `φ` is the product `A × B`. 

### `CoordChange.beta_realEquiv`

 `A` carries the real bicharacter of signs `s` to `σ` of that of signs `s₁`. 

### `CoordChange.vac_realEquiv`

 `A` keeps the Gaussian exp(−|x|²/2). 

### `CoordChange.selfDualAddChar_finEquiv`

 `B` keeps the finite bicharacter, `selfDualAddChar E` of ½ y*x, up to `σ`. 

### `CoordChange.dot_finEquiv`

 `B` turns x*x into −x*x. 

### `CoordChange.finEquiv_mem`

 `B` maps the standard lattice Ô^n onto the standard lattice Ô^{n₁}. 

### `beta_phi`

 A change of coordinates φ with twist σ keeps the adelic bicharacter up to σ: σ(β₁(φx,
φy)) = β(x, y), where β₁ and β belong to the signs `s₁` and `s`. 

### `vacuumFn_apply`

 A change of coordinates keeps the vacuum function: e(φx) = e(x) for e = `New.vacuumFn`. 

### `adelicSum_equiv_zero_fst`

 In the coordinates `adelicSum`, the vector with real part `0` and finite part `z` is
`finVec z`. 

 ### Transport of data 

### `map`

 For a change of coordinates φ with twist σ, the continuous σ-semilinear map from 𝒮(V₁) to
𝒮(V) sending the coefficient function c to σ∘c∘φ. 

### `map_rho`

 For a vacuum-preserving change of coordinates D with underlying map φ, the induced map from
𝒮(V₁) to 𝒮(V) intertwines the Heisenberg operators: it sends ϱ(φx)f to ϱ(x) applied to the
image of f, for all x and f. 

### `norm_map`

 Let D be a change of adelic coordinates from signs `s₁` to `s` that keeps the Heisenberg
bicharacter up to the isometric ring endomorphism σ of ℂ. The map `D.map` : 𝒮(V₁) → 𝒮(V) induced by
D preserves norms. 

### `map_vacElem`

 For a change of adelic coordinates `D` from signs `s₁` to signs `s` (a map φ = A × B that keeps
the Heisenberg bicharacter β up to `σ`, where A keeps the Gaussian and B keeps Ô^n), the induced map
`D.map` from 𝒮(V₁) to 𝒮(V) sends the vacuum `V₁.vacElem` to the vacuum `V.vacElem`. Here `V` and
`V₁` are hermitian spaces with a point, and the vacuum is the Gaussian times the twisted lattice
indicator. 

### `map_omega`

 Let φ be a vacuum-preserving change of coordinates with twist σ. If φ(gx) = g₁φ(x) for all x and
σ(Δ(g₁)) = c·Δ(g), then (ω(g₁)f)^φ = c·ω(g)(f^φ) for all f in 𝒮(V₁), where f^φ = `D.map f` and
Δ = `New.weilMultiplier`. 

### `realMap`

 For a change of coordinates with archimedean part A and twist σ, the continuous σ-semilinear
map from the Fock space of signs s₁ to that of signs s sending v to σ∘v∘A. 

### `map_integrated`

 Transport respects the insertion of a real vector: the transport of v ⊗ f is the transported
Fock vector `D.realMap v` inserted into the transport of f. 

### `starCoordEquiv`

 For a bijection e, units u_i of a topological ring R and a continuous involution `star`,
the topological additive isomorphism sending x to (u_i · star x_{e(i)})_i. 
