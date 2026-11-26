---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rounds/Costs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Costs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Costs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing the occurrences into sphere cells

First treat the group number as a host coordinate. Split it off again
after choosing simultaneous balanced partitions. The candidate host
is common to all groups, while the occupied cells can vary.



# Moving exterior bits to identity stations

Introduce one identity per exterior bit. Coarsening these by cell gives
one immobile station in each cell that has exterior ports.



# The mobile and immobile stations in a cell

Use `D` slots for mobile stations and one for the exterior identity.
Discard the scalar slots only after retaining their product.



# Uniform width for the local input

A station can touch at most `D+1` slots in each of at most `g+1`
cells. Padding both orientations therefore adds at most `4T` to
its arity when `g < D` and `R D² ≤ T`.


 # The grouping step before local concentration 

### `prepare`

 The first grouping step supplies the input to local concentration with
an absolute change in the total budget. 

 # Adding the sphere grouping to the downstream round 

### `design`

 One working extension can serve arbitrarily many width scales. 


# Terminal family of a stage

The weighted sum represents the whole tensor power exactly. This is
the expansion before the realization of its transcript as one network.


### `terminal`

 Sections 4 and 5 up to the terminal expansion. The size of the
working field and the replication bound are uniform in the input. 


# Terminal size estimates

Absorb powers of the logarithm of the height using arbitrary positive
slack. The exponent in the seat estimate does not depend on how many
blocks are reserved at the end.

