---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpJetCellProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpJetCellProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpJetCellProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete addition into one packed jet cell

The persistent jet, unary index, and cell width are on stacks 102, 103, and
104. The array subprogram uses 112--117, and order-preserving moves use 118.
All instruction tables are fixed independently of widths and indices. The
full service reads the old cell, invokes the actual flattened quartic adder,
and writes the sum back. Its endpoint changes only the contribution and jet
stacks; all other caller stacks and registers 8--15 are preserved.


### `flat_encode_eq_block`

 The arithmetic controller and the dense serializer use the same four
stored words, including their order. 

### `updatedState`

 The explicit state expression obtained by composing the eight services. 

### `encode_prepareZero`

 The concrete prepared zero is exactly the all-false fixed-width cell. 

### `updateCell_eval`

 Exact stack endpoint: only the consumed contribution and selected jet
cell change. The persistent index and all other caller stacks are preserved. 

### `updateCell_typed_eval`

 The packed-array theorem specialized to actual typed coefficient cells.
No decoder or abstract array callback is assumed. 
