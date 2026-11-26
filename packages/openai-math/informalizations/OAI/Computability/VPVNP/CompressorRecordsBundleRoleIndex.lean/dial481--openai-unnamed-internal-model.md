---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleRoleIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleRoleIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleRoleIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Converting the old source-port order to the role-record order

The shrink role table keeps the residual lane as its last digit. Its preceding
digits are the same normalized source-port key used to sort CD records.


### `oldArcIndex_eq_key_lane`

 Reindex every old actual wire, including thick wires and parallel padding. 
