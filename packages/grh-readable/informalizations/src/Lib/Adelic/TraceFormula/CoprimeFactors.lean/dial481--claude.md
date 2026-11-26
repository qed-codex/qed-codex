---
{
  "module": "src/Lib/Adelic/TraceFormula/CoprimeFactors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/CoprimeFactors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/CoprimeFactors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coprime factors

Let `w` be a split place, `A, B` coprime non-units of `E_w[X]`, and `C` the set of elements of the
finite adelic group `Gf E n` with characteristic polynomial `A B` at `w`. An invariant distribution
`I` on `C` kills every test function `φ` that is cuspidal at `w` (`eq_zero_of_coprime_factors`).

Let `H` be the block diagonal subgroup of `GL_n(E_w)` with blocks of sizes `deg A` and `deg B`, `N`
the group of the unipotent matrices `1 + z` with `z` an upper right block, and `X ⊆ C` the set of
the `y` whose component `y_w` is block diagonal, with `A, B` as characteristic polynomials of the
blocks up to scalars. First `φ` is replaced by the mean of its conjugates under `GL_n(O_w)`.

* Step 1, images. The projection onto the kernel of `A(y_w)` along the kernel of `B(y_w)` is a fixed
  polynomial in `y_w` for `y ∈ C`. So `X` is a slice of `C` for `H` (`isSlice_blockLocus`), and test
  functions `Ψ` on `GL_n(E_w) × X` can be integrated over the fibres of `(g, y) ↦ g y g⁻¹`.
* Step 2. If the integrals of `Ψ (·, y)` vanish, then `I` kills the image of `Ψ`. This is
  `IsInvariantDistribution.eq_zero_of_isImage`, proved for any slice.
* Step 3, the choice of `Ψ`. Put `Ψ (g, y) = φ (g y g⁻¹)` for `g` in `U = GL_n(O_w) N` and `0`
  otherwise. This is the restriction to `GL_n(E_w) × X` of a test function on `GL_n(E_w) × Gf E n`
  (`exists_testFunction_eq_indicator`), its image is `φ` times the volume of `H ∩ GL_n(O_w)`
  (`isImage_blockLocus_smul`), and its integrals over `GL_n(E_w)` vanish because the conjugates of
  `y ∈ X` under `N` fill the coset `y N` (`integral_indicator_iwasawaSet_eq_zero`).

Notions from other files:
* `upperBlocks ε` is the set of the upper right blocks, the matrices `z` with `ε z = z` and
  `z ε = 0`.
* `radicalHom hε Y` is `1 + ε Y (1 - ε)`, an element of the unipotent radical that belongs to the
  idempotent `ε`; `coordProjector T` is the projector on the coordinates in `T`.
* `intGL n O` is `GL_n(O)`, and `localIntGL n w` is `GL_n(O_w)`. A `TestFunction` on a space is a
  locally constant function to `ℂ` with compact support; `φ.1` is the function itself.
* `IsSlice j H C X`, for a continuous homomorphism `j` of `Γ` into a group, says that
  `(g, y) ↦ j g * y * (j g)⁻¹` takes `Γ × X` onto the closed set `C`, has local sections, and has
  the orbits of `H` as fibres; `IsImage j ν X Ψ f` says that `f` is the integral of `Ψ` over the
  fibres.

## Relation to the literature

Part of a known result: in a simple trace formula with a cuspidal test function the terms that are
not elliptic vanish (Deligne and Kazhdan). The proof here is a descent of invariant distributions to
the block diagonal subgroup.


 ### The block diagonal group and the radical of an idempotent 

### `blockDiagonalGroup`

 The invertible matrices that commute with `ε`: for an idempotent `ε`, the block diagonal group
of the decomposition into the image and the kernel of `ε`. 

### `mem_range_radicalHom`

 The radical of the idempotent `ε` consists of the `u` for which `u - 1` is an upper right
block. 

### `conj_mem_range_radicalHom`

 The block diagonal group of an idempotent `ε` normalises the radical of `ε`. 

### `diagonal_blocks_mul_radical`

 For `h` block diagonal and `u` in the radical of the idempotent `ε`, the two diagonal blocks of
`h u` add up to `h`. 

### `mem_intGL_of_mul_radical`

 Let the idempotent `ε` have entries in the subring `O`. If `h u` lies in `GL_n(O)`, with `h`
block diagonal and `u` in the radical, then `h` lies in `GL_n(O)`. 

### `iwasawaSet`

 The set `GL_n(O) N`, with `N` the radical of the idempotent `ε`. 

### `mul_radical_mem_iwasawaSet_iff`

 The set `GL_n(O) N` is invariant under right translation by the radical `N`. 

### `mul_mem_iwasawaSet_iff`

 Let the idempotent `ε` have entries in `O`, and let `N` be its radical. For `g` in `GL_n(O) N`
and `h` block diagonal, `g h` lies in `GL_n(O) N` exactly if `h` lies in `GL_n(O)`. 

### `semiconjBy_radicalHom_sub`

 If `e` is a projection onto the image of the idempotent `ε`, then the element `1 + (ε - e)` of
the radical conjugates `ε` to `e`. 

### `radicalHom_sub_eq`

 An element `u` of the radical is recovered from the idempotent `e = u ε u⁻¹` as
`1 + (ε - e)`. 

 ### The Iwasawa decomposition and the projection of a coprime factorisation 

### `columnSpace`

 The matrices whose columns lie in the image of `a`. This set stands for the image of `a`, and
`GL n k` acts on such sets by left multiplication. 

### `columnSpace_eq_smul`

 If `a u = g b` with `u` and `g` invertible, then `g` moves the image of `b` onto that of `a`. 

### `mul_eq_of_columnSpace_eq`

 An idempotent fixes the columns of every matrix with the same image. 

### `columnSpace_coordProjector_map`

 The permutation matrix of `σ` moves the coordinate subspace of `T` onto that of `σ T`. 

### `isConj_mul_self_of_mem_range_radicalHom`

 In characteristic zero an element of the radical of `ε` is conjugate to its square, by the
matrix `1 + ε`, which is `2` on the image of `ε` and `1` on its kernel. 

### `columnSpace_diagonal`

 The image of a diagonal matrix is the coordinate subspace of its non-zero entries. 

### `exists_columnSpace_eq_smul_coordProjector`

 **Iwasawa decomposition, for subspaces.** Let `O` be a subring of `F` with `IsValuationPair O`
(of any two elements of `F` one is a multiple of the other by an element of `O`, for instance a
valuation subring), and let `T` be a set of coordinates with as many elements as the rank
of `e`. Then some element of `GL_n(O)`, the group `intGL n O`, moves the coordinate subspace of `T`,
the image of `coordProjector T`, onto the image of `e`, given by `columnSpace e`. 

### `exists_mem_iwasawaSet_semiconjBy`

 **Iwasawa decomposition, for idempotents.** Let `O` be a subring of `F` with `IsValuationPair O`
(for instance a valuation subring). An idempotent `e` of rank `|T|` is `g ε g⁻¹`, with `ε` the
coordinate projector of `T`, for some `g` in `GL_n(O) N`, where `N` is the radical of `ε`. 

### `exists_mul_mem_iwasawaSet`

 **Iwasawa decomposition.** Let `O` be a subring of `F` with `IsValuationPair O` (for instance a
valuation subring). Every invertible matrix lies in `GL_n(O) N H`, with `N` the radical and `H` the
block diagonal group of the coordinate projector of `T`. 

### `trace_aeval_eq_sum_roots`

 Over an algebraically closed field the trace of `p(y)` is the sum of `p` over the roots of the
characteristic polynomial of `y`, with multiplicity. 

### `isIdempotentElem_aeval_of_charpoly_eq`

 If `u A + v B = 1` and `y` has characteristic polynomial `A B`, then `(v B)(y)` is
idempotent (it is the projection onto the kernel of `A(y)` along the kernel of `B(y)`). 

### `trace_aeval_eq_natDegree`

 If `u A + v B = 1` and `y` has characteristic polynomial `A B`, then the projection `(v B)(y)`
onto the kernel of `A(y)` has trace `deg A`. 

### `rank_aeval_eq_natDegree`

 In characteristic zero, if `u A + v B = 1` and `y` has characteristic polynomial `A B`, then the
projection `(v B)(y)` onto the kernel of `A(y)` has rank `deg A`. 

### `exists_finset_card_eq_natDegree`

 If `A B` is a characteristic polynomial and neither factor is a unit, some proper non-empty set
of coordinates has `deg A` elements. 

 ### Step 1: the block diagonal elements form a slice 

### `isClosed_setOf_charpoly_eq`

 Over a Hausdorff topological ring the matrices with a given characteristic polynomial form a
closed set. 

### `isOpenEmbedding_coe_generalLinearGroup`

 Over a complete normed field `GL_n` is open in the space of matrices. 

### `eventually_exists_semiconjBy_of_isIdempotentElem`

 Over a complete normed field, let the idempotent matrices `e y` tend to the idempotent `e₀`
along a filter, and let `O` be a neighbourhood of `1` in `GL_n(F)`. Then eventually `e y` is
`g e₀ g⁻¹` for some `g ∈ O`. 

### `atSplitContinuous`

 The embedding of `GL_n(E_w)` into `Gf E n` at the split place `w`, as a continuous
homomorphism. 

### `ofSplitPlace_conj_eq_mul`

 Let `y_w` be the component of `y` at the split place `w`. If `a⁻¹ y_w a = y_w b` in
`GL_n(E_w)`, then `a⁻¹ y a = y b` with `a` and `b` embedded at `w` (by `ofSplitPlace`). 

### `charpolyLocus`

 The elements of `Gf E n` whose component at `w` has characteristic polynomial `P`. 

### `mem_charpolyLocus`

 An element lies in `charpolyLocus n P` exactly if its component at `w` has the characteristic
polynomial `P`. 

### `blockLocus`

 The elements `y` with characteristic polynomial `P` at `w` and `p(y_w) = ε`. If `p(y_w)` is the
projection that belongs to a coprime factorisation of `P` and `ε` is a coordinate projector, these
are the `y` for which `y_w` is block diagonal and the two blocks have the two factors as their
characteristic polynomials, up to scalars. 

### `semiconjBy_aeval_atPlace_conj`

 For `g` embedded at `w` and a polynomial `p`, the matrix `g` conjugates `p((g⁻¹ x g)_w)` to
`p(x_w)`. 

### `conj_mem_blockLocus_iff`

 The conjugate `g⁻¹ x g` has characteristic polynomial `P` and `p`-value `ε` at `w` exactly if
`x` has characteristic polynomial `P` at `w` and `p(x_w) = g ε g⁻¹`. 

### `isSlice_blockLocus`

 Let `u A + v B = 1` and `|T| = deg A`. The projection onto the kernel of `A(y_w)` is the fixed
polynomial `v B` in `y_w`, so the block diagonal elements form a slice of the set of elements with
characteristic polynomial `A B`, for the block diagonal group. 

 ### Step 3: the choice of the function `Ψ` 

### `exists_testFunction_eq_indicator_of_isCompact`

 For a compact open subset `V` of `GL_n(E_w)`, the function `(g, y) ↦ φ (g y g⁻¹)` on
`V × Gf E n`, extended by zero, is a test function. 

### `exists_testFunction_eq_indicator`

 Let `w` be a split finite place of the CM field `E`, let `ε` be an idempotent matrix over `E_w`,
and let `iwasawaSet hε O_w` be the set `GL_n(O_w) N`, with `N` the unipotent radical of the
parabolic subgroup of `GL_n(E_w)` attached to `ε`. Suppose the test function `φ` on `G_f` is
invariant under conjugation by the images `ofSplitPlace hw k` of all `k ∈ GL_n(O_w)`. Then there is
a test function `Ψ` on `GL_n(E_w) × G_f` such that, for every `y` whose component `y_w` satisfies
`p(y_w) = ε`, `Ψ (g, y) = φ (g y g⁻¹)` when `g ∈ GL_n(O_w) N` and `Ψ (g, y) = 0` otherwise (with `g`
acting through `ofSplitPlace hw`). 

### `integral_indicator_iwasawaSet_mul`

 For every `g`, the set of the block diagonal `h` with `g h` in `GL_n(O_w) N` is a coset of the
integral block diagonal group, so the integral over `h` of a constant `c` on this set is the volume
of the integral block diagonal group times `c`. 

### `isImage_blockLocus_smul`

 Let `Ψ (g, y)` be `φ (g y g⁻¹)` for `g` in `GL_n(O_w) N` and `0` otherwise, for all `y` with
`p(y_w)` the coordinate projector of `T`. Then `φ` times the volume of the integral block diagonal
group is an image of `Ψ`, the integral of `Ψ` over the orbits of the block diagonal group. 

### `measureReal_subgroupOf_localIntGL_ne_zero`

 The integral points of a closed subgroup of `GL_n(E_w)` have finite non-zero Haar measure. 

### `map_mul_right_eq_self_of_mem_range_radicalHom`

 Haar measure on `GL_n(E_w)` is invariant under right translation by the radical of an
idempotent. 

### `exists_conj_eq_mul_radicalHom`

 If `p(y_w)` is the idempotent `ε`, the conjugates of `y` under the radical `N` of `ε` fill the
coset `y N`. 

### `sum_indicator_iwasawaSet_mul_eq_zero`

 Let `φ` be invariant under conjugation by `GL_n(O_w)`, let its right translates by the elements
`radicalHom hε (κ i)` of the radical `N` of `ε`, embedded at `w`, have sum zero, and let `m i ∈ N`
conjugate `y` to the translate of `y` by the same element. Then the right translates by the `m i` of
the function `g ↦ φ (g y g⁻¹)` on `GL_n(O_w) N`, extended by zero, have sum zero. 

### `integral_indicator_iwasawaSet_eq_zero`

 Let `φ` be invariant under conjugation by `GL_n(O_w)`, let its right translates by a non-empty
finite family in the radical `N` of `ε` have sum zero, and let `p(y_w) = ε`. Then the integral of
`φ (g y g⁻¹)` over `g ∈ GL_n(O_w) N` vanishes, if it converges. 

 ### The three steps together 

### `eq_zero_of_coprime_factors`

 **Coprime factors.** Let `A, B` be coprime non-units of `E_w[X]` for a split place `w`, and let
`I` be a linear form on the test functions on the finite adelic group `Gf E n` that is invariant
under conjugation (`translate (g, g) f` is `x ↦ f (g⁻¹ x g)`) and depends only on the restriction to
the set of elements with characteristic polynomial `A B` at `w`. Then `I` kills every `φ` that is
cuspidal at `w`, that is, whose sums of translates over the unipotent radicals of the proper
coordinate parabolic subgroups over the residue field at `w` vanish. 
