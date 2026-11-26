---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the cut lengths from the distributed group index

The first-half group numbered `i` needs the two incident lengths and the
three lengths at its primed pair. Equation (9.1) lets the group compute
all five using the position of the highest set bit and the number of set
bits in its index, without storing the index in a RAM word.


### `Slot`

 Two incident cuts and the three cuts of the primed pair. 

### `index`

 Convert a group number and width slot to the cut index used in the live or primed chain. 

### `blocks`

 Each block has `Δ` bits. Subtracting one from the group index crosses
a power of two precisely when the population count is one. 

### `blocks_width`

 The number of set bits is needed only to distinguish powers of two.
The two clamped endpoints are covered, including the case of just one
first-half group. 

### `Needed`

 Slots actually used at a group. A tail group needs only its incident cuts. 

### `needed_width`

 Correctness of every requested length throughout the chain, including
the final group, where the outgoing live width is clamped to zero. 

### `firstHalf_iff`

 The position and the population suffice to dispatch the two halves.
A group whose highest bit is at the halfway exponent belongs to the first
half precisely when that bit is its only set bit. 

### `endpoints_iff`

 Endpoint tests in the same small word representation. 
