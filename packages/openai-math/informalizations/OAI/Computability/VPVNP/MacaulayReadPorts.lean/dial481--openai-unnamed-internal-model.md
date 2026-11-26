---
{
  "module": "OAI/Computability/VPVNP/MacaulayReadPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Row and column ports of the physical Macaulay reader

The first two inputs of the row decoder refer directly to the caller's row
and column stacks. All other registers use a private bank. The six decoded
fields remain in that bank for the selected coefficient routine, while the
caller's addresses and field result stack retain their separate names.


### `Work`

 Private ports for the row decoder and the coefficient routine embedded in the reader. 

### `Bus`

 Matrix-entry reader ports for the row address, column address, result and private
workspace. 

### `route`

 Connect the decoder's first two input registers to the caller's row and column stacks. Its
other ports use the private decoder bank. 

### `auxBank`

 The caller has separate stacks for the two addresses. The unused private
aliases therefore carry empty strings. 

### `frame`

 Full reader frame with the two incoming addresses installed. 

### `dispatch_runs`

 Physical row dispatch on the ordinary reader ABI. All other ports keep
their actual caller state, including the field result stack. 

### `setAddresses`

 A caller can reset its external addresses without clearing the private
register bank. Only the two aliased registers are affected. 
