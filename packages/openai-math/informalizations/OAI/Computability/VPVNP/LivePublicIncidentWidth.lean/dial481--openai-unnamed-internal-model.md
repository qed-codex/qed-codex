---
{
  "module": "OAI/Computability/VPVNP/LivePublicIncidentWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicIncidentWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicIncidentWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Length expressions for the two kinds of incident fields

The sorter exchanges two blocks per triangular layer. The expression forms
the triangular numerator before division, so its fit proof bounds that
numerator independently of the final incident width.


### `block`

 Bit length of one sorting block, with four times the bucket capacity records of five RAM
words each. 

### `successor`

 Bit length of one successor field containing eight RAM words. 

### `bothSuccessors`

 Combined bit length of the outgoing and incoming successor fields. 

### `layers`

 Number of bitonic layers on the site-address bits, the triangular number for the address
width. 

### `incident`

 Total incident bit length, comprising both successor fields and two sorting blocks for each
layer. 
