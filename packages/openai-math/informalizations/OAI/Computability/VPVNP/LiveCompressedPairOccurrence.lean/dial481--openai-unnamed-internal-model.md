---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairOccurrence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairOccurrence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairOccurrence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compressed path occurrences and the native exponent-stage handoff

The ordinary completion of the pair table is followed by one outer tag
write. The header interval and all dense counter addresses lie beyond the
tag. The output of the simulator can therefore be read at its actual
word addresses by the subsequent exponent check.


### `Execution`

 Facts measured on the actual native pair table and its real prepared
input. The path correspondence covers both directions of accepting tapes.
It records the selected descriptor and site streams via `SelectorReindex`.
The output and bounds below concern its unrelocated reports. 

### `Execution.encoding`

 The trace encoding that records the selector and traversal choices of each mathematical
  occurrence. 

### `Execution.emission`

 The reindexing that emits and decodes the encoded selector choices for the physical
  execution. 

### `Execution.paths`

 The equivalence between emitted selector traces and accepted native pair paths on the
  prepared input memory. 

### `counter_address`

 Each physical array read by the exponent stage names the corresponding
dense counter cell in the native simulator's final memory. 

### `Execution.pairCall`

 Construct the single compressed component of the first-half chronology
from its native execution, preserving the accepting tape and all counters. 
