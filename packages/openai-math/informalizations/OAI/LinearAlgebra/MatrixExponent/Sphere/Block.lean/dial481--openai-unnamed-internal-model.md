---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Block.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Block.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Block.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weighted slot selection

A test can pair only with its target or a strictly heavier slot. If the
available weight cannot exceed the target weight, every test in a
nonzero Wick monomial must occupy its target.


### `wick_pivot`

 Under a total weight budget, triangular pairings select precisely
the target slot list. Reversing the tests cancels the pairing signs. 


# Wedge duality

Reversing the second list of modes gives the ordinary Kronecker pairing
on the ordered wedge basis.


### `wick_last`

 Only the last position can pair with the first. An odd residual
length contributes zero, so no sign survives. 


# Auxiliary marks of bounded weight

A probe is an even ordered subset of the auxiliary marks, with just the
lowest mode at each selected mark. Removing all probe-probe contractions
uses only shorter probe lists. Linear combinations then implement arbitrary
covectors. Kronecker covectors detect a longest nonzero word.


### `auxiliary_marks`

 One mode at each of the prescribed auxiliary positions suffices to
realize every even form on a family of distinct ordered monomials. 

### `weighted_probe`

 A triangular family of interpolated covectors detects one monomial
under a total weight budget. Values on heavier slots are unrestricted. 

### `probe_extension`

 A finite extension and one set of auxiliary marks work simultaneously
for all even forms and all prescribed length bounds on these modes. 

### `Crossing`

 A pair of independent wires splits as a sum across the two other cuts. 

### `ShiftedCrossing`

 The growth rates can trade off across the two cuts. 

 Simultaneous motion of marked points about cluster centers. 


# A colliding cluster and its residual modes

Internal contractions use the site offsets. Every uncontracted generator
is translated to its center. Pairing with a reversed output wedge gives
the coefficient at that wedge.


### `translate`

 Translation by the offset of a site. 

### `Leg`

 A site still in motion, a fused generator, or a dual coordinate test. 

### `block`

 Fuse one cluster in place. Only equal-parity output blocks contribute,
so moving the cluster past the preceding sites creates no net sign. 
