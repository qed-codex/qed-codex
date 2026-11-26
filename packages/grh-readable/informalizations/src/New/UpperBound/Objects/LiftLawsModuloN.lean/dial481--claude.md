---
{
  "module": "src/New/UpperBound/Objects/LiftLawsModuloN.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Direct and mirror data modulo `N`, and the operator `Up`

Let `P` contain one place of each conjugate pair above the split prime `N` of the CM field `E`. A
marked lattice at `P` is a lattice `L` with a vector `ε` of `L / N L` that is non-zero at every
place. Everything here is written in a basis of `L` whose last vector lifts `ε`, at all places of
`P` at once:
* the stabiliser of `(L, ε)` is `mirabolic`, and `diagNInv` takes `L` to `L⁺ = L + 𝒪 ε / N`;
* the direct datum `1[S L ⊆ L', S ε = ε']` is `directDatum`; in bases of `L⁺` and `L'⁺` it is
  `lastRowDatum`;
* the mirror datum `1[S L ⊆ L'⁺] ψ_N (u' (S ε))`, where `u'` is the linear form on `L'⁺` with kernel
  `L'` and `u' (ε' / N) = 1`, is `mirrorDatum` in bases of `L` and `L'⁺`;
* the operator `Up`, which replaces `L` by `L⁺` and sums against `ψ_N` over the primitive vectors
  with unit last entry, is `upOperator`.

A `LiftLaw` records how a lift depends on its datum. On ramified vectors the following hold. A
mirror lift, moved by `diagNInv`, is `Up` after a direct lift, and `Up` moves through a direct lift
up to the factor `γ` of its law. A glued double lift is the number of primitive vectors times a
mirror lift after a direct lift; hence, moved by `diagNInv`, it is a scalar times two direct lifts
after `Up`. So a chain of glued double lifts is a scalar times a chain of direct lifts after a power
of `Up`.

Notions from other files:
* `FinPlace E` is the set of finite places of `E`, `star w` the conjugate place, `LocField w` the
  completion `E_w` with valuation `v` (integral means `v x ≤ 1`) and `ResField w` its residue field.
* `LocProd P` is the product of the `E_w` over `w ∈ P`, and `O` is its ring of integers.
* `stdLattice.selfDualAddChar E` is the additive character of the finite adeles `𝔸f E` fixed by the
  Weil data.
* `liftIntegralFn r f` is `S ↦ f (r S)` on integral matrices `S` and zero elsewhere.
* `compUpTo f j` is the composite `f (j - 1) ∘ ⋯ ∘ f 0` of a chain of linear maps.


### `IsSplitLevel`

 `P` consists of one place of each pair `w, w̄` above `N`; these places are unramified of degree
one. 

### `IsSplitLevel.star_notMem`

 The conjugate of a place in `P` is not in `P`; in particular the places in `P` are split. 

### `IsSplitLevel.q_eq`

 The residue field at each place in `P` has `N` elements. 

### `IsSplitLevel.v_natCast`

 `N` is a uniformiser at each place in `P`. 

### `IsSplitLevel.natCast_mem_iff`

 The places above `N` are those in `P` and their conjugates. 

### `residueOverN`

 The finite adele that is `y w / N` at `w ∈ P`, with `y w` read in `[0, N)`, and `0`
elsewhere. 

### `idem_mul_residueOverN`

 The adele `residueOverN y` is supported on `P`, so the idempotent `idem P` (which is `1` at the
places of `P` and `0` elsewhere) fixes it. 

### `diagN`

 The matrix `diag (1, …, 1, N)` at the places of `P` that lie in `S`, and `1` at the others. 

### `residueEquiv`

 The residue field at a place of `P` is `ℤ / N`. 

### `reduction`

 Reduction modulo `N` of the integers at `P`. 

### `reduction_eq_iff`

 An integer `x` at `P` reduces to `c` modulo `N` exactly if `(x - c) / N` is integral at each
place `w` of `P`, where `c w` is read in `[0, N)`. 

### `inclGL`

 The inclusion of the integral invertible matrices into all invertible matrices at `P`. 

### `reductionGL`

 Reduction modulo `N` of integral invertible matrices. 

### `liftGL`

 A section of `reductionGL`. 

### `diagNInv`

 The matrix `diag (1, …, 1, N⁻¹)` at all places of `P`. 

### `psiN`

 The character `ψ_N (y) = ψ (-y / N)` of the residues at `P`, where `ψ` is the additive character
`stdLattice.selfDualAddChar E` of the finite adeles and `y / N` is the adele `residueOverN y`. 

### `lastBasisVector`

 The last basis vector modulo `N`. 

### `exists_GL_last_col_and_row`

 A vector whose last entry is a unit is both the last column and the last row of an invertible
matrix. 

### `lastRowColGL`

 For `y` with unit last entry, an integral invertible matrix whose last column and last row are
both `y` modulo `N`. 

### `lastRowColGL_col_and_row`

 If the last entry of `y` is a unit, then `y` is both the last column and the last row of
`lastRowColGL y` modulo `N`. 

### `lastRowColGL_smul_lastBasisVector`

 If the last entry of `y` is a unit, then `lastRowColGL y` takes the last basis vector to `y`
modulo `N`. 

### `lastBasisVector_vecMul_lastRowColGL`

 If the last entry of `y` is a unit, then `lastRowColGL y`, acting on row vectors, takes the last
basis vector to `y` modulo `N`. 

### `upOperator`

 The operator `Up = π (D) ∑ y, ψ_N (y_last) π (lastRowColGL y)`, where `D = diagNInv` and `y`
runs over the vectors modulo `N` whose last entry `y_last` is a unit. The matrix `D` replaces the
standard lattice by the lattice enlarged by the last basis vector divided by `N`. 

### `mirabolic`

 The integral invertible matrices whose last column is the last basis vector modulo `N`: the
stabiliser of the standard lattice marked with that vector. 

### `mem_mirabolic`

 An integral invertible matrix that fixes the last basis vector modulo `N` lies in `mirabolic`,
and every element of `mirabolic` has this form. 

### `ramified`

 A vector is ramified if at each place `w` of `P` it has the form `ψ - x ψ` for an integral unit
scalar `x` that is `1` modulo `N` at the other places. A vector that is fixed by the scalars
congruent to `1` modulo `N` has this form if its mean over the unit scalars at each `w` is zero.
The lift laws use only this form. 

### `liftFn`

 A function of matrices modulo `N`, as a function of integral matrices at `P`, extended by
zero. 

### `liftFn_comp_mul`

 Applying `liftFn` to `T ↦ f (reductionGL b * T * reductionGL a)` gives
`T ↦ liftFn f (inclGL b * T * inclGL a)`, for integral invertible matrices `a`, `b`. 

### `liftFn_inclGL`

 At an integral invertible matrix `k`, `liftFn f` (the function `f` of matrices modulo `N`, read
on matrices at `P`) takes the value of `f` at `reductionGL k`, i.e. `k` modulo `N`. 

### `lastRowDatum`

 The indicator of the integral matrices whose last row is the last basis vector modulo `N`. 

### `lastColDatum`

 The indicator of the integral matrices whose last column is `y` modulo `N`. 

### `charDatum`

 On integral matrices, `ψ_N` of the last row paired with `y`. 

### `directDatum`

 The direct datum: the indicator of the integral matrices whose last column is the last basis
vector modulo `N`. For marked lattices `(L, ε)`, `(L', ε')` it is `1[S L ⊆ L', S ε = ε']`. 

### `mirrorDatum`

 The mirror datum: `ψ_N` of the corner entry modulo `N` on integral matrices, zero elsewhere. For
marked lattices `(L, ε)`, `(L', ε')` it is `1[S L ⊆ L'⁺] ψ_N (u' (S ε))` in bases of `L` and
`L'⁺ = L' + 𝒪 ε' / N`, where `u'` is the last coordinate on `L'⁺` modulo `N`. 

### `gluedDatum`

 The glued datum of a double lift: on pairs of integral matrices, `ψ_N` of the corner entry of
the product `R T`. 

### `gluedDatum_eq_sum`

 The glued datum, sorted by the last column `y` of the first matrix modulo `N`: it is the sum of
the indicator `lastColDatum y` at `T` times the character `charDatum y` at `R`. 

### `primitiveVectors`

 The vectors modulo `N` that are non-zero at every place of `P`. 

### `LiftLaw`

 The rules for a lift `L Ψ` from `π` to `π'` that is linear in its datum `Ψ`, a function on
matrices at `P`; the constant `γ` is the cost of the change of lattices `diagNInv`. 

### `LiftLaw.integral_equivariant`

 Integral invertible matrices move between the datum and the two representations with no
  factor. 

### `LiftLaw.diagNInv_lastRowDatum`

 Passing in the direct datum from bases of the enlarged lattices (`lastRowDatum`) to bases of
  the original lattices (`directDatum`) costs the factor `γ`. 

 ## The direct datum in terms of valuations 

### `reduction_eq_zero_iff`

 An integer at `P` reduces to zero modulo `N` exactly if `N` divides it at every place. 

### `reduction_eq_one_iff`

 An integer `x` at `P` reduces to one modulo `N` exactly if `N` divides `x - 1` at every
place. 

### `reduction_comp_eq_lastBasisVector_iff`

 An integral vector is the last basis vector modulo `N` exactly if, at every place of `P`, `N`
divides its entries other than the last and the last entry minus one. 

### `liftFn_indicator_apply`

 Let `p` be a condition on matrices modulo `N`, and let `Q` be equivalent, when `T` is integral,
to `p` for the reduction of `T`. Then the lift of the indicator of `p` is `1` at `T` if `T` is
integral and `Q` holds, and `0` otherwise. 

### `lastRowDatum_apply`

 `lastRowDatum` in terms of valuations: it is the indicator of the matrices `T` with integral
entries whose last row is congruent to the last basis vector modulo the uniformiser `N`. 

### `directDatum_apply`

 `directDatum` in terms of valuations: it is the indicator of the matrices `T` with integral
entries whose last column is congruent to the last basis vector modulo the uniformiser `N`. 

### `lastRowDatum_conj_diagNInv`

 The two descriptions of the direct datum agree. Let `D = diagNInv = diag (1, …, 1, N⁻¹)`. Then
`D⁻¹ T D` is integral with last row the last basis vector modulo `N` (`lastRowDatum`) exactly if
`T` is integral with last column the last basis vector modulo `N` (`directDatum`). 

 ## The stabilisers fix the direct and the mirror datum 

### `exists_inclGL_eq`

 Let `liftFn f` be the extension by zero of `f` from integral matrices modulo `N`. If it is
non-zero at `g` and at `g⁻¹`, then `g` comes from an integral invertible matrix `k` (`inclGL k = g`)
and `f` is non-zero at the reduction of `k`. 

### `directDatum_ne_zero_of_mem_mirabolic`

 The direct datum does not vanish on `mirabolic`, the integral invertible matrices whose last
column is the last basis vector modulo `N`. 

### `exists_inclGL_eq_conj_diagNInv`

 Let `g` lie in `mirabolic`, that is, `g` is integral invertible with last column the last basis
vector modulo `N`. Then its conjugate `D⁻¹ g D` by `D = diagNInv = diag (1, …, 1, N⁻¹)` is an
integral invertible matrix whose last row is the last basis vector modulo `N`. 

### `directDatum_mul_mul_of_mem_mirabolic`

 Let `g` and `h` lie in `mirabolic`. Then `directDatum`, the indicator of the integral matrices
whose last column is the last basis vector modulo `N`, is invariant under `T ↦ h⁻¹ T g`. 

### `mirrorDatum_mul_mul_of_mem_mirabolic`

 Let `g` and `h` lie in `mirabolic`, that is, they are integral invertible matrices at `P` whose
last column is the last basis vector modulo `N`, and let `D = diagNInv = diag (1, …, 1, N⁻¹)`. Then
`T ↦ mirrorDatum (D⁻¹ T)` is invariant under `T ↦ h⁻¹ T g`. 

 ## The operator `Up` 

### `mirabolic_fix_upOperator`

 `Up` preserves the vectors fixed by `mirabolic`, the group of integral invertible matrices at
`P` whose last column is the last basis vector modulo `N`. 

### `commute_upOperator`

 An endomorphism of `π` that commutes with the action of all matrices at `P` commutes with `Up`
(`upOperator`). 

### `map_mem_ramified`

 A linear map `T` from `π` to `π'` that commutes with integral unit scalars sends ramified
vectors to ramified vectors. 

### `upOperator_mem_ramified`

 `Up` (`upOperator`) commutes with integral unit scalars, so it preserves ramified vectors. 

### `upOperator_pow_mem_ramified`

 The powers of `Up` (`upOperator`) preserve ramified vectors. 

 ## Cutting a datum into pieces, and consequences of the lift law 

### `liftFn_comp_eq_sum_smul`

 Let `L` be linear in its datum. If the datum is `g (r T)` for a function `r` of the matrix `T`
modulo `N` with finitely many values, then the lift is the sum over the values `y` of `g y` times
the lift by the indicator of `r T = y`. 

### `exists_GL_smul_lastBasisVector`

 A vector modulo `N` that is non-zero at every place of `P` is the image of the last basis
vector under an invertible matrix modulo `N`. 

### `mem_ramified`

 Let the lift `L Ψ : π → π'`, linear in its datum `Ψ`, obey the lift law. Then the lift by any
function `f` of matrices modulo `N`, extended by zero off the integral matrices (`liftFn f`),
preserves ramified vectors, because scalars pass through it. 

### `apply_liftFn_eq_zero_of_smul_invariant`

 Let the lift `L Ψ : π → π'`, linear in its datum `Ψ`, obey the lift law, and let the function
`f` of matrices modulo `N` be invariant under the unit scalars that are `1` away from the place `w`.
Then the lift by `f`, extended by zero off the integral matrices (`liftFn f`), annihilates ramified
vectors: such a vector is `ψ - x ψ` for an integral unit scalar `x` that is `1` modulo `N` away from
`w`. 

### `apply_liftFn_indicator_eq_zero`

 Let the lift `L Ψ : π → π'` be linear in its datum `Ψ`, a function on matrices at `P`, and obey
the lift law; in particular integral invertible matrices move freely between the datum and the two
representations. Let `φ` be ramified: at each place `w` of `P` it is `ψ - x ψ` for an integral unit
scalar `x` that is `1` modulo `N` away from `w`. Let `r` map matrices modulo `N` to vectors modulo
`N` and commute with scalars, and let the vector `y` vanish at some place `w`. Then `φ` is
annihilated by the lift whose datum is the indicator of the integral matrices with reduction `T`
satisfying `r T = y`. 

### `inclGL_lastColDatum`

 Let the lift `L Ψ : π → π'` be linear in its datum `Ψ` and obey the lift law `H`; in particular
integral invertible matrices move freely between the datum and the two representations. Let `k` be
an integral invertible matrix at `P`, and let `lastColDatum y` be the indicator of the integral
matrices with last column `y` modulo `N`. For every vector `φ` of `π`, the action of `inclGL k` on
`π'` takes the lift of `φ` by `lastColDatum y` to the lift of `φ` by
`lastColDatum (reductionGL k • y)`. 

### `charDatum_inclGL`

 Let the lift `L Ψ : π → π'` be linear in its datum `Ψ` and obey the lift law `H`; in particular
integral invertible matrices move freely between the datum and the two representations. Let `k` be
an integral invertible matrix at `P`, with reduction `reductionGL k` modulo `N` and image `inclGL k`
among all invertible matrices. Let `charDatum y` be `ψ_N` of the last row paired with `y` modulo `N`
on integral matrices and zero elsewhere. For every vector `φ` of `π`, the lift of `π.ρ (inclGL k) φ`
by `charDatum (reductionGL k • y)` is the lift of `φ` by `charDatum y`. 

### `mirrorDatum_eq_unitCorner`

 Let the lift `L Ψ : π → π'` be linear in its datum `Ψ` and obey the lift law; in particular
integral invertible matrices move freely between the datum and the two representations. Let `φ` be
ramified: at each place `w` of `P` it is `ψ - x ψ` for an integral unit scalar `x` that is `1`
modulo `N` away from `w`. Then the lift of `φ` does not change if `mirrorDatum` is restricted to the
matrices whose corner entry is a unit modulo `N`. 

### `mirror_eq_upOperator_direct`

 **Mirror data through direct data, on the target.** Let the lift `L Ψ : π → π'` be linear in its
datum `Ψ` and obey the lift law; in particular integral invertible matrices move freely between the
datum and the two representations. Let `φ` be ramified: at each place `w` of `P` it is `ψ - x ψ` for
an integral unit scalar `x` that is `1` modulo `N` away from `w`. Then the mirror lift of `φ`, moved
by `D = diagNInv = diag (1, …, 1, N⁻¹)`, is `Up` of the direct lift of `φ`. 

### `mirror_eq_direct_upOperator`

 **Mirror data through direct data, on the source.** Let `π`, `π'` be representations (action
`ρ`) of `GL (n ⊕ Unit)`, `GL (n' ⊕ Unit)` over `LocProd P`. Let the lift `L Ψ : π → π'` be linear in
its datum `Ψ` and obey the lift law `H : LiftLaw`. Also, `D = diagNInv = diag (1, …, 1, N⁻¹)` moves
from `π'` to `π` at the cost `γ`, turning `lastRowDatum` into `directDatum`. Let `φ` be ramified: at
each place `w` of `P` it is `ψ - x ψ` for an integral unit scalar `x` that is `1` modulo `N` away
from `w`. Then the lift of `φ` by `mirrorDatum`, moved by `D`, is `γ` times the direct lift
`L directDatum` of `Up φ`. 

### `upOperator_direct`

 Let the lift `L Ψ : π → π'`, linear in its datum `Ψ`, obey the lift law with factor `γ`, and let
`φ` be ramified: at each place `w` of `P` it is `ψ - x ψ` for an integral unit scalar `x` that is
`1` modulo `N` away from `w`. Then `Up` (`upOperator`) moves through the lift by `directDatum`, the
indicator of the integral matrices whose last column is the last basis vector modulo `N`, at the
cost of the factor `γ`. 

### `sum_charDatum_lastColDatum`

 Let the lifts `L Ψ : π → π'` and `L' Ψ : π' → π''` be linear in their data and obey the lift
law; in particular integral invertible matrices move freely between the datum and the two
representations. Let `φ` be ramified: at each place `w` of `P` it is `ψ - x ψ` for an integral unit
scalar `x` that is `1` modulo `N` away from `w`. Then the sum over `y` of
`L' (charDatum y) (L (lastColDatum y) φ)` equals the number of primitive vectors times
`L' mirrorDatum (L directDatum φ)`. 

### `glued_eq_direct_direct_upOperator`

 Let the lifts `L Ψ : π → π'` and `L' Ψ : π' → π''` be linear in their data and obey the lift law
with factors `γ`, `γ'`: integral invertible matrices move freely between the datum and the two
representations, and `D = diagNInv = diag (1, …, 1, N⁻¹)` moves from target to source at the cost of
the factor, turning `lastRowDatum` into `directDatum`. Let `φ` be ramified: at each place `w` of `P`
it is `ψ - x ψ` for an integral unit scalar `x` that is `1` modulo `N` away from `w`. Then the
double lift of `φ` by `∑ y, lastColDatum y ⊗ charDatum y`, moved by `D`, is a scalar times the two
direct lifts of `Up φ` (`upOperator`). The scalar is `γ' γ` times the number of primitive
vectors. 

 ## Chains of lifts 

### `compUpTo_direct_mem_ramified`

 If each `L j`, a lift from `π j` to `π (j + 1)` for places `P` above the split prime `N`, obeys
the lift law, then the composite of the first `j` direct lifts preserves ramified vectors. 

### `upOperator_compUpTo_direct`

 Let each lift `L j Ψ : π j → π (j + 1)` obey the lift law with factor `γ j`. On ramified vectors
`Up` (`upOperator`) moves through the composite `L (j - 1) Ψ ∘ ⋯ ∘ L 0 Ψ` of the first `j` lifts by
`Ψ = directDatum` at the cost of `∏ l < j, γ l`. 

### `gluedLift`

 The `i`-th glued double lift of a chain of lifts `L j` between representations `π j`: it is
`d i` times the sum over the vectors `y` modulo `N` of the lift `L (2 i + 1)` by `charDatum y` after
the lift `L (2 i)` by `lastColDatum y`, moved by `diagNInv`. 

### `compUpTo_gluedLift_eq_smul`

 **All lifts become direct.** Let each lift `L j Ψ : π j → π (j + 1)` be linear in its datum `Ψ`
and obey the lift law with factor `γ j`: integral invertible matrices move freely between the datum
and the two representations, and `D = diagNInv = diag (1, …, 1, N⁻¹)` moves from target to source at
the cost `γ j`, turning `lastRowDatum` into `directDatum`. The glued double lift
`gluedLift π L d i : π (2 i) → π (2 i + 2)` is `d i` times `D` after `∑ y, L (2 i + 1) (charDatum y)
∘ L (2 i) (lastColDatum y)`, and `compUpTo f j` is `f (j - 1) ∘ ⋯ ∘ f 0`. Let `φ` be ramified: at
each place `w` of `P` it is `ψ - x ψ` for an integral unit scalar `x` that is `1` modulo `N` away
from `w`. Then the composite of the first `p` glued double lifts takes `φ` to a scalar times the
composite of `2 p` direct lifts of `Up ^ p φ`. The scalar is the product over `i < p` of `d i`, the
number of primitive vectors in the middle and `∏ l < 2 i + 2, γ l`. 
