---
{
  "module": "OAI/Computability/VPVNP/RAMVirtualParameterBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMVirtualParameterBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMVirtualParameterBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer operands for the virtual site count

Section 11 chooses the least power of two whose buckets cover the probe budget.
Its address width can be computed from the live address width and the product of
the input length with its ceiling logarithm. This computation keeps the live
processor count in exponent form and fits in the prescribed machine words.


### `virtualSiteExponent_eq_add_sub`

 The virtual address width, computed without forming the live processor count. 

### `clog_length_mul_clog_le`

 The product whose logarithm supplies the extra address bits has at most
twice the ceiling logarithm of the input length as its ceiling logarithm. 

### `virtualParameterOperands_lt`

 At every input length the product and its increment, the sum of the two
logarithmic counters, and the numerator for ceiling division by four fit in a
live processor word. 
