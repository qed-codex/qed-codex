---
{
  "module": "OAI/Computability/VPVNP/ShrinkConversion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkConversion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkConversion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Six-party identities on the packed demand words

Section 7.2 applies one fixed instance of Theorem 6.1 to every AB/CD pair.
The independently supplied old half-wire words give the four terminal inputs
of the identity. Its outer index determines the supply widths, while one
shared value per supply edge is summed over inside the selected term.


### `shrinkDemandWidths`

 The widths of the AB and CD wires in the local identity. 

### `shrinkDemandArg`

 Read the AB and CD words independently at both old endpoints. 

### `ShrinkChoice`

 The admissible outer indices in the local conversion of one demand. 

### `shrinkSupplyWidths`

 Supply width of an admitted local term. 

### `shrinkMap`

 A matrix entry at each party, over the ring carrying a solution of the
block's fixed equations. 

### `shrinkDemand_identity`

 Exact six-party expansion on the old independent half-wire inputs, in
every ring satisfying the same parameter equations. 
