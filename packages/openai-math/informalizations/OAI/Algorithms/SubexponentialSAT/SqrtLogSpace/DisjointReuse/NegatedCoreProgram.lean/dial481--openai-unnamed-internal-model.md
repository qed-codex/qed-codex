---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/NegatedCoreProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/NegatedCoreProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/NegatedCoreProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete negated singleton generation for the disjoint B child.
The fixed routine consumes a unary literal-record list on stack 0 and prepends
its negated singleton clauses to the encoded formula on stack 2. 

### `prefix_stackBits_le`

 This polynomial-time phase bounds every intermediate stack, including scratch.
The primitive tape-span transfer is a separate compiler theorem. 
