---
{
  "module": "OAI/Computability/VPVNP/PairNativeFrameDescriptor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameDescriptor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameDescriptor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Geometry fields of the native terminal bootstrap and prefix scan

Six header cells survive the width-prefix scan. The separately computed
role offset is passed in a saved register. Together these seven values
determine the geometry installed by each final vertex.


### `Readback`

 Agreement of six terminal-header cells with the supplied row interval, row stride, two
radices and auxiliary shadow span. 

### `Readback.addHistogram`

 A completed vertex adds its histogram strictly below the terminal
header. Every following vertex therefore reads the same six operands. 

### `Readback.fields_eq`

 Pointwise coincidence of all twelve stored words with the terminal
layout, including the histogram, live role displacement and cache base. 

### `Readback.pointer_before`

 The pointer at live length lies below the geometry, since the private
layout contains an argument interval for each absolute node address up to
the exclusive row end. 

### `Readback.leaf_operands`

 The genuine decoder's address, radix and span data from the same
selected bootstrap and the prepared auxiliary shadow. 
