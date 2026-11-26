---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshMapWorkspace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapWorkspace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapWorkspace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform private workspace bounds for the actual refresh operand slices

All four kinds of physical operand start lie at most one maximum wire width beyond
the larger of the two node-buffer ends. Adding their raw width, including the full
selector suffix, needs at most one more wire width. The resulting bound also covers
absent endpoints, whose starts are nevertheless installed in the native descriptor.


### `operand_input_end`

 A single numerical address bound suffices for all raw fields, independent of their
presence at the local port and the values of the two private half-wires. 

### `headCapacity`

 Reserve the complete private descriptor or the expander pointer directory, whichever
needs more words. Both are consumed before the selector and label arrays. 

### `regions`

 Concrete scratch heads for a single refresh map. The histogram has its own
previously allocated range and may be shared across successive map calls. 

### `regions_ordered`

 Every array in the selected workspace meets its concrete address constraints.
The four scalar capacity bounds suffice for all selector choices and port incidences. 

### `plannedHeads`

 Online evaluation of the source and target heads uses the same stored repetition
word that the raw descriptor publishes. Only the reserved directory and histogram bases
come from the outer private allocation. 
