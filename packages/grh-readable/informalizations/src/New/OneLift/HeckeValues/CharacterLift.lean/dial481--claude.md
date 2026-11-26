---
{
  "module": "src/New/OneLift/HeckeValues/CharacterLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/CharacterLift.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/CharacterLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The lift of a character from U(1): kernel, descent and Galois conjugates

Let `χ` be a character of `U(1)` over the adeles. Its lift is the algebraic form `φ` on the standard
definite space `V` of rank `card n` that is the sum, over the classes of `U(1)` at the level of
the chosen places, of the theta kernel formed with `χ` and the block datum. It is a multiple of the
theta lift of the constant function `1`. This file defines `φ`, computes its inner products through
the descent from `V` to the line, and shows that a Galois conjugate of `φ` is, up to simple factors,
the lift of the conjugate character.

## Main definitions and results

* `New.LValueData`: the chosen places and the places of the twist, the row lengths `rowLength τ`
  and the character `u1Char` of `U(1)`. `New.LValueData.descentPair` is the descent datum
  (`New.DescentPair`) whose source `W` is the definite line and whose weight has one row of length
  `rowLength τ` at `τ`.
* `New.LValueData.kernelForm`: the theta kernel at a finite point `g` of `U(1)`, as a form on `V`;
  the lift `New.LValueData.trivialLift` is its class sum over `U(1)`.
* `New.LValueData.theta_pairThetaKernel_omega_fockDatum`: the pairings of the kernel with vectors of
  the weight are theta values of Fock vectors.
* `New.LValueData.normalizedDescent_eq_inner_kernelForm`, `New.LValueData.inner_trivialLift`: the
  descent `New.DescentPair.normalizedDescent` of a form is its inner product with the kernel, so the
  inner product with the lift is the class sum of the descent.
* `New.DescentPair.heckePolyOnForms_liftHeckeRoot_eq_zero`: the Hecke polynomial
  `New.DescentPair.heckePolyOnForms`, evaluated at the number `New.DescentPair.liftHeckeRoot`,
  annihilates every form with the Hecke polynomials of a lift
  (`New.DescentPair.HasLiftHeckePolynomial`).
* `New.LValueData.map_trivialLift`: the Galois conjugates of the lift.

Notions from other files:

* `New.DescentPair`: a descent datum, that is places, a hermitian space `W` of rank less than
  `card n`, two weights and a character; `New.DescentPair.FormV` is the space of algebraic forms on
  `V` of its weight and level, and `New.DescentPair.blockDatum` is the block datum on `Hom(W, V)`
  times the vacuum.
* `Gf E n`, `stdLevel E n`: the finite adelic points of the unitary group of `V` and their integral
  subgroup; `levelOf w H` is the level of elements of `stdLevel` that reduce into `H` at the places
  `w`.
* `classSum Γ K f`: the weighted sum of `f` over `Γ \ G / K`; `stdClassSum` takes `Γ` rational.
* `schurJet κ`: the jets of a power series along the Schur matrix of the weight `κ`.

## Relation to the literature

Known; see `Lib.SiegelWeil.RallisInner.SharpData` for sources.

The sections "The lift and the descent" and "The parameter of the line and a Hecke operator" set
up, for the data `New.LValueData`, steps of the known expression of critical Hecke L-values of CM
fields as squared norms of theta lifts from U(1).



## The lift and the descent

The lemmas `New.LevelPlaces.LevelForm.inner_eq_petersson` and
`New.LValueData.hookNumber_eq_prod_factorial` give constants in the norm of the lift.


### `LevelPlaces.LevelForm.inner_eq_petersson`

 On a standard space `V` with signs `s`, let `l` be twice the Harish-Chandra parameter of the
weight `(κ, e)`. Let the residue group `H` be a group of families of invertible matrices over the
residue fields at the places `placeAt i`, for `i` in the index set `ChosenIndex ⊕ TwistIndex` of
the chosen places and the places of the twist; the level `levelOf S.placeAt H` is the group of
elements of `stdLevel E n`, the stabilizer of the standard lattice in the finite adelic unitary
group, that reduce into `H`. Let `φ`, `φ'` be algebraic forms of weight `(κ, e)` on which the level
acts by `χ`. Their inner product is the weighted sum, over the double cosets of the rational points
and the level, of the Gram pairings of their values. It equals the index of the level in
`stdLevel E n`, times the dimension `card (WeylIndex n κ)` of the weight, times the Petersson
product of `ofAlgForm l s φ` and `ofAlgForm l s φ'`, the functions on the adelic unitary group that
belong to the forms. 

### `nonempty_unit_embedding`

 The one-point type `Unit` embeds in every non-empty type. 

### `arbitraryIndexEmbedding`

 For non-empty `n`, an arbitrary embedding of the one-point type `Unit` into `n`, that is, an
arbitrary index. 

 ### The data and the theta kernel 

### `LValueData`

 Data for a lift from `U(1)` to the definite unitary group of rank `card n > 1`: two finite
families of finite places (`New.LevelPlaces`), the chosen places, which give the level, and the
places of the twist; row lengths `rowLength τ`; and a character of weight
`-(rowLength τ + ⌊card n / 2⌋)` whose tame part is trivial off these places. 

### `LValueData.rowLength`

 The length of the one row of the weight at `τ`; it is the order of the derivatives taken. 

### `LValueData.u1Char`

 The character of `U(1)` over the adeles that enters the lift. 

### `LValueData.tamePart`

 The tame part of `u1Char`: a character of the residue field at each finite place. 

### `LValueData.hasWeight`

 `u1Char` has weight `-(rowLength τ + ⌊card n / 2⌋)` at `τ` and tame part `tamePart`. 

### `LValueData.one_lt_card`

 The rank `card n` is at least `2`. 

### `LValueData.unramified`

 The tame part is trivial off `toLevelPlaces.places`, the places of the two families. 

### `descentPair`

 The descent datum (`New.DescentPair`) attached to `X`: the source `W` is the standard definite
line, and the weight has one row of length `rowLength τ` at each `τ`. 

### `descentPair_colsPlus_apply`

 At the place `τ` the weight `colsPlus` of `X.descentPair` has `rowLength τ` columns of height
one and no column of any other height. 

### `kernelValue`

 The vector of derivatives, for the one-row weight of `X` and with variables scaled by `c`, of
the theta function of the datum `ω(g, h) f`, for a finite point `(g, h)` of `U(1) × U(n)`. 

### `isLiftWeight`

 The weight `X.descentPair.columnCount` with exponent `0` in rank `1` goes up to rank `card n`
along the exponent `-rowLength τ` (`New.IsLiftWeight`): it has no column of height strictly between
`1` and `card n`, `1 < card n`, and its `rowLength τ` columns of height `1` make up the difference
of the two exponents. 

### `charW_hasWeight`

 The character `X.descentPair.charW`, the power of the splitting character of the Weil
representation whose exponent is the number of negative signs of the source, has trivial tame part
and weight `X.descentPair.detExp`, the exponent of the determinant in the weight on `V`. The source
is definite and the weight has no `colsMinus`, so both exponents are `0`. 

### `charV_hasWeight`

 The character `X.descentPair.charV`, which is `X.u1Char` times the power `⌊card n / 2⌋` of
`WeilData.upsilonU1`, has weight `-rowLength τ` at each infinite place `τ` and tame part
`X.tamePart`. 

### `liftKernel`

 The theta kernel `New.thetaKernel` between the standard spaces of ranks `1` and `card n`, for
the weight and the characters of `X`, with derivatives scaled by `1`. As a `New.Kernel` it is an
action of the finite points of both groups on Schwartz functions, with a jet map to vectors of the
weight, of exponent `0` in rank `1` and `detExp` in rank `card n`. The subgroup `⊤` is the level
at which its lifts would integrate. 

### `conjWeylRep_eq_one`

 Every point `x` of the archimedean unitary group `GInf E X.descentPair.signs` of the definite
line acts trivially: `conjWeylRep` of the weight `X.descentPair.columnCount` with exponent `0` sends
`x` to `1`. 

 ### The kernel as a form on `V`, and the lift 

### `kernelForm`

 For a finite point `g` of `U(1)`, the function `h ↦ X.kernelValue 1 f g h` as an algebraic
form on the standard space `V` of rank `card n`. Here `f = X.descentPair.blockDatum` is the block
datum at the places of `X` times the vacuum. 

### `chosenLevel`

 The principal level of the finite adelic U(1) at the places `chosenPlace`: integral elements
that reduce to 1 at each of these places. 

### `trivialLift`

 The lift of the character of `X`: the class sum of the kernel `New.LValueData.kernelForm` over
`U(1)` at the principal level at the chosen places. It is a multiple of the theta lift of the
constant function `1`. 

### `kernelForm_invariant`

 Let `X` be data for a lift from `U(1)`. The theta kernel `X.kernelForm` is a function from the
finite adelic points `g` of `U(1)` to algebraic forms on the definite space of rank `card n`. It is
invariant under rational points on the left and, on the right, under `X.chosenLevel`, the integral
points that reduce to `1` at the places `X.chosenPlace`, one of the two finite families of places
in `X`. 

### `trivialLift_eq_stdClassSum_translate`

 Let `X` be data for a lift from `U(1)`, and let `z` be a finite adelic point of `U(1)`. The lift
`X.trivialLift` is the weighted sum (`stdClassSum`) of the theta kernel `g ↦ X.kernelForm g` over
the double cosets of the rational points and `X.chosenLevel`, the group of integral points that
reduce to `1` at the chosen places. It is also the weighted sum of the translated kernel
`g ↦ X.kernelForm (g * z)` over the same double cosets. 

 ### Adjointness of the lift and the descent 

### `toPoly_eq_rename_fockPoly`

 Let `X` be data for a lift from `U(1)`, and let `η` be a coordinate vector of the Weyl module
whose weight, that of the descent datum `X.descentPair`, has one row of length `X.rowLength τ` at
each infinite place `τ`. The polynomial `toPoly (fun _ ↦ n) _ η`, with rows indexed by `n` at every
place, is `∑ i, (G η) i • b i`, for the Gram matrix `G` and the basis `b` of products of minors. It
is obtained from the Fock polynomial `X.descentPair.fockPoly η` by renaming the variable at the
place `τ`, row `a` and the one column `u` to the variable with row index `⟨τ, a⟩` and column `0`. 

### `fockPoly_eq_schurCoeffPoly`

 The Fock polynomial of a coordinate vector `η` for the weight `κ` of `X.descentPair` is the
matrix coefficient `z ↦ (ηᵀ G) S_κ(z) 1` (`New.schurCoeffPoly`) of the Schur matrix `S_κ`, where
`G = weylGramOver` is the Gram matrix of the weight. 

### `theta_pairThetaKernel_omega_fockDatum`

 Let `X` be data for a lift from `U(1)`. The space `X.descentPair.W.hom (stdSpace E n)` is
`Hom(W, V)`, for the standard definite spaces `W` of rank `1` and `V` of rank `card n`; `Space.θ` is
its theta functional and `ω` the Weil action of `U(W) × U(V)` on its Schwartz space. The vector
`X.descentPair.fockDatum η` is the Fock vector of the polynomial `fockPoly η` at the infinite
places, tensored with the finite datum `blockDatum`: the function `residueBlockDatum` of the
residues at the places of `X`, and the vacuum at the other finite places. The theta value of its
image under `ω((x, g), (y, h))` is the bilinear pairing, by the Gram matrix, of `η` with the vector
`X.kernelForm g h` moved by `y⁻¹`. The value does not depend on the real point `x` of `U(1)`. 

### `kernelForm_of_rowLength_eq_zero`

 Let `X` be data for a lift from `U(1)` with all row lengths `0`, so that the weight is trivial
and no derivative is taken. Then every coordinate of the vector valued theta kernel
`X.kernelForm g h` is the value of the scalar theta kernel `modKernel W V a b 𝔪 Ψ P`, the function
`(g, h) ↦ θ (ω(g, h) f)` for the datum `f` made of a function `Ψ` on matrices modulo `𝔪` and the
Fock vector of a polynomial `P`, at the adelic points `(1, g)` and `(1, h)` with trivial real parts.
The characters that twist `ω` are `a = 1` and `b = X.descentPair.charV`, which is `X.u1Char` times
the power `⌊card n / 2⌋` of the character `WeilData.upsilonU1`, and `P = 1`. The modulus
`𝔪 = X.levelModulus 2` is the square of the product of the chosen places times the product of the
places of the twist. The function `Ψ` reduces a matrix at each of these places (`levelResidueAt`)
and applies `residueBlockDatum`: this is `0` unless the reductions at the chosen places are the
basis vector `incl ()`, and then the product, over the places of the twist, of the tame characters
at the entry in the row `incl ()`. 

### `kernelForm_eq_vectorKernelForm`

 The form `X.kernelForm g` is the kernel `New.DescentPair.vectorKernelForm` of the pair
`X.descentPair` at the point `(x, g)` of `U(1)`, for every real component `x`. 

### `normalizedDescent_eq_inner_kernelForm`

 The descent `New.DescentPair.normalizedDescent` of a form `y` on `V`, at the point `(x, g)` of
`U(1)`, is the inner product of the kernel `X.kernelForm g` with `y`. 

### `inner_trivialLift`

 For a form `y` on `V` and a finite point `z` of `U(1)`, the inner product of the lift
`X.trivialLift` with `y` is the class sum over `U(1)`, at the principal level at the chosen places,
of `g ↦ θ y (g z)`, where `θ` is the descent `New.DescentPair.normalizedDescent`. 

 ### The hook number of the weight 

### `hookNumber_eq_prod_factorial`

 The hook number (the Fock pairing of the highest weight polynomial with itself) of the weight
`κ` of `X.descentPair`, in rank `card n` at every place, is the product of the `(rowLength τ)!`. 

### `schurJet_jetSeries_eq_kernelForm`

 Let `X` be data for a lift from `U(1)`, with row lengths `X.rowLength τ`. Let `pairWeil` be the
Weil action `ω` of `U(1) × U(n)`, twisted by `charW` and `charV`, and let `blockDatum` be the
finite datum that is given by residues at the places of `X` and is the vacuum elsewhere. The jet
series `jetSeries _ c f` is the Taylor series `F` of the theta function of `f` in the variable
multiplied by `c`, and `schurJet κ F` is the matrix of the `P(∂) F` at `0`, for `P` the entries of
the Schur matrix of the weight `κ`. For `f = ω(g, h) blockDatum` its row sums are
`c ^ ∑ τ, X.rowLength τ` times the coordinates of `X.kernelForm g h`, the row sums at `c = 1`. 

 ## The parameter of the line and a Hecke operator 

### `LValueData.isHCParam_zero`

 On a line, the weight of `X.descentPair` with determinant exponent `0` has the Harish-Chandra
parameter `0`. 

### `LValueData.fitsParams_descentPair`

 Let `X` be data for a lift from `U(1)`. Its descent datum `X.descentPair` goes from the standard
positive definite space `W` of rank `1` to the standard space `V` of rank `card n`, with a weight
that has one row at each infinite place. The parameter `0` on `W` fits this datum. It corresponds
under the block rule to `paramV`, twice the Harish-Chandra parameter of the weight of the forms on
`V`. The index `numbering` of the one basis vector of `W` is `0`, its position in the order by the
parameter. The partitions `colsPlus` and `colsMinus` have no column higher than the number of basis
vectors of `W` with sign `1` and `-1`. 

### `DescentPair.heckePolyOnForms_liftHeckeRoot_eq_zero`

 Let `O` be a descent datum from a space `W` of rank `card r` to the standard space `V` of rank
`card n`, and let `w` be a split place of norm `q` with `w` and `star w` off the places of `O`. Let
`y` be an algebraic form on `V` of the weight and level of `O` (`O.FormV`) with the Hecke
polynomials of a lift of the eigensystem `z`: at such places `y` is spherical, and its Hecke
polynomial is `∏_{l < t} (1 - q ^ l ν T)` times a rescaled Hecke polynomial of rank `card r` with
eigenvalues `z w`, where `t = card n - card r` and `ν = O.charW.frobValue r w`. Then the operator
`O.heckePolyOnForms hw hw_level T = ∑_i (-T) ^ i q ^ (i (i - 1) / 2) T_{w,i}` annihilates `y` at
`T = O.liftHeckeRoot w = (ν q ^ (t - 1))⁻¹`, the zero of the factor with `l = t - 1`. 


## Galois conjugates of the lift

With no places of the twist and even rank, a conjugate of the lift is, up to simple factors, the
lift of the conjugate character. The semilinear map that conjugates Taylor series of theta
functions is moved past the Weil operators; on the block datum it acts by a central element, which
only permutes the classes of `U(1)`.


### `schurJet_rename_perm`

 Let `κ τ j` be the number of columns of height `j` of a partition at the index `τ : Φ`, and let
this weight `κ` fit the ranks `1` and `card n`. For a power series `F` in the entries of columns
`z τ` of size `n`, the matrix `schurJet κ F` has the entries `P(∂) F` at `0`, for `P` the entries of
the Schur matrix `schur κ z`. Let `e` be a permutation of `Φ`. If the variables of `F` are renamed
along `e.symm`, this matrix for `κ` is that of `F` for the weight `κ ∘ e.symm`, with rows and
columns permuted by `e`. 

### `onHom_mul_scalarFin_inv`

 In `U(1) × U(n)` acting on matrices `n × 1` (`G.onHom`), right translation of `g` by the scalar
`z⁻¹` of `U(1)` is right translation of the image of `(g, h)` by the scalar `z`. 

### `stdLineHom`

 The space `Hom(W, V)` from the standard line `W` to the standard space `V` of rank `card n`;
its signs `homSigns 1 1`, the products of those of `W` and `V`, are all `1`. 

### `LValueData.map_pairWeilFinite_blockDatum`

 Let `L` be a `σ`-semilinear map on the Schwartz space of `stdLineHom`, the space `Hom(W, V)` of
columns for the standard spaces `W`, `V` of ranks `1` and `card n = 2 * m`. Let `L` scale finite
translations by `b`. Let `X` be data for a lift from `U(1)` with no places of the twist; `X.u1Char`
is its character of adelic `U(1)`. For a Schwartz–Bruhat function `Ψ` at the places of `X`, let
`schrodingerOp X.places Ψ` be the combination of Heisenberg operators that realizes `Ψ` in the
Schrödinger model, and let `vacElem` be the vacuum. For every such `Ψ` let `L` send
`schrodingerOp X.places Ψ vacElem` to `l ω(z)` applied to the same vector for `σ ∘ Ψ`. Let `Y` be
data with the places of `X` whose character agrees with `σ ∘ X.u1Char` on finite points. Let `g` and
`h` be finite points of `U(1)` and `U(n)`. Let `f = X.descentPair.blockDatum` be the block datum: at
the chosen places the indicator of the columns that reduce to a fixed basis vector, and the vacuum
elsewhere. Then `L` carries `ω(g, h) f`, for the Weil action `ω` of the pair, to a multiple of the
same vector for `Y` at `(g z⁻¹, h)`. The factor is the product of `l`, the value at `z⁻¹` of
`Y.descentPair.charV`, and `multiplierRatio σ = σ Δ / Δ`, for the multiplier `Δ` of the Weil
representation, at the finite component of `x ↦ h x`, the image of `(1, 1, h)` under `G.onHom`. 

### `LValueData.map_trivialLift`

 Conjugates of the lift. The parameters `P` and the natural number `s` give the CM field `P.E s`
over the imaginary quadratic field `K P`, the positive number `P.bigOmega s` and the scale
`P.jetScale s` at which Taylor series of theta functions are taken. Fix places `S` of `P.E s` with
no places of the twist (`S.TwistIndex` is empty), and `σ ∈ Gal(ℂ/K P)`. Data `X : LValueData` on
`S` add row lengths `X.rowLength τ` at the infinite places and a character `X.u1Char` of adelic
`U(1)`. The lift `X.trivialLift` is the class sum over `U(1)` of the theta kernel of `X`; its value
at a finite point `h` of `U(n)` is a vector of the Weyl module of the one-row weight, with
coordinates `i` indexed by a basis tableau `i τ` at each `τ`.

There are constants `t`, `l` and `u` with `‖t‖ = (√(P.bigOmega s))⁻¹` and `l ≠ 0` such that the
following holds for all data `X` on `S` with `card n = 2 * m`. Let `e = placePerm s σ`, the
permutation of the infinite places by `σ`. Let `μ` be a character of weight
`-(X.rowLength (e⁻¹ τ) + card n / 2)` at each infinite place `τ`, with tame part `ψ` trivial off the
places, and `μ v = σ (X.u1Char v)` at finite points `v`. Let `Y` be the data on `S` with character
`μ` and row lengths `X.rowLength (e⁻¹ τ)`. Put `D = ∑ τ, X.rowLength τ`. The conjugate under `σ` of
the `i`-th coordinate of `P.jetScale s ^ D • X.trivialLift` at `h` is the product of `t ^ D`, `l`
and three more factors. The first is the value at `u` of `Y.descentPair.charV`, which is `μ` times
the `m`-th power of the character `WeilData.upsilonU1`. The second is
`multiplierRatio σ = σ Δ / Δ`, for the multiplier `Δ` of the Weil representation, at the finite
component of the map `x ↦ h x` on columns, the image of `(1, 1, h)` under `G.onHom`. The third is
the coordinate of the lift of `Y` at `h` with index `τ ↦ i (e⁻¹ τ)`. 
