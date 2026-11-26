---
{
  "module": "OAI/Computability/VPVNP/PairTreeSelectedFrontier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeSelectedFrontier.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeSelectedFrontier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descendant address lists of the actual selected descriptor rows

Each new layer uses a fresh interval of row addresses. Assign its placed
children's complete preorders there, while keeping all earlier row values.
This gives one address-indexed function for all leaves and intermediate
rows, valid for every assignment of the private half-wire packets.


### `childAddresses`

 Concatenate each selected child's root address and descendants in the local parser's child
order. 

### `children_addresses`

 These are the descendant addresses in precisely the native child
packet list, independently of its guessed half-wire values. 

### `DescLayers`

 At every selected layer, a parent's descendant list is exactly the concatenation of its
ordered child subtrees. 

### `selected_descendants`

 A single consistent descendant lookup suffices for the frozen selected
execution. It gives empty leaf lists and the full root preorder on all rows. 
