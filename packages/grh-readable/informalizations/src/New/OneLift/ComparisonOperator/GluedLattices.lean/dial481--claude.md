---
{
  "module": "src/New/OneLift/ComparisonOperator/GluedLattices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluedLattices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluedLattices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gluing: residue rings, divided lattices, the congruence group and glued lattices

This file sets up the change of lattice at the chosen places for a divided splitting
`V : New.Rows.DividedSplitting N m a O z` of `V = V″ ⊕ V°`. It introduces the residue rings
modulo `ϖ²` and `ϖ²Q`, the conjugate kernel vector and the kernel summed over classes. It then
defines divided lattices, the congruence group of matrices that are `1` modulo `ϖ`, and product
forms. It constructs, for every matrix `s` modulo `ϖ²`, a lattice glued for `s`, and writes the
datum of the lift at `γ⁻¹ x` as a sum over the congruence group.

Here `O` is a descent pair with the space `W = O.W` of rank `r`. `N` indexes `V″`, `m` indexes
`V°`, `z : r ↪ m` marks `r` basis vectors of `V°`, and `a` indexes the rows of a matrix `s` modulo
`ϖ²`, the linear forms on `V″` on which a finer congruence is imposed. The idele `ϖ = O.genIdele`
generates the product of the chosen places `O.chosenPlace i`, and `Q` is the product of the places
`O.twistPlace i`. We write `(1; 0)` for an inclusion matrix `New.inclMatrix` with `r` columns.
The datum of the theta lift from `W` to `V` asks for `x ≡ (1; 0)` modulo `ϖ`. A product datum asks
for conditions modulo `ϖ²` on the two blocks of `x`. The lattice that connects them is spanned by
the columns of the matrix that is `(1; 0)` on both summands, by `L″_s = {u | s u ≡ 0 modulo ϖ}` in
`V″` and by `ϖ` times the standard lattice of `V°`. The matrix of a basis is called `γ`, and it is
handled through the integral matrix `ϖ γ⁻¹`.

## Main definitions and results

* `New.Rows.DividedLattice`, `New.Rows.DividedLattice.reducedInverse`: a point `γ` of G_f supported
  at the chosen places such that `ϖ γ⁻¹` is integral, and the reduction of `ϖ γ⁻¹` modulo `ϖ²`.
* `New.Rows.DividedSplitting.congruenceGroup`: the invertible `r × r` matrices modulo `ϖ²` that are
  `1` modulo `ϖ`.
* `New.Rows.DividedSplitting.productForm`: the form supported on the class of `(h, h°) γ` with the
  product of two vectors as its value. The product of vectors is `New.Rows.cartanProduct`.
* The datum. `New.Rows.DividedSplitting.exists_isGlued`: for every `s` there is a lattice glued for
  `s`. `New.Rows.DividedSplitting.IsGlued.indicator_eq_sum`: the datum of the lift at `γ⁻¹ x` is the
  sum of the translates of the product datum under the congruence group.

Notions from other files:
* `New.DescentPair`: A descent pair: chosen places and twist places, a space W of rank r with
  numbered basis vectors, an embedding of indices into n > r, two diagrams given by their numbers of
  columns of each height, and a character μ whose tame part, a character `O.tamePart w` of the
  residue field at each place w, is trivial off these places.
* `New.LevelPlaces.levelModulus`: `levelModulus c` is the modulus ϖ^c·Q, and `levelModulus c false`
  is ϖ^c.
* `New.inclMatrix`: For a map u: m → n of index sets, the n×m matrix whose j-th column is the
  standard basis vector e_{u(j)}.
* `New.Rows.liftMod`: A chosen lift of an invertible matrix modulo an ideal to an integral point of
  G_f that is 1 outside the places dividing the ideal and their conjugates.



## Residue rings modulo ϖ² and ϖ²Q and the divided splitting

* `New.Rows.DividedSplitting.genResidue_smul_eq_inclMatrix_iff`: a matrix agrees with an inclusion
  matrix modulo `ϖ²` after multiplication by `ϖ` exactly when they agree at every chosen place.


### `_root_.New.LevelPlaces.chosenModulusSq`

 The modulus `ϖ²`, the square of the product of the chosen places of `S`. 

### `map_block_eq_blockGL`

 The block diagonal matrix of two integral unitary matrices, reindexed by `ε`, is integral. Its
reduction along a homomorphism `f` from the integral finite adeles is the block diagonal matrix of
the two reductions. 

### `levelModulus_ideal_le`

 The ideal `ϖ² Q` is contained in `ϖ²`, where `ϖ` generates the product of the chosen places
and `Q` is the product of the twist places of `S`. 

### `places_levelModulus_false`

 For `c ≠ 0`, the places dividing the `c`-th power of the product of the chosen places of `S`
are the chosen places. 

### `reduceToChosenModulusSq`

 The reduction homomorphism from the residue ring modulo `ϖ² Q` to that modulo `ϖ²`. 

### `liftMod_mem_supportedOn`

 The chosen lift `liftMod B` to G_f of an invertible matrix `B` modulo `ϖ²` is supported at the
chosen places of `S`, whose product `ϖ` generates. 

### `atPlace_twistPlace_eq_one`

 A point `k` of G_f supported at the chosen places of `S` is `1` at every twist place of `S`. 

 ### The splitting and the generator `ϖ` 

### `DividedSplitting`

 A splitting `N ⊕ m ≃ n` of the indices of `V = V″ ⊕ V°` with embeddings of `r` and of `a` in
`N`, with `O.incl` landing in `N` through the embedding of `r`. The diagram `O.colsPlus` for `V″`
and the diagram `O.colsMinus` for `V°` satisfy `New.Rows.HasColumnsBelow`: each column of height
below the rank of `V` has height below the rank of the summand. 

### `DividedSplitting.fixedEmb`

 The `r` indices of `V″` that form the top block of a datum. 

### `DividedSplitting.equiv_inl_fixedEmb`

 The embedding `O.incl` lands in `V″`, where it is given by `fixedEmb`. 

### `DividedSplitting.dividedEmb`

 As many indices of `V″` as `a` has elements. After a change of basis these are the directions
  in which the lattice of `V″` is made smaller. 

### `DividedSplitting.hasColumnsBelow`

 The diagram `O.colsPlus` has no column of a height `h` with `#N ≤ h < #n`, and `O.colsMinus`
  none with `#m ≤ h < #n`. 

### `_root_.New.DescentPair.genIdele`

 The integral idele `ϖ` that generates the product of the chosen places of `O`. It equals `1` at
all other places. 

### `_root_.New.DescentPair.genIntAdele`

 The idele `ϖ = O.genIdele` as an element of the ring `Ô E` of integral finite adeles. 

### `reduction_levelModulus_eq_zero_iff`

 An integral finite adele `x` is `0` modulo the `c`-th power of the product of the chosen places
(the modulus `O.levelModulus c false`, where `false` leaves out the twist places) if and only if
`ϖ⁻¹ ^ c * x` is integral, where `ϖ = O.genIdele` generates that product. 

### `genResidue`

 The class modulo `ϖ²` of the idele `ϖ = O.genIdele`, which generates the product of the places
`O.chosenPlace i`. It depends on `O` only. The argument allows the notation `V.genResidue`. 

### `genResidue_smul_eq_inclMatrix_iff`

 Let `T` be a matrix modulo `ϖ² Q = O.levelModulus 2`, with `Q` the product of the twist places,
and let `inclMatrix _ u` be the matrix whose `j`-th column is the basis vector `u j`. Then `ϖ T` and
`ϖ • inclMatrix _ u` agree modulo `ϖ²` if and only if `T` reduces to that inclusion matrix in the
residue field of every chosen place, the place of index `inl i` among the chosen and the twist
places. 


## The conjugate kernel vector and the kernel summed over classes

The theta kernels (`New.modKernelStdSpace`) of the space `O.W` of a descent pair `O`
(`New.DescentPair`) with the standard definite space `I_m` on the indices `m` are packaged in two
ways.

* `New.Rows.kernelVector`: the vector of conjugate kernels for a basis of polynomials in the columns
  of sign `-1`. It is used for `V°`.
* `New.Rows.kernelClassSum`: the kernel with the polynomial of a vector `y h` in the columns of sign
  `1`, summed over the classes `h` of level `New.Rows.rowFixingLevel`. It is used for `V″`.

`New.fockLetters` and `New.letterPoly` substitute for each variable the sum of the variables at the
basis vectors of `O.W` of a given sign and number.


### `kernelVector`

 The vector whose i-th coordinate is the conjugate theta kernel of (W, I_m) at (g, h), with
datum Ψ modulo 𝔪 and the basis polynomial `nablaBasis ℂ _ κ i` of weight κ put into the columns of
sign `-1`. The characters `O.charW` and `b` of U(1)(𝔸) are those that the kernel takes for W and for
I_m. 

### `rowFixingLevel`

 The level that fixes the rows `w`: the integral points (elements of `stdLevel E m`) whose
reduction modulo `ϖ² Q` has the columns of the identity matrix off `e`, and whose reduction `A`
modulo `ϖ²` satisfies `w A = w`. Here `ϖ` generates the product of the chosen places of `S`, and `Q`
is the product of its twist places. 

### `kernelClassSum`

 The sum, over the classes h of level `New.Rows.rowFixingLevel` for `w` and `e`, of the theta
kernel of (W, I_m) at (g, h), with the characters `O.charW` of W and `b` of I_m. The polynomial is
that of y(h) in the columns of sign `1`. The datum `columnDatum` at `σ` modulo `ϖ² Q` is
`χ (det of the rows e of σ)` if `w σ ≡ w (1; 0)` modulo `ϖ²` and `0` otherwise, where `χ`, the
`charOfTamePart`, is the product of the characters `O.tamePart w` of the residue fields at the
places. 

 ## Divided lattice points, the congruence group and product forms 

### `DividedLattice`

 A lattice `γ 𝒪ⁿ`, where `γ` is the field `point`, with `ϖ 𝒪ⁿ ⊆ γ 𝒪ⁿ ⊆ 𝒪ⁿ` at the chosen places,
where `ϖ = O.genIdele`. The one condition, that `ϖ γ⁻¹` is integral, gives the first inclusion; read
at the conjugate places, it gives the second by unitarity. 

### `DividedLattice.point`

 The point of G_f. 

### `DividedLattice.mem_supportedOn`

 The point is supported on the chosen places. 

### `DividedLattice.mul_inv_mem`

 The entries of `ϖ γ⁻¹` are integral. 

### `DividedLattice.reducedInverse`

 The reduction modulo `ϖ²` of the integral matrix `ϖ γ⁻¹`. 

### `DividedLattice.weilScalar`

 The scalar `c_γ = χ(δ) / √|δ| ^ r` by which the matrix `γ` of the lattice multiplies the finite
datum. Here `δ` is the determinant of `γ` at the chosen places, `χ` the character that `O.charW`
attaches to a space of rank `r`, and `r` the rank of `O.W`. 

### `DividedLattice.reduceAt_conj_eq_one`

 Let `ϖ = O.genIdele` generate the product of the chosen places, and let `γ = L.point` be a point
of the finite adelic unitary group, supported at the chosen places, with `ϖ γ⁻¹` integral (a
`DividedLattice`). If the integral point `j` is `1` modulo `ϖ²`, then `γ⁻¹ j γ` is integral and
reduces to `1` at every chosen place. 

### `DividedLattice.exists_reducedInverse_eq`

 If integral matrices C and G satisfy `C * G = ϖ • 1`, where `ϖ = O.genIntAdele` generates the
product of the chosen places, then some divided lattice (a point γ of G_f at the chosen places with
`ϖ γ⁻¹` integral) has `ϖ γ⁻¹ ≡ G` modulo `ϖ²`. 

### `DividedSplitting.stackOverGenScalar`

 The rows of `s`, indexed by `a`, stacked above the rows of `ϖ • 1`, indexed by `N`. With this
matrix `w`, the one equation `w x = w x'` modulo `ϖ²` says that `s x ≡ s x'` modulo `ϖ²` and
`x ≡ x'` modulo `ϖ`. 

### `rowFixingLevel_le_levelOf`

 Let `V` split the indices `n` as `N ⊕ m`, with the embedding `V.fixedEmb : r ↪ N`, and let `s`
be an `a × N` matrix modulo `ϖ²`. Consider the integral unitary `N × N` matrices whose reduction
fixes the rows `V.stackOverGenScalar s` modulo `ϖ²` and has the columns of the identity off
`V.fixedEmb` modulo `ϖ² Q` (`rowFixingLevel`). Each of them reduces to `1` at every chosen place,
that is, lies in the level `levelOf O.chosenPlace ⊥`. 

### `congruenceGroup`

 The subgroup Γ of GL_r(`O.chosenModulusSq.ResidueRing`) of matrices that are 1 modulo ϖ. It is
defined as the stabiliser of the scalar matrix `V.genResidue • 1` under multiplication. 

### `mem_congruenceGroup_iff`

 An invertible matrix `A` lies in `V.congruenceGroup` exactly when
`V.genResidue • A = V.genResidue • 1`. Here `V.genResidue` is the class of `ϖ = O.genIdele` modulo
`ϖ²`, so this says that `A` is `1` modulo `ϖ`. 

### `reduceAt_liftMod_congruenceGroup`

 The lift of an element of the congruence group (the matrices that are `1` modulo `ϖ`) reduces to
`1` at every chosen place. 

### `IsBlockNormalised`

 The two conditions on the blocks of a matrix `x`: its block on `V°` is `(1; 0)` modulo `ϖ²`, and
its block on `V″` lies in `(1; 0) + ϖ L″_s`, where `L″_s` consists of the `u` with `s u ≡ 0` modulo
`ϖ`. Here the `1` of `(1; 0)` stands in the rows `z` of `V°` and in the rows `V.fixedEmb` of `V″`,
which are the rows `O.incl` of `V`. 

### `IsGlued`

 `L` is glued for `s`. With `γ = L.point`, the congruence `γ⁻¹ x ≡ (1; 0)` modulo `ϖ`, written as
`(ϖ γ⁻¹) x ≡ ϖ (1; 0)` modulo `ϖ²`, holds exactly when `x Y` satisfies the conditions on the two
blocks (`IsBlockNormalised`) for some `Y` in the congruence group, and this `Y` is then unique.
Moreover `γ⁻¹` is integral at the chosen places on all vectors of a suitable basis of `V″`, apart
from those indexed by `V.dividedEmb`, the chosen copy of the index set `a` of the rows of `s` in the
index set `N` of `V″`. 

### `IsGlued.existsUnique`

 If `γ⁻¹ x ≡ (1; 0)` modulo `ϖ`, then for exactly one `Y` that is `1` modulo `ϖ` the translate
  `x Y` satisfies the conditions on the two blocks. 

### `IsGlued.mul_eq_of_isBlockNormalised`

 Conversely, a matrix with such a translate satisfies the congruence. 

### `IsGlued.exists_cols_eq_zero`

 After a column operation, the columns of `ϖ γ⁻¹` in `V″` vanish modulo `ϖ` outside
  `V.dividedEmb`. 

### `IsGlued.indicator_eq_sum`

 As `L` is glued for `s` (`IsGlued`), the congruence `(ϖ γ⁻¹) x ≡ ϖ • inclMatrix _ O.incl` modulo
`ϖ²` holds exactly when `x Y` is block normalised for some `Y` in `V.congruenceGroup`, and this `Y`
is unique. So the indicator of the congruence is the sum over `Y` of the indicators that `x Y` is
block normalised. 

 ### Product forms and the construction of glued lattices 

### `productForm`

 For a pair `h = (h.1, h.2)` of points on `V″` and `V°` and a vector `y` of weight `O.colsPlus`
on `V″`, the linear map sending a vector `η` of weight `O.colsMinus` on `V°` to the form on `V` that
is supported on the class of `U.block V.ε h * γ`, the block diagonal point of `h` times the matrix
of the lattice `L`. Its value there (`classForm`) is the product `cartanProduct V.ε 1 y η` of `y`
and `η`, moved by the identity. 

### `exists_congruenceGroup_inv_eq_one_sub`

 Let `ϖ` generate the product of the chosen places of `O`, with class `V.genResidue` in the
residue ring modulo `ϖ²`. If an `r × r` matrix `Y` has `ϖ Y = 0` modulo `ϖ²`, then `1 - Y` is the
inverse of an element of `V.congruenceGroup`, the invertible matrices modulo `ϖ²` that are `1`
modulo `ϖ`. 

### `glueMatrix`

 The matrix with the blocks `D`, `-D ι_e ι_zᵀ`, `0` and the diagonal matrix that is `ϖ` on the
range of `z` and `1` elsewhere, where `ι_e` and `ι_z` are the inclusion matrices (`inclMatrix`) of
`e` and `z`. For suitable `D` and `e` it is `ϖ γ⁻¹` at the chosen places, up to the order of the
rows, for the lattice of `exists_isGlued`. 

### `isBlockNormalised_iff`

 Let `V.ε : N ⊕ m ≃ n` split the indices, let `ϖ` generate the product of the chosen places, with
class `V.genResidue` modulo `ϖ²`, and let `w = V.stackOverGenScalar s` be `s` stacked above `ϖ • 1`.
Write `ι_e` for the inclusion matrix of `e`, whose `j`-th column is the basis vector `e j`. A matrix
`x` modulo `ϖ²` is block normalised if its rows in `m` form `ι_z` and its rows `u` in `N` satisfy
`w u = w ι_e`, for `e = V.fixedEmb : r ↪ N`. Let the integral matrix `D` impose the same equations
as `w` modulo `ϖ²`, and let `glueMatrix` have the blocks `D`, `-D ι_e ι_zᵀ`, `0` and the diagonal
matrix that is `ϖ` on the range of `z` and `1` elsewhere. Then `x` is block normalised if and only
if its rows `z` in `m` form the identity matrix and `glueMatrix` takes `x` to `ϖ ι_{inr ∘ z}`. 

### `reducedInverse_mul_eq_iff`

 Let `ϖ` generate the product of the chosen places, with class `V.genResidue` modulo `ϖ²`, and
let `L.reducedInverse` be `ϖ γ⁻¹` modulo `ϖ²` for the point `γ` of the lattice `L`. Suppose that it
is the reduction of an integral matrix `G` whose rows are ordered by `ε'` and whose columns are
ordered by the splitting `V.ε : N ⊕ m ≃ n`, where `ε'` takes the indices `z : r ↪ m` to the indices
`O.incl : r ↪ n`. Then `(ϖ γ⁻¹) x` is `ϖ` times the inclusion matrix of `O.incl` if and only if `G`
takes `x`, with its rows ordered by `V.ε`, to `ϖ` times the inclusion matrix of `inr ∘ z`. 

### `mul_congruenceGroup_eq_smul_iff`

 Right multiplication by an element of the congruence group, whose elements fix `ϖ • 1`, does not
change whether a matrix equals `ϖ B` modulo `ϖ²`. 

### `isBlockNormalised_mul_iff`

 Let `V.ε : N ⊕ m ≃ n` split the indices, let `ϖ` generate the product of the chosen places, and
let the integral matrix `D` impose modulo `ϖ²` the same equations as `w = V.stackOverGenScalar s`,
which is `s` stacked above `ϖ • 1`. Write `ι_e` for the inclusion matrix of `e`. Suppose that
`L.reducedInverse`, the matrix `ϖ γ⁻¹` modulo `ϖ²` for the point `γ` of `L`, is `glueMatrix`, with
rows ordered by an `ε'` taking `z` to `O.incl`. Let `Y` be invertible and `1` modulo `ϖ`. Then `x Y`
is block normalised if and only if the rows `z` of `x` in `m` form `Y⁻¹` and
`(ϖ γ⁻¹) x ≡ ϖ ι_{O.incl}` modulo `ϖ²`. 

### `exists_divisor_assoc_stackOverGenScalar`

 Let `ϖ = O.genIntAdele` be the integral finite adele (element of `Ô E`) that generates the
product of the chosen places of `O`, and let `s` be an `a × N` matrix over the residue ring modulo
`ϖ²`. There are integral `N × N` matrices `B` and `D` with `B D = ϖ • 1` such that, modulo `ϖ²`,
each of `D` and `V.stackOverGenScalar s` is a left multiple of the other. 

### `exists_genResidue_mul_stackOverGenScalar_eq_zero`

 There is an invertible `K` such that the columns of `V.stackOverGenScalar s * K` outside
`V.dividedEmb` vanish modulo `ϖ`, that is, are killed by `V.genResidue` modulo `ϖ²`. 

### `exists_mul_glueMatrix_eq`

 Let `ϖ = O.genIntAdele` be the integral finite adele that generates the product of the chosen
places, and let `e = V.fixedEmb : r ↪ N` and `z : r ↪ m` be the
embeddings. If `B D = ϖ • 1` for integral `B` and `D`, then some integral matrix `C` satisfies
`C * glueMatrix O z e D = ϖ • 1`. 

### `exists_isGlued`

 Let `V.ε : N ⊕ m ≃ n` split the indices, let `ϖ` generate the product of the chosen places of
`O`, and write `ι_e` for the inclusion matrix of `e`. For every `a × N` matrix `s` modulo `ϖ²` there
is a divided lattice `L` (a unitary point `γ` at the chosen places with `ϖ γ⁻¹` integral) that is
glued for `s`. This means two things. First, an `n × r` matrix `x` modulo `ϖ²` satisfies
`(ϖ γ⁻¹) x ≡ ϖ ι_{O.incl}` if and only if `x Y` is block normalised for some invertible `Y ≡ 1`
modulo `ϖ`, and this `Y` is unique. Block normalised means that the rows in `m` form `ι_z` and the
rows `u` in `N` have `s u ≡ s ι_e` modulo `ϖ²` and `u ≡ ι_e` modulo `ϖ`, for `e = V.fixedEmb`.
Second, for some invertible `N × N` matrix `K`, the columns of `ϖ γ⁻¹` in `N`, multiplied by `K` on
the right, vanish modulo `ϖ` outside the range of `V.dividedEmb : a ↪ N`. 
