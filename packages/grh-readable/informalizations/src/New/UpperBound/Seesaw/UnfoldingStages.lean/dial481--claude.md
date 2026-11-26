---
{
  "module": "src/New/UpperBound/Seesaw/UnfoldingStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Unfolding the chain of lifts: double lifts and the functions of the unfolding

A double theta integral over two definite unitary groups is a coefficient of the composite of two
lifts. Two unfolding steps give the double lift of the finite evaluation. Starting from `𝒲_φ`, each
unfolding step then gives an equivariant function on the next group `R_j`. Their supports are
bounded when the source form is ramified.

## Main definitions and results

* `New.Seesaw.DoubleLiftData.exists_integral_constTermAtStringMap_mul_eq`: take the product of two
  constant terms. Integrate it over the Bessel subgroup `New.Grading.besselGroup` of `Y'`, and over
  that of `Y` against an equivariant function `W`. The result is an integral over the unitary group
  of `X`. Its integrand is `W` times a constant times a theta integral over the unitary group of
  `X'`. The theta integral is of the datum translated by `New.Seesaw.stackedStringMap` and cut down
  along `New.Seesaw.DoubleLiftData.splitting`.
* `New.Data.unfoldStage`: the function `𝒲_{k+1}` that the first `k + 1` unfolding steps leave;
  `New.Data.exists_unfoldStage_eq_algFormCoeff` evaluates it after each double lift.
* `New.Data.hasLatticeBounds_of_unfoldStage_ne_zero`: the support lemma, in terms of graded
  lattices.

Notions from other files:
* `New.Grading`: A presentation of a hermitian space as a definite part `X` (grade 0) plus a string
  of `s` graded basis vectors; `Y.inclX` embeds the unitary group of `X`.
* `New.Seesaw.DoubleLiftData`: For gradings `Y, Y', Y''` of `V, V', V''`, it identifies the
  grade-zero part of V⁻ ⊕ V'' with X⁻ ⊕ X'' plus hyperbolic planes.
* `New.Space.Splitting.zeroTerm`: For a splitting with frames `i`, `k`, the map that sends a datum f
  to y ↦ the mean of f(i y + k b) over adelic vectors b modulo rational ones.
* `New.Seesaw.flipSum`: For hermitian spaces V and V'', the orthogonal sum V⁻ ⊕ V'' of V with its
  form negated and V''.
* `New.Seesaw.stackedStringMap`: The adelic map (T*, T') from V' to V⁻ ⊕ V'', where
  `T = Y.stringMap Y'` and `T' = Y'.stringMap Y''`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work. See
`Lib.Weil.CompactLift.DefiniteThetaLift` for sources.



## Two unfolding steps and the double lift of the finite evaluation

Notation as in `New.UpperBound.Seesaw.EdgePairEvaluation`. `D : New.Seesaw.DoubleLiftData X'' q Y Y'
Y''` describes three graded spaces `V, V', V''` with definite parts. `New.Seesaw.arrowProduct` joins
data on `Hom (V, V')` and `Hom (V', V'')`, and `New.Seesaw.tripleWeil` is the joint Weil action.
`New.stdSpace E X` is the standard definite space on `X`, and `(stdSpace E X).quotMeasure`
integrates over its unitary group modulo rational points. `New.Grading.constTermAtStringMap` is the
constant term at the map `Y.stringMap Y'` along maps of positive degree. `New.algFormCoeff 1 t φ` is
the coefficient of an algebraic form `φ` at a linear form `t`.


### `integrable_algFormCoeff_mul_theta_tripleWeil`

 A coefficient of an algebraic form times the theta function of a triple Weil translate is
integrable over the compact quotients of the two definite unitary groups. 

### `arrowProduct_integrated_polyVector`

 Write `P ⊗ Φ` for `integrated` applied to the Fock vector `polyVector P` and the finite datum
`Φ`. Combining with `arrowProduct` the data `P ⊗ Φ` on `Hom(X, X')` and `Q ⊗ Φ'` on `Hom(X', X'')`,
for polynomials `P` and `Q`, gives the datum `P Q ⊗ arrowTensor (Φ ⊗ Φ')` on `Hom(X', X⁻ ⊕ X'')`.
The variables of `P` are transposed into the block of `X`, and those of `Q` go into the block of
`X''`. 

### `integral_theta_tripleWeil_eq_lift_comp`

 Write U(X) for the adelic unitary group of the standard definite space `stdSpace E X`, and
`flipSum` for the sum X⁻ ⊕ X'' of X with its form negated and X''. Let the families `k`, `k'`
compute the theta lifts of algebraic forms from `X` to `X'` and from `X'` to `X''` (`IsThetaLift`)
for the characters `rankTwist (a o)` and `rankTwist (b o)`, the twists of the automorphic characters
`a o`, `b o` of U(1) by a power of a fixed character that depends on the rank. Let `L o` be the
composite lift, which sends `Φ ⊗ Φ'` to `k' o Φ' ∘ k o Φ`. For every vector `u` of the Fock space of
`Hom(X', X⁻ ⊕ X'')` and every linear form `t` there is a linear form `t''` with the following
property for all `o`, finite data `y`, forms `φ` and points `g` of U(X''). Carry `y` to
`Hom(X', X⁻ ⊕ X'')` by `arrowTensor`, tensor it with `u` (`integrated`), and move it by `(x, r, g)`
under the Weil action `tripleWeil (a o) (b o)` of U(X) × U(X') × U(X''). Integrate its theta value
over `r`, and then over `x` against the coefficient of `φ` at `t`, both modulo rational points. The
result is the coefficient of `L o y φ` at `t''`, taken at `g`. 

### `DoubleLiftData.constTerm_mul_constTerm_eq_inv_mul_zeroTerm`

 Let `Y, Y', Y''` be gradings of the hermitian spaces `V, V', V''`, and let `D` be data for two
consecutive lifts. The constant term `Y.constTerm Y'.gradeOf f w` is the mean of the theta function
of `f`, Heisenberg translated by `w` (`homHeisenbergOp w`), over the maps `V → V'` that raise
grades. The datum `arrowProduct f f'` on `Hom(V', V⁻ ⊕ V'')` joins `f` and `f'`, where `V⁻` is `V`
with its form negated; by `hθ` its theta value is `z ≠ 0` times the product of those of `f` and
`f'`. The splitting `D.homZeroPart.splitting` cuts `Hom(V', V⁻ ⊕ V'')` down to its part of degree
zero, and its zero term is the mean over the maps of positive degree. Then the product of the
constant terms of `f` at `w` and of `f'` at `w'` is `z⁻¹` times the value at 0 of the zero term of
the join of the two translates. 

### `formAdjoint_fromRows`

 The adjoint of a map (A, B) into V⁻ ⊕ V'' is (−A*, B*). 

### `DoubleLiftData.exists_add_eq_homAtPoint_stackedStringMap`

 Let `D` be data for the two consecutive lifts `Y → Y' → Y''`, and let `n` be a unipotent element
of U(V'), with matrix `V'.ratCoordMatrix n` in rational coordinates. Let
`S = stackedStringMap Y Y' Y''` be the map (T*, T') from V' to V⁻ ⊕ V'' made of the maps `T`, `T'`
between consecutive strings. As a vector of `Hom(V', V⁻ ⊕ V'')` in adelic coordinates
(`homAtPoint`), the map `S (n - 1)` is a sum of two parts. The first is a map of positive degree,
with entries `y`. The second is a map of degree zero that sends `X'` into an isotropic half of the
hyperbolic planes indexed by `q`. Its matrix is `Y'.genericConst`, the constant of the grading,
times the block of `n - 1` whose rows are the basis vectors `D.gradeOne` of grade one and whose
columns are `X'`. 

### `formAdjoint_stackedStringMap_mul_stackedStringMap`

 The stacked map `stackedStringMap Y Y' Y''` = (T*, T'), with `T = Y.stringMap Y'` and
`T' = Y'.stringMap Y''`, is isotropic. Its `formAdjoint` for `flipSum V V''` times it is -T T* + T'*
T' = 0: given the double-lift data `D`, both products depend only on `Y'` and the common constant
`genericConst`. 

### `constTermAtStringMap_unipotent_mul_right`

 In the second argument `h` of `constTermAtStringMap`, a unipotent `n` in `Y'.unipotent` moves
into the map at which `constTerm` is taken: `Y.stringMap Y'` is multiplied on the left by the matrix
of `n⁻¹` in rational coordinates. 

### `constTermAtStringMap_unipotent_mul_left`

 For `n` in `Y.unipotent`, `Y.constTermAtStringMap Y' α f (n * g) h` is `Y.constTerm` for the
weights `Y'.gradeOf` of `twistedPairWeil α (g, h) f` at `Y.stringMap Y' * V.ratCoordMatrix n`: the
factor `n` moves into the point of the constant term, on the right. 

### `mul_constTermAtStringMap_unipotent_mul`

 For odd `s` and `W` equivariant for `Y` (left translation by unipotents acts by a character),
the product of `W` and the constant term at `Y.stringMap Y'`, with the characters `rankTwist a`, is
invariant under the unipotent group of `Y`: the two characters cancel. 

### `DoubleLiftData.zeroTerm_stackedStringMap_planes`

 Let `D` be data for the two consecutive lifts `Y → Y' → Y''`. Let `n` be a unipotent element of
U(V'), with matrix `V'.ratCoordMatrix n` in rational coordinates, and put `T = Y.stringMap Y'`,
`T' = Y'.stringMap Y''`. Join `f` and `f'` to the datum `arrowProduct f f'` on `Hom(V', V⁻ ⊕ V'')`;
by `hθ`, its theta value is `z ≠ 0` times the product of those of `f` and `f'`. Translate this datum
by the map `stackedStringMap Y Y' Y''` = (T*, T'). Then take the zero term along
`D.homZeroPart.splitting`, which is the mean over the maps of positive degree. Evaluate the result
at the map from `X'` to an isotropic half of the hyperbolic planes indexed by `q`. Its matrix is
`Y'.genericConst` times the block of `n - 1` whose rows are the basis vectors `D.gradeOne` of grade
one and whose columns are `X'`. Then `z⁻¹` times this value is the product of the constant terms of
`f` at `n⁻¹ T` and of `f'` at `T' n`. 

### `DoubleLiftData.exists_integral_constTermAtStringMap_mul_eq`

 Let `Y, Y', Y''` be gradings of the hermitian spaces `V, V', V''` over `E` with definite parts
`X, X', X₀`, and let `D` be data for two consecutive lifts. There is a constant `z` with the
following property. Let `a`, `b` be automorphic characters of U(1), which normalise the two Weil
actions; let `f`, `f'` be data on `Hom(V, V')` and `Hom(V', V'')`, and `k` a point of U(X₀). Let `W`
be a continuous function on the Bessel (Fourier–Jacobi) subgroup of `Y`, invariant under rational
points and equivariant for the unipotent character (`Y.IsEquivariant W`). Let `F g r` be `W g` times
the constant terms of the Weil translates of `f` by `(g, r)` and of `f'` by `(r, Y''.inclX k)`. The
integral of `F` over the Bessel subgroups of `Y` and `Y'` is the integral over `g` in U(X) of
`W (Y.inclX g)` times `z` times a theta integral over `r` in U(X'), all modulo rational points. Its
datum is made from the join `arrowProduct f f'` on `Hom(V', V⁻ ⊕ V'')`: translate by
`stackedStringMap Y Y' Y''`, the map V' → V⁻ ⊕ V'' along the strings; cut down to
`Hom(X', X⁻ ⊕ X'')` by the mean over the isotropic part of `D.splitting` (`zeroTerm`); and act by
`(g, r, D.embX k)` under the joint Weil action `tripleWeil a b`. 

 ## The functions produced by the unfolding 

### `inclXFin_mem_chosenLevel`

 The embedding `inclXFin` of the finite points of `U(X_k)` in those of `U(Y_k)` maps the level
`D.levelX k` into the level `D.chosenLevel`. 

### `movedDatum`

 The datum of lift `k + 1` (`New.Data.datumY`) moved by the outer variable `g_k = (ξ k, y k)`,
which acts on `Y_k`. 

### `twistedPairWeil_movedDatum`

 The action of `(g, h)` on the moved datum of lift `k + 1` is that of `(g * g_k, h)` on the
original datum, where `g_k = (ξ k, y k)`. 

### `constTermAtStringMap_movedDatum`

 In the constant term `constTermAtStringMap` of the moved datum at `(g, g' * a)`, the point `a`
may be moved into the datum: it is the constant term at `(g, g')` of `datumY` acted on by
`(g_k, a)`, where `g_k = (ξ k, y k)`. 

### `unfoldStageOn`

 The function on `R_k` that enters step `k + 1` of the unfolding: `𝒲_φ` for `k = 0`, and
`γ ↦ 𝒲_k (γ g_k)` with `g_k = (ξ k, y k)` for `k > 0`. 

### `unfoldStage`

 The function `𝒲_{k+1}` on `U(Y_{k+1})` that the first `k + 1` unfolding steps leave. 

### `unfoldStageOn_succ`

 On `R_{k+1}`, the Bessel group of `D.gradingY (k + 1) hk`, the function `unfoldStageOn` of the
unfolding is `γ ↦ 𝒲_{k+1} (γ g_{k+1})`, where `𝒲_{k+1}` is `unfoldStage` at `k` and
`g_{k+1} = (ξ (k + 1), y (k + 1))`. 

### `unfoldStageOn_update`

 For `k < l`, the function `unfoldStageOn` on `R_k` does not change when the points `ξ l` and
`y l` of stage `l` are replaced by any `a` and `b`. 

### `unfoldStage_update`

 The function `𝒲_{k+1}` (`unfoldStage`) depends only on the outer variables `g_j = (ξ j, y j)`
for `j ≤ k`: changing `ξ` and `y` at an index `l > k` does not change it. 

### `isEquivariant_unfoldStageOn`

 The function `unfoldStageOn` on the Bessel group `R_k` of `D.gradingY k hk` is equivariant under
the unipotent character and invariant under the rational points (`New.Grading.IsEquivariant`). 

### `fixesLeft_ratBessel_unfoldStage`

 The function `𝒲_{k+1}` is invariant on the left under the rational points of `R_{k+1}`, the
Bessel group of `Y'`. 

### `integral_unfoldStageOn`

 Fix a tame character `ϑ`, a source form `φ` on U(X_0) with a linear form `t` on its values, and
adelic points `g_k = (ξ k, y k)` of the unitary groups U(Y_k). Let `Y'` be a grading of `Y_{k+1}`
with a string of length `2 ϱ + 1 - (k + 1)`, and let `𝒲_{k+1}` be the function `unfoldStage` on
U(Y_{k+1}) that `k + 1` unfolding steps leave, the last one with `Y'`. Let `z` be automorphic and
rapidly decreasing on U(Y_{k+1}). Take the theta lift of `z` to U(Y_k) with the datum `datumY ϑ k`
on `Hom(Y_k, Y_{k+1})` and the Weil action `twistedPairWeil` normalised by the character
`D.chainChar ϑ (k + 1)`, and translate the lift on the right by `g_k`. Its integral against the
function `unfoldStageOn` of the previous stage, over the Bessel group `R_k` of `D.gradingY k` modulo
rational points, is the integral of `𝒲_{k+1} z` over U(Y_{k+1}) modulo the rational points
`Y'.ratBessel` of the Bessel group of `Y'`. The latter integral converges absolutely. 

### `exists_zeroTerm_eq_integrated`

 Let `R` be data for the two lifts `Y_{2i} → Y_{2i+1} → Y_{2i+2}`, the last space with the
grading `Y`. Suppose that the linear map `D.doubleLiftEvalY i` on finite data is `R.finEval`, the
finite analogue of the translation and zero term below. Fix archimedean points `ξ k` of U(Y_k) and
`x` of U(Y_{2i+2}). Move the data `datumY` of lifts `2 i + 1` and `2 i + 2` under the Weil action by
`(ξ k, y k)` for `k = 2 i, 2 i + 1` and by `(x, y (2 i + 2))`. Join them (`arrowProduct`), translate
by the map `stackedStringMap` along the strings, and cut down to
`Hom(X_{2i+1}, X_{2i}⁻ ⊕ X_{2i+2})` by the mean over the isotropic part of `R.splitting`
(`zeroTerm`). The result is a pure tensor (`integrated`) of a vector `v` of the Fock space,
independent of the tame character `ϑ` and the finite points `y`, and of `evaluatedDatum ϑ y i`, the
value of `D.doubleLiftEvalY i` on the finite factors, carried to this space by `arrowTensor`. 

### `exists_unfoldStage_eq_algFormCoeff_of_sourceFn`

 A double unfolding step. Let `R` be data for the two lifts `Y_{2i} → Y_{2i+1} → Y_{2i+2}`, the
last space with a grading `Y` of definite part `X`. Suppose that `D.doubleLiftEvalY i`, the linear
map that turns finite data for the spaces `Y_k` into finite data for their definite parts `X_k`, is
the map `R.finEval` of `R`. Fix archimedean points `ξ k` of U(Y_k) and `x` of U(Y_{2i+2}), and a
linear form `l` on the values of algebraic forms on U(X_{2i}). There is a linear form `l''`,
independent of `ϑ`, `t`, `φ`, `y` and `ψ`, with the following property. Suppose the function
`unfoldStageOn` on the Bessel group of the grading of `Y_{2i}` is `sourceFn l ψ`. This is the
function that is equivariant for the unipotent character and equals the coefficient
`algFormCoeff 1 l ψ` of the form `ψ` on U(X_{2i}). Then for `g` in U(X), the value of `𝒲_{2i+2}` at
`Y.inclX g * (x, y (2 i + 2))` is the coefficient at `l''` of `Θ ψ`, taken at the image `R.embX g`
of `g` in U(X_{2i+2}). Here `Θ` is the composite (`liftInPairs`) of the theta lifts
`X_{2i} → X_{2i+1} → X_{2i+2}`, with kernels `D.liftKernel ϑ` and datum `evaluatedDatum ϑ y i`. 

### `exists_unfoldStageOn_even_eq_sourceFn`

 At an even stage `2 i` there is a linear form `l`, independent of the tame character `ϑ`, the
source form `φ` and the finite points `y`, such that the function `unfoldStageOn` that `2 i`
unfolding steps leave on the Bessel group `R_{2i}` is `sourceFn l (Θ φ)`: it is equivariant for the
unipotent character and equals the coefficient of `Θ φ` at `l` on U(X_{2i}). Here `Θ` is the
composite `doubleLiftChain` of the first `i` pairs of theta lifts between the definite spaces `X_k`,
with kernels `D.liftKernel ϑ` and finite data `evaluatedDatum ϑ y`. 

### `exists_unfoldStage_eq_algFormCoeff`

 Let `R` be data for the two lifts `Y_{2i} → Y_{2i+1} → Y_{2i+2}`, the last space with a grading
`Y` of definite part `X`. Suppose that `D.doubleLiftEvalY i`, the linear map that turns finite data
for the spaces `Y_k` into finite data for their definite parts `X_k`, is the map `R.finEval` of `R`.
Fix a linear form `t` on the values of source forms and archimedean points `ξ k` of U(Y_k) and `x`
of U(Y_{2i+2}). There is a linear form `l`, independent of `ϑ`, `φ` and `y`, such that for `g` in
U(X) the value of `𝒲_{2i+2}` (`unfoldStage`) at `Y.inclX g * (x, y (2 i + 2))` is the coefficient
`algFormCoeff 1 l (Θ φ)` of `Θ φ` at `l`, taken at `R.embX g`. Here `Y.inclX` and `R.embX` map U(X)
to U(Y_{2i+2}) and to U(X_{2i+2}), and `Θ` is the composite `doubleLiftChain` of the first `i + 1`
pairs of theta lifts between the spaces `X_k`, with kernels `D.liftKernel ϑ` and finite data
`evaluatedDatum ϑ y`. 

### `liftWeilFin_pointDatumY`

 Elements of the levels at `Y_k` and `Y_{k+1}` fix the datum `pointDatumY ϑ k` of lift `k + 1` of
the lower chain. 

### `doubleLiftEvalY_inclXFin`

 The map `D.doubleLiftEvalY i` sends the join `arrowProduct Φ Φ'` of finite data `Φ`, `Φ'` on
`Hom(Y_{2i}, Y_{2i+1})` and `Hom(Y_{2i+1}, Y_{2i+2})` to a tensor of finite data on
`Hom(X_{2i}, X_{2i+1})` and `Hom(X_{2i+1}, X_{2i+2})`. If `2 i + 2 ≤ 2 ϱ + 1`, so that `Y_{2i+2}` is
graded by `D.gradingY`, it is equivariant for the finite points `u` of U(X_{2i+2}): acting on `Φ'`
by the image of `u` in U(Y_{2i+2}) before the map is acting by `u` on the second factor after it. 

### `liftWeilFin_translatedPointDatumY`

 If `z`, conjugated by `y (j + 1)`, lies in the level `levelY ϑ (j + 1)`, then `(1, z)` fixes the
translated datum `translatedPointDatumY ϑ y j` of lift `j + 1` under the finite Weil representation
`liftWeilFin` with the character `D.chainChar ϑ (j + 1)`. 

### `map_evaluatedDatum_of_conj_mem`

 Let `ϑ` be a tame character and `y k` finite points of U(Y_k). The tensor
`evaluatedDatum ϑ y i` is the finite datum of the two theta lifts `X_{2i} → X_{2i+1} → X_{2i+2}`.
Let `u` be a finite point of U(X_{2i+2}) whose image in U(Y_{2i+2}), conjugated by `y (2 * i + 2)`,
lies in `levelY ϑ`: it is integral and reduces to `1` at the chosen places and at those of `ϑ.Q`.
Then `(1, u)`, acting on the second tensor factor through the Weil action `ω` of the theta kernel
`D.liftKernel ϑ (2 * i + 1)`, fixes `evaluatedDatum ϑ y i`. 

### `evaluatedDatum_out`

 The evaluated data do not change if each `y k` is replaced by the chosen representative of its
class modulo the level `levelY ϑ k`. 

### `twistIdele`

 An idele that generates the ideal `Q`: the generator of `π_M Q` divided by that of `π_M`. 

### `valued_twistIdele`

 At the places of `ϑ.Q` the idele `twistIdele ϑ` has the valuation of a uniformiser, and at all
other places it is a unit. 

### `finHeisenbergOp_generator_smul_pointDatumY`

 The modulus `D.twistModulus ϑ 1` is the product of the chosen places and the places of `ϑ.Q`.
The finite datum `pointDatumY ϑ k` on `Hom(Y_k, Y_{k+1})` is the indicator function of the inclusion
matrix modulo it, and the vacuum at the other places. This datum is fixed by the Heisenberg
translation `finHeisenbergOp` by the generator of the modulus times any integral vector `x`. 

### `unfoldStage_eq_zero_of_scalingGenerator`

 Let `𝒲_{2j+2}` be the function `unfoldStage` on `U(Y_{2j+2})` built from a ramified source form
`φ`, the linear form `t` and the points `(ξ k, y k)` of U(Y_k). Let `w` be a place dividing
`π_N = D.piN`. View the chosen scaling `z_w = D.scalingGenerator w`, a finite adele of norm one, as
the point `inclXFin (scalarFin z_w)` of `U(Y_{2j+2})` that is the scalar `z_w` on the definite part
`X_{2j+2}` and the identity on the string. Suppose `x⁻¹ z_w x` lies in `levelY`: it is integral and
reduces to `1` at the chosen places and at those of `ϑ.Q`. Then `𝒲_{2j+2}` vanishes at `γ (a, x)`
for every `γ` in the Bessel group `R_{2j+2}` and every archimedean point `a`. 

### `map_stringMapFin_latticePlus_gradingY`

 For consecutive gradings `D.gradingY k` and `D.gradingY (k + 1)`, the finite string map
`stringMapFin` between them sends `latticePlus 1` of `Y_k` (the projection `Λ_k⁺` of the standard
lattice to the span of the string) onto `D.ideleA • latticeMinus 1` of `Y_{k+1}`, that is onto
`𝔞 Λ_{k+1}⁻`, where the idele `D.ideleA` generates `𝔞`. 

### `notMem_Q_of_mem_piNPlaces`

 A place `w` with `w` or its conjugate `star w` in `D.piNPlaces` (the places dividing `D.piN`) is
not among the places `ϑ.Q` of the tame character `ϑ`. 

### `unfoldStage_eq_zero_of_latticeSplitsAt`

 Let `𝒲_{2j+2}` be the function `unfoldStage` on `U(Y_{2j+2})` built from the character `ϑ`, a
ramified source form `φ`, the linear form `t` and the archimedean and finite points `(ξ k, y k)` of
U(Y_k). Let `w` be a place dividing `π_N = D.piN`, and let `x` be a finite point whose lattice `Λ'`
splits along `X_{2j+2}` at `w`: there the projection of `Λ'` to the span of the string lies in `Λ'`.
Then `𝒲_{2j+2}` vanishes at `γ (a, x)` for every `γ` in the Bessel group `R_{2j+2}` and every
archimedean point `a`. 

### `hasLatticeBounds_of_unfoldStage_ne_zero`

 **Support**. Let `j = k + 1 ≤ 2 ϱ + 1`, so that `D.gradingY j` presents the hermitian space
`Y_j` as a definite part `X_j` of grade zero plus a string of `2 ϱ + 1 - j` graded basis vectors.
Let `𝒲_j` be the function `unfoldStage` on U(Y_j) that `j` unfolding steps leave. It is built from a
tame character `ϑ` of modulus `ϑ.Q`, a source form `φ` on U(X_0) with a linear form `t` on its
values, and adelic points `(ξ i, y i)` of U(Y_i). Assume that `φ` is ramified and that `y 0` is
integral and reduces to `1` at the chosen places (`D.chosenLevel`). Suppose `𝒲_j (a, x) ≠ 0` for an
archimedean point `a` and a finite point `x`, and let `r'` be a finite point of the Bessel subgroup
of the grading such that the lattice `Λ'` of `r' x` is graded: it contains the part in each grade of
each of its vectors. Then `q̄ ^ j Λ⁻ ⊆ Λ'⁻` and `q ^ j Λ'⁻ ⊆ Λ⁻`. Here the idele `q = twistIdele ϑ`
generates the product of the places of `ϑ.Q`, `q̄` is its complex conjugate, `Λ` is the lattice of
`1` in `Y_j`, and `Λ⁻`, `Λ'⁻` (`latticeMinus`) are the intersections with the span of the string. 
