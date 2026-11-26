---
{
  "module": "OAI/Computability/VPVNP/StructuredStackClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StructuredStackClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Stop bounds through deterministic prefixes of the transcript validator

A deterministic parser consumes a known number of steps before entering the
nondeterministic part of the validator. At that point every accepting or rejecting
branch has its own path length. A common bound on all leaves permits any larger
clock to be used without changing the path count.


### `StackRuns.stopsWithin_iff`

 The normal stop budget of a deterministic prefix is added to the budget at its exit. 

### `StopsWithin.stackPaths_eq`

 Once every leaf has halted, enlarging the budget preserves the entire multiplicity. 
