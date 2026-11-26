---
{
  "module": "OAI/Computability/VPVNP/ShrinkLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Regrouping all six-party matrices at the sites of the shrinking step

For one choice of outer term at every motif, the layout uses one new
numbered wire per surviving subdivision. Each absorbed wire is internal
to a single site. The product of the six-party matrices agrees with the
product of the entries at the new sites for every original assignment.


### `partyProduct_eq_resident`

 Computing a site entry requires precisely its list of resident map occurrences. 

### `shrinkLayout`

 Layout of the selected six-party terms, including each absorbed word's
owner and the arguments available to every map at its site. 

### `shrinkLayout_group`

 Regrouping the selected motif factors, the final hypothesis of
`Step.ofMotifProduct` for the actual padded output graph. 
