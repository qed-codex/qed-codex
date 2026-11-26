---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafBootRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafBootRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafBootRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The linked native rows for the complete cursor-zero leaf startup 

### `Reg`

 Register names for the scalar initializer together with 30 additional slots used by the
cursor-zero startup. 

### `incident`

 The incident-bit stack port of the concrete validator with 52 registers and 34 public
operands. 

### `scalar`

 Embed the scalar initializer's register bank into the physical startup registers. 

### `sources`

 Place the scalar initializer's source words, including the 34 public operands, in their
physical startup registers. 

### `geometryName`

 Assign the incident loader's 30 register indices to startup registers, sharing the
dimension, site address, bucket, word width and incident stack pointers with the scalar
initializer. 

### `geometry`

 The injective placement of the incident loader's geometry registers in the host machine. 

### `stack`

 Physical placement of the stack interpreter's named registers during cursor-zero
initialization. 

### `pointer`

 Physical placement of the allocation cursor, stride and stack registers used to assign the
validator's private stack intervals. 

### `cacheBase`

 Startup register holding the private address of the first cached operand. 

### `nodeBase`

 Startup register holding the base of the current node's private argument frame. 

### `tmp`

 Temporary register used while calculating the stack capacity. 

### `Label`

 Program labels for the startup prelude, the 38 cache reads and increments, the capacity
calculation, and the scalar and incident loaders. 

### `readPC`

 Jump to the cache read at the given index, or to the first capacity instruction when all 38
words have been consumed. 

### `scalarEntry`

 Entry label for allocating the first scalar port's stack, with the allocation finalizer as
the empty-list continuation. 

### `instruction`

 The startup instruction at a leaf-boot label, linking the cache scan and capacity
calculation to scalar initialization and the incident copy. 

### `Linked`

 Every startup label in the host machine executes its prescribed instruction with the
designated length operand and return label. 
