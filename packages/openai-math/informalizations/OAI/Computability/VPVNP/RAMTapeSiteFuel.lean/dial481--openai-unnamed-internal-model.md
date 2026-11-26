---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteFuel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteFuel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteFuel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing the private fuel and choice bound on a finite stack machine

At input length `n` each call uses at most `n^u` private instructions. The
site uses a unary stack for this bound, one for its `2H-1` call credits and one
for the maximum `2H*(n^u+w)` bits in the canonical choice string. The fixed
parameter `u` affects only the finite control.


### `Port`

 Unary tallies for input length, bucket size, word width, instruction fuel, call credits,
choice bits, and arithmetic scratch. 

### `initial`

 Initial allowance-computation state containing only the input length, bucket capacity, and
word width. 

### `powered`

 Intermediate state with the input length raised to the fixed exponent on the fuel counter. 

### `result`

 State with fuel `n^u`, call credits `2*H - 1`, and choice-string bound `2*H*(n^u + w)` in
unary. 

### `power`

 Unary program computing the fixed power of the input length by starting with one and
multiplying in each round. 

### `program`

 Compute private instruction fuel and use it to prepare the call-credit and choice-string
tallies. 

### `work_le`

 Under the live transcript bounds, constructing all three tallies takes
a fixed polynomial number of stack instructions. 
