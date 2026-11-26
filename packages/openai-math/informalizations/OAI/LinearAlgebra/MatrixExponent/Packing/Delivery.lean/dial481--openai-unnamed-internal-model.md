---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/Delivery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Delivery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Delivery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal loads at a good base

Loads and reserved capacities are measured in units of `F B`. The
reservation slots depend only on capacities. The assignment of units
to slots on a contact can be used at both ends of that contact.


### `input_terminals`

 Assign each old tensor whole to one input terminal. 

### `reserve_terminals`

 Reserve disjoint output terminals using the contact capacities alone. 

### `contact_terminals`

 One slot choice per unit suffices at both endpoints of a contact. 

### `good_base_layers`

 Place a good base's demand matrix on permutations with total normalized
width at most ten. Each layer has `Y` rows of `w` ports of width `u`. 

 # Consistent delivery slots at both ends of each contact 

### `delivery_slots`

 Assign a slot to each unit once, independently of the endpoint. A
contact carrying no units needs no slots, even when its capacity is zero. 


# Leaves of a dyadic partition

A mark splits its cell into two children. Following the prefix of a point
until the first unsplit cell gives its unique leaf.


### `Reached`

 The cells reached by splitting marked cells, including the root. 

### `leafDepth`

 Stop at the first unmarked prefix, or at full depth. 

### `leafAt_eq_iff`

 The fiber over a leaf consists of precisely the points with that prefix. 

### `card_leafAt`

 A leaf of depth `i` contains exactly `2 ^ (h-i)` points, even
after a common permutation of the indices. 

### `leafDepth_le_add`

 A split propagated up by `d` levels costs at most `d` levels of depth
at a common point. 

### `card_leaves`

 Each marked cell adds one leaf. 


# Units routed through a good base

The demand units are individually named. After assigning input items and
reserving output terminals, place each unit in a distinct port at each end
of its permutation layer.


### `route_good_base`

 Route named units, keeping all input items whole and respecting the
predetermined assignment to reserved output slots. 

### `BaseContact`

 Each contact between two base cells has a slot at either endpoint. 

### `reserve_base`

 The capacities at both ends of a contact prescribe the same number
of slots. This reservation precedes the choice of a permutation. 


# Routing all good units through reserved output terminals

Choose the same link slot at both ends, then apply the per-base routing
theorem independently at each leaf. No rotor layers are needed on leaves
without good demand.


### `delivery_bound`

 Bounds at either end of a routing problem, independent of the
particular balanced choice of slots. 

### `deliver`

 All widths are measured in units of the common base capacity. 

 # Placing bases and their adaptive leaves on the common host 

### `leafSite_mass`

 Slots in the common host that are not used in this group have zero load. 


# Uniform reservations across groups

Choose output terminal numbers using only the relative contact address.
At any given absolute base the relative slot map is injective, even
though all groups share the same terminal numbers.


### `dropSlot`

 Local slot numbers are preserved under removal of the group prefix. 


# Shared direct links on the reset host

An output terminal used by a good contact has a unique peer. The
involution depends only on the reservations, and pairs the same
relative terminals in all groups when the reservations are lifted.


### `peer`

 This involution fixes unused terminals. 
