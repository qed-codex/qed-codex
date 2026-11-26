---
{
  "module": "OAI/Computability/VPVNP/CompressorBranchSegments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBranchSegments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBranchSegments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Factoring a native compression pass at its term-selection row

Every surrounding descriptor scan has a verified run on empty choice tapes.
An accepting stream must follow those scans exactly. The selector row is
inverted on the actual intervening memory, and its source-worker inverse
recovers the selected term. Concatenation preserves the remaining native
calls, their reports and the memory used by the next compression level.


### `Segment`

 A finite initial portion of a run of the fixed table. 

### `Segment.bits`

 One choice tape for each successive native call in the segment. 

### `Segment.logs`

 Reports returned by those calls, in execution order. 

### `state`

 The cursor returned by the segment, computed from its initial state and reports. 

### `memory`

 External memory obtained by applying all events in the segment to its initial memory. 

### `append`

 Concatenate consecutive runs, feeding the first segment's ending cursor and memory to the
second. 

### `empty`

 The zero-call segment with empty tape and report lists. 

### `remainder`

 Once the choice prefix is known, the reports and continuation memory
are uniquely determined by native execution. 

### `Cut`

 Distinct mathematical choices have incompatible prefixes on the physical
tape, and every accepting run starts with one of these prefixes. 

### `Cut.part`

 The initial native segment associated with each possible branch index. 

### `split`

 Restore the precise logs and native execution of the suffix. 

### `bind`

 The next branch tree is chosen in the actual memory left by this one. 

### `deterministic`

 A run on empty choices is forced call by call, even if a later term
selection has no valid branches. 

### `before`

 Prepend a forced part without adding an index to the selected terms. 

### `afterChoice`

 Attach the forced output-directory scans for each selected term. 

### `pathsEquiv`

 Physical path bijection, retaining a cap or observation on the entire
concatenated report sequence. 
