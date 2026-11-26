---
{
  "module": "OAI/Computability/VPVNP/PairTerminalShadowTransfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalShadowTransfer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalShadowTransfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preservation of the histogram descriptor through actual pair-stage transfers

A completed native stage can write the pair tag below the workspace. The
tag follows the grammar and motif counter arrays, whereas the auxiliary
histogram descriptor immediately precedes those arrays. Thus neither a tag
transfer nor a write in the compression workspace changes the shadow length.


### `histogramCell`

 Physical address of the auxiliary histogram descriptor's target word. 

### `histogramCell_report`

 Literal report emitted by the outer pair linker, including its transfer
when a source stage accepts. 

### `histogramCell_reports`

 Each source report writes in the workspace. The actual chronological
sequence may transfer the pair tag arbitrarily many times. 
