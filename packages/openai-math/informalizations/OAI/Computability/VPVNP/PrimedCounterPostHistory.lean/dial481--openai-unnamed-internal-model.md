---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterPostHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterPostHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterPostHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Execution of the entire native parser after input assembly

The machine starts with the actual assembled memory and advances one cursor
slot per clear, root initialization, node visit or histogram comparison. The
logical and native loops reject together. On success their final histogram,
mark and stack memories agree, the last report halts, and each call incurs at
most fourteen probes.


### `postItems`

 The scheduled parser and histogram operations after the two input passes for this pair. 

### `postTape`

 The sequence of private choice lists for the post-assembly operations, read from their
absolute slots. 

### `postLogical`

 Execute all post-assembly items in the logical parser from empty pending frames, empty
marks and a zero histogram. 

### `postNative`

 Run the same post-assembly choice lists on the native machine, beginning at the first
parser cursor with the assembled input memory. 

### `postRun_match`

 Success and rejection coincide on the entire native suffix. The relation
records exactly the memory with which the last report leaves the machine. 
