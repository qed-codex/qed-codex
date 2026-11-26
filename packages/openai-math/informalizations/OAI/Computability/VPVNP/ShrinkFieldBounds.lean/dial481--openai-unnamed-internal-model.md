---
{
  "module": "OAI/Computability/VPVNP/ShrinkFieldBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkFieldBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkFieldBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Widths and local map descriptions in the shrinking step

With a fixed six-party conversion block, every supply width (including its
selectors), outer coordinate, and matrix-entry degree is linear in the
maximum old width plus one. At each packed site each of the six parties has
exactly `dQ` resident maps and each of the four absorbed types has `dQ`
resident fields. The resulting local bounds depend only on the block and
degree, allowing different widths and different selections on every lane.


### `fieldFactor`

 If the conversion index bound is `A`, the supply payload and its selector
list together have width at most `A * (1 + selectorBits) * (W + 1)`. 

### `shrinkDemandWidths_le`

 Dividing the thick bundle among its assigned demands keeps even the
AB demand within the maximum old width. The CD demand uses its old wire. 

### `shrinkTerm_bounds`

 For each admitted term, bound the number of base entries in a map, its
outer coordinates and all eight supply fields with one block constant. 

### `shrinkEntry_degree_le`

 The scalar-independent polynomial specified by each local matrix entry
is zero or a monomial with at most the stated total exponent. 

### `shrinkSlotWidth_le`

 The bound holds on the actual slots, including the dummy arcs, for any
list of admitted motif terms and either layout. 

### `card_shrinkPartySite`

 The resident map records include a separate occurrence of each party,
even when several parties of one motif are assigned to the same site. 

### `card_shrinkInternalOwner`

 Every absorbed wire is recorded at its common owner exactly once. 

### `shrinkSite_repetitions_le`

 Total length of the parameter lists of all resident maps before their
product is evaluated. Failed entry checks require no additional entries. 

### `shrinkSite_internalWidth_le`

 Total width of all the fields summed inside one packed site. 
