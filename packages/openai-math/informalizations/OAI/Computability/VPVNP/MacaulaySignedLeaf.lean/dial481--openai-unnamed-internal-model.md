---
{
  "module": "OAI/Computability/VPVNP/MacaulaySignedLeaf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySignedLeaf.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulaySignedLeaf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Installing the signed coefficient routine on the Macaulay reader bus 

### `ports`

 Row and exponent inputs refer directly to the caller's register and
buffer. The result port belongs to the enclosing matrix reader. 

### `Loaded`

 Preloaded private stacks, including the checker advice, width words and
field modulus. The three externally aliased ports require no payload. 

### `bounded`

 A bounded run on the named coefficient bank lifts to a returning reader
arm. The input registers, payload, flags, and both scan buffers are restored. 
