---
{
  "module": "src/Lib/Adelic/TraceFormula/OffPlace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/OffPlace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/OffPlace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Test functions with a deeper level at an auxiliary place

Let `v` be a split place at which the level `K` is maximal, and let `K'` be the part of `K` whose
component at `v` lies in a subgroup `J` of `GL_n(E_v)`. For a group algebra element `a` that is
integral at `v`, removing the components at `v` and its conjugate gives an element whose function
of level `K'` is the function of `a` of level `K`, cut off to the points with component at `v` in
`J`. So it is cuspidal at a place `w` other than `v` and its conjugate if the function of `a` is.
The function of a product with a factor at `v` in a set `S` is supported at `v` in `S J`.

Notions from other files:

* `Gf E n` is the finite adelic unitary group, and `g.atPlace v` is the component of `g` at `v`.
* For a split place `v` (one that differs from its conjugate), `ofSplitPlace hv k` is the element
  with component `k` at `v`, the inverse conjugate transpose of `k` at the conjugate of `v`, and `1`
  at all other places.
* `spanOn ℂ S` is the space of the group algebra elements that are combinations of the elements
  of the set `S`.
* `convIndicator` sends a group algebra element `a` to the test function `a ⋆ 1_K` of level `K`.
* `maxCompactAt n v` is the group of integral elements supported at `v` and its conjugate, and
  `localIntGL n v` is `GL_n(O_v)`.

## Relation to the literature

Known result: Test functions with a deeper level at an auxiliary split place, by removing the
components there. It serves `Lib.Adelic.TraceFormula.CuspidalComparison`.


### `offPlace`

 The homomorphism that removes from an element its components at the split place `v` and at
the conjugate of `v`. 

### `offPlace_apply`

 Removing the components of `g` at `v` and its conjugate is dividing `g` by the element
`ofSplitPlace hv (g.atPlace v)`, which has these components and is `1` at all other places. 

### `convIndicator_mapDomain_offPlace`

 Let `v` be a split place, let `K` be a compact open subgroup of the adelic unitary group
`Gf E n` that contains the maximal compact group at `v`, let `J` be a subgroup of `GL_n(E_v)`
such that `K ⊓ J.comap (Gf.atPlace v)` is compact open, and let `a` be a combination (`spanOn`)
of elements with component at `v` in `localIntGL n v = GL_n(O_v)`. Removing (`offPlace`)
the components of `a` at `v` and its conjugate and deepening the level to
`K ⊓ J.comap (Gf.atPlace v)` gives the function of `a` of level `K`, cut off outside the points
with component at `v` in `J`. Here `convIndicator` sends a group algebra element to its
convolution with the characteristic function of the level. 

### `IsCuspidalAt.convIndicator_offPlace`

 Let `v` be a split place, let `K` be a compact open subgroup of the adelic unitary group
`Gf E n` that contains the maximal compact group at `v`, let `J` be a subgroup of `GL_n(E_v)`,
let `a` be a combination (`spanOn`) of elements that are integral at `v` (component in
`localIntGL n v`), and let `w` be a split place other than `v` and its conjugate. If the function
`a ⋆ 1_K` (`convIndicator`) is cuspidal at `w` (its sums of translates over the cosets of each
unipotent radical at `w` vanish), then so is the function of level `K ⊓ J.comap (Gf.atPlace v)`
of `a` with the components at `v` and its conjugate removed (`offPlace`). 

### `exists_atPlace_eq_of_convIndicator_ne_zero`

 Let `u` be a combination (`spanOn`) of elements of a set `S` of `GL_n(E_v)`, let `J` be a
subgroup of `GL_n(E_v)`, and let `b` be any element of the group algebra of the adelic unitary
group `Gf E n`. Form the product of `u`, placed at `v` by `ofSplitPlace`, with `b` after removing
(`offPlace`) its components at `v` and its conjugate, and take the function (`convIndicator`) of
level `K ⊓ J.comap (Gf.atPlace v)` of this product. Where it is not zero, the component at `v`
lies in `S J`. 
