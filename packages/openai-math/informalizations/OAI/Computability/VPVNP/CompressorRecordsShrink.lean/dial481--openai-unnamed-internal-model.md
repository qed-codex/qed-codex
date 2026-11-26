---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrink.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrink.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrink.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric addresses in the shrinking placement pass

An old position is scanned in base, color-mask, slot-label, tag, residual-lane order.
The four directory reads are the base color, base offset, base slot mate, and its
displacement. The low tag and lane fields are kept together when the offset and the
base displacement are applied. This computes both possible layout owners even when
the two endpoints are thin.


### `join`

 Concatenate a most-significant field and a low binary field. 

### `bitWord_test`

 The color bit selected by the indexed greedy coloring, in big-endian lane order. 

### `Fields`

 The four natural-number fields obtained by decoding an old site for the shrinking placement
scan. 

### `Fields.base`

 The index of the old base vertex whose greedy color and offset are consulted. 

### `Fields.mask`

 The old site's color mask, tested at its base vertex's assigned color to determine
  thickness. 

### `Fields.slot`

 The old site's slot label, used to look up the mate and displacement at its base port. 

### `Fields.low`

 The combined tag and residual-lane bits, kept together when applying the greedy offset
  and the arc displacement. 

### `decode`

 The concatenated tag and residual lane occupy the least significant bits. 

### `Row`

 The packed site, bundle endpoints, assigned port, thickness, and layout-dependent owner
calculated for one old position. 

### `Row.packed`

 The packed index obtained by retaining the old position's base, tag, and residual lane. 

### `Row.source`

 The bundle's source site A, obtained by applying the base vertex's greedy offset to the
  low lane bits. 

### `Row.target`

 The bundle's target site B, obtained from the base mate and the displaced source lane. 

### `Row.assigned`

 The bundle's outgoing port, combining its source-site index with the old slot label. 

### `Row.thick`

 Whether the bit at the old base vertex's greedy color is set in this position's mask. 

### `Row.owner`

 The packed owner of the old position, using the packed site for a thick position and the
  chosen bundle endpoint for a thin one. 

### `row`

 Four source columns and a layout bit determine the records for this position. 

### `J`

 Number of packing-tag bits for a graph whose degree is two to the given exponent. 

### `colors`

 The number of greedy colors for the old graph, twice its degree plus one. 

### `Packed`

 A site after shrinking, consisting of a base vertex, packing tag, and residual lane. 

### `Old`

 A position before shrinking, with its base site, tag, residual lane, color mask, and slot
label. 

### `lowNumber`

 Concatenate the binary packing tag above the residual-lane bits to form the low part of a
site number. 

### `packedNumber`

 Number a packed site by concatenating the ordered base vertex with the tag-and-lane number. 

### `oldNumber`

 Number an old position in base, mask, slot-label, tag, and residual-lane order. 

### `Directory`

 Directory invariant at the start of a placement scan. Base slots retain both their
outgoing and incoming numbers; displacement is stored in the full old lane order. 

### `oldNumber_original`

 The full old site scan follows the order of the original compression state. 

### `row_exact`

 Correctness for every old site, including the color and tie conventions of Appendix C. 

### `oldIndex`

 Old sites are scanned in the original state numbering. 

### `packedIndex`

 The packed vertex combines the promoted tag and remaining lane. 

### `owner_encoded`

 On the numerical old-site prefix, the computed owner is exactly the placement
whose fibers are scanned by the native preimage-list builder. 

### `demandRoles`

 Read the two endpoint rows to determine the thin C role and opposite D owner.
The source is used as C when both endpoints are thin. 
