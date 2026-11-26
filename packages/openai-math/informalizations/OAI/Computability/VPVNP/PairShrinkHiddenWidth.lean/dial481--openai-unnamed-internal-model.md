---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the width of a hidden shrinking field

A dense field identifier encodes a motif ordinal and one of four roles.
The reader looks up the motif's repetition count and the role's payload in
the layout opposite the surviving one. The resulting bit width is their
payload plus the selector bits for all repetitions.


### `instruction`

 Registers zero through four hold the ID pointer, term base, term stride,
layout bit, and selector width. Register five receives the width, six keeps
the ID, and registers seven through nine are temporary. 

### `Linked`

 The machine implements all 18 width-reader instructions at their assigned addresses with
the specified register bank and continuation. 

### `rowBase`

 Word address of the selected term record. The quotient of the dense hidden ID by four
selects the motif ordinal in the strided term array. 

### `coordinate`

 Payload offset among the eight role coordinates of a term. It takes the role from the ID
modulo four and chooses the four-role half opposite the surviving layout. 

### `events`

 The 18 events of a width lookup, including the dense ID read at `ptr`, the repetition count
at `base + 1`, and the payload at `base + 2 + coord`. 

### `native`

 Exact native execution, including the retained ID and the complete
frame on the caller's configuration. 

### `rowBase_eq`

 Decode the motif ordinal in the dense field ID. 

### `coordinate_eq`

 Decode the role and switch to the hidden half of the eight payload words. 

### `value_eq`

 Numeric readback of the native width register for an arbitrary fitted
row. Both the payload and the repetition factor are read from memory. 

### `term_value_eq`

 The term directory's chosen hidden width is precisely the native
readback for its corresponding dense ID. 
