---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpaceNamed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceNamed.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceNamed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reachable space of a named stack bank

Installing a fixed bank of labeled stacks in the physical machine adds one
spare empty port. The size of its packed tape is the number of separators
plus the total bit count in the named stacks.


### `reflect_reach`

 All reachable numbered banks have a corresponding reachable named bank. 

### `installed_length`

 The one spare physical label is empty at initialization and stays empty. 

### `named_reach_packed_le`

 A size invariant on reachable named banks bounds every packed physical
instruction boundary, starting on the raw input tape. 

### `input_space`

 The two literal table heads stay in a fixed interval for every prefix
of witness bits, including padded execution after a halt. 

### `input_space_labeled`

 A bound on the total reachable bit count of the evaluator's named stack
bank gives a time-independent space bound for the compiled universal program. 
