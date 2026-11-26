---
{
  "module": "src/New/Spanning/RemainingTerms/ColumnLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/ColumnLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/ColumnLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The covolume of the lattice of columns

The tuples of vectors of the lattice `Λ ∩ X₀` of a class form a lattice in the product of the
complex places. The real inner product of two of its points is an integer, so its covolume is at
least `1`.

## Main definitions and results

* `New.Filling.columnLattice`, `New.Filling.exists_isAddFundamentalDomain_columnLattice`: the
  lattice of tuples of vectors of `Λ ∩ X₀` and its fundamental domain.

Notions from other files:

* `S : Filling E 𝔰`: the data of the filling theorem over the CM field `E` for the shape `𝔰`; the
  space `X₀` has a basis indexed by `𝔰.κ`, a set of `𝔰.k` elements.
* `c : S.Classes`: a class of the definite unitary group of `X₀`, with lattice `Λ`.
* `S.classCoordX₀ c`: the matrix that writes vectors of `X₀` in a basis of `Λ`; thus a vector lies
  in `Λ ∩ X₀` if its image under this matrix is integral.
* `Φ v`: the chosen complex embedding of `E` at the infinite place `v`.
* `Ô E`, `finAdeleMatrix q`: the integral finite adeles, and the matrix `q` over the finite adeles.

## Relation to the literature

See `New.Spanning.RemainingTerms.Sum` for related work.


### `conjColumnsAtInfinity`

 The point of the product of the complex places given by a matrix over `E` whose columns are
`ι` vectors of `X₀`: at the place `v`, the entry `q a l` goes to the conjugate of `Φ v (q a l)`. 

### `denseRange_conjColumnsAtInfinity`

 Let `Φ v` be the chosen complex embedding of `E` at the infinite place `v`. The map
`conjColumnsAtInfinity`, which sends a matrix `q` over `E` to the family of the complex conjugates
of its images `Φ v (q a l)`, indexed by the place `v`, the column `l` and the row `a`, has dense
range. 

### `integralColumns`

 The tuples of vectors of `Λ ∩ X₀`, for the lattice `Λ` of the class `c`, as the columns of a
matrix. 

### `columnLattice`

 The image of the tuples of vectors of `Λ ∩ X₀` in the product of the complex places. 

### `mem_columnLattice`

 A point is in the lattice of columns if and only if it is the image under
`conjColumnsAtInfinity` of a matrix over `E` whose columns lie in the lattice of the class `c`. 

### `isIntegral_conjTranspose_mul`

 If `q` and `q'` are matrices whose columns lie in `Λ ∩ X₀`, for the lattice `Λ` of the class
`c`, then the hermitian products of their columns, the entries of `qᴴ * q'`, are algebraic
integers. Here `E` contains a primitive root of unity of order `5040`. 

### `instance {S : Filling E 𝔰} {c : S.Classes} [HasPrimitiveRoot5040 E] [S.IsAdmissible] : DiscreteTopology (S.columnLattice ι c)`

 A nonzero vector of `Λ ∩ X₀`, for the lattice `Λ` of the class `c`, has length at least `1` at
some place, so the lattice of columns is discrete. 

### `span_columnLattice`

 Let `S` be filling data of shape `𝔰` over the CM field `E`, let `c` be a class of the definite
unitary group of `X₀ = E ^ 𝔰.κ`, with lattice `Λ`, and let `ι` be a finite set. The subgroup
`S.columnLattice ι c` is the image of the `ι`-tuples of vectors of `Λ ∩ X₀`, under the conjugates
of the chosen complex embeddings of `E`, in the product over the infinite places of `E` of the
spaces of `ι`-tuples of vectors of `ℂ ^ 𝔰.κ`. It spans this product over `ℝ`. 

### `exists_int_eq_sum_re`

 Let the CM field `E` contain a primitive root of unity of order `5040`, hence a square root of
`-1`. For an algebraic integer `x` of `E`, the sum over the infinite places `v` of the real parts of
the images `Φ v x` under the chosen embeddings, which is half the trace of `x`, is an integer. 

### `exists_isAddFundamentalDomain_columnLattice`

 Let `E` be a CM field that contains a primitive root of unity of order `5040`. Let `S` be
admissible filling data over `E`: the level in `U(X₀)`, for `X₀ = E ^ 𝔰.κ`, is the preimage of the
principal congruence subgroup of level `S.M`, reduction at the chosen places is onto, and size
bounds in terms of `S.b` hold. The subgroup `S.columnLattice ι c` is the image of the `ι`-tuples of
vectors of `Λ ∩ X₀` under the conjugates of the chosen complex embeddings, one for each infinite
place. It has a measurable fundamental domain whose Lebesgue measure is finite and at least `1`. 
