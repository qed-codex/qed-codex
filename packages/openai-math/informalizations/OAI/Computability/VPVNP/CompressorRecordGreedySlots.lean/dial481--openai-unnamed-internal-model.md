---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedySlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedySlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedySlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descriptor rows for the greedy vertex scan

Each record lists addresses of the fields needed for its comparisons.
The pointer-row invariant is independent of the current partial assignment.
Reading through those pointers in the native template recovers the forbidden
indices of the mathematical scan, including at as-yet unassigned neighbors.


### `Stores`

 Consecutive descriptor words, in word-address order. 

### `advance`

 Advance a word address by one cell for each of the given number of steps. 

### `rowValue`

 Dereference each operand address before taking the bitwise sum. 

### `Returns`

 The result and the exact accounting of the call from a fresh private state. 

### `incidences`

 Direction then local port, with both incidences even on a parallel edge. 

### `neighbor`

 Find the adjacent vertex at a directed incidence, following the target for outgoing ports
or its inverse for incoming ports. 

### `colorRows`

 Every color row has one operand, the address of the neighboring label. 

### `increments`

 Enumerate zero and all the outgoing tag increments, with multiplicities. 

### `tagTests`

 Local exclusions come first, followed by all pairs of increments. 

### `TagAddresses`

 The immutable displacement cells and the current mutable assignment cells. 

### `TagAddresses.zero`

 Address of the constant zero word used for absent tag increments. 

### `TagAddresses.displacement`

 Address of the displacement word for a specified outgoing arc. 

### `TagAddresses.label`

 Address of the current tag assignment for a specified vertex. 

### `TagAddresses.increment`

 Select the displacement address for a present local port and the zero cell for an absent
port. 

### `tagPointers`

 The four operands of a local or a two-end tag exclusion. Padding a local
test with two references to the zero cell permits one fixed instruction table. 

### `TagAddresses.Represents`

 The addressed cells contain zero and the word encodings of the specified displacements and
vertex tags. 

### `tag_returns`

 For a partially filled offset table the native output is exactly the
index used by the next visit in `orderedTagOffsets`. 
