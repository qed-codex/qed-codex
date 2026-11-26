---
{
  "module": "OAI/Computability/VPVNP/PairTraversalLowReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalLowReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalLowReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Low-address preservation in each selected traversal report

The reference traversal preserves the low workspace after each tag, leaf and
fiber call. The controller inserts read-only setup and reset reports between
these calls. Its actual traversal therefore retains the low word at every
call boundary, including the final sentinel.


### `Segment.replay_of_reference`

 The controller lifts a word preserved at all reference-call boundaries
to a word preserved at every controller-call boundary. 

### `selected_low_replay`

 Each native controller report in the selected traversal preserves every
address below the row base, on its actual input memory. 

### `selected_linked_low_replay`

 Any completed physical traversal-row phase has the selected raw reports
with precisely their terminal dispatch and handoff writes. Every report
preserves the requested low word, on the memory supplied to that call. 
