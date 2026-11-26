---
{
  "module": "OAI/Computability/VPVNP/RefreshHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local records of a degree refresh

Each physical port keeps exactly one old vertex. Its kernel checks the two
diagonal segment equalities and evaluates one expander-motif entry. The demand
arguments read the old half-wires and the two lists of external segments. The
supply arguments use the two directions of the inner expander slots. The
remaining slot fields, including the external and padding wires, are recorded
by the common pass constructor.


### `placedPort`

 Identify old sites with physical ports in the dyadic refresh. 

### `segmentWidth`

 The actual outgoing and incoming segment widths at the indicated port. 

### `refreshLocalRecords`

 Local views used by the refresh map. `Fin 3` distinguishes the motif map
from the two diagonal equality checks, whose scalar degree is zero. 

### `refreshExtraCount`

 A degree-dependent upper bound on the counts of the local descriptors,
including the complete demand and supply argument views. 

### `refreshLengthConstant`

 An integral constant large enough for both refreshed widths and expander entry degrees. 

### `refreshPreimage_card`

 The placement is a bijection even when it is viewed in the term's own output coordinates. 

### `refreshPass_records_bounded`

 The chosen layout and every local field and monomial-degree descriptor
satisfy the one-step bound with constants independent of the lanes and old widths. 
