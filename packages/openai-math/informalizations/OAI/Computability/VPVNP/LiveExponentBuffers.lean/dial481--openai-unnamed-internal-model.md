---
{
  "module": "OAI/Computability/VPVNP/LiveExponentBuffers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentBuffers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentBuffers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The exponent stage on the paper's serialized cut buffers

The addresses are three disjoint flat arrays. The input and output buffers
contain the little-endian serialization of their exponent words. Processing
a label clears that label's counter word and leaves every other label's
initial increment available for its own row of calls.


### `counterAddr`

 Address of the increment word for a label. 

### `posWord`

 Encode the flattened address offset of a given label and exponent digit. 

### `BufferLayout`

 Data and address contract of the stage after the header and pair phases. 

### `BufferValues`

 The actual little-endian word arrays produced by the header scan. 

### `BufferValues.write_counter`

 Clearing a completed carry preserves both read-only arrays. 

### `wordRow`

 One row of the digit scan in its physical order. 

### `run_wordRow`

 Full native row specification on the actual serialized buffers. 
