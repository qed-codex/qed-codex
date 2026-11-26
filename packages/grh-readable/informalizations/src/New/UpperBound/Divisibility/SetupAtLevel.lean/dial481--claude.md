---
{
  "module": "src/New/UpperBound/Divisibility/SetupAtLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/SetupAtLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/SetupAtLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The places `Σ_N` above N and the set-up at p = N

This file sets up the case `p = N`. It defines the set `Σ_N` of the conjugates of the places above
`N` that `ιₚ` induces, and shows that it is a split level for `N`. Levels, forms and the operator
`Up` are described at the places of `Σ_N`, in bases of the lattices `L_j` (see
`New.Data.diagPointN`). The file ends with the module `𝒜'` of forms that `Up ^ (ϱ + 1)` sends to
source forms with values integral for `L_0`.

## Main definitions and results

* `New.Data.nonInducedPlaces`, `New.Data.upIntegralForms`: the places `Σ_N` and the module `𝒜'`.
* `New.Data.upOperator_mem_sourceForm`: the operator `Up = upOperator (D.formRepAtN 0)` preserves
  the source forms `D.SourceForm`, the forms on `X_0` fixed by its level.

Notions from other files:
* `New.Data.piNPlaces`: the set of primes dividing `π`, where `π π̄ = N`.


### `nonInducedPlaces`

 The set `Σ_N` of the conjugates of the places above `N` that `ιₚ` induces. 

### `natCast_mem_of_mem_nonInducedPlaces`

 The places of `Σ_N = D.nonInducedPlaces` lie above `N`. 

### `isSplitLevel_nonInducedPlaces`

 The set `Σ_N = D.nonInducedPlaces` is a split level for `N`: it contains exactly one place of
each pair `w, w̄` above `N`, and these places are unramified of degree one. 

### `diagPoint`

 The point supported above `N` that is `diag (1, …, 1, N)` at the places of `Σ_N` in `S`, and `1`
at the other places of `Σ_N`. 

### `diagPointN`

 The point `δ_j`, which is `diag (1, …, 1, N)` at the places of `Σ_N` that divide `π` and `1` at
the others. It takes the standard lattice at `Σ_N` to `L_j`, the lattice of integral vectors whose
last coordinate is divisible by `π`. 

### `dualPointN`

 The point `δ_j^∨`, which takes the standard lattice to the dual lattice `L_j^∨` at `Σ_N`. 

### `conjEmbedGL`

 A matrix `a` over `LocProd D.nonInducedPlaces`, the product of the completions at `Σ_N`, goes to
`δ_j * embedGL a * δ_j⁻¹`. Here `embedGL a` is the unitary adelic point supported above `N` with
components `a` at `Σ_N`, and `δ_j = D.diagPointN j`. So `a` is read in a basis of `L_j`. 

### `formRepAtN`

 Forms on `X_j` as a representation of `GL` at `Σ_N`, in a basis of `L_j`. 

### `map_adeleExtension_diagPoint`

 The point `D.diagPoint j S` is supported above `N`, and is `diag (1, …, 1, N)` at the places of
`Σ_N` in `S` and `1` at the other places of `Σ_N`. For an infinite place `τ`, the map
`adeleExtension (weightEmbedding ιₚ τ)` reads an adele in `ℂ_[N]` through its component at the
conjugate `w̄` of the place `w = inducedPlace τ`. It sends the point to `diag (1, …, 1, N)` if `w̄`
lies in `S`, and to `1` otherwise. 

### `directDatum_ne_zero_iff`

 The direct datum is non-zero at a matrix `M` over the completions at `Σ_N` exactly if at each
place `w` of `Σ_N` the matrix `M` is integral and its last column is that of `1` modulo `w`. Here
`v` is the valuation of the completion at `w`, with `v N = exp (-1)`. 

### `directDatum_conj_ne_zero_iff`

 Let `Σ_N = D.nonInducedPlaces` be the conjugates of the places above `N` induced by the
embedding of `[PadicPlace D.N]`, let `D.piNPlaces` be the primes dividing `π = D.piN` (where
`π π̄ = N`), and let `δ_j = D.diagPointN j` be `diag (1, …, 1, N)` at the places of `Σ_N` that
divide `π` and `1` at the others. The matrix of `δ_j⁻¹ k δ_j` at `Σ_N` is integral with last column
that of `1` modulo `N` exactly if, for each `w` in `Σ_N`, `k` is integral at `w`, the last row of
`k⁻¹` is that of `1` modulo `w̄` if `w̄ ∣ π`, and the last row of `k` is that of `1` modulo `w` if
`w ∣ π`. 

### `atPlaces_conj_mem_mirabolic`

 Let `Σ_N = D.nonInducedPlaces` be the conjugates of the places of `E` above `N = D.N` induced by
the embedding `ιₚ` of `[PadicPlace D.N]`, and let `δ_j = D.diagPointN j` be the point supported
above `N` that is `diag (1, …, 1, N)` at the places of `Σ_N` dividing `π = D.piN` (where `π π̄ = N`)
and `1` at the other places of `Σ_N`. Let `k` lie in `D.levelX j`, the group of finite adelic points
of the unitary group of the hermitian space `X_j` (basis `D.X j`) that lie in the integral subgroup
`D.chosenLevel` and have last row that of `1` modulo `π`. Then the components of `δ_j⁻¹ k δ_j` at
`Σ_N` lie in `mirabolic`, the group of integral invertible matrices whose last column is that of
`1` modulo `N`. 

### `mem_levelX_of_mem_mirabolic`

 Let `Σ_N = D.nonInducedPlaces` be the conjugates of the places of `E` above `N = D.N` induced by
the embedding `ιₚ` of `[PadicPlace D.N]`, and let `δ_j = D.diagPointN j` be the point supported
above `N` that is `diag (1, …, 1, N)` at the places of `Σ_N` dividing `π = D.piN` (where `π π̄ = N`)
and `1` at the other places of `Σ_N`. Let `g` be a finite adelic point of the unitary group of the
hermitian space `X_j` (basis `D.X j`). Suppose that `g` is `1` at every place outside `Σ_N` and its
conjugates (`supportedOn`), and that the components of `δ_j⁻¹ g δ_j` at `Σ_N` lie in `mirabolic`:
they are integral and invertible, with last column that of `1` modulo `N`. Then `g` lies in
`D.levelX j`, the elements of the integral subgroup `D.chosenLevel` with last row that of `1`
modulo `π`. 

### `mem_ramified_of_mem_ramifiedSourceForms`

 The representation `ρ = D.formRepAtN 0` is the action of matrices at `Σ_N` on algebraic
automorphic forms for the unitary group of the hermitian space `X_0`, by right translation after
conjugation by `D.diagPointN 0`. Let `φ` be a source form, one fixed by the level subgroup
`D.levelX 0`, and let it be ramified: at each prime `u` dividing `π = D.piN` (where `π π̄ = N`), its
mean over the powers of the scaling `D.scalingGenerator u` is `0`. Then `φ` is a ramified vector of
`ρ`: for each `w` in `Σ_N` it has the form `ψ - ρ x ψ`, with `x` an integral unit scalar matrix that
is `1` modulo `N` at the other places of `Σ_N`. 

### `conjEmbedGL_mem_supportedOn`

 For a matrix `a` over the completions at `Σ_N = D.nonInducedPlaces`, the adelic point
`D.conjEmbedGL j a` (`a` read in a basis of the lattice `L_j`) lies in
`supportedOn (D.X j) D.nonInducedPlaces`. That is, its component is `1` at every place outside `Σ_N`
and the conjugate places. 

### `conjEmbedGL_mem_levelX`

 The stabiliser `mirabolic` of the standard marked lattice, read in a basis of `L_j`, lies in the
level of `X_j`. 

### `upOperator_mem_sourceForm`

 The operator `Up = upOperator (D.formRepAtN 0)` acts on `D.FormX 0`, the algebraic automorphic
forms for the unitary group of the hermitian space `X_0`, and preserves `D.SourceForm`, the forms
fixed by the level subgroup `D.levelX 0`. 

### `upIntegralForms`

 The module `𝒜'` of the forms `φ` on `X_0` such that `Up ^ (ϱ + 1) φ` is a source form with
values integral for `L_0`, over the ring `embValRing` of complex numbers that `ιₚ` sends to `N`-adic
integers. Here `Up` is the operator `upOperator` at `Σ_N` (see `upOperator_mem_sourceForm`), and
`ϱ = D.ϱ` with `ϱ + 1 = m / 2`. The module does not depend on the twist. 
