---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native loop control for a placement-fiber argument scan

A three-instruction test exits on an empty row. On a nonempty row it removes
one unit from the child counter and enters the descriptor-address block.
The scan consumes only the supplied argument bits and returns with the
unconsumed suffix and the remaining private memory available.


### `Prefix`

 A linked prefix that consumes exactly its own list of choices. 

### `slotRegs`

 Slot routines use the first nine registers of the enclosing loop. 

### `guard`

 The loop branches to the address calculation or to its continuation. 

### `GuardLinked`

 The machine contains the three child-loop guard instructions at the specified counters.
With its unit register set, the guard returns on a zero count or decrements the count and
enters the child body. 

### `guard_empty`

 The empty loop exits without consuming a choice or changing the argument buffers. 

### `guard_cons`

 For a nonempty child row the guard subtracts one in the word register,
retains the source pointer and enters the single common child body. 
