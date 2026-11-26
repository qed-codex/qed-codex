---
{
  "module": "src/Lib/Adelic/Reduction/FirstMinimumShortBases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/FirstMinimumShortBases.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/FirstMinimumShortBases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transference, first minima and short bases of lattices of hermitian spaces

Minkowski's bound and weak transference in a Euclidean space `E` of dimension `m` give short vectors
and a covering radius for a subgroup `Λ` whose dual has no nonzero vectors shorter than `ρ > 0`. For
a hermitian space `V` with a point, the lattice of `V` defines a first minimum, cut off at `1`, and
a height on the adelic unitary group, against which growth and decay are measured.

## Main definitions and results

* `New.weak_transference`: if `m ≥ 1`, `Λ` has a nonzero vector shorter than `2 m / ρ`.
* `New.weak_transference_covering_radius`: every vector is within `m ^ 2 / ρ` of `Λ`.
* `New.Space.archCoords`, `New.Space.firstMinimum`, `New.Space.height`: the archimedean coordinates
  of a rational vector, the first minimum of the lattice cut off at `1`, and the inverse of the
  first minimum of the moved space `V.move g`, the height at `g`.
* `New.Space.IsModerate`, `New.Space.IsRapid`: moderate growth and rapid decay against the height.
* `New.Space.form_eq_zero_of_norm_mul_lt_one`, `New.Space.firstMinimum_move_eq_one`,
  `New.Space.firstMinimum_pos`: lattice vectors whose lengths have product below `1` are orthogonal;
  the minimum is `1` in a definite space, and positive in any space as the lattice is discrete. The
  comparison of heights on `Γ g Ξ` for compact `Ξ` is `New.Space.exists_height_le_mul` in
  `Lib.Adelic.AutomorphicForms.Basic`.
* `New.Space.exists_short_basis`: the lattice contains a basis of vectors of length at most a
  constant over the first minimum.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over a CM field E (class
  `CMType E`) and x in GL_n(𝔸) with xᴴJx equal to diag(s) at the infinite places and 1 at the finite
  places; `V.move g` is (J, xg).
* `New.G`: the adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the
  identity matrix at the finite places.
* `New.Space.vecAtPoint`: for a space (J, x), the adelic coordinates x⁻¹y of a vector y in E^n.
* `New.Space.baseLattice`: for a space (J, x), the lattice E^n ∩ x_f Ô^n, as an additive subgroup of
  E^n.
* `New.Space.sum`: for spaces V, W with signs s, t, the space with concatenated signs whose matrix
  and point are the block diagonal sums of those of V and W.

## Relation to the literature

Known result: Transference theorem for the covering radius of a lattice against its dual's first
minimum. The constant here is m squared in dimension m, where the sharp forms have a constant linear
in m. The result holds for any subgroup of a Euclidean space whose dual has no short nonzero vector,
and is proved by projecting along a short vector. Source: Lagarias-Lenstra-Schnorr, Korkin-Zolotarev
bases and successive minima of a lattice and its reciprocal lattice, Combinatorica 10 (1990); sharp
forms in Banaszczyk, Math. Ann. 296 (1993), and Miller-Stephens-Davidowitz, Kissing numbers and
transference theorems from generalized tail bounds, SIAM J. Discrete Math. 33 (2019).

See also `Lib.Adelic.AutomorphicForms.Cuspidality` and `Lib.Adelic.Reduction.FiniteVolume`.



## Weak transference: Minkowski's bound and the covering radius

Geometry of numbers in a Euclidean space `E` of dimension `m`, for a subgroup `Λ` whose dual has no
nonzero vectors shorter than `ρ > 0`. This hypothesis forces `Λ` to span `E`, but `Λ` need not be
discrete.


### `minkowski_pow_le_abs_det`

 Minkowski's bound. If the nonzero vectors of the lattice spanned by a basis `b` of a Euclidean
space of dimension `m ≥ 1` have length at least `ρ > 0`, then its covolume `|det b|`, in the
coordinates of an orthonormal basis `o`, is at least `(ρ / √m) ^ m`. 

### `span_eq_top_of_le_norm_dual`

 A subgroup `Λ` of a Euclidean space spans the space if the nonzero vectors of its dual (the `y`
with `⟪y, x⟫ ∈ ℤ` for all `x ∈ Λ`) have length at least `ρ > 0`. 

### `weak_transference`

 Weak transference. Let `Λ` be a subgroup of a Euclidean space of dimension `m ≥ 1`. If the
nonzero vectors of its dual (the `y` with `⟪y, x⟫ ∈ ℤ` for all `x ∈ Λ`) have length at least
`ρ > 0`, then `Λ` has a nonzero vector of length less than `2 m / ρ`.

A consequence of Minkowski's convex body theorem. 

### `weak_transference_covering_radius`

 Covering radius. Let `Λ` be a subgroup of a Euclidean space of dimension `m`. If the nonzero
vectors of its dual (the `y` with `⟪y, x⟫ ∈ ℤ` for all `x ∈ Λ`) have length at least `ρ > 0`, then
every vector `u` lies within distance `m ^ 2 / ρ` of some vector of `Λ`.

Known result: the Lagarias–Lenstra–Schnorr transference theorem for the covering radius of a
lattice against its dual's first minimum, here with a weaker constant. 

### `span_norm_le_eq_top_of_covering`

 Short vectors span. If every vector of a finite-dimensional Euclidean space lies within distance
`r > 0` of a set `S`, then the vectors of `S` of length at most `3 r` span the space. 


## Dilations, first minimum, height, moderate and rapid functions

* `New.dilationGroup`: pairs `(g, c)` of a unitary matrix `g` and a unit `c` such that `g` scales
  the columns of a matrix `A` by `c` and satisfies `wᴴ J (g v) = wᴴ J v` for `v`, `w` orthogonal to
  `A`, that is, acts trivially on the orthogonal complement modulo its radical.


### `dilationGroup`

 The dilations along the columns of `A` for the form `J` (implicit, read from the type of the
unitary group `U J`): the pairs `(g, c)` in `U J × Rˣ` such that `g` is the scalar `c` on the
columns of `A` and `wᴴ J g v = wᴴ J v` whenever `Aᴴ J v = 0` and `Aᴴ J w = 0`. The test objects `v`,
`w` are square matrices, standing for families of vectors orthogonal to the columns of `A`. 

### `archCoords`

 The additive map sending y ∈ E^n to the archimedean components of x⁻¹y (`V.vecAtPoint y`), with
x the point of V, as a vector in a Euclidean space indexed by the infinite places and `n`. Its norm
is the length of y. 

### `latticeBall`

 The set of vectors `y` of the lattice `V.baseLattice` whose length `‖V.archCoords y‖` is at most
`r`. 

### `firstMinimum`

 The first minimum cut off at 1: `λ = min(1, inf ‖y‖)`, where `y` runs over the nonzero vectors
of the lattice `V.baseLattice` and `‖y‖` is the norm of `V.archCoords y`. 

### `height`

 The height `ht(g) = 1 / λ`, with `λ` the first minimum cut off at 1 (`New.Space.firstMinimum`)
of the moved space `V.move g`. 

### `IsModerate`

 A function `F` on the adelic unitary group has moderate growth: `|F g| ≤ C * ht(g) ^ B` for all
`g`, for some real `C` and natural number `B`, where `ht` is the height `V.height`. 

### `IsRapid`

 A function `F` on the adelic unitary group has rapid decay: `|F g| * ht(g) ^ B` is bounded for
every natural number `B`, where `ht` is the height `V.height`. 


## The first minimum: bounds, positivity, orthogonality of short vectors

A space `V` (`New.Space`) with point `x` gives a lattice `New.Space.baseLattice` in `E ^ n` and a
length `‖V.archCoords y‖` (`New.Space.archCoords`), from the finite and the infinite part of the
coordinates `x⁻¹ y` (`New.Space.vecAtPoint`) respectively.

* `New.Space.form_eq_zero_of_norm_mul_lt_one`: lattice vectors with product of lengths below `1` are
  orthogonal, as the value of the form is an algebraic integer (`New.Space.isIntegral_form`) that
  is small at every infinite place (`New.Space.norm_form_le_norm_archCoords_mul`).


### `stdForm_dotProduct_fst`

 At an infinite place `w`, the standard adelic form `stdForm E s` is the complex hermitian form
with the diagonal matrix `signMatrix s` of the signs `s`. Here `z.1 w` is the complex component at
`w` of an adele `z : 𝔸 E`. 

### `eq_zero_of_vecAtPoint_fst_eq_zero`

 A rational vector `a` is zero if its adelic coordinates `V.vecAtPoint a = x⁻¹ a` (`x` the point
of `V`) vanish at one infinite place `w`; `z.1 w` is the component at `w` of an adele `z`. 

### `vecAtPoint_move`

 Moving the point `x` of `V` to `x g`, for `g` in the adelic unitary group, multiplies the adelic
coordinates `x⁻¹ ξ` of a rational vector `ξ` by the matrix of `g⁻¹`. 

### `move_ratEmbed_mul_vecAtPoint_mulVec`

 For a rational isometry `γ` of `V` and `g` in `G`, the coordinates of `γ y` at `γ g` are the
coordinates of `y` at `g`. Here `γ` enters `G` as x⁻¹γx, with x the point of `V`
(`New.Space.ratEmbed`), and the coordinates at `g` are those in the moved space `V.move g`. 

### `baseLattice_move_ratEmbed_mul`

 For a space `V` = (J, x), a rational isometry `γ` of J (an element of `U V.J`), and `g` in the
adelic unitary group `G E s` of the standard form (diag(s) at the infinite places, 1 at the finite
places), we have L_{γg} = γ L_g. Here L_g = E^n ∩ x_f g_f Ô^n is the base lattice of the moved space
`V.move g`, and `γ` enters `G E s` as x⁻¹γx (`New.Space.ratEmbed`). 

### `norm_archCoords_move_ratEmbed_mul_mulVec`

 For a space `V` = (J, x), a rational isometry `γ` of J (an element of `U V.J`), `g` in the
adelic unitary group `G E s` of the standard form (diag(s) at the infinite places, 1 at the finite
places), and `y` in E^n, we have ‖γy‖_{γg} = ‖y‖_g. Here ‖y‖_g is the norm of the archimedean
coordinates of `y` in the moved space `V.move g`, and `γ` enters `G E s` as x⁻¹γx
(`New.Space.ratEmbed`), since x carries the form J to the standard one. 

### `exists_smul_mem_baseLattice`

 Every rational vector has a nonzero integer multiple in the lattice `V.baseLattice` of the
vectors whose adelic coordinates are integral at the finite places. 

 ### The first minimum and comparison of lengths 

### `le_firstMinimum_iff`

 A number `l` is at most the first minimum of `V`, cut off at `1`, iff it is at most `1` and at
most the length `‖V.archCoords y‖` of every nonzero vector `y` of the lattice `V.baseLattice`. 

### `mem_baseLattice_of_vecAtPoint_eq`

 Let the adelic coordinates `V.vecAtPoint ξ` of `ξ` be `N • k` times those of `η` in a second
space `W`. If `N * k` is integral at the finite places (`z.2` is the finite part of an adele `z`,
`Ô E` the ring of integral finite adeles) and `η` lies in the lattice of `W`, then `ξ` lies in the
lattice of `V`. 

### `norm_archCoords_le_of_vecAtPoint_eq`

 Let the adelic coordinates `V.vecAtPoint ξ` of `ξ` be `N • k` times those of `η` in a second
space `W`, with `k` of operator norm at most `c` at each infinite place `w` (`z.1 w` is the
component at `w` of an adele `z`). Then the length `‖V.archCoords ξ‖` is at most `N * c` times the
length of `η` in `W`. 

### `mem_and_norm_le_of_vecAtPoint`

 If the coordinates of `ξ` in `V` are `N • k` times those of `η` in `W`, with `k` of operator
norm at most `c` at each infinite place, then `ξ` is a lattice vector if `η` is one and `N * k` is
integral at the finite places, and the length of `ξ` is at most `N * c` times that of `η`. 

### `exists_smul_mulVec_mem_latticeBall`

 Let Ω be a compact subset of G_f, the finite part of the adelic unitary group. There is a
natural number c ≠ 0 with the following property. For γ in the rational unitary group, g and g' in G
and a real R, suppose that g⁻¹γg' (γ embedded by `V.ratEmbed`) has finite part in Ω and operator
norm at most R at every infinite place. If y lies in the lattice of `V.move g'`, then cγy lies in
the lattice of `V.move g` and its length there is at most cR times the length of y in
`V.move g'`. 

### `isIntegral_form`

 The hermitian form `V.J` takes algebraic integer values on pairs of vectors of the lattice
`V.baseLattice`. 

### `coordsAt`

 The coordinates of the rational vector `a` in the basis `V.x` at the infinite place `w`, as a
vector in the Euclidean space `ℂ^n`. 

### `norm_coordsAt_le`

 The length of `a` at one infinite place, in the coordinates of `V`, is at most its length
`‖V.archCoords a‖` over all infinite places. 

### `norm_form_le`

 The Cauchy–Schwarz inequality for the form at one infinite place `w`: in the embedding `Φ w`,
the value of the hermitian form `V.J` on `a` and `b` has absolute value at most the product of the
lengths of `a` and `b` at `w`. 

### `norm_form_le_norm_archCoords_mul`

 At each infinite place `w`, the value of the hermitian form `V.J` on `a` and `b`, embedded by
`Φ w`, has absolute value at most the product of the lengths of `a` and `b` over all infinite
places. 

### `form_eq_zero_of_norm_mul_lt_one`

 Two vectors of the lattice of `V` whose lengths have product less than `1` are orthogonal for
the hermitian form `V.J`. 

### `eq_zero_of_isotropic_of_definite`

 A definite space has no nonzero isotropic vector. Let `V` be a hermitian space with a point over
the CM field `E`: a matrix `J = V.J` over `E` and an invertible adelic matrix `x` with `xᴴJx` equal
to `diag(s)` at the infinite places and `1` at the finite places, for signs `s i = ±1` indexed by
the finite type `n`. If all signs are equal and `ξ ∈ E^n` has `ξᴴJξ = 0`, then `ξ = 0`. 

 ### Lower bounds for the first minimum 

### `one_le_firstMinimum`

 If all signs are equal, so that `V` is definite, then its first minimum is at least `1`: every
nonzero lattice vector has length at least `1`. 

### `firstMinimum_move_eq_one`

 Let `V` be a hermitian space with a point over the CM field `E`: a matrix `J` and an adelic `x`
with `xᴴJx = diag(s)` at the infinite places and `1` at the finite places. If all signs `s i` are
equal, so that `V` is definite, then for every `g` in the adelic unitary group `G E s` the moved
space `V.move g`, with point `xg`, has `firstMinimum` equal to `1`. Here `firstMinimum` is
`min(1, inf ‖y‖)`, with `y` running over the nonzero vectors of `baseLattice` and `‖y‖` the norm of
`archCoords y`. 

### `finite_latticeBall`

 The lattice of `V` is discrete: only finitely many of its vectors have length at most `r`. 

### `norm_archCoords_pos`

 A nonzero rational vector has positive length. 

### `firstMinimum_pos`

 The first minimum of `V`, cut off at `1`, is positive. 


## Short bases of lattices by transference

The lattice `L` of a hermitian space `V` contains a basis of `E ^ n` whose lengths are bounded by a
constant over the first minimum. For a nonzero `d` in the different, the dual of `2 d⁻¹ L` has no
nonzero vector shorter than the first minimum, as `L` is unimodular. So transference applies to
`2 d⁻¹ L`.


### `smul_mem_baseLattice_of_trace_int`

 Let `V` be a hermitian space over the CM field `E`, given by a matrix `V.J` over `E` and a point
`x`, and let `V.baseLattice = E^n ∩ x_f Ô^n` be the `y` with `x⁻¹ y` integral at the finite places.
Let `d` be in the different of `E` and `a ∈ E ^ n`. If the trace from `E` to `ℚ` of `ξᴴ V.J a` is an
integer for every `ξ` in `V.baseLattice`, then `d • a` lies in `V.baseLattice`. 

### `inner_archCoords_two_div_smul`

 For `d` in `E` and a vector `x` of the archimedean coordinate space, the real inner product of
`x` with the coordinates of `(2 / d) ξ`, written with the components `(V.vecAtPoint ξ i).1 w` at the
infinite places `w` and the embeddings `Φ w` of `E`: the factor `1 / d` moves onto `x` as division
by the conjugate of `Φ w d`. 

### `firstMinimum_le_norm_of_inner_int`

 Let `V` be a hermitian space with a point, `d` a nonzero element of the different of `E`, and
`x` a nonzero vector of the Euclidean space indexed by the infinite places and `n`. Suppose the
real inner product of `x` with `V.archCoords ((2 / d) ξ)` is an integer for every `ξ` in
`V.baseLattice = E^n ∩ x_f Ô^n`. Here `V.archCoords` sends a vector to the archimedean components of
its image under the inverse of the point. Then `‖x‖ ≥ V.firstMinimum`, which is
`min(1, least length of a nonzero lattice vector)`. 

### `exists_norm_sub_archCoords_le`

 Approximation by lattice vectors. Let `d` be a nonzero element of the different of `E`. Every
point `u` of the archimedean coordinate space lies within `(2 f n)² / λ` of the archimedean
coordinates of `(2 / d) a` for some `a` in the lattice `V.baseLattice`. Here `n` in the bound means
`Fintype.card n`, and `f` is the number of infinite places. `λ` is the first minimum
`V.firstMinimum` of `V`, cut off at `1`. 

### `span_eq_top_of_span_archCoords`

 A set `S` of rational vectors spans `E ^ n` over `E` if the archimedean coordinates
`V.archCoords ξ` (the components of `x⁻¹ ξ` at the infinite places, `x` the point of `V`) of its
members span their space over `ℝ`. 

### `shortBasisConst`

 The constant `6 N (f n)²` in the bound for short bases, where `f` is the number of infinite
places of `E` and `n` is the rank. 

### `exists_short_basis`

 Short bases. `V` is a hermitian space with a point: a matrix `J` over `E` and `x ∈ GL_n(𝔸)` with
`xᴴJx` equal to `diag(s)` at the infinite places and `1` at the finite places. Let `N ≠ 0` be a
natural number in the different of `E`. The lattice `V.baseLattice` contains a basis of `E ^ n`, the
columns of `Y`, whose vectors `y` have length `‖V.archCoords y‖` at most `6 N (f n)² / λ`. Here `n`
in the bound means `Fintype.card n`, `f` is the number of infinite places and `λ` the first minimum
of `V`, cut off at `1`. The constant `shortBasisConst E n N` is `N / 2` times the transference bound
`3 (2 f n)²` in real dimension `2 f n`. 

### `exists_short_basis_stdSpace`

 Short bases in the standard space `New.stdSpace`, which has all signs `1` and so is definite.
Let `N ≠ 0` be a natural number in the different of `E` and `g` a finite adelic unitary matrix. Some
`Y` in `GL n E` has `g⁻¹ Y` integral (all entries in `Ô E`, `New.IsIntMatrix`) and entries of
absolute value at most `6 N (f n)²` at every complex embedding, where `f` is the number of infinite
places. 

 ## The first minimum of the lattice of an orthogonal sum of spaces 

### `New.Rows.inf_le_firstMinimum_sum`

 The shortest vector length, cut off at 1 (`New.Space.firstMinimum`), of the lattice of V ⊕ W
(`New.Space.sum`) moved by the block sum `G.sum (g, h)` is at least the minimum of those of V moved
by g and W moved by h. 
