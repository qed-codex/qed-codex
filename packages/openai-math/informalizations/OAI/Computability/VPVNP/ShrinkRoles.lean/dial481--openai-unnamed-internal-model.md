---
{
  "module": "OAI/Computability/VPVNP/ShrinkRoles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkRoles.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkRoles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placing the six parties in the two shrinking layouts

In the first layout C and M move to A, and N moves to D. In the second
layout C and N move to B, and M moves to D. Each absorbed edge has one
owner, while the endpoints of the other four edges agree with the roles of
the surviving slots.


### `partyRole`

 Site role of A, B, C, D, M and N in each layout. 

### `internalRole`

 Owner of the edge of this type from the absorbed group. 

### `partyProduct`

 All six-party factors resident at a site, with its equality proof available
when reading the factor's local arguments. 

### `prod_partyProduct`

 Placing the factors at their resident sites preserves the full product. 

### `packedSiteEquiv`

 Site coordinates used in the new lifted graph, with the tag in its base. 

### `shrinkPlace`

 Placement of each whole old position on the new lifted graph. 

### `shrinkPartySite`

 The six map matrices are assigned to three packed positions. 

### `shrinkInternalOwner`

 Each absorbed supply edge is summed at the common site of its endpoints. 
