---
{
  "module": "OAI/Computability/VPVNP/MacaulayPairPower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairPower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairPower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Returning the powered-row equality flag on the caller's physical ports 

### `powerParams`

 Radices, scaling factor and marked coordinate for comparing a powered source monomial with
a column monomial. The comparison requests no residual coordinate. 

### `powerRaw`

 Run the exponent comparison on the caller's pair of raw monomial codes and push its
equality flag onto the public flag stack. 

### `powerWork`

 Instruction allowance for loading the exponent registers, returning the equality flag and
clearing the call bank. 

### `powerSpace`

 Bound on the length of any stack during a powered-row comparison, including the caller's
stacks and the local exponent registers. 

### `powerClock`

 Tick bound for comparing all `t` coordinates of a powered row, including the transfers to
and from the local call bank. 

### `powerMatch`

 Test whether the column exponents equal the source exponents after incrementing the marked
coordinate, if present, and multiplying every exponent by the scale. 
