---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed stack table for a complete burst site

On entry the initialization record is staged and the parser has supplied the
local header, cuts and public budgets. Every call starts with fresh registers
and private log. Each probe first pays its unit, then stages its record, emits
it, and increments the ordinal. A returning call either starts another call
in this bucket or finishes the site. The normal exit exposes the padded record
block to the local bitonic and memory checks.


### `mapExits`

 Apply a continuation-label map to every normal exit of a fragment. 

### `Label`

 Locations in the site's call, probe, record and acceptance graph. 

### `route`

 Select the first call, a subsequent call, the final check or rejection. 

### `blocks`

 Fixed jump graph, instantiated once from a literal-width call template. 

### `Control`

 The finite control type obtained by linking the site's fragments. 

### `table`

 The executable stack instruction table for a fixed RAM template. 

### `atLabel`

 Enter the fragment belonging to a site graph location. 

### `segment_run`

 Physical execution of a segment of the actual graph, including its fuel
and choice cutoffs. 
