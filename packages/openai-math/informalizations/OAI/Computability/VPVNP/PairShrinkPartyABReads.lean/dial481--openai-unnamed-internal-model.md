---
{
  "module": "OAI/Computability/VPVNP/PairShrinkPartyABReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPartyABReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPartyABReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of a shrinking AB copy

The copy visits the old-port list in append order, resolves the selected
arc's thick rank, and follows the frame at that rank. Its source payload
lives in a private child packet. Only the published old level, incidence
columns, append list, rank column and slice bank are read externally.


### `Header.arc_reads`

 Access the identifier at the chosen position of the thick row. 

### `Header.frame_reads`

 The only additional indirect read in the frame expression is the rank
at the actual outgoing ID obtained from the old list. 

### `frame_lt_end`

 All three external reads of an indexed frame lie within its own AB bank. 

### `Job.ABAreas`

 External extents of the selected old-level data used by a native AB copy. 

### `InputsReadable`

 The enclosing shrink role provides these entry expressions. Its concrete
register ABI only reads the old level's degree-independent length word. 

### `Job.old_field_reads`

 A caller may supply any bounded old outgoing-ID expression, including
the CD rank-selection expression or one cell of the thick AB list. 

### `Job.ab_readBounds`

 External bounds for all six pointer-program operands and all three
direct frame reads at a genuine thick-wire visit of an active AB party. 

### `Job.abi_inputs_readable`

 The canonical six-register ABI satisfies the expression bounds from the
published level header alone. Its only external operand load is cell 17. 

### `Job.abi_ab_readBounds`

 Bound every AB setup and frame load for the register ABI installed in
the shrinking party evaluator. 
