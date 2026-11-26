---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/Suffix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Suffix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Suffix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Matching whole items to bins of given capacity 

### `match_units`

 Match each selected unit to a distinct unit of the specified bin. 


# Affine colorings of binary cells

For two distinct cells, translating the color by an affine form that
vanishes at just one of them cancels their cross term in the second moment.



# Matching core wire units within one dyadic group

Treat a thin occurrence as one indivisible item. After the matching,
thin occurrences with the same destination can be gathered into one
pack. This gives at most one thin pack per bin plus an unmatched pack,
with total load bounded by the load of the colony.


### `Matching`

 All outgoing units of an occurrence are either unmatched or paired
with distinct thick units from one source colony to one destination. 

### `subround_of_matching`

 The width estimate preserves any property supplied by the matching construction. 

### `subround`

 Width bound with the imbalance absorbed by Young's inequality.
Here `E` indexes bundles of common positive width `u`. 

 # Common host for dyadic groups 

### `near`

 Host contacts depend only on the original adjacency and depth limit,
independently of the chosen group, matching and contraction layout. 


# Size and degree of the common dyadic host

An overlapping interval at depth within `s` of a fixed site is determined
by its depth and at most `s` additional prefix bits.



# Relative addresses inside a group

Forgetting a common prefix commutes with taking the endpoint of a contact.
The relative address and either absolute endpoint recover the whole address.


 # Data and bounds for a dyadic grouping of blocks 

### `coreBins`

 The bound on the number of core destinations per colony. 


# The two subround contractions on old occurrences

Row contraction sends each occurrence to its own colony. Column contraction
moves precisely the matched thin source occurrences to the thick destination.
A whole occurrence has the same destination for all its outgoing units.


### `route_cases`

 Only a source of core units can move, and it moves by at most one core hop. 

 # Load of a site after row or column contraction 

### `route_load`

 Each nearby colony contributes at most one full colony load. 
