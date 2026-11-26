---
{
  "module": "src/Lib/Weil/DualPair/MixedModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/MixedModel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/MixedModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Mixed models and zero terms of a pair with one split space: Levi and radical laws

Let V = range l ⊕ ιV₀ ⊕ range k be a splitting of a hermitian space V over V₀
(`New.Space.Splitting`: isotropic dual frames k, l and an isometry ι, the field `i`, from V₀), and
let T be another space. The splitting induces splittings of Hom(V,T) and Hom(T,V). This file
computes, for these, the zero term and the mixed model of the representation `New.pairWeil` of the
pair.

* `New.Space.Splitting.homSource`, `New.Space.Splitting.homTarget`: the induced splittings of
  Hom(V,T) over Hom(V₀,T) and of Hom(T,V) over Hom(T,V₀).
* `New.Space.Splitting.homSlice`: the term f[x] of an adelic n' × p matrix x in the mixed model;
  `New.Space.Splitting.hasSum_theta_homSlice`: θ(f) is the sum of the θ(f[T.x⁻¹x]) over rational
  x; `New.Space.Splitting.symm_homSource_zeroTerm_eq_integral`: the integral of the terms over
  adelic x is the zero term for the splitting with k and l exchanged;
  `New.Space.Splitting.homSlice_rho`: the law of f[x] under the Heisenberg operators.
* `New.Space.Splitting.homSource_zeroTerm_pairWeil`,
  `New.Space.Splitting.homTarget_zeroTerm_pairWeil`: the zero term of ω(g,h)f, resp. ω(h,g)f, when
  gk = km.
* `New.Space.Splitting.homSlice_levi`, `New.Space.Splitting.homSlice_radicalElement`: the laws of
  f[x] under the Levi subgroup and under the radical of the stabiliser of range k.

Notions from other files:
* `New.pairWeil V T a b (g, h)`, written ω_{a,b}(g,h): the Weil representation of x ↦ h x g⁻¹ on the
  data of Hom(V,T), twisted by a(det h) b(det g)⁻¹.
* `New.Space.ϱ`: the Heisenberg operators on the data space 𝒮 of a space.
* `New.Space.Splitting.zeroTerm` (ev): the mean of f(ιy + kb) over b in 𝔸^p / E^p;
  `New.Space.Splitting.slice x f` is ev(ϱ(lx) f).

`kAdelic`, `iAdelic` and `lAdelic` are the frames in adelic coordinates; `kCoord`, `iCoord` and
`lCoord` send kb + ιw + la to b, w and a. In formulas ȷ is `WeilData.j`, ψ is `stdAddChar`, υ is the
splitting character and * is the conjugate transpose.

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence` for sources.


### `dualFrame`

 For a space T with adelic frame x, the invertible adelic matrix (x⁻¹)* ε, with inverse ε x*,
where ε is the standard form of its signs. 

### `rho_pairWeil`

 For q = (g, h), the Heisenberg operator ϱ(x) of Hom(V,T) moves past ω_{a,b}(q) by turning x,
read as an n' × n matrix, into h⁻¹xg: ϱ(x) ω(q) f = ω(q) ϱ(h⁻¹xg) f. 

 ### The induced splittings and their frames 

### `homSource`

 From a splitting (k, l, ι) of V over V₀, the splitting of Hom(V,T) over Hom(V₀,T) with
frames J_T⁻¹⊗(k*J)ᵀ, 1⊗(l*J)ᵀ, 1⊗(J₀⁻¹ι*J)ᵀ; the first spans the maps killing k^⊥. 

### `homTarget`

 From a splitting (k, l, ι) of V over V₀, the splitting of Hom(T,V) over Hom(T,V₀) with
frames k⊗J_Tᵀ, l⊗1, ι⊗1. 

### `zeroTerm_homSource_congr`

 The zero term on Hom(V,T) is the same for two splittings of V with orthogonal frames k and
equal ι. 

### `zeroTerm_homSource_comp`

 Zero terms on Hom(·, T) can be taken in stages: for splittings D of V over V₀ and D' of V₀ over
V₁, the zero term for the splitting of Hom(V,T) induced by the composite `D.comp D'` is the zero
term for D' applied after the zero term for D. 

### `homSource_kAdelic`

 The adelic k-frame of the splitting `New.Space.Splitting.homSource` of Hom(V,T) is the Kronecker
product of the inverse of `New.Space.dualFrame` of T with the transpose of `lCoord`. 

### `homSource_lAdelic`

 The adelic l-frame of the splitting `New.Space.Splitting.homSource` of Hom(V,T) is the Kronecker
product of x_T⁻¹ with the transpose of `kCoord`, where x_T is the point of T. 

 ### The mixed model on Hom(V,T) 

### `homSlice`

 For an adelic n′×p matrix x, the map f ↦ f[x]: the zero term, along maps killing k^⊥, of
ϱ(x̃)f, where x̃ ∈ Hom(V,T) has x̃k = x and kills l, ι. 

### `homSlice_eq_slice`

 For a splitting `D` of V over V₀ and an adelic n′ × p matrix x, `New.Space.Splitting.homSlice`
at x_T⁻¹x (x_T the point of T) equals `New.Space.Splitting.slice` at x, read as a vector on n′ × p,
for `homSource`. That is the splitting of Hom(V,T) over Hom(V₀,T) induced by `D`. A slice at x is
the bounded map f ↦ ev(ϱ(lx)f) from 𝒮(Hom(V,T)) to 𝒮(Hom(V₀,T)). 

### `hasSum_theta_homSlice`

 For split V and any datum f on Hom(V,T), θ(f) is the convergent sum of the θ(f[x]) over
rational n' × p matrices x, taken at the adelic matrices x_T⁻¹x (x_T the point of T), f[x] being
the term of x in the mixed model. 

### `symm_homSource_zeroTerm_eq_integral`

 On Hom(V,T), the zero term for the splitting with k and l exchanged, that is along the maps
killing l^⊥, is the integral over adelic x, in rational coordinates, of the terms of the mixed model
(the terms f[x_T⁻¹x], by `New.Space.Splitting.homSlice_eq_slice`). 

### `homSlice_rho`

 For split V, y in Hom(V,T) and f[x] = `New.Space.Splitting.homSlice` x f:
(ϱ(y)f)[x] = ψ(½ȷ tr((yl)*ε'(2x + yk))) ϱ(yι) f[x + yk], with ε' the standard form of T. 

### `upsilonU1_apply`

 The character `New.WeilData.upsilonU1` is υ on the norm-one ideles. 

### `chiAdelic_toUnits`

 On a norm-one idele u, the character `New.chiAdelic` x ↦ υ(x)|x|^(−1/2) is υ: the idele norm
of u is one. 

### `det_eq_divStar_mul`

 If g k = k m for an invertible adelic p × p matrix m (`hk`), and g₀ is the block of g on ιV₀,
that is, the ι-coordinates of gι (`hi`), then det g = (det m / star (det m)) · det g₀. 

### `homSource_zeroTerm_pairWeil`

 Suppose g k = k m with m ∈ GL_p(𝔸) (`hk`), and g₀ is the block of g on ιV₀ (`hi`). On Hom(V,T),
ev ω_{aυ^p,b}(g,h)f = χ_T(det m)⁻¹ |det m|^(n′/2) ω_{a,b}(g₀,h) ev f,
with ev the zero term, n′ the rank of T and χ_T(x) = b(x/x̄)υ(x)^(−n′) (`New.AutChar.spaceChar`). 

### `homTarget_zeroTerm_pairWeil`

 Suppose g k = k m with m ∈ GL_p(𝔸) (`hk`), and g₀ is the block of g on ιV₀ (`hi`). On Hom(T,V),
ev ω_{a,bυ^p}(h,g)f = χ(det m) |det m|^(n′/2) ω_{a,b}(h,g₀) ev f, with ev the zero term, n′ the rank
of T and χ(x) = a(x/x̄)υ(x)^(−n′) (`New.AutChar.spaceChar`). 

 ### The Levi and radical laws 

### `homSlice_levi`

 For the Levi element g = `New.Space.Splitting.levi` (m, g₀), which has gk = km and gι = ιg₀:
(ω_{aυ^p,b}(g,h)f)[x] = χ_T(det m)⁻¹ |det m|^(n′/2) ω_{a,b}(g₀,h) f[h⁻¹xm],
with f[x] = `New.Space.Splitting.homSlice` x f, n′ the rank of T and χ_T(y) = b(y/ȳ)υ(y)^(−n′). 

### `homSlice_radicalElement`

 For the unipotent element u = `New.Space.Splitting.radicalElement` c z, which fixes k:
(ω_{a,b}(u,1)f)[x] = ψ(½ tr(z x*ε′x)) ϱ(x c* ε₀) f[x], where ε′, ε₀ are the standard forms of T
and V₀ and f[x] = `New.Space.Splitting.homSlice` x f. 
