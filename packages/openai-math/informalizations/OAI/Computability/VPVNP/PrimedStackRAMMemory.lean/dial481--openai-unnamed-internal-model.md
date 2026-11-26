---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External memory and the preorder stack

The two frame planes store the stack from bottom to top. The pointer cell
contains its length, so the degree and state of the top frame have index
one less than the pointer. The typed scratch addresses give the frame rules
for the other words in the rectangle.


### `Locations`

 Typed parser scratch cells for two groups of `R` input rows, `n` frame slots, `m`
positions, and a histogram indexed by the grammar’s production labels. 

### `noncomputable local instance : DecidableEq (Locations R n m H)`

 Classical decidable equality on typed parser locations for updating one cell in the
scratch-memory view. 

### `degCell`

 Cell in the degree plane that stores degree minus one for the frame at stack slot `i`. 

### `stateCell`

 Cell in the state plane that stores the nonterminal state for the frame at stack slot `i`. 

### `markCell`

 Mark for input position `i`, used to detect a repeated position during a parse. 

### `countCell`

 Histogram cell counting uses of the production with dense label index `i`. 

### `depthCell`

 Single scratch word holding the current stack length, which also indexes the next free
frame slot. 

### `publicData`

 Runtime public word table. The input base is the start of the assembled rows. 

### `view`

 Read a typed parser location from external memory using the scratch layout based at `base`. 

### `store`

 Write to a typed cell. All other scratch coordinates retain their previous values. 

### `Represents`

 Stack representation for a list of frames in preorder (top first). 

### `represents_push`

 Storing a frame in the first free slot and incrementing the depth represents a push. 

### `push_rep`

 The compiled push inserts the two actual words and preserves every
older pending frame. 

### `pop_rep`

 The compiled pop returns the abstract top frame in the two destination
registers and represents the exact remaining preorder stack. 

### `mark_cell`

 The location test reads its own mark and succeeds with exactly that mark set. 

### `increment_cell`

 A valid counter increment writes only the indexed production's cell. 
