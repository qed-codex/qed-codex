---
{
  "module": "OAI/Computability/VPVNP/LiveTerminalReachableFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveTerminalReachableFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveTerminalReachableFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # All reachable terminal reports preserve a selected cell

The forced empty-choice prefix uses its chronological input memories. The
subsequent calls may halt or continue. Both outcomes preserve the word
whenever their actual reachable source table preserves it.


### `PreservesCell`

 A frame for every successful call, including the final accepting call. 

### `reached_after_empty_call`

 Each reachable boundary is either the starting one or a boundary in
the suffix of the forced call. 

### `preservesCell_after_replayed_prefix`

 Replay the deterministic reports on their actual incoming memories, then
apply the suffix's frame to every successful call, including a halting one. 

### `SourceReachable.reached`

 A physically reachable pair source has the same continuing history
in the ordinary burst RAM semantics. 

### `Protected.ofPreservesCell`

 Use a full reachable frame on the source's tag to establish the pair
linker's invariant, even when a partial computation cannot be extended. 
