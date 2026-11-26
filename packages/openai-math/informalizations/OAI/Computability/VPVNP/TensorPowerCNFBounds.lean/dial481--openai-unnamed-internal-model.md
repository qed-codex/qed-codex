---
{
  "module": "OAI/Computability/VPVNP/TensorPowerCNFBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerCNFBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerCNFBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Input lengths for the tensor-power CNF

For fixed bit width and number of parties, the control-state count and payload
length grow at most exponentially in the number of tensor factors. The exponent
of the local dimension in the compiled input length is absolute.


### `sizeCoefficient`

 Uniform coefficient for the CNF width, literal count and query state count. 

### `lengthCoefficient`

 Coefficient of the bound for the compiled table together with the payload. 

### `width_add_one_le`

 Bound for the payload width including one unit of control overhead. 

### `literalCount_add_two_le`

 The CNF compiler needs one read state per literal and two halting states. 

### `compiledLength_le`

 The entire table and payload fit at this length, uniformly in the tensor entries. 

### `projection`

 At every sufficiently large source length, the universal polynomial projects
onto the regrouped tensor power. The projection uses the entries of the given
tensor as scalar constants. 
