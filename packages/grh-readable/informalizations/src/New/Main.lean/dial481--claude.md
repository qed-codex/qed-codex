---
{
  "module": "src/New/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From non-vanishing in Re s > 1/2 to zeros on the critical line

The last step: the usual forms of the hypothesis follow from `DirichletLNonvanishingRightOfHalf`,
the non-vanishing of all Dirichlet L-functions in `re s > 1 / 2`, by the symmetry `s ↦ 1 - s` of the
zeros.

* `New.zeros_on_line`: the zeros of `L(s, χ)` in `0 < re s < 1` have `re s = 1 / 2`.
* `New.zeta_zeros_on_line`: the nontrivial zeros of `ζ` have `re s = 1 / 2`.

## Relation to the literature

Known result: the passage from the half-plane to the critical line by the functional equation. The
non-vanishing itself is `New.grh`.


### `New.zeros_on_line`

 Assume `DirichletLNonvanishingRightOfHalf` (hypothesis `h`): Dirichlet L-functions do not vanish
for Re s > 1/2, the pole excepted. Then `DirichletLZerosOnLine` holds: every zero s of a Dirichlet
L-function with 0 < Re s < 1 has Re s = 1/2. 

### `New.zeta_zeros_on_line`

 Assume `DirichletLNonvanishingRightOfHalf` (hypothesis `h`): Dirichlet L-functions do not vanish
for Re s > 1/2, the pole excepted. Then `RiemannZetaZerosOnLine` holds: every zero s of ζ outside
{1, −2, −4, …} has Re s = 1/2. 
