---
{
  "module": "OAI/Computability/VPVNP/PairNodeDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dispatching an ordered history visit by its recorded role

The common DFS pop leaves the absolute descriptor address in register 7.
A single external word lookup selects the cursor leaf, six-party shrinking,
or degree-refresh entry routine. The six instructions preserve the
private stack, histogram, pending suffix and the node address itself.


### `Role`

 The three handlers for a visited DFS node are the cursor leaf, the six-party shrink step
and the degree refresh step. 

### `role`

 Decodes the stored role word. Zero selects the leaf handler, one selects shrink, and every
other value selects refresh. 

### `instruction`

 Fetch the role word from the side table indexed by the absolute
descriptor address. Only two temporary registers are modified. 

### `Linked`

 Requires the machine to contain all six dispatcher instructions at the specified program
counters, with the supplied register placement, role-table offset operand and handler entry
points. 

### `events`

 Trace for dispatching one node. The external read is at offset + node, and a nonzero tag
takes one further tick to distinguish shrink from refresh. 

### `enter_loaded`

 The common five rows after the offset load work for either a public
word or a base obtained from the terminal geometry record. 

### `enter`

 The fetched word selects the corresponding native continuation without
consuming any of the remaining private choices. 

### `parser`

 Parser of the actual dispatch opcode, retaining its deterministic
prefix in the visit path. 

### `parser_exactOn`

 Exact leaf, shrink and refresh handlers at their native entry labels
compose with the fixed role router, on successful reads and rejection. 

### `parser_exact`

 Exact leaf, shrink and refresh handlers at their native entry labels
compose with the fixed role router, on successful reads and rejection. 
