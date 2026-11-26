---
{
  "module": "OAI/Computability/VPVNP/ShrinkHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resident map and field occurrences for shrinking histories

At a new site of §7.2 the four absorbed types contribute shared local
fields. The six-party maps resident there have their own incident demand
and supply words. Each map's degree is bounded by its number of base
copies. These records accompany the old and new actual slots of the
substep in the recursive histories of Theorem 7.1.


### `ResidentMap`

 Distinct occurrences of the six local matrix entries assigned to a site. 

### `readsArgument`

 A matrix argument at party `j` reads the half-word of each incident
demand and supply edge. 

### `ResidentArgument`

 Map argument occurrences retain both their resident map and edge label. 

### `shrinkSiteRecords`

 The locally summed fields and local matrix arguments at each new site.
The bounds assigned to each map are the lengths of the conversion entry
descriptions, before parameter specialization. 

### `shrinkSiteRecords_count_le`

 A site has `6dQ` local maps, `4dQ` absorbed fields, and at most ten
argument fields per resident map. 

### `shrinkSiteRecords_largest_le`

 Every local wire word and every individual map degree obey the same
linear envelope, independent of the particular selections and site. 

### `card_reindexed_shrinkPlace`

 Reassembling the old lane fields and promoting the tag into the new
base both preserve the exact immediate-preimage count. 
