---
{
  "module": "src/Lib/GaloisRep/TaylorWiles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/TaylorWiles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/TaylorWiles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Auxiliary places, base level, integral Hecke algebra and operators at the auxiliary places

Base data `D` consist of a finite set `D.places` of places and a space `D.forms` of forms of a fixed
type at `D.places`. The forms of principal level at finitely many further places make up a
finite-dimensional space with an integral lattice. Functions on the systems of eigenvalues act on
this space, by a scalar on the forms of each system. Those that keep integral forms make up a closed
integral Hecke algebra. At the auxiliary places, translations and the action of `GL_N` over the
residue fields give operators that commute with this algebra.

## Main definitions and results

* `New.Patching.TaylorWilesPlaces`: Frobenius data at places `w j` whose residue fields have
  order ≡ 1 mod m.
* `New.Patching.BaseLevel.formsOfLevel`: the forms of that type and principal level at `L`, with the
  lattice `New.Patching.BaseLevel.ellIntegralForms` of integral forms and the algebra
  `New.Patching.BaseLevel.integralEnd` that keeps it.
* `New.Patching.BaseLevel.heckeAlgebra`, `New.Patching.BaseLevel.heckeAction`: the functions whose
  operator keeps integral forms, and their action; `New.Patching.BaseLevel.isClosed_heckeAlgebra`:
  they form a closed set for the product topology on functions from systems to `PadicAlgCl ℓ`.
* `New.Patching.BaseLevel.localOperators`: the operators that come from translations at one place
  `w j`. They commute with the Hecke algebra.
* `New.Patching.BaseLevel.residueRep`: the action of the groups `GL_N` over the residue fields,
  `N = |n|`; its fixed forms are those of base level
  (`New.Patching.BaseLevel.mem_formsOfLevel_empty_iff_residueRep_fixed`).
* `New.Patching.BaseLevel.exists_higman_operator`: for a finite group `Δ` embedded in the product of
  the groups `GL_N` over the residue fields at the places `w j` (all off level), an operator `Ψ`
  with `∑ g⁻¹ Ψ g = c`.

Notions from other files:
* `New.levelOf`: The elements of K₀ = `stdLevel E n` whose reductions modulo the places w_i lie in a
  subgroup H of ∏_i GL_n(k_{w_i}); for H = ⊥ this is the principal level at these places.
* `New.Space.forms`: Algebraic modular forms of weight κ on a definite space V: functions f on G_f
  with open right stabiliser and f(γg) = ρ_κ(γ)f(g) for rational γ, ρ_κ = `New.Space.weightRep`.
* `New.Patching.Isotypic`: An isotypic space of forms: for a system t of Hecke eigenvalues at the
  finite places, the forms that are Hecke eigenforms with eigenvalues t at almost all places.
* `New.Patching.localFormRep`: The action of GL_N(E_w), N = |n|, on forms at a split place w.

## Relation to the literature

Known result: Taylor–Wiles freeness at auxiliary primes, up to the orders of the stabilisers. Here
the setting is integral forms of principal level on a definite unitary group, with any finite
subgroup of the product of the finite general linear groups at the auxiliary places. Freeness holds
only up to a fixed integer and is expressed as one Higman operator. Source: Taylor–Wiles, Ann. Math.
141 (1995); Clozel–Harris–Taylor, Publ. IHES 108 (2008), §3.



## Auxiliary places, base level and integral forms

* `New.Patching.TaylorWilesPlaces`, `New.Patching.BaseLevel`: the auxiliary places and the base
  data.
* `New.Patching.BaseLevel.ellIntegralForms`, `New.Patching.BaseLevel.formsOfLevel`,
  `New.Patching.BaseLevel.integralEnd`: the integral forms, the forms of level `L`, and the
  endomorphisms of the latter that keep integral forms.
* `New.Patching.BaseLevel.Eigensystem`, `New.Patching.BaseLevel.IsOffLevel`: the systems of
  eigenvalues that occur, and the places at which all of them have their eigenvalues.


### `TaylorWilesPlaces`

 Auxiliary places as in the Taylor–Wiles method: for each index `j` a Frobenius datum at a
finite place `w j` of `E`, such that no two of these places are equal or conjugate and `m` divides
`q_j − 1`, where `q_j` is the order of the residue field at `w j`. 

### `TaylorWilesPlaces.frobData`

 For each index `j`, the Frobenius datum at the place `w j`. 

### `TaylorWilesPlaces.apart`

 No two of the places `w j` are equal or conjugate. 

### `TaylorWilesPlaces.dvd_q_sub_one`

 `m` divides `q_j − 1` for each `j`. 

### `TaylorWilesPlaces.place`

 The place `w j` of `Q`: the finite place of its Frobenius datum with index `j`. 

 ### The base level and deeper levels 

### `BaseLevel`

 Base data: a finite set `places` of places; a space `forms` of forms of fixed type at `places`;
a common multiple m of the orders of all stabilisers Γ ∩ gK₀g⁻¹. Here Γ is the group of rational
points and K₀ = `stdLevel E n`. 

### `BaseLevel.places`

 The finite set of places of the level. 

### `BaseLevel.forms`

 The space of forms of weight `κ` that have the given type at `places`. 

### `BaseLevel.map_mem_forms`

 `forms` is kept by every operator that commutes with the maximal level at the places of
  `places` and their conjugates. 

### `BaseLevel.exists_level`

 Some open subgroup acts on `forms` by a character, through its components at the places of
  `places` and their conjugates. 

### `BaseLevel.card_aut_dvd`

 `m` is a multiple of the order of each stabiliser `Γ ∩ g K₀ g⁻¹`, where `Γ` is the group of
  rational points and `K₀ = stdLevel E n`. 

### `ellIntegralForms`

 Integral forms: the `New.Patching.EllAdicIntegers`-module of forms whose values at all points g
integral above ℓ (the components of g at the places above ℓ lie in the local level) have coordinates
that ιℓ sends to ℓ-adic integers. 

### `localGroupAlgebra_le_endPreserving`

 For a finite place `w` not above `ℓ`, the operators generated by the translations supported at
`w` and `w̄` keep the integral forms. 

### `repOff`

 The action of G_f on forms of weight κ on V by right translation through the components at the
places outside `D.places` and its conjugates. 

### `formsOfLevel`

 The forms in `D.forms` that are fixed by the components off `D.places` and its conjugates of the
principal level subgroup of K₀ at the places L. 

### `Eigensystem`

 Systems of eigenvalues of level L: the isotypic spaces that contain a nonzero form of
`New.Patching.BaseLevel.formsOfLevel`. 

### `IsOffLevel`

 The places off the level `L`: (a) neither `w` nor its conjugate is in `D.places`, and `w` is not
above `ℓ`; (b) for each system `x` of level `L`, the forms of `x` in `D.formsOfLevel L` lie in
`eigenformsAt V κ w (t w)`, where `t = x.heckeEigenvalues` is the chosen system of eigenvalues that
defines `x`. If `w` splits, (b) says that these forms are spherical at `w` with Hecke eigenvalues
`t w`; otherwise it is no condition. 

### `repOff_eq_of_mem_trivialOn`

 An element `k` with component `1` at the places of `D.places` acts through `D.repOff`, the
action through the components off `D.places` and its conjugates, as the plain translation by `k`. 

### `FormEnd`

 The `New.Patching.EllAdicIntegers`-algebra of ℂ-linear endomorphisms of the space of forms
`New.Patching.BaseLevel.formsOfLevel` attached to the base data D and the family of finite places
L. 

### `integralEnd`

 The `New.Patching.EllAdicIntegers`-algebra of ℂ-linear endomorphisms of the space of forms
`New.Patching.BaseLevel.formsOfLevel` that preserve its integral forms. 

### `formsOfLevel_base_le`

 The forms of the base level, with no auxiliary places, are forms of every level `L`. 


## Scalar action of systems and the integral Hecke algebra

For base data `D` (`New.Patching.BaseLevel`) and finitely many places `L`,
`New.Patching.BaseLevel.formsOfLevel` is the space of forms in `V.forms κ` with two properties. At
`D.places` they satisfy the level condition of `D`. Off `D.places` and its conjugates they have
principal level at `L` and maximal level elsewhere.

* The space has finite dimension and is spanned by its isotypic parts
  (`New.Patching.BaseLevel.formsOfLevel_le_of_eigensystem`), so operators can be compared there
  (`New.Patching.BaseLevel.formEnd_ext`).
* The space has only finitely many systems, and almost every place is off the level
  (`New.Patching.BaseLevel.eventually_isOffLevel`).
* `New.Patching.BaseLevel.diagOp`, `New.Patching.BaseLevel.systemAction`: a function `t` from
  systems to `PadicAlgCl ℓ` acts on the part `x` by the scalar `ιℓ.symm (t x)`.


### `instance : FiniteDimensional ℂ (D.formsOfLevel L)`

 The forms of level `L` make up a finite-dimensional space: an open subgroup acts on them by a
character. 

### `instance : Fintype (D.Eigensystem L)`

 Only finitely many systems of eigenvalues have level `L`. 

### `_root_.New.Patching.Isotypic.eventually_le_eigenformsAt_of_fg`

 A finitely generated space `U` of forms inside an isotypic space `x` lies in
`eigenformsAt V κ w (x.heckeEigenvalues w)` for almost every finite place `w`: its forms are
eigenforms at `w` with the eigenvalues of `x`. 

### `eventually_isOffLevel`

 Almost every finite place is off the level `L`: it avoids `D.places`, its conjugates and the
places above `ℓ`, and each system of level `L` has its eigenvalues there. 

### `formsOfLevel_le_levelSpace`

 Forms of level `L` are fixed by the elements of K₀ = `stdLevel E n` whose components at the
places of `L` and of `D.places` are `1`. 

 ### Functions on systems as operators 

### `diagOp`

 For a function `t` from systems to `PadicAlgCl ℓ`, a chosen endomorphism of the space of forms
acting on the isotypic space of each system `x` by the scalar `ιℓ.symm (t x)`. 

### `diagOp_apply`

 On the isotypic space of a system `x`, the operator `diagOp t` is the scalar `ιℓ⁻¹ (t x)`. 

### `formsOfLevel_le_of_eigensystem`

 The space `New.Patching.BaseLevel.formsOfLevel` is spanned by its eigenforms: a subspace N
containing its intersection with every isotypic space of level L contains all of it. 

### `formEnd_ext`

 Two endomorphisms of the space `New.Patching.BaseLevel.formsOfLevel` L are equal if they agree
on every form that lies in an isotypic space of a system of level L. 

### `systemAction`

 The `EllAdicIntegers`-algebra map that sends a function t from the systems of eigenvalues of
level L (`New.Patching.BaseLevel.Eigensystem`) to `PadicAlgCl ℓ` to the operator (in `D.FormEnd L`,
the ℂ-linear endomorphisms; ιℓ : ℂ → `PadicAlgCl ℓ` is the identification fixed by `PadicIso ℓ`) on
`New.Patching.BaseLevel.formsOfLevel` L that multiplies the forms of each system x by the scalar
`ιℓ.symm (t x)`. 

 ### The Hecke algebra 

### `heckeAlgebra`

 The Hecke algebra: the functions t from the systems of level L to `PadicAlgCl ℓ` whose
operator `systemAction t` (multiplication of the forms of each system x by `ιℓ.symm (t x)`) keeps
the integral forms of `New.Patching.BaseLevel.formsOfLevel` L integral. 

### `heckeAction`

 The `EllAdicIntegers`-algebra map that sends t in the Hecke algebra to its operator
`systemAction t`, which multiplies the forms of each system x by `ιℓ.symm (t x)` and keeps the
integral forms. 

### `isClosed_heckeAlgebra`

 The Hecke algebra is closed in the space of functions from the systems of level `L` to
`PadicAlgCl ℓ`. 


## Operators at the auxiliary places

Fix base data `D : New.Patching.BaseLevel` (a type of forms at a finite set of places, a multiple
`c` of the orders of all stabilisers) and auxiliary split places `w j` given by
`Q : New.Patching.TaylorWilesPlaces`.


### `reindexResidueGL`

 The isomorphism ∏_j GL_N(k_{w_j}) ≅ ∏_j GL_n(k_{w_j}), N = |n|, that relabels rows and
columns along a chosen ordering of the index set n. 

 ### Operators at one place and the action of the finite groups 

### `localOperators`

 The operators at `w j`: the endomorphisms of the forms of principal level at the places
`Q.place` that keep the integral forms and agree there with an element of
`localGroupAlgebra (Q.place j)`, the `EllAdicIntegers`-combinations of translations by elements of
G_f supported at `w j` and its conjugate. 

### `residueRep`

 The action of ∏_j GL_N(k_{w_j}), with k_{w_j} = `ResField (Q.place j)` and N = |n|, on forms of
principal level at the places `Q.place`: an element acts by `D.repOff` of a lift to `stdLevel E n`
(`liftResidue`), the translation by its components off `D.places` and its conjugates. It keeps the
integral forms. 

### `mem_formsOfLevel_empty_iff_residueRep_fixed`

 A form of principal level at the auxiliary places has the maximal level `stdLevel` off
`D.places` and its conjugates exactly when it is fixed by the group ∏_j GL_N(k_{w_j}), N = |n|. 

### `localOperators.commute_heckeAction`

 An operator at `w j` commutes with the operator of every element t of the Hecke algebra. 

 ### Auxiliary places off the level

In the results below, the hypothesis `hQ`, where it is assumed, says that every place `w j` is off
the base level: `w j` and its conjugate are not in `D.places`, `w j` is not above `ℓ`, and the forms
of base level in each system have its eigenvalues at `w j` (`New.Patching.BaseLevel.IsOffLevel`).


### `residueRep_mulSingle`

 Let the places `w j` be off the base level. For an integral matrix `k` at `w j`, its reduction
placed at the index `j` acts on a form `y` of principal level as `k` does in the representation
`New.Patching.localFormRep` of GL_N(E_{w j}) on forms. 

### `residueRep_mem_localOperators`

 Let the places `w j` be off the base level. An element `g` of GL_N(k_{w j}), placed at the
index `j`, acts by an operator at `w j`. 

### `reindexGL_atPlace_mem_proIwahori_of_mem_levelOf`

 An element `k` of the principal level at the places `Q.place` has its component at `w j`,
reindexed along the chosen ordering of `n`, in the pro-p Iwahori group: it is integral and reduces
to `1`. 

### `exists_localOperators_aeval_hecke`

 Let `w j = Q.place j` be the Taylor–Wiles places, all off the base level (`D.IsOffLevel ![]`).
Let `a` be an operator at `w j`, i.e. an element of `D.localOperators Q j`: an endomorphism of the
forms `formsOfLevel Q.place` that keeps the integral forms and agrees with an
`EllAdicIntegers`-combination of translations supported at `w j` and its conjugate. If the values of
`a` are fixed by the pro-p Iwahori group I₁ = `proIwahori` in the representation
ρ = `New.Patching.localFormRep` of GL_N(E_{w j}), N = |n|, then for g in GL_N(E_{w j}) (stated over
`(Q.frobData j).place`, which is `Q.place j` by definition) and G in `EllAdicIntegers[X]` there is
an operator `b` at `w j` with b(y) = G([I₁gI₁])(a(y)) for all y, where
[I₁gI₁] = `heckeCoset ρ.ρ proIwahori g` is the Hecke operator of the double coset I₁gI₁. 

### `exists_orbit_weight`

 Let `Γ`, `K` be subgroups of `G`, let `π` map `K` and let `ψ` embed a finite group `Δ` into
`H`, and let `c` be a multiple of the orders of all the groups `classAut Γ K g` = Γ ∩ gKg⁻¹. Then
there are weights `u q d` in ℕ, for `q` in `G ⧸ Γ` and `d` in `Δ`, such that
`u (y⁻¹ • q) 1 = u q d` whenever `y` in `K` has `π y = ψ d⁻¹`, and the weights `u q d` add up to
`c` over `d` for each `q`. 

### `exists_higman_operator`

 Higman's criterion up to c, for auxiliary places `w j` off the base level: for a finite group Δ
embedded by φ in ∏_j GL_N(k_{w_j}), N = |n|, some operator Ψ on forms of principal level that keeps
the integral forms has ∑_{g∈Δ} g⁻¹Ψg = c, with g acting by `New.Patching.BaseLevel.residueRep` and c
the common multiple of the stabiliser orders fixed in `D`. 
