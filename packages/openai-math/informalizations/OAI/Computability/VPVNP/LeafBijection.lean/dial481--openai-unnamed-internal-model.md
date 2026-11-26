---
{
  "module": "OAI/Computability/VPVNP/LeafBijection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LeafBijection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LeafBijection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matching terminal occurrences to query slots

The terminal word and the query have a label-preserving bijection of positions
exactly when they represent the same multiset. For a query with distinct labels
the bijection is unique.


### `LeafBijection`

 An assignment of every terminal occurrence to a distinct query slot with its label. 

### `nonempty_iff`

 Assignments exist exactly for the multiset of terminals selected by the query. 

### `subsingleton_of_injective`

 Distinct query labels determine the assignment at every terminal occurrence. 
