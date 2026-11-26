---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/BinaryCompareProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/BinaryCompareProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/BinaryCompareProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Minimal actual binary comparison, extracted from SubexpGuardProgram.
Only the concrete Boolean borrow operation and fixed comparison machine are retained.
The source map and hashes are recorded in verification/counting-draft/worker04/extraction.json. 

### `carry`

 Borrow propagation with implicit high zero bits. 

### `carry_iff`

 The final borrow is the strict comparison, even for unequal word lengths. 

### `program`

 Eight one-bit registers, two stacks, and twelve fixed labels. Register zero
is the result; both operand stacks are consumed. Entry resets the borrow bit. 

### `round_trace`

 A concrete nonterminal round, including its branch instruction. 

### `loop_trace`

 Exact instruction count for the data-dependent loop. 

### `run`

 Complete comparator contract. Leading zero bits and unequal widths are allowed. 

### `restrictState`

 Restrict caller data to the fixed ports of a subroutine. This is assertion
notation, not an instruction available to the program. 

### `compare_call`

 A measured comparison call on fixed injective ports, with every other
caller register and stack preserved. 
