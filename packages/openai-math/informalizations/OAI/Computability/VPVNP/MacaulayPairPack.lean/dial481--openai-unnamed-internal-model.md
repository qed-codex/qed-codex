---
{
  "module": "OAI/Computability/VPVNP/MacaulayPairPack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairPack.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairPack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Staging the residual packer with preserved caller inputs 

### `packRaw`

 Run the staged residual-exponent routine on the two raw keys and return the packed
differences and divisibility flag to their caller stacks. 

### `packTicks`

 Tick bound for one comparison and residual-word copy per variable, including the loop
tests. 

### `packInnerSpace`

 Private stack-height bound for the residual packer, accounting for register width, the
unary marker and the work of all iterations. 

### `packWork`

 Copying and cleanup allowance for the packer's twelve input stacks, two returned outputs
and thirteen cleared private stacks. 

### `packSpace`

 Stack bound for the whole staged packer call, including the caller, private working space
and copy overhead. 

### `packClock`

 Tick bound for staging the packer, running all variable iterations and returning the two
outputs. 

### `keys`

 The source and column raw graded monomial codes as fixed-width little-endian bit stacks. 

### `difference`

 Packed exponent vector obtained by coordinatewise truncated subtraction of the source
monomial from the column monomial. 
