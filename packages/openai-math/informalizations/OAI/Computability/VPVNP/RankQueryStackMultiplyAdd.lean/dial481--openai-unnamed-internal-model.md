---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackMultiplyAdd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackMultiplyAdd.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackMultiplyAdd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Schur stack machine's multiply-and-add callback

After the right child returns, the live frame contains its parent's
accumulator and the saved left factor. The callback mounts the coefficient
arithmetic on these fields and the returned value. It then clears the two
consumed factors and resumes the parent's scan with its updated accumulator.


### `Advice`

 Persistent arithmetic inputs for a Schur product, consisting of the prime, a zero word, the
extension degree, and the reduction coefficients. 

### `Aux`

 Private stacks and persistent arithmetic inputs for the multiply-and-add callback. 

### `port`

 Connect the arithmetic routine to its auxiliary stacks and to the Schur frame's left
operand, returned right operand, and accumulator. 

### `expected`

 Initial arithmetic stack contents, with empty private stacks and the field parameters
encoded at limb width `v`. 

### `Ready`

 The other auxiliary ports are available for the query description and
the controller's remaining subroutines. 

### `machine`

 Add the product of the saved left factor and the returned right factor to the parent
accumulator, then clear both factors. 

### `callCap`

 Step bound for the multiply-and-add callback, including the cost of clearing two scalars of
`e*v` bits. 

### `machine_runs`

 The precise multiply-and-add execution required by the engine's contracts.
The stored stack history and the entire auxiliary bank are preserved. 
