---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundlePass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundlePass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundlePass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native classification and list construction in a shrinking pass

The classification worker follows the old graph's outgoing incidence and reads
both endpoints' placement rows. Its owner output supplies the physical input of
the bounded-append worker. The two passes together charge fourteen calls plus
probes per old outgoing port. Widths remain indexed by these same absolute IDs.


### `classify_directory`

 Complete classification from the two constructed directories, with the precise
source width still addressable by old absolute ID wherever the width column is
reserved outside the two new columns. 

### `classify_and_collect`

 The classifier's bucket column supplies every owner word needed to append all
old arc IDs. The combined cost uses the same old-port count for both passes. 
