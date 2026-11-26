---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native instruction image of a descriptor leaf

The address reader shares the DFS node slot. A transit cursor returns directly
from the route check. At cursor zero, seven instructions copy the site and header
and supply the two private-memory pointers to the stack initializer. The
initialized stack pointers are the ones used by the auxiliary processor.


### `Label`

 Internal labels of the leaf call. The return label belongs to its caller. 

### `Reg`

 The address reader uses the caller's node register and eight private slots. 

### `Pub`

 Public operands of the leaf image, grouped into address fields, private arena fields, and
input size. 

### `dfsReg`

 Embed the nine caller DFS registers into the register bank of the linked leaf. 

### `leafReg`

 Assign the address decoder's registers, sharing its node input with DFS register 7. 

### `routeReg`

 Assign the routing test's 32 registers to their slots in the linked leaf. 

### `bootReg`

 Assign the leaf initializer's registers to their slots in the linked leaf. 

### `bootPC`

 Locate an initializer instruction using its boot label in the linked leaf image. 

### `stackPC`

 Locate the specified native instruction row of an auxiliary stack-machine state. 

### `front`

 Connect the address decoder and routing instructions to the cursor-zero handoff and the
caller's transit return. 

### `instruction`

 Literal-width five retains the constants of the geometry and initializer
rows. The placement functions and the return label are supplied by the host. 

### `Linked`

 All native interfaces used by the caller's execution proof. 

### `Address`

 Canonical finite image with an accepting return. An enclosing DFS template
can instead use `instruction` at its own labels and supply its loop continuation. 

### `locations`

 Number the internal leaf instructions in the standalone template's address space, which
also reserves a return address. 

### `returnPC`

 The standalone template's designated return address, occupied by an accepting instruction. 

### `registers`

 Number the named leaf registers for use by the standalone template. 

### `publics`

 Number the named leaf operands for use in the standalone template's public data. 

### `template`

 The standalone native leaf program with five-bit literals, entry at the first
address-decoding row, and an accepting return instruction. 
