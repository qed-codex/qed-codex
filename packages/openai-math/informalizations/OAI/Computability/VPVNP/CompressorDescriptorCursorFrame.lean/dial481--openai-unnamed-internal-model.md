---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorCursorFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorCursorFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorCursorFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Persistent cursor parameters from the pair ABI

The native parameter body reads the eight inputs prepared at workspace
offset nine. A seventeen-word loader starts at the workspace base, using
the last eight cached words for the body. The body publishes the eight
computed cursor fields at level zero, scalar offset six. A final native
copy restores the computed fields to the active frame for the stride pass.


### `loader`

 The loader uses workspace public slot two and the input bank at offset nine. 

### `saved`

 The eight reserved scalar cells begin immediately after the six live level scalars. 

### `outputs`

 The cursor parameters consumed by the scalar, stride and incidence passes. 

### `loaderReport`

 The parameter-loader report, including its reads of the external frame, writes of the
computed operands and returned cursor. 

### `publish`

 With the prepared bank in memory, the compiled pair-ABI call writes the
persistent bank, changes no other external word and uses 25 probes. 

### `copy`

 Read the computed persistent words into registers before writing their
active-frame copies. 

### `copyTable`

 The persistent-frame copy instruction table with its public operands embedded in the pair
machine's eleven-word bank. 

### `copy_run`

 Copying uses the stored chronological row count to locate the first level. 

### `Trace`

 The reports refer to the actual entry memory of each successive stage. 

### `Trace.raw`

 Report publishing the raw input-length, geometry and address operands of the cursor
  frame. 

### `Trace.loaded`

 Report loading the raw frame and computing the final cursor parameters. 

### `Trace.copied`

 Report copying the final cursor parameters to their persistent level-zero locations. 

### `Trace.postRaw`

 External memory after executing the raw parameter publisher's report. 

### `Trace.postLoad`

 External memory after the raw publisher and parameter loader reports. 

### `Trace.post`

 External memory after the raw publisher, parameter loader and persistent frame copy. 

### `Trace.log`

 The three descriptor-parameter reports in their execution order. 

### `trace`

 Construct the raw, loader and copy reports using the specified cursors and each preceding
report's output memory. 

### `run`

 Execute the three fixed pair-ABI tables. Each entry state may be chosen
by its enclosing linker. Both banks contain the actual cursor parameters,
and all other memory, including the row count, is preserved. 
