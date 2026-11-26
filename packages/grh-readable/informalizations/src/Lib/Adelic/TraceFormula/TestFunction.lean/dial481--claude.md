---
{
  "module": "src/Lib/Adelic/TraceFormula/TestFunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/TestFunction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/TestFunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Test functions and the two local conditions of the comparison of traces

Test functions on a topological group, their translates, and the function `a ⋆ 1_K` of an element
`a` of the group algebra. On the finite adelic group the comparison of traces asks for two
conditions: the test function is cuspidal at a split place (`IsCuspidalAt`), and at a second place
the components of the elements of its support are integral with a simple eigenvalue zero modulo the
place. `HasSimpleZero` is this last property of one matrix over the completion at the place.

Notions from other files:
* `Gf E n`: the group of finite adelic points of the unitary group of the `n × n` identity matrix;
* `LocField w`, `LocInt w`, `ResField w`, `localIntGL n w`: the completion at a finite place `w`,
  its ring of integers, its residue field, and `GL_n` of that ring inside `GL_n` of the completion;
* `ofSplitPlace hw`: at a split place `w`, the map from `GL_n` of the completion at `w` to `Gf E n`;
* `radicalHom`: for an idempotent `ε`, the homomorphism `Y ↦ 1 + ε Y (1 - ε)` onto the unipotent
  radical of the parabolic subgroup that keeps the image of `ε`.

## Relation to the literature

Known; see `Lib.Adelic.TraceFormula.TraceComparison` for sources.


### `TestFunction`

 The space of test functions on `G`: the locally constant complex functions of compact
support. 

### `TestFunction.comp_mul_mem`

 The composite of a test function with `x ↦ a⁻¹ * x * b` is again a test function. 

### `TestFunction.translate`

 Left and right translation of test functions: `(a, b)` takes `f` to `x ↦ f (a⁻¹ * x * b)`. 

### `TestFunction.translate_apply`

 The translate of `f` by the pair `g = (a, b)` takes `x` to `f (a⁻¹ * x * b)`. 

### `TestFunction.indicator`

 The characteristic function of a compact open subgroup. 

### `convIndicator`

 The linear map `a ↦ a ⋆ 1_K` from the group algebra to the test functions, for a compact open
subgroup `K`: the group element `b` goes to the characteristic function of the coset `b K`. 

### `convIndicator_single`

 For a compact open subgroup `K`, a group element `b` and a scalar `c`, the test function
`(c b) ⋆ 1_K` given by `convIndicator` is `c` on the coset `b K` and zero elsewhere. 

### `convIndicator_single_mul`

 For a compact open subgroup `K` and an element `a` of the group algebra, write `a ⋆ 1_K` for
the test function given by `convIndicator`. Then `(c b * a) ⋆ 1_K` is `c` times the left translate
of `a ⋆ 1_K` by the group element `b`. 

### `instance [WeaklyLocallyCompactSpace G] : IsSmoothRep (TestFunction.translate (G`

 The representation of `G × G` on test functions by translation is smooth: each test function is
fixed by all translations near the identity. 

### `coordProjector`

 The diagonal projector on the coordinates in `T`. 

### `map_radicalHom_coordProjector`

 A ring homomorphism `f`, applied entrywise, takes the element `1 + ε Z (1 - ε)` of the unipotent
radical (`radicalHom`), with `ε` the diagonal projector on the coordinates in `T`, to the element
attached in the same way to `T` and `f(Z)`. 

### `IsCuspidalAt`

 The test function `φ` is cuspidal at the split place `w`. Let `U` be the unipotent radical of a
proper parabolic subgroup of `GL_n(F_w)`, with `F_w` the residue field at `w`, that is cut out by a
set `T` of coordinates. Then every left translate of `φ` has sum zero over each coset `U t`, lifted
to `GL_n(O_w)` and put into the adelic group at `w` by `ofSplitPlace`. In detail, the sum runs over
all matrices `Z` over `F_w`, each with a lift of the element `radicalHom Z * t` of the coset; every
element is met equally often, and every choice of these lifts is allowed. 

### `exists_radicalHom_reduceGL_eq`

 Let `T` be a set of coordinates. Every element `1 + ε Z (1 - ε)` (`radicalHom`, with `ε` the
projector on `T`) over the residue field at `w` is the reduction (`reduceGL`) of an element
`1 + ε Y (1 - ε)` over `E_w` that lies in `localIntGL n w`, the group `GL_n(O_w)`. 

### `IsCuspidalAt.exists_sum_translate_eq_zero`

 Let the test function `φ` on the finite adelic group `Gf E n` be cuspidal at the split place
`w` and let `T` be a set of coordinates, neither empty nor everything. Then there is a finite
nonempty family `κ` of matrices over `E_w`, written multiplicatively, with the following property:
for every `k` in `GL_n(O_w)`, the right translates of `φ` by the images in `Gf E n` of the products
`(1 + ε (κ i) (1 - ε)) * k` sum to zero over `i`. Here `1 + ε (κ i) (1 - ε)` is `radicalHom` of
`κ i` for the projector `ε` on `T`, and the images are taken under the embedding `ofSplitPlace` at
`w`. 

### `IsCuspidalAt.convIndicator_mul`

 Let `K` be a compact open subgroup of the finite adelic group `Gf E n` and `a`, `b` elements of
its group algebra. If the test function `a ⋆ 1_K` (`convIndicator`) is cuspidal at the split place
`w` (`IsCuspidalAt`: zero sums over the cosets of unipotent radicals modulo `w`), then so is
`(b * a) ⋆ 1_K`. 

### `HasSimpleZero`

 The matrix `g` has entries in `O_w`, and `0` is a simple root of its characteristic polynomial
modulo `w`. 

### `exists_eq_pow_of_monic_of_map_eq_pow`

 If a monic polynomial over an integrally closed domain is a `j`-th power over the fraction
field, with `j ≠ 0`, then it is the `j`-th power of a polynomial over the domain. 

### `HasSimpleZero.charpoly_ne_pow`

 If the matrix `g` has entries in `O_w` and `0` is a simple root of its characteristic polynomial
modulo `w` (`HasSimpleZero g`), then the characteristic polynomial of `g` over `E_w` itself is no
`j`-th power for `j > 1`. 
