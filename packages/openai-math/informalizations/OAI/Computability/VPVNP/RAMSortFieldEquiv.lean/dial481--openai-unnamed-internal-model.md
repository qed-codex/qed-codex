---
{
  "module": "OAI/Computability/VPVNP/RAMSortFieldEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortFieldEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortFieldEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Identifying distributed sort transcripts with physical send fields

The chronological list of layer checks uses a dependent product of field
assignments. This product indexes exactly the sorting send fields allocated
by the physical layout, once at each cross-site layer and site.


### `fieldsOfStages`

 A duplicate-free schedule stores its indexed fields once each. 

### `physicalIndex`

 Reindex the sorting fields by their physical layer and source site. 

### `physicalFieldsEquiv`

 Bijection with the send blocks allocated in the paper's equation (10.1). 

### `existsUnique_physicalFields`

 Every physical sorting send slot is constrained by the local validator.
For any initial record array exactly one physical send assignment passes. 
