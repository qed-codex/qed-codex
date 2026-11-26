---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the cursor input frame in the tight descriptor layout

The chronological row count is already in the workspace at offset eight.
From that count the pair-ABI program recovers the number of compression
blocks, the lane exponent and the first level address. It places eight raw
words in the active frame. Their destination points to eight persistent
scalar cells in the first level, starting at offset six.


### `operand`

 The formula compiler uses the actual pair ABI's workspace, input length and address width. 

### `firstLevel`

 Expression locating the first level header immediately after the calendar's fixed-width
directory rows. 

### `persistentBank`

 Expression locating the persistent cursor bank six words into the first level header. 

### `calendarBlocks`

 Recover the number of complete repeated blocks from the published row count. 

### `raw`

 Eight published raw words consumed by the cursor parameter program. 

### `table`

 The pair ABI exposes all the operands of the native frame publisher. 

### `Ready`

 Inputs available at normal entry after the calendar has published its count. 

### `raw_values`

 The row's eight native word expressions are exactly the raw cursor parameters. 

### `prepare`

 Executing the pair-ABI publisher writes the raw bank at workspace offset nine.
It preserves the calendar count, the controller header and all other cells. 
