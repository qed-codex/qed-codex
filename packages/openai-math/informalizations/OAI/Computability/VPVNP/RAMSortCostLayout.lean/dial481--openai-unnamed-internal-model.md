---
{
  "module": "OAI/Computability/VPVNP/RAMSortCostLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCostLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCostLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loop bounds and word addresses for replaying a sorting stage

The validator enumerates the public phase and stride counters. It computes
each partner by a shift and xor, and computes the start of an incident
record field using a triangular layer number and a linear bit offset.


### `length_phases`

 Exactly this many comparator layers are visited, regardless of the data. 

### `IndexExpr`

 A straight-line calculation of addresses and routing flags. Input
registers and public constants are available before this calculation. 

### `IndexExpr.eval`

 Evaluate a sorting address or routing expression using natural-number arithmetic, shifts,
and exclusive-or. 

### `IndexExpr.work`

 Count one operation for every binary node of the routing expression, treating its given
arguments as available registers. 

### `wireIndex`

 Arithmetic expressions for the current index, its comparator partner,
and the direction bit of the phase. 

### `wirePartner`

 Comparator partner index obtained by toggling bit j of the global wire index formed from
the site and offset. 

### `directionBit`

 Extract bit a of the global wire index to determine ascending or descending order in phase
a. 

### `fieldStart`

 Linear bit address of the first bit of a single five-word record. The
two direction fields at each cross layer immediately follow the two
eight-word successor fields. 

### `fieldStart_physical`

 The straight-line address is the address in the allocation of equation
(10.1), including the offset of an individual bit inside its record. 

### `wireAddress_work`

 Two address comparisons after computing all three expressions, even
when the current index is recomputed for each use. 
