---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairDeterministic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairDeterministic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairDeterministic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Indexing a deterministic stage by its verified empty-choice execution

The invariant consists of the unconsumed part of the verified run. Exact
use of the input choices implies that every other accepted path begins
with the same calls and reports.


### `deterministicIndexed`

 Index a deterministic stage by the unique unit value when its verified all-empty-choice
segment terminates, fits the linked clock, and preserves the tag on returns. 

### `deterministic_reports`

 Replaying the unique stage path returns the original, concrete reports. 
