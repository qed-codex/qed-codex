---
{
  "module": "OAI/Computability/VPVNP/PairNativeLeafSetupTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeLeafSetupTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeLeafSetupTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # One native instruction block for initializing a vertex's leaf verifier

The first part installs the descriptor geometry and supplies the cache base
to the operand compiler. One deterministic jump enters the compiler, which
writes the 38 auxiliary-counter operands before returning to the vertex body.


### `Placement`

 Register assignment for the terminal geometry and the auxiliary operand cache. 

### `Placement.degree`

 Fixed port degree of the final layer. 

### `Placement.numerator`

 Numerator of the live bucket exponent. 

### `Placement.denominator`

 Denominator of the live bucket exponent. 

### `Placement.frame`

 Registers used by the geometry reader and private store loop. 

### `Placement.cache`

 Registers used by the auxiliary operand compiler. 

### `Block`

 The geometry and cache components with the compiler's saved base register. 

### `frameFlow`

 Native geometry calculation preceding the private stores. 

### `cacheFlow`

 Native expression evaluator that precedes the cache writes. 

### `frameSize`

 Number of program-counter locations reserved for geometry installation. 

### `cacheSize`

 Number of program-counter locations reserved for the operand cache. 

### `size`

 Number of locations in the concatenated instruction table. 

### `framePC`

 Include a geometry instruction address in the combined table. 

### `cachePC`

 Include a cache instruction address after the geometry block. 

### `entry`

 First instruction executed by the geometry reader. 

### `cacheEntry`

 Destination of the jump from geometry installation to cache computation. 

### `done`

 Location where the caller's continuation replaces the cache return. 

### `handoff`

 Unconditional native jump to the cache initializer. 

### `row`

 Opcode of the combined table with all program counters relocated. 

### `template`

 Standalone eleven-operand table with an accepting continuation. 
