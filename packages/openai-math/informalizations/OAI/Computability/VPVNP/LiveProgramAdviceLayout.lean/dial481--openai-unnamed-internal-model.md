---
{
  "module": "OAI/Computability/VPVNP/LiveProgramAdviceLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The live program's concrete advice allocations

The length, prefix and order stages use the public expressions installed in
the linked program. A single upper bound on the end of the order map puts
all their public addresses, lengths and scheduled cursors in range.
The physical header length bounds the distributed source interval, and the
prefix capacity bounds the number of packed prefix words.


### `bank`

 Evaluate a bank of public geometry expressions and encode each result as a word of the
geometry's width. 

### `preparedLayout`

 The actual three operand rows meet every address, count and disjointness
hypothesis of the four-stage native advice initializer. 
