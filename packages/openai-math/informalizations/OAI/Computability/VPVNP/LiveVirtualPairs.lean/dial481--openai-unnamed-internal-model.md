---
{
  "module": "OAI/Computability/VPVNP/LiveVirtualPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveVirtualPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The concrete auxiliary pair data of the fixed diagonal program

At each admissible length choose one uniform coefficient-counter layout
for each pair index. All exterior bit strings and nominations use that same
layout. Their compressed witnesses use the actual virtual machine, its
actual reset word, private clock, and header. Thus the exponent histogram
returned by the pair path and its algebraic weight belong to the same
finite occurrence. The lane numbering reverses the coordinates within
each address block, as in the physical cursor descriptor reader.


### `groupIndices`

 Zero-based indices of the pairs at the fixed program's chain height, with one index for
each first-half group. 

### `pairLengths`

 Primed input lengths for one pair, including the two exterior cuts and the intervening cut,
using the fixed program's chain height, cut width and advice length. 

### `pairLayout`

 Type of primed RAM input layouts for this pair's field lengths and the program's physical
site exponent, bucket size and word width. 

### `pairNom`

 Production histograms nominated at length n and circuit exponent C. Each production count
is strictly less than `2^(2*d)`, where d is the physical site address width. 

### `auxData`

 Degree, root and production histogram passed to the actual auxiliary program. 

### `virtualCap`

 Resource conditions on the virtual processor at length n, using the virtual site exponent,
the rounded quarter-power bucket exponent and the fixed program's RAM word width. 

### `reservedLanes`

 Number of lane coordinates used by all scheduled compression blocks, equal to the block
count times the lanes per block. 

### `VirtualPairs`

 Physical choices shared by all calls to the auxiliary pair program
at this one length. The degree inequality precedes the choice of
specialization, input, and path. 

### `VirtualPairs.layout`

 Primed input layout for each pair index at this length, shared across all advice,
  exterior bits and nominations for that index. 

### `VirtualPairs.data`

 Instantiate the auxiliary coefficient counter at this pair index with its layout, the
header derived from advice and exterior cuts, and the nominated production counts. 

### `VirtualPairs.witness`

 Compressed count witness for the nominated auxiliary machine under the given label
solution, using its actual private fuel, zero starting state and initialized memory. 

### `VirtualPairs.pairData`

 The finite paths, their exponents, and their joint coefficient identity
for the literal processor and precisely the same advice used at the midpoint. 

### `grammarCapacityPower`

 A fixed exponent covering all grammar labels before the address exponent
is selected. It depends only on the hypothesized circuit exponent. 

### `eventually_virtualPairs`

 At sufficiently large lengths the auxiliary virtual layouts and their
path identities exist simultaneously at every pair, before the advice,
exterior cuts and nominations are selected. 
