---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorOrdinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorOrdinal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorOrdinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Incrementing a probe ordinal after recording it

The timestamp field of a probe is the ordinal before this increment. The
routine scans the ordinal word and scratch stack. It returns with the
incremented ordinal, or reaches the rejecting halt on overflow.


### `ordinalPorts`

 The incrementer's active word is the ordinal. Its other labels are
injected into the usual budget ports. 

### `finishProbe`

 Increment the probe ordinal after emitting its old value as the timestamp. Overflow of the
fixed-width word leads to rejection. 

### `finishProbe_run`

 Increment only the ordinal after its old value has been emitted. 

### `finishProbe_reject`

 Overflow reaches the rejecting row after exactly the same fixed-width
scan. It makes no further probe or program choice. 
