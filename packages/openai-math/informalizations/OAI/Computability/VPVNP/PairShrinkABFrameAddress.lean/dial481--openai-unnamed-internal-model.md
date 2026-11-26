---
{
  "module": "OAI/Computability/VPVNP/PairShrinkABFrameAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkABFrameAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkABFrameAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical pointers for the AB operand copies

The resident map supplies its dense motif ordinal. Dividing this by the
number of AB pieces selects a thick-wire list, in the order actually written
by the preimage scan. Its old arc ID locates the independent child half. The
rank at that same ID selects the source-major slice frame in the bundle bank.


### `Header`

 Operands available at the entry of a resident AB copy. 

### `Header.oldHalf`

 Private argument-arena parameters and incidence heads for recovering an old endpoint's
  half-wire address. 

### `Header.motif`

 Dense ordinal of the selected CD motif. Division by the piece count gives its bundle
  number. 

### `Header.lists`

 Start of the classified bundle rows containing original arc IDs in append order. 

### `Header.listStride`

 Distance in words between consecutive classified bundle rows. 

### `Header.rankBase`

 Head of the array mapping each old arc ID to its rank within its bundle. 

### `Header.banks`

 Base of the consecutive AB frame banks, one bank per bundle. 

### `Header.destination`

 Private staging address where this party gathers its AB demand word. 

### `Header.bundle`

 Quotient of the dense motif ordinal by the fixed number of pieces in each bundle. 

### `Header.piece`

 Remainder of the dense motif ordinal modulo the bundle's piece count, used to select the
frame column. 

### `Header.arc`

 The row contains original old arc IDs in append order. 

### `Header.frame`

 Address the three-word AB frame at the old arc's stored rank and the motif's piece number,
after the bundle's two width arrays. 

### `noncomputable local instance : DecidableEq X.Base`

 Classical equality on old base vertices for the thick-arc fiber and its ordinal
enumeration. 

### `members`

 Convert a fixed loop ordinal to the old thick arc encountered by the
original ID list. This is a bijection even if the key ordering differs. 

### `Header.Stored`

 Agreement of the evaluated AB header with the selected motif ordinal, classified lists,
rank array, frame bank, and private destination. 

### `Header.setup`

 The static pointer program for one frame in the thick-wire row. 

### `row`

 Logical copy at the actual old-ID row index. Its source and target offsets
refer to the same thick-rank / motif-rank frame as the pointer calculation. 

### `writes_operand`

 The final native column writes every coordinate of the selected resident
AB operand, although the original append order may differ from thick rank. 
