---
{
  "module": "OAI/Computability/VPVNP/PairNodeArguments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeArguments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeArguments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The private argument buffer for a descriptor node

One contiguous interval per node holds its outgoing half-wire bits followed
by its incoming half-wire bits. An incoming slot looks up the width of the
matched outgoing arc. The two half-wires are independent in a child guess,
including when the graph has parallel arcs or loops. A child later reads
exactly the private words that its parent filled.


### `Arena`

 The private argument interval of a node is indexed by its absolute DFS address. 

### `Arena.start`

 Private memory address from which the per-node half-wire argument intervals are
  allocated. 

### `Arena.stride`

 Distance in private words between the starts of argument intervals for consecutive
  descriptor addresses. 

### `Arena.base`

 Starting address of the private argument interval for an absolute descriptor address,
obtained by scaling the address by the arena stride. 

### `fieldBits`

 The actual slot field as seen by the old vertex, independently at each end. 

### `fields`

 The half-wire bit strings at site `u` in numbered slot order, using outgoing arcs for
`false` and incoming arcs for `true`. 

### `packed`

 Concatenation used both when a parent guesses a child and at its later visit. 

### `packed_eq_encode`

 The concrete RAM byte order agrees with the abstract traversal's old-half parser. 

### `offset`

 Slot offset uses widths only and has no dependence on the guessed values. 

### `Arena.fieldAddress`

 Start of a numbered half-wire field within a node's private interval. Incoming fields
follow the entire outgoing block, and earlier fields contribute their widths. 

### `packed_member`

 Each endpoint's declared slot is precisely its slice of the private buffer. 

### `stored_member`

 Guessing the whole child buffer supplies each individual native slot at its
calculated private address and preserves private words outside the interval. 

### `value`

 External address of the selected width. Incoming fields use the inverse slot
column before addressing the old width array. 

### `value_actual`

 A concrete field header reads the old forward width or the width at the
original source of the incoming half, retaining all slot multiplicities. 
