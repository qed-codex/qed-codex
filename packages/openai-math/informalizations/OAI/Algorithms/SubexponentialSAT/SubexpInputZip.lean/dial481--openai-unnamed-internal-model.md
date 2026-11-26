---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpInputZip.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpInputZip.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpInputZip.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical pairing of row and input-coordinate streams

Two ordinary framed lists are read on stacks 0 and 1. The fixed program builds
the exact paired-record stream consumed by `SubexpDotControl`, on stack 6.
No array lookup, pairing, or serialization is a semantic machine instruction.


### `program_encoded_trace`

 The zipper consumes two separate input streams and produces the exact
paired stream used by the arithmetic loop, with a linear transition count. 

### `sourceBound_polynomial`

 Explicit polynomial bound for pairing, the dot loop, and canonical lifting
when the target width is (D+1) times the residue-word width. 
