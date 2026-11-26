---
{
  "module": "OAI/Computability/VPVNP/MotifDemandPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifDemandPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifDemandPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Demand padding in a repeated wire identity

Theorem 6.1 fixes surplus bits to zero at both ends of each demand wire.
A desired index is included as the same natural number in the larger range
and read in consecutive fields of the base width. Equality at the two ends
is then equivalent to equality in every field.


### `padFields`

 Widen an index by leading zeros, then split it into `u` fields of width `a`. 

### `padFields_digit`

 Each field can be read directly from the original index by division and remainder. 

### `HalfBits`

 The half-wire coordinates of a binary network at a party. 

### `demandChunk`

 Read the fields of a single repeated base copy at all incident half-wires. 

### `coeff_eq_prod_chunks`

 The product of the repeated base demands on the padded input is exactly
the desired demand tensor. This is an entrywise identity over any coefficient
semiring, also for zero copies or zero widths. 
