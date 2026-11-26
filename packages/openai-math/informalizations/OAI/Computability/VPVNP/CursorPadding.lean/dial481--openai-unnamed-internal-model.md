---
{
  "module": "OAI/Computability/VPVNP/CursorPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Zero-width parallel slots of the cursor network

Section 12 pads the two original arcs to the compressor's prescribed degree
by making extra copies of the no-flip arc. Each copy carries a singleton
alphabet. Distinct copies retain distinct slot numbers at both endpoints.


### `PaddedArc`

 Original cursor arcs together with the padding slots indexed by a position and a local
padding ordinal. 

### `paddedNetwork`

 Add one zero-width copy of the no-flip arc for each extra slot. 

### `unpadHalf`

 The incident fields on the genuine arcs of a padded position. 

### `paddedFactors`

 Evaluate each original tensor on the two genuine incoming and outgoing slots. 

### `unpadFields`

 Deleting the singleton fields is a bijection on shared-edge assignments. 

### `contract_padded`

 Padding preserves the contraction for arbitrary factors on the original network. 

### `paddingSlots`

 The first two slot numbers are the stay and flip arcs; padding follows them. 

### `slotSide`

 Only the original flip arc changes the current address bit. 

### `paddedEdgeEquiv`

 Number each physical edge by its source position and outgoing slot. 

### `paddedSlotGraph`

 The slot permutation advances the cursor and preserves the slot number.
Thus incoming copies and outgoing copies are independently numbered at every site. 

### `paddedEdge_source`

 The source endpoint of a numbered edge is its outgoing position. 

### `paddedEdge_target`

 The target permutation gives the incoming position of every edge, retaining
the slot number even for parallel copies. 
