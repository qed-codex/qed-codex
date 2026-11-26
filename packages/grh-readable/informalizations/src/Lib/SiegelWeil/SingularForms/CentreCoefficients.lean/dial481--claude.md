---
{
  "module": "src/Lib/SiegelWeil/SingularForms/CentreCoefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/SingularForms/CentreCoefficients.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/SingularForms/CentreCoefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fourier coefficients along the centre of a unipotent radical and their partial means

This file studies the Fourier coefficients `New.Space.Splitting.centreCoeff` of a continuous
function f on the adelic unitary group of W that is left invariant under the rational points. The
coefficients are taken along the centre of the unipotent radical of the stabiliser of an isotropic
frame. The splitting `A` splits off a hyperbolic plane with isotropic vectors u, u', `B` splits off
a frame of p vectors from its complement, and `D` splits off the image k of that frame in W. The
shifts n₊(a), n₋(b) move u and u' along k. The file studies the partial mean f⁺ of the coefficient
along `D` at a p×p matrix T over the shifts n₋(b), and the function φ⁺_g(a) = f⁺(n₊(a) g).
Exchanging u and u' gives f⁻ and φ⁻_g; the functions φ⁺_g and φ⁻_g behave like a function and its
Fourier transform. The file also defines equivariant lifts of local data and representability at the
infinite places for comparing theta integrals.

## Main definitions and results

* `New.Exchange.IsEquivariantLift`: a linear map from local data at `𝔠.ramifiedPlaces` to functions
  on the unitary group of `X`, sending a given submodule of Schwartz–Bruhat functions to automorphic
  functions.
* `New.Space.Splitting.lineShift`, `New.Space.Splitting.partialMean`,
  `New.Space.Splitting.shiftedMean`: the shifts n₊(a), the partial mean f⁺ and the function φ⁺_g.
* `New.Space.Splitting.centreCoeff_eq_mul_of_shiftedMean_eq_smul`,
  `New.Space.Splitting.shiftedMean_symm_eq_smul`: for det T ≠ 0, a relation φ⁺_{g'} = c φ⁺_g passes
  to the coefficients along `D` at the points n₋(b) n₊(a) g and to φ⁻.
* `New.Space.Splitting.partialMean_radicalElement_mul`: singularity. Let f⁺ be invariant under the
  shears at a nonempty set of finite places (`New.Space.Splitting.ShearInvariant`) at all points
  that fix e·k for an adele e (`New.Space.Splitting.frameStabilizer`). Then f⁺(h g) = f⁺(g) for h in
  the adelic radical of the stabiliser of the line of u, whenever g and h g fix e·k. The proof
  compares f⁺ with `New.Space.Splitting.borderedCentreCoeff`.

Notions from other files:
* `New.Space`: A hermitian space with a point: a matrix J over E and x in GL_n(𝔸) with xᴴJx equal to
  diag(s) at the infinite places and 1 at the finite places; `W.Γ` is the group of rational points
  x⁻¹ U(J)(E) x in the adelic unitary group `New.G`.
* `New.Space.Splitting`: a decomposition W = (lE^p ⊕ kE^p) ⊥ iW₀ with dual isotropic frames l, k.
* `New.Space.Splitting.radicalCentre`: z(M) = 1 + k(M − M*)k*ε (ε the standard form), an element of
  the centre of the unipotent radical of the stabiliser of the frame k.
* `New.Exchange.SplitTameChar`: a character of [U(1)] of a given weight, positive at every infinite
  place, with tame part non-trivial exactly on a non-empty finite set S of places disjoint from its
  conjugate.
* `New.Space.Splitting.comp`: From splittings of V over V₀ (rank p) and V₀ over V₁ (rank q), the
  splitting of V over V₁ with frames (k, ik'), (l, il') and embedding ii'.



## Laws of the Fourier coefficients along the centre of the radical

In this section `H` is the splitting and `D` the function.


### `_root_.New.Exchange.IsAutFunction`

 D is a continuous function on the adelic unitary group of W that is left invariant under the
rational points. 

### `isContPeriodic_radicalCentre`

 If D is continuous and left invariant under the rational points, then M ↦ D (z(M) g) is
continuous and periodic under rational matrices, z(M) being the element `H.radicalCentre M` of the
centre of the radical. 

### `centreCoeff_mul_right_sub_smul`

 Let D and D' be continuous and left invariant under the rational points. The coefficient at T
of D(· Y) − c D' at the point g is that of D at g Y minus c times that of D' at g. 

### `centreCoeff_add`

 The coefficient at T is additive on functions that are continuous and left invariant under the
rational points. 

### `continuous_centreCoeff`

 For D continuous and left invariant under the rational points, its Fourier coefficient at T
along the centre of the radical, the mean of ψ(tr TM) D(z(M) g) over M modulo rational matrices, is
a continuous function of g. 

### `centreCoeff_radicalCentre_mul`

 For D continuous and left invariant under the rational points, left translation by
z(M) = `H.radicalCentre M` divides the coefficient at T by ψ(tr TM), ψ the standard additive
character. 

### `centreCoeff_rat_mul`

 For D continuous and left invariant under the rational points, a rational point γ that acts on
the isotropic frame k of H through the rational matrix c (γ k = k c) carries the coefficient at T to
the coefficient at cᴴ T c. 

### `centreCoeff_rat_mul_of_actsOnFrame_one`

 For D continuous and left invariant under the rational points, a rational point that fixes the
isotropic frame of H does not change the coefficient at T. 


## Equivariant lifts of local data and forms represented at infinite places
Definitions for the comparison of theta integrals attached to a tamely ramified character `𝔠`, with
set of ramified places `𝔠.ramifiedPlaces`; `New.LocProd P` is the product of the completions of E at
the finite places in P.


### `componentsAt`

 The ring map sending an adele to its components at the ramified places S of 𝔠. 

### `_root_.New.atPlaces`

 The homomorphism G_f → GL_n(∏_{w∈P} E_w) sending an element to its components at P. 

### `IsEquivariantLift`

 Let X be a hermitian space with index type m, let S = `𝔠.ramifiedPlaces` be the ramified places
of the character 𝔠, and let M be a space of functions of m × b matrices over the completions at S. A
linear map 𝒟 from such functions to functions on U(X) is an equivariant lift on M if M consists of
locally constant functions with compact support in the left invertible matrices, and on M the map 𝒟
has automorphic values, is equivariant at S up to a character of the determinant, and has values
right invariant under the elements of `stdLevel` with component 1 at S. 

### `IsEquivariantLift.le_schwartzBruhat`

 The data in `M` are locally constant, with compact support in the left invertible matrices. 

### `IsEquivariantLift.isAutFunction`

 `𝒟 Ψ` is continuous and left invariant under the rational points of `U(X)`. 

### `IsEquivariantLift.map_translate`

 For `g` supported on `S ∪ S̄`, the translate `Φ y = Ψ (g_S y)` lies in `M`, and `𝒟 Φ`,
  translated on the right by `g`, is `𝒟 Ψ` divided by `(υ |·|^(1/2)) (det g_S) ^ card b`. 

### `IsEquivariantLift.invariant_off`

 `𝒟 Ψ` is right invariant under the elements of `stdLevel` that are `1` at `S`. 

### `atRealPlace`

 The complex matrix of components of the adelic matrix x at the infinite place v. 

### `RepresentedBy`

 An adelic b × b matrix T is represented by the signs t if at every infinite place its component
has the form cᴴ diag(t) c for some complex matrix c. 

### `gram_atRealPlace`

 For an adelic matrix x and an infinite place v with component x_v (`atRealPlace x v`), the Gram
matrix x_vᴴ diag(s) x_v is the component at v of xᴴ ε x, where ε = `stdForm E s` is the standard
form with signs s. 


## Coordinates of opposite and composite splittings

A splitting `H : W.Splitting W₂ p` consists of dual isotropic frames `k`, `l` of p vectors and an
embedding of the orthogonal complement `W₂`. Below, `A : W.Splitting W₀ Unit` splits off one line,
`B : W₀.Splitting W₂ p` splits `W₀`, and `A.comp B` is the splitting of `W` whose frame is the line
of `A` followed by the frame of `B`.


### `comp_lCoord`

 For the composite of the splittings A of W and B of the complement W₀, the coordinate
`lCoord` (which reads off the coefficients of the dual frame l) has the block rows of A and of B,
the latter after the projection `A.iCoord` to W₀. 


## Shifts of an isotropic line and partial means

The splitting `A` splits off a hyperbolic plane with isotropic vectors u (its frame) and u' (the
frame of `A.symm`), and the frame k of `D` is the image in W of the frame of `B`. The shifts
n₊(a) = `A.lineShift B a` and n₋(b) = `A.symm.lineShift B b` move u and u' along k. Each statement
about `A` has a second form for `A.symm`, with the two signs exchanged.


### `frameStabilizer`

 For an adele e, the group of the points g that fix e·k, where k is the frame of D. If e is an
idempotent, these are the points that fix the frame at the places where e is 1. 

### `lineShift`

 The shift n₊(a) : u ↦ u − k aᴴ of the isotropic vector u of A by the image k in W of the frame
of B. Here a is an adelic row. It is a central element of the radical for the splitting
`A.symm.comp B`. 

### `actsOnFrame_lineShift`

 The shift n₊(a) carries the frame (u, k) of the composite of A and B, k the image in W of the
frame of B, to (u − k aᴴ, k). 

### `partialMean`

 The partial mean f⁺(g): the mean, over the adelic rows b modulo the rational rows, of the
coefficient of f along D at T at the point n₋(b) g, where n₋(b) = `A.symm.lineShift B b`. The
partial mean for `A.symm` is f⁻. 

### `shiftedMean`

 The function φ⁺_g(a) = f⁺(n₊(a) g) of an adelic row a, where f⁺ is the partial mean and
n₊(a) = `A.lineShift B a`. The function for `A.symm` is φ⁻_g. 

### `exists_centreCoeff_ne_zero`

 If the partial mean f⁺ is not zero at g, then the coefficient of f along D at T is not zero at
some point n₋(b) g. 

### `lCoord_eq_lCoord_mul_iCoord`

 If the frame of D is the image of the frame of B, the coordinate `D.lCoord` is that of B after
the projection to the complement W₀. 

### `actsOnFrame_lineShift_one`

 If the frame of D is the image of the frame of B, the shifts n₊(a) fix it. 

### `lineShift_mul_lineShift_symm`

 Let the frame of `D` be the image under `A` of the frame of `B` (`hD`), and for adelic rows a, b
let n₊(a) = `A.lineShift B a` and n₋(b) = `A.symm.lineShift B b` be the shifts of the two isotropic
vectors of `A` by the frame of `D`: n₊(a) is u ↦ u − k aᴴ on the vector u, and n₋(b) does the same
for the other vector. Then n₊(a) n₋(b) = z(−aᴴ b) n₋(b) n₊(a), where z = `D.radicalCentre`
parametrises the centre of the unipotent radical of the stabiliser of the frame of `D`. 

### `centreCoeff_lineShift_symm_mul_lineShift`

 Let the frame of D be the image of the frame of B and let f be automorphic. The coefficient
along D at T at the point n₋(b) n₊(a) g is ψ(−tr T aᴴ b) times that at n₊(a) n₋(b) g. 

### `isContPeriodic_centreCoeff_lineShift`

 If the frame of D is the image of the frame of B and f is automorphic, then the coefficient of f
along D at T at the point n₊(a) g is a continuous function of a, periodic under rational rows. 

### `continuous_partialMean`

 If the frame of D is the image of the frame of B and f is automorphic, the partial mean f⁺ is
continuous. 

### `partialMean_add`

 If the frame of D is the image of the frame of B, the partial mean is additive on automorphic
functions. 

### `partialMean_lineShift_symm_mul`

 If the frame of D is the image of the frame of B and f is automorphic, the partial mean f⁺ is
left invariant under all shifts n₋(b). 

### `partialMean_radicalCentre_mul`

 Let the frame of D be the image of the frame of B and let f be automorphic. Left translation by
the element z(M) of the centre of the radical for D divides the partial mean f⁺ by ψ(tr TM). 

### `shiftedMean_lineShift_mul`

 Replacing g by n₊(a) g translates φ⁺_g by a. 

### `shiftedMean_symm_lineShift_mul`

 Replacing g by n₊(a) g multiplies φ⁻_g(b) by ψ(−tr T aᴴ b), for f automorphic and the frame of D
the image of the frame of B. 

### `shiftedMean_rat_add`

 Let the frame of D be the image of the frame of B and let f be automorphic. For a rational row
a₀, the value φ⁺_g(a₀ + a) is the Fourier coefficient at −T a₀ᴴ of the function that sends b to the
coefficient of f along D at T at the point n₋(b) n₊(a) g. 

### `centreCoeff_eq_mul_of_shiftedMean_eq_smul`

 Let the frame of D be the image of the frame of B, f automorphic and det T ≠ 0. If
φ⁺_{g'} = c φ⁺_g, then the coefficient of f along D at T at each point n₋(b) n₊(a) g' is c times
that at n₋(b) n₊(a) g. 

### `shiftedMean_symm_eq_smul`

 Let the frame of D be the image of the frame of B, f automorphic and det T ≠ 0. If
φ⁺_{g'} = c φ⁺_g, then φ⁻_{g'} = c φ⁻_g. 

### `centreCoeff_eq_zero_of_shiftedMean_eq_zero`

 Let the frame of D be the image of the frame of B, f automorphic and det T ≠ 0. If φ⁺_g is zero,
then the coefficient of f along D at T is zero at g. 

### `shiftedMean_symm_eq_zero`

 Let the frame of D be the image of the frame of B, f automorphic and det T ≠ 0. If φ⁺_g is zero,
then so is φ⁻_g. 


## Singularity of the partial mean

Invariance under the shears at a nonempty set of places spreads, by strong approximation for the
additive group, first to the centre of the radical for `A` and then to the whole radical.


### `ShearInvariant`

 For an adele e and a point g, the condition that the partial mean f⁺ takes the same value at g
and ν g for every shear ν, that is, every ν with matrix 1 + ē·uc − e·a. Here u = `A.kAdelic` is the
isotropic vector of A, c is a row with cu = 0, and a is arbitrary. If e is the idempotent of a set
of places U disjoint from its conjugate, such a ν is 1 + uc on Ū and 1 outside U ∪ Ū. 

### `borderedCentreCoeff`

 The Fourier coefficient of f along the composite of the splittings A (one line) and B, at the
block diagonal matrix 0 ⊕ T. 

### `radicalCentre_comp_fromBlocks`

 If the frame of D is the image of the frame of B, the central element for the composite of A and
B with blocks z, b, c, N is the product of the central element for D at N, the shift n₋(b − cᴴ) and
the central element for A at z. 

### `borderedCentreCoeff_eq_quotMean`

 Let `A` split one hyperbolic plane off `W` over `W₀`, `B` split `p` planes off `W₀` over `W₂`,
and `D` split `p` planes off `W` over `W₁`. Let the frame of `D` be the image under `A` of the frame
of `B` (`hD`), and let `f` be automorphic. Then the coefficient of `f` along the composite of `A`
and `B` at `0 ⊕ T` is the mean, over the centre of the radical for `A`, of the partial mean f⁺. Here
f⁺(g) is the mean over adelic rows `b` modulo rational rows of the coefficient of `f` along `D` at
`T` at `n₋(b) g`. 

### `actsOnFrame_radicalCentre_one`

 If the frame of D is the image of the frame of B, the centre of the radical for A fixes it. 

### `ShearInvariant.partialMean_radicalCentre_mul`

 Let the frame of `D` be the image under `A` of the frame of `B` (`hD`), let `f` be automorphic,
`T` a p×p matrix over E and `U` a nonempty set of finite places, and let f⁺(x) be the mean, over
adelic rows b modulo rational rows, of the Fourier coefficient of `f` along `D` at `T` at
`A.symm.lineShift B b * x`. If f⁺ takes the same value at `g` and at νg for every shear
ν = 1 + ē·uc − e·a (e the idempotent adele of `U`, u = `A.kAdelic`, cu = 0), then
f⁺(`A.radicalCentre z * g`) = f⁺(g) for every adelic 1×1 matrix `z`. 

### `ShearInvariant.borderedCentreCoeff_eq`

 Let the frame of D be the image of the frame of B, let f be automorphic and U a nonempty set of
finite places. If the partial mean f⁺ is invariant at g under the shears for U, then f⁺(g) is the
coefficient of f along the composite of A and B at 0 ⊕ T. 

### `borderedCentreCoeff_radicalElement_mul`

 Let the frame of D be the image of the frame of B, let f be automorphic, T a p×p matrix over E
and U a nonempty set of finite places. Let f⁺(g) be the mean over adelic rows b, modulo rational
ones, of the coefficient of f along D at T at n₋(b) g. Suppose f⁺ is invariant at all points z g,
for z in the adelic centre of the radical for A, under the shears for U: the ν with matrix
1 + ē·uc − e·a, where e is the idempotent of U, u the isotropic vector of A and cu = 0. Then the
coefficient of f along the composite of A and B at 0 ⊕ T is invariant at g under the elements
`A.radicalElement c z` of the adelic radical for A. 

### `partialMean_radicalElement_mul`

 Singularity. Let the frame of D be the image of the frame of B, let f be automorphic, T a p×p
matrix over E, U a nonempty set of finite places and e an adele. Let f⁺(g) be the mean over adelic
rows b, modulo rational ones, of the coefficient of f along D at T at n₋(b) g. Suppose f⁺ is
invariant under the shears 1 + 1̄_U·uc − 1_U·a for U (1_U the idempotent of U, u the isotropic
vector of A, cu = 0) at all points that fix e·k, k the frame of D. If g and h g fix e·k, for
h = `A.radicalElement c z` in the adelic radical of the stabiliser of the line of A, then
f⁺(h g) = f⁺(g). 
