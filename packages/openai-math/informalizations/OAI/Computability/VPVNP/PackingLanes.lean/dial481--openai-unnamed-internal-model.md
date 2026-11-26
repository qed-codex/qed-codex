---
{
  "module": "OAI/Computability/VPVNP/PackingLanes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackingLanes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackingLanes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing and consuming binary lane coordinates

Appendix C uses one bit per base color, enough bits to index an outgoing
slot, and a tag large enough for the greedy exclusions. All three block
lengths depend only on the degree. The remaining coordinates are arbitrary.
The input may have any displacement on any directed base arc.


### `splitBitWord`

 Split a binary vector into two coordinate blocks. Addition splits in the
same way, so both blocks retain constant displacements on each base arc. 

### `packingTagBits`

 Logarithmic tag length sufficient to avoid all forbidden choices. 

### `packingLaneBits`

 For degree `2^a` and `g` unused coordinates, this is the whole original
lane length. Only the color and slot fields reduce the position count. 

### `packingFields`

 Separate the color, slot, tag, and remaining-lane fields. 

### `DyadicPackingData`

 Packing data for bit-word slots, tag shifts and residual lanes, with dyadic degree and the
corresponding finite color bound. 

### `packingArcEquiv`

 Reorder the actual arc coordinates after splitting its lane. 

### `orderedDyadicPacking`

 Construct the packing data by scanning the supplied base order. Candidate
tags are enumerated by their binary integers, independently of the unused lanes. 

### `orderedDyadicPacking_actual`

 The relabeling respects the directed endpoints, slot numbers, and all
translated fields of the actual input for every choice of base order. 

### `dyadicPacking`

 Apply the ordered construction using a chosen enumeration of a finite base. 

### `packing_position_count`

 Position count before packing is `K` times the new count. The tag moves
into the base, while the color and slot fields are removed. 
