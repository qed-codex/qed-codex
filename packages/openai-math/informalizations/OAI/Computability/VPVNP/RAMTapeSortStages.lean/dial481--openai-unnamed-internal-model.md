---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable local sorting of the transcript records

The nested stage and offset loops run on the literal site stacks. For every
input bit vector, they consume exactly the suffix after the two successor
fields, materialize the selected block and retain every validity flag.


### `Port`

 Registers for the phase and stride scheduler together with the registers used by each
sorting layer. 

### `program`

 Run the finite bitonic sorting schedule with the physical single-layer routine at every
stage. 

### `data`

 State between stages, with the actual remaining incident stream. 

### `result`

 Fold the site replay update over all bitonic stages on the combined row and site address
bits. 

### `run_incident`

 Every finite stage callback returns on every raw slot and field value.
Only the public stream lengths enter the clock. 

### `run_checked`

 The program returns the same decision as the word-level validator.
On every accepted input it returns the same parsed block, including the
final padded record used by the boundary pass. 

### `run_messages`

 On the actual live processor input, the final flags check every sorting
send and receive and the successful output is the typed validator's block. 
