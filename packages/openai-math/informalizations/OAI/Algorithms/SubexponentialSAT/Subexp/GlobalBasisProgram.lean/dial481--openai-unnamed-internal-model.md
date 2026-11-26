---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed global basis-bundle source program

All iteration counts, local matrices, and packing data are runtime words.
The program first selects the current type's local-search group.  It emits
inner matrices while counting colors downward, then emits the outer matrix;
prepending complete records gives the public outer-first, ascending-color
bundle order.  Every matrix row is generated in ascending ambient order.

Persistent inputs: scalar frame width/zero/one on 13/14/15, unary type index
32, packing table 33, universal type records 37, unary color count 38,
unary ambient dimension 46, grouped local
search records 47, unary block count 48, and unary leftover count 49.
The final encoded bundle is on 63.  Its records contain a framed unary
column count followed by a frame containing flat row-major scalar frames.
Port 39 is unused and preserved; no canonical-bit promise on a saved width
word is needed by the head-only Side filter.

This file defines the concrete finite source composition.  Its complete
execution/refinement proof is a separate remaining integration obligation.


### `splitPorts`

 Temporary decoding for one inner matrix. Only the actual split word is
needed by the kernel-column generator; the other decoded fields are cleared. 
