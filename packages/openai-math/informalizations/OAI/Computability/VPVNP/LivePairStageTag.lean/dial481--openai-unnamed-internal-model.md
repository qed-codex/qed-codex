---
{
  "module": "OAI/Computability/VPVNP/LivePairStageTag.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePairStageTag.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePairStageTag.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The nested stage tag of the compressed pair routine

During the first half the evaluator's old-state bank is unused. Its first
word immediately follows the live counter array, so its address is the sum
of the counter base and the two label counts. Five private instructions
compute this address at call entry. The linked pair table sees the original
eleven public operands and the computed tag address in its twelfth slot.


### `address`

 The nested pair tag cell immediately following the counter base and both label-count
intervals. 

### `data`

 Append the computed tag-cell address as the twelfth public operand of the nested pair
table. 

### `compile`

 Compile a twelve-operand linked table to the eleven-operand pair interface by computing its
tag address in five entry instructions. 

### `execute_start`

 Five deterministic ticks recover the extra operand. The original report,
including every continuing word, external access and binary choice, is then
returned exactly, at every runtime width and remaining fuel. 
