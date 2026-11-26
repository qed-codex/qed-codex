---
{
  "module": "OAI/Computability/VPVNP/PairTraversalNativeRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalNativeRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalNativeRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From the native placement scan to the ordered children of a site

The descriptor scan enumerates numerical identifiers in increasing order. The
local history reader restricts that same order to the placement fiber. Equality
of these lists keeps their indices aligned even when the placement is many to
one or its fiber is empty.


### `siteWord`

 The numerical site identifier stored in a word. 

### `RepresentsPlacement`

 Each stored owner agrees with the placement on the represented old sites. 

### `orderedIds`

 The old identifiers in the order chosen by the site's local history reader. 

### `preimagePrefix_eq_orderedIds`

 The native identifier list equals the restricted order entry by entry. 

### `native_step_row`

 Apply the native row and header routines to a completed placement scan for a
selected term. The resulting DFS descriptor uses the local parser's exact
child list, with each identifier converted to its preceding-layer address. 
