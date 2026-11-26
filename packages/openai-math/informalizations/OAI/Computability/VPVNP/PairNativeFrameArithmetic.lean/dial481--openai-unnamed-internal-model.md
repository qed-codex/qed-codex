---
{
  "module": "OAI/Computability/VPVNP/PairNativeFrameArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word arithmetic for the terminal vertex's pair frame

After the six descriptor reads, the native program computes the histogram
base, graph arena, cache base and remaining frame fields. Each equality is
in the machine's word ring, so the code equations also hold when an
intermediate wraps.


### `arithmetic`

 Native program that constructs the fixed degree in register 16 and uses the loaded header
words to compute the private frame addresses. 

### `argumentStride`

 Word distance between consecutive node argument packets, equal to twice the degree times
the public input length plus one. 

### `histWord`

 Histogram base as a machine word, obtained by skipping one argument packet per address
below the exclusive end of the node rows. 

### `graphWord`

 Base word of the graph arena and its geometry frame, immediately after the histogram's
public number of label slots. 

### `arithmeticBank`

 Register bank obtained by installing the degree in register 16 and carrying out the frame
arithmetic updates in instruction order. 

### `arithmetic_run`

 The fixed post-read program emits only ticks, for an exact cost of the
degree plus eighteen native instructions. 

### `ArithmeticValues`

 Register equations after address computation, including the graph, histogram and cache
bases, the frame fields, and preservation of the loaded descriptor registers. 
