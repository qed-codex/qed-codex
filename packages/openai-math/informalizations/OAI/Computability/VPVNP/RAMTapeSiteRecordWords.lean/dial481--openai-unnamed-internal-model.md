---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteRecordWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteRecordWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteRecordWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the address and header words for the initial memory record

Allocate `w` zero bits, trim as many cells as the source width, and prepend the low-order
source bits. For the site address the trim count comes from its public tally. For the
header a scan counts its four actual cells. Every source and scratch stack is restored.


### `Port`

 Ports for parsed address and header bits, their padded word outputs, public widths, and
conversion scratch. 

### `addressWord`

 The same unsigned site address, represented with `w` bits. 

### `prepare`

 The same finite table prepares both words for all public widths. 

### `steps`

 Exact step count for forming the padded address and header words used in the initial
record. 

### `extendHeader`

 Extend the actual contents of the header source to the indicated word
width. The source may have any length that fits. 
