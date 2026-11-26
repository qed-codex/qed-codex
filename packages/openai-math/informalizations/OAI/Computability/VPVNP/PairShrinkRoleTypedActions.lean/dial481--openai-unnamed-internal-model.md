---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleTypedActions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleTypedActions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleTypedActions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed resident actions for the parsed raw field lists

The old children and hidden rows have unique typed encodings. A list of
resident actions may therefore be indexed by the physical readers' outputs.
On every completed parse the recovered values are exactly the supplied fields.


### `recover`

 Decode a value in the image of a fixed injective encoding. The default only
serves to define a total indexing function outside that image. 

### `oldFields`

 Recover the old placement from the child list in descriptor order. 

### `hiddenFields`

 Recover the absorbed half-wire fields from their dense IDs and little-endian bits. 

### `rows_hiddenFields`

 A successful native hidden parse is always in the image of the typed encoding. 

### `typedActions`

 Run the same resident calls when the physical interface provides raw lists. 
