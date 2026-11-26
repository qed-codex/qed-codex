---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reachable memory frames for nested compressed-pair stages

A prefix is traced on the original finite table at its actual reduced clock.
At the outer level, only the stage named by the current tag can produce a
report. Thus an address frame need only be checked on that selected table at
the physically reached cursor and memory.


### `SourceReachable`

 Prefixes on a selected original component, before any pair-tag transfer. 

### `Protected.ofSource`

 Recover the inner tag invariant from an external-address frame for actual
continuing executions of the original online or terminal instruction table. 

### `preservesOuter`

 Protect the live outer tag across every native prefix of the concrete
nested table. A malformed inner tag rejects before any source instruction.
For a valid tag the source-frame obligation uses only the selected stage. 
