---
{
  "module": "src/New/UpperBound/Objects/Columns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Levels of the chain, chain data, and the composite lift

The map `New.Data.compositeLift` on source forms is built from chains of `m` theta lifts
`X_0 → X_1 → ⋯ → X_m` between definite unitary groups, followed by restriction to the block `Y_m` of
one rank less. Here `X_j` is an index set of `𝗇_j = k + j(t + 1)` elements. The weight at stage `j`
is given by the column numbers `New.Data.columnCount` and the determinant exponents
`New.Data.lastEntry`. This file defines the levels and spaces of forms of the stages, the
restriction from `X_m` to `Y_m`, the kernels of the lifts, the glued datum at `N` in the
Schrödinger model, and chain data.

## Main definitions and results

* `New.Data.restrictedChain`: ∑_x Ψ(x) · (chain with the data of x), then `New.Data.restrictToY`.
* `New.Data.IsChainDatum`, `New.Data.compositeLift`: chain data, and the same map for the data glued
  above `N` in each double lift.

Notions from other files:
* `New.classAut`: `classAut Γ K g` is Γ ∩ gKg⁻¹, the stabiliser in Γ of the coset gK; here
  Γ = `stdRatPoints` is the rational unitary group of the standard definite space `New.stdSpace`,
  inside the finite adelic group.
* `New.Data.n`: The rank 𝗇_j = k + j(t + 1) of X_j.
* `New.Data.columnCount`: The number of columns of height h < 𝗇_j at the infinite place τ in the
  weight on X_j; it does not depend on j. For h = 1 it is `D.a` at the places in `New.Data.aPlaces`
  and 0 elsewhere; for h = k ≠ 1 it is κ_1(τ) − ⌊𝗇_1 / 2⌋, with κ_j = `D.liftWeight j`; for h > k
  with h ≡ k mod t + 1 it is `D.gap` − (t + 1); otherwise it is 0.
* `New.chain` (in `New.UpperBound.Objects.LiftChains`): the composite of the first `j` theta lifts.
* `New.Data.chosenLevel` (in `New.UpperBound.Objects.LiftChains`): the integral elements that
  reduce to `1` at every chosen place, that is, at every prime divisor of `D.piM`.

## Relation to the literature

This file sets up the objects of the upper bound. Related work is listed with the results on them,
in `New.UpperBound.Divisibility.LocalDivisibility`, `New.UpperBound.Seesaw.SeesawIdentity` and
`New.UpperBound.Divisibility.ValuationAtLevel`.



## The glued datum at `N` in the Schrödinger model

For a set `P` with one place of each conjugate pair above `N`, functions of matrices at `P` define
operators on finite data (`IsSplitLevel.schrodingerOpAt`). For a double lift, the seesaw produces
the sum of translates `doubleLiftGluing`; read in the model at any such `P`, this sum is the glued
datum, with no constant.


### `scalarFin_atPlace`

 The component at a finite place `w` of the scalar element `ν` is the scalar matrix `ν w`. 

### `Seesaw.pairWeilFinite_scalarFin`

 Let `ν`, `ν'` be finite adeles of norm one. The Weil action with characters `a`, `b` of the pair
of scalar matrices `(ν, ν')` on the finite part for the standard spaces on `n` and `n'` is the value
of the character `pairChar a b`, `(g, h) ↦ a (det h) * (b (det g))⁻¹`, at this pair, times the
action with trivial characters of the pair of scalar matrices `(1, ν' / ν)`. 

### `Seesaw.poleColumn`

 The finite adelic matrix whose last column is `-y / N` at the places of `P` and zero at the
other places, and whose other columns are zero. 

### `Seesaw.poleRow`

 The finite adelic matrix whose last row is the conjugate of `-y / N`, supported at the
conjugates of the places of `P`, and whose other rows are zero. 

### `Seesaw.poleColumn_apply_eq_zero`

 The entries of `poleColumn n y` vanish at the places outside `P`. 

### `Seesaw.poleRow_apply_eq_zero`

 The entries of `poleRow m y` vanish at the places whose conjugate is outside `P`. 

### `Seesaw.doubleLiftGluing`

 For a double lift, the sum over the vectors `y / N` with at most simple poles at `P`, modulo
integral vectors, of the translation of the first datum by the last column `-y / N` and of the
second by the last row `-ȳ / N`. 

### `Space.vacuumProjFinPart`

 The projection `V.projOn S` on the vacuum at the places of `S` and their conjugates, restricted
to the finite part of the data space of `V`. 

### `detCharAt`

 The character `g ↦ χ (det g) |det g| ^ (-k / 2)` of `GL n` over `LocProd P`, the product of the
completions of `E` at the places of `P`. 

### `schrodingerOpAt`

 The operator `v ↦ Ψ ⊗ v` of the Schrödinger model at `P` on the finite part for the standard
spaces on `n` and `n'`, as a linear function of the function `Ψ` of matrices over `LocProd P`. Here
`Ψ` is read as a function of finite adelic matrices through their components at `P`. 

### `embedGL`

 The element of the finite adelic unitary group that is supported above `N` and has the given
components at `P`. 

### `atPlace_embedGL_diagN`

 At a place `w` of `P`, the component `atPlace w` of `embedGL (h.diagN n S)` is
`diag (1, …, 1, N)` if `w` is in `S`, and `1` otherwise. 

### `mem_integralAbove_of_inclGL_eq`

 Let `P` hold one place of each conjugate pair above the prime `N` (`IsSplitLevel P N`). An
element `g` of the finite adelic unitary group whose component at `P` is an integral invertible
matrix `a` (through `inclGL`) is integral at all places above `N`, that is,
`g ∈ integralAbove n N`. 

### `reduction_eq_iff_idem_mul_mem`

 Let `x` be the component at `P` of `N u`, assumed integral. Its reduction modulo `N` is `c`
exactly when `u - c / N` is integral at `P`, with `c / N = residueOverN c`. 

### `exists_embedGL_scalar_eq_scalarFin`

 Let `P` hold one place of each conjugate pair above the prime `N`, all unramified of degree one
(`IsSplitLevel P N`), and let `w` be in `P`. Let `ν` be an integral finite adele of norm one that
is `1` away from `w` and `w̄`. Then there is a unit `x` of the integers at `P`, with reduction `1`
modulo `N` at the places of `P` other than `w`, such that the scalar matrix `ν` is the unitary
element `embedGL` supported above `N` whose component at `P` is the scalar matrix `x`. 

### `liftFn_eq_residueDatum`

 Let `P` hold one place of each conjugate pair above the prime `N`, all unramified of degree one
(`IsSplitLevel P N`), so that `residueEquiv` identifies the residue fields at `P` with `ZMod N`.
Let `f` be a function of matrices modulo `N`, and `h.liftFn f` the function of matrices at `P` that
is `f` of the reduction on integral matrices and zero elsewhere. Evaluated on finite adelic matrices
through their components at `P`, it is the residue datum of `f`: the value of `f` at the residues
at `P` if the matrix is integral there, and zero otherwise. 

### `isSchwartzBruhat_liftFn`

 The composite of `h.liftFn f` with the map sending `T` to the entrywise image of `vecToMatrix T`
under `evalPlaces P` is a Schwartz–Bruhat function at `P`. 

### `isSchwartzBruhat_liftFn_mul`

 Let `P` hold one place of each conjugate pair above the prime `N`, all unramified of degree one
(`IsSplitLevel P N`). Let `f` be a function of matrices modulo `N`, and `h.liftFn f` the function of
matrices at `P` that is `f` of the reduction on integral matrices and zero elsewhere. For invertible
matrices `g` and `k` at `P`, the function `T ↦ h.liftFn f (k⁻¹ T g)` of finite adelic matrices, read
through their components at `P`, is Schwartz–Bruhat at `P`. 

### `pairWeilFinite_schrodingerOpAt`

 Let `P` hold one place of each conjugate pair above the prime `N`, all unramified of degree one
(`IsSplitLevel P N`). Let `Ψ = liftFn f` be `f` of the reduction modulo `N` on integral matrices at
`P` and zero elsewhere. Let `v` lie in the finite part of the Schwartz space of
`(stdSpace E n).hom (stdSpace E n')`, the matrices between the standard definite spaces, and let
`Ψ ⊗ v = schrodingerOpAt Ψ v` in the Schrödinger model at `P`. The Weil action `pairWeilFinite` with
characters `a`, `b` of the unitary elements above `N` with components `g`, `k` at `P` turns `Ψ ⊗ v`
into `(T ↦ Ψ (k⁻¹ T g)) ⊗ v`, times a scalar. The scalar is a quotient of values of
`detCharAt χ l : x ↦ χ (det x) |det x| ^ (-l / 2)`, for `χ = c.spaceChar l` the base change of `c`
divided by `υ ^ l`, with `υ` the splitting character: the value at `k` for `c = a`, `l = card n`,
over the value at `g` for `c = b`, `l = card n'`. 

### `detCharAt_inclGL`

 Let `P` hold one place of each conjugate pair above `N`, all unramified of degree one
(`IsSplitLevel P N`), and let the base change of `a` be unramified at every place of `P`. Let
`χ = a.spaceChar i` be this base change divided by the `i`-th power of the splitting character `υ`.
The character `detCharAt χ k: x ↦ χ (det x) |det x| ^ (-k / 2)` of the invertible matrices at `P` is
trivial on those that are invertible over the integers, which `inclGL` includes. 

### `norm_detCharAt_diagN_anti`

 Let `P` hold one place of each conjugate pair above the prime `N`, all unramified of degree one
(`IsSplitLevel P N`). The character `detCharAt χ k` is `g ↦ χ (det g) |det g| ^ (-k / 2)` over the
completions at `P`, and `h.diagN n S` is `diag (1, …, 1, N)` at `P ∩ S` and `1` at `P \ S`. For an
embedding `ι` of `ℂ` into `ℂ_[N]` and `k ≤ k'`, the `N`-adic size of `detCharAt χ k'` at this matrix
is at most that of `detCharAt χ k`, whatever the sizes of the two matrices. 

### `diagN_eq_sdiff_mul`

 The matrix `diag (1, …, 1, N)` at all of `P` is the product of those at `P \ S` and at `S`. 

### `exists_sub_residueOverN_mem_iff`

 Let `P` hold one place of each conjugate pair above the prime `N`, all unramified of degree one
(`IsSplitLevel P N`). An adele is integral at `P` if it lies in the integral adeles `Ô E` after
multiplication by `idem P`, the adele that is `1` at `P` and `0` elsewhere. If `N z` is integral at
`P`, then `z - y / N` is integral at `P` for exactly one class `y` modulo `N`, and otherwise for
none. 

### `star_residueOverN_mul_self`

 The finite adele `residueOverN y`, which is `y w / N` at each `w ∈ P` and `0` elsewhere,
multiplied on the left by its conjugate `star (residueOverN y)`, is zero. 

### `idem_add_star_eq`

 The idempotent of the places in `P` and their conjugates is that of the places in `S` and their
conjugates, both being the places above `N`. 

### `exists_sub_mem_and_sub_star_mem_iff`

 Let `P` and `S` each hold one place of every conjugate pair above the prime `N`, all unramified
of degree one (`IsSplitLevel`). Let `y / N = residueOverN y` run over the classes with simple poles
at `S`. Let `p` be `N` at `S` and `1` elsewhere, so that `N + 1 - p` is `1` at `S` and `N`
elsewhere. If `t p` and `(N + 1 - p) s` are integral at `P`, then `t - y / N` and `s - ȳ / N` are
both integral at `P` for exactly one class `y`; otherwise for none. 

### `sum_translate_eq_gluedDatum`

 Let `P` and `S` each hold one place of every conjugate pair above the prime `N`, all unramified
of degree one (`IsSplitLevel`); neither need contain the other. Translate the indicators of the
matrices integral at `P`, in the Schrödinger model at `P`, by `poleColumn` and `poleRow` (last
column `-y / N` at `S`, last row its conjugate). The products of their values at `T` and `R`, summed
over `y`, give `gluedDatum T' R'` at `T' = T diag (1, …, 1, N)_S` and
`R' = diag (1, …, 1, N)_{P \ S} R`. This is zero unless `T'` and `R'` are integral at `P`, and then
it is `ψ_N c`, where `c` is the residue modulo `N` at `P` of the entry of `R' T'` in the last row
and last column. Here `ψ_N c = ψ₀ (-c / N)` (`psiN`), with `ψ₀` the additive character
`stdLattice.selfDualAddChar E`. So the sum is supported on the pairs `(T, R)` that are integral at
`P` up to simple poles in the last column of `T` at `P ∩ S` and in the last row of `R` at
`P \ S`. 

### `doubleLiftGluing_eq_sum_schrodingerOpAt`

 **The glued datum in any model.** Let `P` and `S` each hold one place of every conjugate pair
above the prime `N`, all unramified of degree one (`IsSplitLevel`). Let `v`, `v'` be finite data of
`Hom (n + 1, n')` and `Hom (n', m + 1)`. Average each over the Heisenberg operators of the integral
vectors supported above `N` (`vacuumProjFinPart`), and apply `doubleLiftGluing`, the sum over `y`
modulo `N` at `S` of the translations by the last column `-y / N` and the last row `-ȳ / N`. The
result is given in the Schrödinger model at `P` by a sum over the vectors `z` modulo `N` at `P`.
Here `lastColDatum z` is the indicator of the matrices integral at `P` whose last column reduces to
`z` modulo `N`. The function `charDatum z` is zero off the integral matrices, and on these it is
`ψ_N (r ⬝ᵥ z)`, with `r` the reduction of the last row and `ψ_N c = ψ₀ (-c / N)` (`psiN`) for the
additive character `ψ₀ = stdLattice.selfDualAddChar E`. The matrices are first multiplied by
`hP.diagN n S` and `hP.diagN m (P \ S)`, which are `diag (1, …, 1, N)` at `P ∩ S` and at `P \ S`
respectively, and `1` at the other places of `P`. 


## Levels, spaces of forms and branching along the chain

* `New.Data.IsBranchingMap`: the properties of an integral branching matrix from `X_m` to `Y_m`.
  It intertwines the actions up to the character with exponents `New.Data.branchExponent`. Its
  operator norm is bounded, and over `ℂ` it spans the equivariant maps.

A weight is a pair `(κ, e)`: `κ τ h` counts the columns of height `h` of the diagram at `τ`, and
`e τ` is the power of the determinant (`New.weylRep`).


 ### The primes dividing `π` 

### `piNPlaces`

 The finite set of primes w of E dividing π = `D.piN`, the integer of E with π π̄ = N. 

### `star_mem_piNPlaces_iff`

 Of a place `w` above the prime `D.N` and its conjugate `star w`, exactly one lies in
`D.piNPlaces`, that is, divides the integer `D.piN` of E. 

### `isSplitLevel_piNPlaces`

 The primes `D.piNPlaces` dividing `π = D.piN`, the integer of `E` with `π π̄ = N`, are split of
degree one above `N = D.N` (`IsSplitLevel`): none is conjugate to one of them, each has norm `N`,
and `N` is a uniformiser at each. 

### `card_piNPlaces`

 The number of primes of E dividing π = `D.piN` (the set `D.piNPlaces`) equals `D.f`, the number
of infinite places of E. 

 ### The level of stage `j` 

### `levelX`

 The level of stage j: elements of the chosen level `New.Data.chosenLevel` on X_j whose last row
is congruent to (0, …, 0, 1) modulo π. 

### `isLevel_levelX`

 The level of stage j is a level: it lies in `New.stdLevel` and is open. 

### `lastIndexEquiv`

 A chosen bijection between the finite index sets Y_m and `InitIndex m`, which have the same
cardinality. 

### `cast_diagramWeight_columnCount`

 For each `i`, the `i`-th row length of the diagram with `D.columnCount τ u` columns of each
height `u < n_{j+1}` (`New.diagramWeight`; `rankAt` gives the rank at `τ`) is row `i` of the diagram
`New.Data.liftDiagram` of lift `j + 1`. 

### `IsBranchingMap`

 The properties of a branching map from the Weyl module of the weight `μ(X_m)` to that of
`μ(Y_m)`. The weights have the column numbers `D.columnCount` and `D.columnsY`, and both have the
determinant exponents `D.lastEntry D.m`. 

### `IsBranchingMap.mul_weylRep`

 Over every field of characteristic zero, `br` takes the action of `y = diag (g, z)` to
  `∏ τ, z τ ^ n_τ` times the action of `g`, where `n_τ = D.branchExponent τ` is the sum of the
  entries of `μ(X_m)` at `τ` less that of `μ(Y_m)`. 

### `IsBranchingMap.weylNormSq_le`

 The square of the operator norm of `br` is at most `exp (x ^ 70)`, with `x = D.x` the length
  of the prime sum. 

### `IsBranchingMap.spans`

 Every complex matrix that is equivariant for the elements `diag (g, 1)`, `g` unitary, is a
  multiple of `br`. 

### `exists_sum_columnsY_le_and_pow_le_exp`

 The weight on `Y_m` has `D.columnsY τ u` columns of height `u` at the infinite place `τ`. There
is a number `l` that bounds the boxes in the columns of height at least `k` and less than
`n_m - 1`, summed over `τ`, and satisfies `((l ^ l) ^ 3) ^ 2 ≤ exp (x ^ 70)`, with `x = D.x` the
length of the prime sum. 

### `exists_isBranchingMap`

 There is an integer matrix `br` from the Weyl module on `X_m` to that on `Y_m` that is a
branching map (`IsBranchingMap`). It is equivariant for the block matrices `diag (g, z)` up to the
character `∏ τ, z τ ^ n_τ`, where `n_τ = D.branchExponent τ` is the sum of the entries of the weight
on `X_m` at `τ` less that on `Y_m`. The square of its operator norm is at most `exp (x ^ 70)`, with
`x = D.x` the length of the prime sum. Over `ℂ` it spans the maps that are equivariant for
`diag (g, 1)`, `g` unitary. 

### `branching`

 A fixed branching map `br` from the Weyl module of `μ(X_m)` to that of `μ(Y_m)`. 

### `classAut_levelX_zero_eq_bot`

 The level of stage 0 is free: for the group `Γ` of rational points and this level `K`, the
groups `Γ ∩ g K g⁻¹` are trivial. 

 ### Source forms and smooth forms 

### `SourceForm`

 The space of source forms: algebraic forms on X_0 of weight (`D.columnCount`, `D.lastEntry 0`)
(column numbers, determinant exponents) fixed by the level `New.Data.levelX` of stage 0. 

### `FormX`

 The space of smooth algebraic forms on X_j of weight (`D.columnCount`, `D.lastEntry j`): column
numbers and determinant exponents. 

 ### Restriction of forms from `X_m` to `Y_m` 

### `borderU`

 The homomorphism g ↦ diag(g, 1) from the finite adelic unitary group on Y_m to that on X_m,
relabelling along `New.Data.lastIndexEquiv`. 

### `restrictToY`

 The restriction of algebraic forms from X_m to Y_m: restrict to points diag(h,1), apply the
branching matrix, and multiply by ∏_τ τ(π̄)^{−n_τ}, τ read as its embedding in the CM type. 


## Kernels of the lifts of source forms, translated data and combinations of chains

* `New.Data.liftKernel`: the kernel of lift j + 1, built from `New.thetaKernel`.
* `New.Data.Translations`, `New.Data.translateDatum`: tuples of translations, and the translated
  vacua they define.
* `New.Data.restrictedChain`: a combination of chains with such data, restricted to `Y_m`.


### `isLiftWeight_columnCount`

 The column numbers `D.columnCount` and determinant exponents `D.lastEntry j` form a lift weight
(`IsLiftWeight`) from `X_j = D.X j` to `X_{j+1}` along the exponent ⌊n_{j+1} / 2⌋ - κ_{j+1}. That
is, n_j < n_{j+1}, and no column has a height strictly between n_j and n_{j+1}. Also,
`D.lastEntry j τ` is this exponent plus the number of columns of height n_j at `τ`. 

### `homX`

 The hermitian space Hom(X_j, X_{j+1}) of the standard definite spaces on the index sets X_j
and X_{j+1}. 

### `liftKernel`

 The theta kernel of lift j + 1, for a character ϑ of U(1)(𝔸) of weight 0 with given tame part
(`New.Data.TameChar`). It goes from forms on X_j to forms on X_{j+1}, and its level on X_j is
`D.levelX j`. Its two characters are the twists `New.rankTwist`, by the ranks of X_j and X_{j+1}, of
`D.chainChar ϑ (j + 1)`, the product of `D.untwistedLiftChar (j + 1)` and ϑ^{j+1}. Derivatives are
scaled by π_M times the period `P.jetScale D.towerExp`, where π_M is the conjugate of the integer
`D.piMBar` of K of norm `D.M`. 

### `Translations`

 Tuples (x_j) of finite adelic matrices with rows X_{j+1} and columns X_j, the translations
that define the data of a chain. 

### `translateDatum`

 The j-th datum of the tuple x: the normalised vacuum `New.Parameters.intVacuum` of Hom(X_j,
X_{j+1}) translated by the finite Heisenberg operator of x_j. 

### `chainCombination`

 The linear map ∑_x Ψ(x)·C_x from algebraic forms of stage 0 to stage j, where C_x is the chain
(`New.chain`) of j theta lifts with data Φ x. 

### `restrictedChain`

 The combination `Ψ` of the chains of `m` lifts whose data are translates of the integral vacuum,
followed by the restriction to `Y_m`. The composite lift of a chain datum has this form, with `Ψ`
obtained by expanding its glued tensor (`IsChainDatum.exists_isWeakChainDatum_compositeLift_eq`). 

### `m_eq_two_mul_varrho_add_two`

 The number of lifts satisfies m = 2ϱ + 2, where ϱ = `New.Data.ϱ` is ⌊m/2⌋ − 1 truncated at
zero; so m is even and at least 2. 


## Chain data

A chain datum is a finitely supported function `Ψ` on tuples of translations, with conditions on
denominators, integrality and size, whose glued tensor `Glue φ♭` is jointly invariant. Here `φ♭` is
the combination `Ψ` of translates of the integral vacuum, and `Glue` applies to each double lift a
sum of translates with simple poles above `N` (`gluedDoubleLiftDatum`).


### `gluedDoubleLiftDatum`

 The gluing for the double lift `X_{2i} → X_{2i+1} → X_{2i+2}`: the sum `doubleLiftGluing` of the
translates of `v (2 i) ⊗ v (2 i + 1)`, with simple poles at the places `w ∣ π` in the first factor
and at their conjugates in the second. 

### `admissibleTranslations`

 The tuples of translations that become integral at all places prime to `q` after multiplication
by the conjugate of `D.piM`. 

### `ChainTensor`

 Tensors of finite data for the chain `X_0 → ⋯ → X_m`, grouped by double lifts. 

### `ChainTensor.IsInvariant`

 A tensor is jointly invariant if the levels of `X_0, …, X_{m-1}` fix it under the Weil actions
for `ϑ`, with the identity on `X_m`. 

### `gluedVacuum`

 The tensor of the translates of the integral vacuum by `t`, glued in each double lift. 

### `plainTensor`

 The tensor `φ♭ = ∑ x, Ψ x • ⊗ⱼ translateDatum x j`. 

### `gluedTensor`

 The glued tensor `φ^ch = Glue φ♭`, with `Glue` applied to each term of `φ♭`. 

### `supportedTranslations`

 The tuples of translations that vanish at all places prime to `q`. 

### `IsChainDatum`

 `Ψ` is a chain datum for the twist `ϑ`, a character of weight 0 whose tame part is non-trivial
exactly at the places of the finite set `ϑ.Q`. Let `q` be the product of their norms and `M` the
principal level `D.M`. The translations in the support of `Ψ` vanish at the places prime to `M q`
and lie in `admissibleTranslations q`; the values of `Ψ` are integral away from `q`, with
denominator `1`; if `ϑ.Q` is empty, then `∑ x, |σ (Ψ x)| ≤ M ^ (3 f m n_m²)` for every automorphism
`σ` of `ℂ`; and the glued tensor is jointly invariant. 

### `IsChainDatum.isInvariant`

 The glued tensor is jointly invariant. 

### `IsChainDatum.mem_admissibleTranslations`

 The translations in the support of a chain datum for `ϑ` are admissible for the norm of its
set `Q` of places: times the conjugate of `D.piM` they are integral away from that norm. 

### `restrictToYOfEq`

 The restriction map `restrictToY` on forms on `X_l`, for a number `l` equal to `m`. 

### `restrictToYOfEq_apply`

 At `F l` with `l = m`, the map `restrictToYOfEq` takes the value `restrictToY (F m)`. 

### `chainOfTensor`

 The chain of double lifts of a form on `X_0`, as a linear function of the tensor of data. 

### `compositeLift`

 The composite lift: the chain of double lifts with the glued tensor of `Ψ` as data, followed by
the restriction of forms from `X_m` to `Y_m`. 

### `IsWeakChainDatum`

 A weak chain datum: the coefficients `Ψ` of a jointly invariant sum of translates of the
integral vacuum. The conditions are those of a chain datum, but there is no gluing, the translations
need not vanish anywhere and may have denominators above `N`, and the size is at most
`exp (D.x ^ 60)` if `ϑ.Q` is empty. For a chain datum, both `φ♭` and the expansion of `Glue φ♭` have
this form. 

### `IsWeakChainDatum.isJointlyInvariant`

 The tensor `∑ x, Ψ x • ⊗ⱼ translateDatum x j` is jointly invariant. 
