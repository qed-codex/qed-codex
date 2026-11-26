---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackFrameField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackFrameField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackFrameField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Saving and restoring one variable-length Schur frame field

Saving empties the live register and prepends the tagged field to its history
stack. Popping uses the evaluator's existing self-delimiting field reader.
Both routines use a fixed control independent of the register width.


### `WritePhase`

 Control phases for moving a field's bits into its delimited history encoding. 

### `Port`

 The ten live-field ports together with the ten corresponding history ports. 

### `pushField`

 Move the live field at index `i` into its history stack using the frame-field encoding. 

### `popField`

 Restore the most recently saved field at index `i` from its history stack. 

### `registers`

 Combine the live and history banks into the stack state of the frame store. 

### `pushField_runs`

 Move one live field to its history, preserving every other field. 

### `popField_runs`

 Restore the top self-delimiting field and retain the rest of its history. 
