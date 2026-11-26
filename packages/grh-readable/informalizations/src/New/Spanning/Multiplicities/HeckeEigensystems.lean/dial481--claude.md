---
{
  "module": "src/New/Spanning/Multiplicities/HeckeEigensystems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spherical Hecke operators away from the level, and eigensystems

The level `M` is the product of the primes `D.levelPrime 0`, `D.levelPrime 1`, and `D.chosenPlace`
runs through the chosen places above it. The spherical Hecke operators away from `M` form an algebra
that acts at once on the forms `D.principalForms V` of principal level for all hermitian spaces `V`.
It commutes with the finite group `D.chosenGL`, so it acts on the good forms `D.goodForms V`, the
image of the idempotent `D.e₀`.

## Main definitions and results

* `New.Data.sphericalAlgebra`, `New.Data.heckeAlgebra`: the spherical elements of the group algebra
  and the operators that they give; `New.Data.heckeOnGood` is the action on good forms.
* `New.Data.heckeOperator`: the operators `T_{w,i}` at the places `New.Data.IsSplitOffLevel`, as
  members of the Hecke algebra; `New.Data.principalHeckeSplit` is the operator on one space.
* `New.Data.eigenPart`: the part with a given eigensystem. The parts are independent
  (`New.Data.iSupIndep_eigenPart`), and in finite dimension they span the forms
  (`New.Data.iSup_eigenPart_eq_top`).
* `New.Data.exists_hecke_proj_eigenPart`: a Hecke operator that is `1` on one part and `0` on
  finitely many others.

Notions from other files:
* `New.Data.principalForms`: the forms on `V` of archimedean type `typeKernel D.paramW s` that are
  fixed by the principal level `J_M = D.chosenLevel` at the chosen places; `V.formRep` is the
  action of the finite adelic unitary group `G_f = Gf E n` on forms, and `K₀ = stdLevel E n` is its
  standard maximal compact subgroup.
* `New.heckeSplit`: the Hecke operator `T_{w,i}` at a split place `w`, of the double coset of
  `diag (ϖ 1_i, 1)`.
* `New.universalLevelAlgebra`: the elements of a group algebra that keep the vectors of a given
  level in every representation.


### `mem_levelSpace_iff_forall_apply_eq`

 A vector has level `K` (with trivial character) if and only if every element of `K` fixes it. 

### `commute_asAlgebraHom_mapDomain_trivialOn`

 Let `G_f = Gf E n` be the finite adelic unitary group over the CM field `E` in the variables
indexed by `n`, let `S` be a set of finite places of `E`, and let `H = trivialOn n S` be the
subgroup of the elements with component `1` at the places of `S`. In every representation `ρ` of
`G_f`, an element `a` of the group algebra of `H` commutes with the action of each `k` that is
supported at the places of `S` and their conjugates. 

### `mapDomain_mem_universalLevelAlgebra`

 Let `G_f = Gf E n` be the finite adelic unitary group over the CM field `E` in the variables
indexed by `n`, `S` a set of finite places of `E`, and `H = trivialOn n S` the subgroup of the
elements with component `1` at the places of `S`. Let `J` be a subgroup of the maximal compact group
`K₀ = stdLevel E n` that contains `K₀ ∩ H`. If an element `a` of `ℂ[H]` keeps the vectors fixed by
`K₀ ∩ H` in every representation of `H`, then its image in `ℂ[G_f]` keeps the vectors fixed by `J`
in every representation of `G_f`. 

### `IsSplitOffLevel`

 The level `M` is the product of the two primes `D.levelPrime 0` and `D.levelPrime 1`, and the
places `D.chosenPlace x` are the chosen places of `D.E` above them. The Hecke operators are read at
the finite places `w` that are split (`star w ≠ w`, where `star w` is the complex conjugate) and are
neither a chosen place nor the conjugate of one. In this file, "not above `M`" and "away from `M`"
refer to the places that are neither chosen nor conjugate to a chosen one. 

### `IsSplitOffLevel.isSplit`

 The place `w` differs from its conjugate. 

### `IsSplitOffLevel.notMem_conjClosure`

 The place `w` is neither a chosen place nor the conjugate of one. 

### `IsSplitOffLevel.star`

 If the place `w` is split and neither it nor its conjugate is a chosen place above the level
`M`, then the same holds of the conjugate `star w`. 

### `offLevelGroup`

 The group `G^M` of the elements of the finite adelic unitary group `G_f` that have component
`1` at the chosen places above `M`. 

### `IsSplitOffLevel.ofSplitPlace_mem`

 If `w` is split and neither it nor its conjugate is a chosen place above the level `M`, the
embedding `ofSplitPlace` of `GL(E_w)` in the finite adelic unitary group `G_f`, at the places `w`
and `star w`, has its image in the group `G^M = D.offLevelGroup` of the elements that are `1` at
every chosen place. 

### `principalForms_le_sphericalAt`

 If `w` is split and not above `M`, the forms of principal level are spherical at `w`, that is,
fixed by the part of `K₀` supported at `w` and its conjugate. 

### `heckeSplit_mem_principalForms`

 Let `w` be a split place such that neither it nor its conjugate is a chosen place above the
level `M`. The Hecke operator `T_{w,i}` keeps the forms of principal level on `V`. 

### `principalHeckeSplit`

 The restriction of the Hecke operator `T_{w,i}` to the forms of principal level on `V`, at a
split place `w` such that neither it nor its conjugate is a chosen place above the level `M`. 

### `sphericalAlgebra`

 The spherical elements away from `M`: the elements of the group algebra of
`G^M = D.offLevelGroup` that keep the vectors fixed by the principal level `J_M = D.chosenLevel` in
every representation of `G_f`. 

### `mem_sphericalAlgebra_of_mem_universalLevelAlgebra`

 An element `a` of the group algebra of `G^M = D.offLevelGroup`, the elements of the finite
adelic unitary group `G_f` that are `1` at the chosen places above the level `M`, is spherical away
from `M` as soon as it keeps the vectors fixed by `K₀ ∩ G^M` in every representation of `G^M`. 

### `heckeAlgebra`

 The spherical Hecke operators away from `M`: the families `T` of operators `T V` on the forms of
principal level of all hermitian spaces `V` that are given by one spherical element `a` of the group
algebra of `G^M = D.offLevelGroup`. 

### `mem_heckeAlgebra`

 Let `G^M = D.offLevelGroup` be the group of the finite adelic elements that are `1` at the
chosen places above the level `M`. A family `T` of operators on the forms of principal level of all
hermitian spaces `V` lies in the Hecke algebra if and only if one spherical element acts as `T V`
for every `V`. 

### `exists_heckeAlgebra_eq_asAlgebraHom`

 Let `G^M = D.offLevelGroup` be the group of the elements of `G_f` that are `1` at the chosen
places, the prime divisors of `D.piM`. Let `a` be a spherical element of its group algebra. Then `a`
gives a member `T` of the Hecke algebra `D.heckeAlgebra`. On each hermitian space `V` with signs `s`
at the infinite places, `T` acts on `D.principalForms V` as `a` does through `V.formRep`. 

### `exists_asAlgebraHom_eq_heckeSplit`

 Let `w` be a split place of `D.E` such that neither `w` nor its conjugate is a chosen place
above the level `M`, and let `G^M = D.offLevelGroup` be the elements of the finite adelic unitary
group `G_f` that are `1` at the chosen places. One element `a ∈ ℂ[G^M]` acts as the Hecke operator
`T_{w,i}` in every representation `ρ` of `G_f`, on any complex vector space `W`. 

### `principalHeckeSplit_mem_heckeAlgebra`

 Let `w` be a split place of `D.E` such that neither `w` nor its conjugate is a chosen place
above the level `M`, and let `T_{w,i}` be the Hecke operator of the double coset of
`diag (ϖ 1_i, 1)` at `w`. The family of its restrictions `D.principalHeckeSplit V hw i` to the forms
of principal level, as `V` runs over the hermitian spaces, lies in `D.heckeAlgebra`: one spherical
element of the group algebra of `D.offLevelGroup` gives all of them. 

### `heckeOperator`

 The Hecke operator `T_{w,i}`, as a member of the Hecke algebra, for `x = (w, i)` with `w` split
and not above `M`; it is `0` at the other places. 

### `coe_heckeOperator_apply`

 At a split place `w` not above `M`, `D.heckeOperator (w, i)` acts on forms as `T_{w,i}`. 

### `eigenPart`

 The part of the forms of principal level on `V` for the eigensystem `p`: the forms on which
each `D.heckeOperator (w, i)` acts by the scalar `p (w, i)`. 

### `hasHeckePolynomial_of_mem_eigenPart`

 Let `w` be a split place such that neither it nor its conjugate is a chosen place above the
level `M`, let `q` be the norm of `w` and `r` the number of elements of `D.RowIndex`, the rank of
`V`. A form `y` of principal level with Hecke eigensystem `p` is spherical at `w`, and for each
complex `X` the operator `∑_{i ≤ r} (-X)^i q^{i(i-1)/2} T_{w,i}`, the Hecke polynomial at `X`,
multiplies it by `∑_{i ≤ r} (-X)^i q^{i(i-1)/2} p (w, i)`. 

### `smul_mul_heckeOperator_sub_smul_apply`

 Let `T` be in the Hecke algebra, `T_x = D.heckeOperator x` for a pair `x = (w, i)`, and `a, b`
complex numbers. On a form `y` of principal level with eigensystem `d`, the operator
`a (T T_x - b T)` acts as `a (d x - b) T`. 

### `exists_hecke_proj_eigenPart`

 For an eigensystem `q` and a finite set `F` of eigensystems, one member `T` of the Hecke algebra
is, on all `V`, the identity on the forms with eigensystem `q` and zero on those with an eigensystem
`d ∈ F` other than `q`. 

### `coe_principalRep_apply`

 An element `g` of `D.chosenGL` acts on forms of principal level through its integral lift
`liftResidue g` to `G_f`. 

### `liftGroupAlgebra`

 The lift to the group algebra of `G_f` of an element of the group algebra of the finite group
`D.chosenGL`: each group element is replaced by an integral lift that is `1` off `M`. 

### `coe_principalRep_asAlgebraHom_apply`

 An element `x` of the group algebra of `D.chosenGL` acts on forms of principal level through its
lift to the group algebra of `G_f`. 

### `liftResidue_apply_mem_levelSpace`

 The integral lift `liftResidue g` of `g : D.chosenGL` normalises the principal level
`D.chosenLevel`. So in every representation `ρ` of `G_f` it maps `levelSpace ρ D.chosenLevel`, the
vectors fixed by that level, into itself. 

### `liftGroupAlgebra_mem_universalLevelAlgebra`

 The lift to `G_f` of an element of the group algebra of `D.chosenGL` keeps the vectors fixed by
the principal level `D.chosenLevel` in every representation. 

### `commute_heckeAlgebra_principalRep`

 Let `D.chosenGL` be the finite group `∏ GL(𝔽_w)` over the chosen places `w` above the two primes
of the level `M`, with `𝔽_w` the residue field and rows indexed by `D.RowIndex`. The action of every
`x` of its group algebra commutes with every member `T` of `D.heckeAlgebra`, the spherical Hecke
operators away from `M`, which are given by elements of `G_f` that are `1` at the chosen places. 

### `heckeOnGood`

 A spherical Hecke operator away from `M` preserves the good forms of `V`, the image of the
idempotent `D.e₀` in the forms of principal level. This is the resulting action of the Hecke
algebra on the good forms. 

### `coe_heckeOnGood_apply`

 On good forms a member of the Hecke algebra acts as it does on the forms of principal level. 

### `principalRep_mem_eigenPart`

 The forms of principal level with eigensystem `p` are stable under the group algebra of
`D.chosenGL`. 

### `iSupIndep_eigenPart`

 The parts of the forms of principal level for the Hecke eigensystems are independent, so their
sum is direct. 

### `finite_setOf_inf_eigenPart_ne_bot`

 If the forms of principal level on `V` are finite-dimensional, only finitely many Hecke
eigensystems occur in a subspace `N`. 

### `exists_mem_eigenPart_of_heckeSplit_eq_smul`

 Let `y` be a form of principal level on `V` that is an eigenvector of the Hecke operator
`T_{w,i}` for every `i` and every split place `w` away from the level `M`. Then `y` lies in
`D.eigenPart V p` for some eigensystem `p`. 

### `iSup_eigenPart_eq_top`

 Let `D` be admissible data with CM field `E = D.E`, and `V` a hermitian space over `E` with
signs `s` at the infinite places. An eigensystem `p` assigns a complex number `p (w, i)` to each
finite place `w` of `E` and natural number `i`, and `D.eigenPart V p` consists of the forms of
principal level on `V` on which each `D.heckeOperator (w, i)` acts by `p (w, i)`. If the forms of
principal level on `V` are finite-dimensional, they are the sum of these parts over all `p`. 
