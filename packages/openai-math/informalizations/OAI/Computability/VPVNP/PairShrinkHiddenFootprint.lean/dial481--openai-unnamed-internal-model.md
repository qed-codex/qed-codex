---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses read by the absorbed-field scan

The setup reads five cells in the old-level header. The loop reads the
owner count, one dense ID per field, and the repetition and payload cells
of the selected term. The private guesses perform no external accesses.


### `Header.trace_reads`

 All chronological header probes belong to the five selected cells. 

### `FieldCells`

 The three addresses of one field's actual external reads. 
