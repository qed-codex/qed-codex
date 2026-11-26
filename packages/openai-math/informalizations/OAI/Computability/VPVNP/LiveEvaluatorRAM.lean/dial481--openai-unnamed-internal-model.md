---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking one tape cell of a live evaluator transition

Each scheduled cell call reads one old symbol and one proposed new symbol.
The head-relative window is shifted cyclically at its endpoints. At a clipped
endpoint, the overwritten old symbol must be blank and the newly exposed
cell is checked against that blank. Thus every input and every output cell
is examined, including when the radius is zero.


### `Reg`

 The register indices of the 32-register native evaluator transition checker. 

### `Code`

 Native transition-checking code over 32 registers and a parameterized public operand bank. 

### `exits`

 Can this fragment reach its normal exit with the stated postcondition? 

### `compareCell`

 Compare the symbol at an output index to a specified register. 

### `moved`

 For a running target the old cell either maps to an adjacent output cell,
or leaves the window and pairs with the newly exposed blank. 

### `cell`

 Registers 0–3 contain their literal values, 5 is the target state, 6 and
7 are this tape's write symbol and move, 11 and 12 are the radius and last
cell, 13 is the old cell index, 14 and 15 are the old and new tape-field base
addresses, and 16 is the source state. Scratch registers are 17 and 19–21. 

### `destination`

 Destination of an old cell in head-relative word coordinates, with the
clipped endpoint paired to the newly exposed opposite endpoint. 

### `clipped`

 Whether the written old symbol would move outside the window. 

### `cellTest`

 Local condition on the two addressed memory words. The first condition
validates the source symbol, even if the transition overwrites it. A halting
target has zero in every cell. 

### `cell_exec_iff`

 Successful execution of the fixed cell code is equivalent to checking
the source, the clipped boundary and the proposed output symbol. 

### `reads`

 Certify a fixed read count for acyclic code with neither writes nor
choices. Both continuations of a comparison must have the same read count. 

### `cell_cost`

 Each successful cell check makes exactly two read probes, consumes no
choice bit and leaves the external memory unchanged. 

### `loopFree`

 Loop-free fragments have a fixed maximum instruction count across
all branch choices, independent of word width and tape radius. 
