---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleLists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleLists.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleLists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning original wires into the two lists of each packed bundle

In the first scan of Appendix E, an arc thick at both ends belongs to the
payload of its source bundle. Every other arc is a CD motif assigned to the
bundle of its thin C endpoint. The classified arc directory supplies one row
identifier per original arc. The native bounded-append pass then visits each
original arc once, recording its identifier in exactly one row.


### `mem_preimagePrefix_iff`

 The filtered physical identifiers are exactly those earlier than the cursor
which map to the row's owner. 

### `preimagePrefix_pairwise`

 In a representable range, filtering the consecutive word identifiers keeps
their strict numeric order. 

### `preimagePrefix_get_at_rank`

 Looking up the number of preceding identifiers in an owner's row recovers
the identifier at that rank. 

### `Port`

 A packed site and one of its outgoing slots, identifying the bundle at that port. 

### `Bucket`

 The choice of a thick-wire payload row or a CD motif row at a packed port. 

### `bucketOf`

 The left summand receives thick wires, the right summand receives motifs. 

### `thickEquiv`

 The left row over a port consists of exactly its original thick wires. 

### `motifEquiv`

 The right row over a port consists of exactly its assigned CD motifs. 

### `portIndex`

 Contiguous bundle indices, with slot number varying fastest. 

### `bucketIndex`

 Number the thick-wire rows first and the CD motif rows second, using the same site-and-slot
order in each half. 

### `wordOwner`

 Map a physical old arc identifier to the encoded row that collects it during bounded
append. 

### `arcList`

 The ordered list of original arc identifiers for a classified row. 

### `mem_arcList_iff`

 Physical row membership of an original wire in either summand. 

### `memberEquiv`

 Decode a stored arc ID to the corresponding member of the typed fiber. 

### `ordinalEquiv`

 Scan-order numbering of the complete fiber. Reading a cell at this
ordinal and decoding its original arc identifier implements this equivalence. 

### `rowLength`

 The number of thick wires or motif pieces expected in a classified bundle row. 

### `fill_run`

 Once the classification and zero counts occupy their physical arrays,
the native preimage pass fills every bundle's two lists. There is one call
and four external probes per original arc. 
