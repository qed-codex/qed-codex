---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafRole.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafRole.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafRole.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The eleven-public-word leaf segment of the final-vertex program 

### `operands`

 The ten operand values appear in private registers on the native machine.
The caller's original eleven public words occupy the other side of the
verification machine's public bank. 

### `pubSlot`

 The position of a leaf operand in the ten geometry slots preceding the eleven original
vertex operands. 

### `body`

 A verifier body instruction with its registers placed in the host, calls directed to leaf
body labels and returns directed to the caller. 

### `instruction`

 Physical rows emit only register copies for the ten geometry fields. 

### `segment`

 The actual disjoint placement supplied by the vertex table uses the body
and geometry rows. An aliased placement outside that ABI rejects. 

### `Contains`

 The eleven-operand host machine contains every leaf instruction at the chosen label and
resized to its word width. 

### `inside`

 Host addresses of the leaf body, after its geometry reload. 

### `text`

 Verifier body code at a placed leaf-body label, with rejection at indices outside that
body. 

### `publicData`

 Prepend the ten loaded geometry words to the eleven public operands of the host vertex
machine. 

### `verification`

 The shadow machine that executes the leaf body using the extended operand table and
preserves access to the host caller. 
