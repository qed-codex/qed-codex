---
{
  "module": "OAI/Computability/VPVNP/PairNativeCacheRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeCacheRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Executing the native 38-word private cache initializer

The prefix ends at the continuation supplied by the surrounding vertex
burst. The private cache holds every fixed virtual parameter and every
auxiliary public word. External memory and binary choices are untouched.


### `code`

 Arithmetic flow whose labels form the first part of the cache table in the enclosing
machine. 

### `storeSrc`

 Map each fixed leaf source to the enclosing machine register read by its private store
instruction. 

### `ptr`

 Enclosing machine register that points to the private cell for the next cache store. 

### `one`

 Enclosing machine register containing the unit increment used to advance the cache cursor. 

### `run`

 Native evidence for the one private computation that prepares the leaf
cache, including the caller's register and private-memory frame. 
