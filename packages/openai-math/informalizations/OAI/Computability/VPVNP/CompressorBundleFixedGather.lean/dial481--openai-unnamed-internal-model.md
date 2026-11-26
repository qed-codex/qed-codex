---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleFixedGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleFixedGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleFixedGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed-bank worker for gathering the complete pair of bundle key tables

The cursor visits a packed port's thick-wire entries followed by its motif
entries. The physical rectangular arrays keep all thick rows first and all
motif rows second. Integer division and a single bit computed from the
within-port position give the correct physical row without changing the
public parameter bank between calls.


### `word`

 Encode a natural table size, index or address as a machine word of the chosen width. 

### `visit`

 Public words are the total per port, thick entries per port, port count,
row stride, ID base, classifier key base, and gathered key base. 

### `offset`

 The quotient test is positive exactly in the thick part of a port. 

### `events`

 The visit reads the stored arc identifier, looks up its key, and writes that key into the
corresponding output slot. 
