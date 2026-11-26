---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/ResetLocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/ResetLocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/ResetLocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting bases and a common mixer

The total exceptional load can be made arbitrarily small. The length
parameter `k` is fixed before the group size, graph and loads. The
delay bound `s` is only imposed on core contacts.


### `reset_bases`

 Quantitative bad-base estimate with loads normalized by `FB`.
The maximum base length is `2^(h-a)` and the minimum is `F = 2^k`. 


# Subdivision of reset bases

Force all cells above each base to split. Below it, split only if the
load is above twice the normalized capacity or a neighbor forces the split.
Good bases survive unchanged.



# Packing one dyadic group

Use the two host degree bounds separately. Only the core degree enters
the bound on the number of destinations of one source part.


### `neighbors_le`

 At depth `i`, at most `2 ^ s` destination parts meet a given
source part if they all have depth at most `i + s`. 

### `edge_weight_sum`

 Each of the core and tether classes consumes at most a quarter of
the incoming weight budget. 

### `groupBy`

 Use any minimizer of the total propagated split count. 


# Distributing indivisible core wire units

A unit belongs to one block and one oriented contact. Both counts of the
same units are needed: load at a contact for reserving links and load
at the endpoint occurrences for packing whole tensors.



# A reset schedule for individual wire units

Transfer the exceptional load bound to actual demands. A contact between
good bases fits its predetermined capacity. Assign each old occurrence
to a leaf, preserving both endpoints of every such contact.


### `exceptional`

 Charge each unit using an exceptional route to at least one failed endpoint. 


# Reset routing over all groups at once

Each old contact carries named units on specified blocks. Active terminals,
layers and the mixer are chosen using all blocks. The allowable links
between terminals use only the contact means and the relative addresses.


### `reset_schedule`

 The only delay and degree assumptions on contacts are for the core.
Tether edges enter via the geometric budget, independent of their number. 


# Applying the reset to a host graph

Count each oriented core contact separately. This costs a factor of two
in the degree, absorbed by using the tighter base-depth difference.


### `Schedule.reserve`

 Every schedule with the stated margin admits relative reservations,
including the schedule elected by the integer controller. 


# Geometry of reset terminals

An absolute leaf address splits into a group index and a site in the
common host. Contacts within a group respect the corresponding host
adjacencies, using the smaller bound on core contacts.


### `terminalNear`

 All terminals of possible neighboring leaves are eligible. 
