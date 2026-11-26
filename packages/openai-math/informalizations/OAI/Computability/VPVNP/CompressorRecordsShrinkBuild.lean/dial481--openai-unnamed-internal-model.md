---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkBuild.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkBuild.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkBuild.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A shrinking pass on the represented RAM wire graph

The deterministic prefix ends at the actual term-chooser entry. Every admissible
term stream induces one chosen layout, its role and child lists, and a subsequent
width and slot construction. The last memory represents the precise next
compression state on the same branch. The computation retains the immediate
old-site preimages used by the backward history evaluator.


### `Complete`

 The stored outcomes of every native part of a full shrinking pass. 

### `Complete.selected`

 The chosen term and geometry runs extending this deterministic shrinking prefix. 

### `Complete.output`

 The native passes building the next state's widths and slot directory from the selected
  records. 

### `reports`

 The complete branch trace in prefix, selected-term and geometry, then output order. 

### `replay`

 The physical RAM memory after the entire branch is the post-memory of the slot construction. 

### `build_complete`

 Compile the actual wire-state transition for all admitted choices, in the same order
in which the fused term worker reads their canonical tapes. 
