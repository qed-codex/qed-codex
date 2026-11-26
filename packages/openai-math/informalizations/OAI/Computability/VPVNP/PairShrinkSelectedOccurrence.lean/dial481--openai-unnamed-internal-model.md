---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSelectedOccurrence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSelectedOccurrence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSelectedOccurrence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The selected shrinking state and packed argument at a physical site 

### `shrinkLevel`

 The selected chronological level at a particular scheduled shrink degree. 

### `of_selected_shrink`

 Specialize a dependent statement about a selected shrinking level and
its output site to the actual input state, selection and scheduled index. 

### `ShrinkOccurrence`

 The operands and numerical ordinal of the map row chosen by this level.
Its input and selection are recovered from the actual stored pass origin. 

### `ShrinkOccurrence.i`

 The degree transition in the fixed block schedule. 

### `ShrinkOccurrence.lanes`

 The number of residual lane coordinates. 

### `ShrinkOccurrence.state`

 The original state before this transition. 

### `ShrinkOccurrence.selection`

 The admitted choice at each motif of the input state. 

### `ShrinkOccurrence.site`

 The native packed output site addressed by the vertex reader. 

### `ShrinkOccurrence.halves`

 The independent input half of this row in both network presentations. 

### `occurrence`

 Decode the selected output occurrence, preserving its site and chronological ordinal. 

### `ShrinkSite.occurrence`

 Resolve a physically decoded shrinking-row address to its kernel operands. 

### `ShrinkOccurrence.nextState`

 The native output state read at a recovered shrinking occurrence. 

### `halfEquiv`

 Both directions on independent output half assignments of the real map row. 

### `halfEquiv_packed`

 The address-level conversion preserves the literal packed bit list,
including the ordering of the incoming and outgoing halves. 
