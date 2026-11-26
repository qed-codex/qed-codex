---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CanonicalWordProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CanonicalWordProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CanonicalWordProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Canonical unsigned binary output by a fixed finite word program.
The program reverses its input, removes high zeroes, reverses back, and emits
one false bit in the empty case. All source stack prefixes have a linear local
bound. No algebraic construction is imported to implement normalization. 

### `normalizeUnsigned`

 A single fixed finite control table, independent of input length/value. 

### `normalizeUnsigned_prefix_space`

 All stacks of the normalization subroutine are bounded at every source
instruction. Its own linear runtime is used only for this local routine. 
