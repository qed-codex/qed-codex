---
{
  "module": "OAI/Computability/VPVNP/SliceGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A nonempty finite geometric slice with short affine cuts

Section 8.2 needs a finite geometric slice whose cardinality and base-field
cardinality have polynomial bit length. The construction here uses the same
effective weak Nullstellensatz bound `H` needed for characteristic descent.
A one-parameter Macaulay matrix detects each coordinate image. Outside the
exceptional roots of two minors its rank comparison is constant. Coordinate
pins consequently suffice to produce a finite slice.

The resulting point bound is `(2 * (H + d + 1)^t)^t`. Section 8.2's
projective Bézout argument gives the sharper bound `d^(t+1)`.


### `projectionBound`

 A monotone upper bound on the exceptional scalar count, independent of
the pins already chosen. 

### `projectionBound_pow_le`

 The resulting point-count bound has at most `(tL+1)t+1` binary digits if
`H+d+1 ≤ 2^L`. 

### `pinnedIdeal`

 The ideal of the original system and the selected affine coordinate equations. 

### `exists_finite_coordinate_slice`

 A coordinate pinning with at most `t` base-field coefficients gives a
nonempty finite geometric zero set of explicitly bounded cardinality. 
