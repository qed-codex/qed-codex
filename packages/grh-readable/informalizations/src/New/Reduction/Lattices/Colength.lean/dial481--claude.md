---
{
  "module": "src/New/Reduction/Lattices/Colength.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Colength.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Colength.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Colength of modules, and endomorphisms surjective up to a bounded colength

A substitute for the colength of one module in another, and the bookkeeping of such colengths under
images, preimages, sums of submodules and products of endomorphisms.

* `New.ColengthDvd`: every finite family in `M` is carried into `N` by a square matrix whose
  determinant divides `z`; read it as "the colength of `N` in `M` divides `z`" or, over a valuation
  ring, "`N` has colength at most `v(z)` in `M`". `N ≤ M` is not required.
* `New.ColengthDvd.comap`, `New.ColengthDvd.map`, `New.ColengthDvd.trans`, `New.ColengthDvd.comp`:
  it passes along linear maps, and the bounds multiply along chains and compositions.
* `New.IsOntoUpToColength`, `New.IsOntoUpToColength.prod`: endomorphisms that keep `M` and are onto
  modulo `p ^ n` up to a colength dividing `p ^ l` with `l ≤ c`; the bounds `c` add under products.
* `New.ColengthDvd.of_det_dvd`: over a valuation domain the image of a square matrix `A` has
  colength dividing every multiple of `det A`, by the Smith normal form.
* `New.ColengthDvd.relLength_le`, `New.IsOntoUpToColength.exists_relLength_le`: over a discrete
  valuation ring `New.ColengthDvd` bounds a length.


### `ColengthDvd`

 `New.ColengthDvd M N z`, for submodules `M`, `N` of `V` and `z : O`, is read as "the colength of
`N` in `M` divides `z`" (over a valuation ring: it is at most `v(z)`). It needs no bases and no
inclusion `N ≤ M`: for every finite family `Φ k` (`k : Fin n`) of vectors of `M` there is a square
matrix `m` indexed by `Fin n` with `det m ∣ z` such that all `∑ k, m i k • Φ k` lie in `N`. 

### `ColengthDvd.trans`

 Colength bounds multiply along chains. Let `M`, `N`, `P` be submodules of `V`, with no inclusion
assumed. If every finite family in `M` is carried into `N` by a square matrix whose determinant
divides `z` (this is `ColengthDvd M N z`), and likewise from `N` into `P` with `a`, then every
finite family in `M` is carried into `P` by a square matrix whose determinant divides `z * a`. 

### `ColengthDvd.comap`

 Colength bounds pull back along a linear map `f : U → V`. Let every finite family in `M` be
carried into `N` by a square matrix whose determinant divides `z` (this is `ColengthDvd M N z`). If
`M'`, `N'` are submodules of `U` such that `f (M') ⊆ M` and every `x ∈ M'` with `f x ∈ N` lies in
`N'`, then the same holds for `M'`, `N'` and `z`. 

### `ColengthDvd.map`

 Colength bounds push forward along a linear map `f : V → U`. Let every finite family in `M` be
carried into `N` by a square matrix whose determinant divides `z` (this is `ColengthDvd M N z`). If
`M'`, `N'` are submodules of `U` such that `M' ⊆ f (M) + N'` and `f (N) ⊆ N'`, then the same holds
for `M'`, `N'` and `z`. 

### `ColengthDvd.comp`

 Let `M`, `N` be submodules of `V` and let the endomorphism `f` keep `M`. If every finite family
in `M` is carried into `f (M) + a • M` by a square matrix whose determinant divides `z`, and into
`N + a • M` by one whose determinant divides `z'` (these are instances of `ColengthDvd`), then it is
carried into `f (N) + a • M` by one whose determinant divides `z * z'`. 

 ### Endomorphisms that are onto up to a bounded colength 

### `IsOntoUpToColength`

 The endomorphism `y` of `V` keeps `M` and is onto on `M` modulo `p ^ n` up to a colength
dividing `p ^ l`, for some natural number `l ≤ c`: every finite family in `M` is carried into
`y (M) + p ^ n • M` by a square matrix whose determinant divides `p ^ l` (see `ColengthDvd`). 

### `IsOntoUpToColength.prod`

 The bounds on exponents add under products. Here `IsOntoUpToColength z M s y c` says that the
endomorphism `y` keeps the submodule `M` and that, for some natural number `j ≤ c`, every finite
family in `M` is carried into `y (M) + z ^ s • M` by a square matrix whose determinant divides
`z ^ j`. If each `T l`, `l` in the list `L`, satisfies this with bound `t l`, then the product of
the `T l` satisfies it with bound the sum of the `t l`. 

 ### The image of a square matrix over a valuation domain 

### `colengthDvd_inf_comap_span`

 Let `O` be a valuation domain, `M` a submodule of `V`, `f` a linear form on `V` and `a : O`. The
vectors of `M` on which `f` is divisible by `a` have colength dividing `a` in `M`, in the sense of
`ColengthDvd`: every finite family in `M` is carried into them by a square matrix whose determinant
divides `a`. 

### `ColengthDvd.of_det_dvd`

 Let `O` be a valuation domain and `A` a square matrix over `O` indexed by `ι` whose determinant
divides `z`. If the submodule `L` of `ι → O` contains the image of `A`, then `L` has colength
dividing `z` in the sense of `ColengthDvd`: every finite family in `ι → O` is carried into `L` by a
square matrix, of the size of the family, whose determinant divides `z`.

A consequence of the elementary divisor theorem (Smith normal form) over a valuation domain. 

### `colengthDvd_top_smul_top`

 Over a valuation domain `O`, the submodule `a • O ^ ι` of `O ^ ι` has colength dividing
`a ^ #ι` in the sense of `ColengthDvd`: every finite family in `O ^ ι` is carried into `a • O ^ ι`
by a square matrix whose determinant divides `a ^ #ι`. 

### `colengthDvd_sup_span`

 Over a valuation domain `O`, let `N` be a submodule of `V` and `s` a finite set of vectors. The
colength of `N + z • V` in `N + span s` divides `z ^ #s`, in the sense of `ColengthDvd`: every
finite family in `N + span s` is carried into `N + z • V` by a square matrix whose determinant
divides `z ^ #s`. 

 ### Comparison with lengths 

### `ColengthDvd.relLength_le`

 Over a discrete valuation ring `O`, `ColengthDvd` bounds a length. Let `M`, `N` be submodules of
`V` with `M` finitely generated; `N` need not lie in `M`. If every finite family in `M` is carried
into `N` by a square matrix whose determinant divides `z`, then `relLength M N`, the length of
`M / (M ∩ N)`, is at most the length of `O / z`. 

### `IsOntoUpToColength.exists_relLength_le`

 Let `M` be a finitely generated submodule of `V` over a discrete valuation ring `O`, and let
`IsOntoUpToColength p M n y c` hold: the endomorphism `y` keeps `M` and, for some natural number
`l ≤ c`, every finite family in `M` is carried into `y (M) + p ^ n • M` by a square matrix whose
determinant divides `p ^ l`. Then, for some natural number `l ≤ c`, the length
`relLength M (y (M) + p ^ n • M)` of `M / (y (M) + p ^ n • M)` is at most `l` times the length of
`O / p`. 
