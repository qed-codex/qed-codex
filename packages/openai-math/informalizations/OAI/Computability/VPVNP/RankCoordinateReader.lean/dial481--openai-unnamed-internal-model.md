---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Installing a scalar coordinate query in the weighted evaluator

The reader uses the live little-endian basis ordinals and the unary label without
copying. Its returned scalar is already on the next field multiplier's operand
port. The caller's product, field coefficients and remaining index registers are
outside the installed bank and survive every step of the query.


### `Port`

 Public input and scalar output ports of the coordinate reader together with its auxiliary
stack labels. 

### `mount`

 Wire the coordinate callback into the weighted evaluator's label, ordinal,
arithmetic-result, and auxiliary ports. 

### `bank`

 Assemble the label, current and next basis indices, result bits, and auxiliary stacks as a
reader configuration. 

### `install`

 Install the coordinate reader on the weighted evaluator's physical ports. 

### `ordinal`

 Encode the zero-based basis index, without changing its value, as a
least-significant-bit-first word of the evaluator’s index width. 

### `readsEntry`

 A returning native scalar query suffices for the evaluator's exact reader
contract. Current and next are in transition order, so a column-vector matrix is
queried at the transpose position. 

### `reclaim`

 The physical core may leave its finite scratch bank occupied. A fixed
cleanup pass discharges those ports while retaining advice and output. 
