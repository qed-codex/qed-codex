---
{
  "module": "OAI/Computability/VPVNP/RAMSortScanMessages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortScanMessages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortScanMessages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Costed sorting replay on the validator's physical messages

The linear-address scan inspects the exact incident bit intervals allocated
to the site's own sort sends and to its partner's sends. Its acceptance
therefore checks canonicality of both physical fields and exactly the typed
send constraints. Its output recovers the typed validator's sorted block.


### `SortCanonical`

 Both blocks actually incident at this site in each cross-layer have
canonical record encoding. 

### `sortScan_messages`

 Exact acceptance criterion for the costed local sorting scan on an
arbitrary raw assignment. 

### `sortScan_output`

 With canonically parsed sorting fields, the record array handed to the
predecessor check is the exact `outputAt` array of the typed validator. 
