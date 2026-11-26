---
{
  "module": "OAI/Computability/VPVNP/ShrinkSupplyLocal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkSupplyLocal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkSupplyLocal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a six-party supply map at its packed site

The four surviving wires are read from the contiguous slices incident at the
site. Each absorbed wire is read from the single internal index at its owner.
This reconstructs both endpoint columns of every map in the shrinking layout,
including when the half-wire indices on the output graph are independent.


### `internalLabel`

 Indices of the four absorbed wires of each motif. 

### `layoutCases`

 Read one of two dependent fields, according to its layout bit. 

### `splitSupply`

 Split all eight motif labels into the surviving words and the four
internally summed indices. 

### `shrinkAssignmentsEquiv`

 Reindex a sum over all shared supply labels by one shared assignment
to the output graph and one shared index per absorbed edge. 

### `shrinkLocalSupplyArg`

 All columns of the supply basis at a party, using only half-wires
and absorbed indices available at that party's packed site. 

### `shrinkLocalSupplyArg_eval`

 A shared assignment gives exactly the original motif column at every
party after slicing the surviving words and placing the absorbed indices. 
