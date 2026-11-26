---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/TupleProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/TupleProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/TupleProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control Cartesian tuple generation

Alphabet words, tuple payloads, and iteration depths are stack data.  The
instruction tables below do not depend on any of their lengths.


### `escaped`

 Frame payload without its final delimiter. 

### `escapeProgram`

 Consume a reversed payload and prepend its escaped forward payload.
The caller supplies frame/list delimiters. 

 The fixed ABI uses ten Boolean registers and nine Boolean stacks:
0 prior tuples, 1 saved alphabet, 2 current reversed tuple, 3 alphabet cursor,
4 reversed word, 5 output, 6 copied tuple, 7 copy scratch, 8 unary depth.
Registers 0--2 and 3--5 belong to the two framed iterators, 6--7 are scratch,
and 8--9 belong to the eventual depth loop. 

### `cartesianProgram`

 The Cartesian expansion has one fixed finite control table. 

### `expandStep`

 Reuse the same tuple storage after each Cartesian expansion. Two actual
stack transfers restore the forward serialized order. 

### `powerProgram`

 Runtime unary iteration of one fixed Cartesian expansion. 

### `initCmd`

 Install the constant singleton empty tuple and empty output list using
eight real bit instructions. No tuple array is supplied by the caller. 

### `generateProgram`

 One finite instruction table for all alphabets and all tuple dimensions. 
