---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkHeaderGreedyTapes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkHeaderGreedyTapes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkHeaderGreedyTapes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Branch tapes in the shrinking header and greedy visits

For a successful native call the supplied branch tape equals the choice
bits in its report. The three header visits and six greedy visits all
produce empty tapes, including the indirect operand readers.


### `greedy_reports_empty`

 All reports of the six native greedy visits have empty branch paths. 

### `empty_choices`

 In any chronological packetization of these actual source reports, every
individual call consumes an empty branch tape. 
