---
{
  "module": "OAI/Computability/VPVNP/RAMSortPulse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortPulse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortPulse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean bitonic sequences

A cyclic block of consecutive ones describes the thresholded input to a
bitonic merge. Comparing opposite positions splits the block into two
shorter blocks, independently of its starting position.


### `pulse`

 A periodic sequence whose first `ones` positions after shifting are true. 

### `pulse_and`

 The smaller Boolean output at each opposite pair is a pulse with the
excess over half the original width. 

### `pulse_or`

 The larger Boolean output at each opposite pair is a pulse capped at
half the original width. 

### `pulse_of_segments`

 A rising segment at cut `a` followed by a falling segment at cut `b`
forms one cyclic pulse of length `n - a + b`. 
