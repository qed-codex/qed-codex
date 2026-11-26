---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordPlacement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPlacement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPlacement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed placement fibers in the physical descriptor table

Numbering sites transports the placement function to words in the old-site array. A full
preimage scan stores precisely the old identifiers mapping to each new owner. The number
of records in that row equals the cardinality of the original placement fiber, so the
native scan's capacity condition follows directly from the combinatorial bound.


### `preimagePrefix_card`

 Size of the physical prefix list equals the size of the filtered ordinal set. 

### `encodedPlacement`

 Read a placement as numeric identifiers in the chosen site order. 

### `encodedPlacement_rowLength`

 The preimage bound on the mathematical layout is the exact length of the
corresponding physical row. This also applies to repeated role occurrences by
numbering the occurrences themselves. 
