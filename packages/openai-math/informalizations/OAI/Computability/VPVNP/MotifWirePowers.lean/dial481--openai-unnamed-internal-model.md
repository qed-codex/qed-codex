---
{
  "module": "OAI/Computability/VPVNP/MotifWirePowers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifWirePowers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifWirePowers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Width arithmetic for binary wire networks

A wire of width `w` has `2 ^ w` index values. Concatenating two indices at
both endpoints multiplies the corresponding networks under tensor product.
This realizes repetitions of a motif as ordinary powers of its restriction
class, including for loops and repeated edges.


### `binaryNetworkClass`

 The restriction class of a graph with an integer bit width at each edge. 

### `binaryNetworkClass_add`

 Adding widths pointwise amounts to taking the tensor product. 

### `binaryNetworkClass_zero`

 Width zero gives the tensor unit. 

### `binaryNetworkClass_pow`

 Repeating all edge widths `n` times gives the `n`th power of the class. 

### `binaryNetworkClass_sum`

 The widths accumulated by a finite family of motifs give the product
of the corresponding restriction classes. 
