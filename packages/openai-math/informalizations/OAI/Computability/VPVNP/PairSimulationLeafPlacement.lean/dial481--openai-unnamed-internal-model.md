---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafPlacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPlacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPlacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Allocating the leaf role inside the final vertex instruction image 

### `Label`

 Labels of the cursor-leaf segment, covering both the private geometry loader and the
verifier body. 

### `Private`

 Only the nine common DFS registers are external to this allocation. 

### `labelCount`

 Number of instruction rows reserved for the leaf geometry loader and verifier body
together. 

### `privateCount`

 Number of leaf-local register names to reserve in the enclosing vertex image. 

### `labelIndex`

 Number the loader and body labels for placement in the leaf segment of the vertex
instruction table. 

### `privateIndex`

 Number the leaf-local registers for allocation in the vertex's register bank. 

### `Apart`

 Every shared DFS register has a physical index distinct from every leaf-local register. 

### `place`

 Assign a leaf body register to the shared DFS bank or to the private address, routing or
startup bank according to its name. 

### `bodyReg`

 The injective placement of all verifier body registers, using disjoint DFS and leaf-local
register banks. 

### `ports`

 Embed the geometry loader's source registers in the leaf-local operand bank. 

### `values`

 The ten physical registers receiving the geometry words used as operands by the verifier
body. 

### `loadPC`

 Place a private geometry-load instruction at its label in the combined leaf segment. 

### `bodyPC`

 Place a verifier body instruction at its label in the combined leaf segment. 
