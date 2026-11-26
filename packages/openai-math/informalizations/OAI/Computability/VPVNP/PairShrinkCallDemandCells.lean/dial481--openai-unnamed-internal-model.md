---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallDemandCells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallDemandCells.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallDemandCells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The four demand endpoints of a resident shrinking map

The assembled AB word uses the demand-bit repartition of the old thick arcs.
The two unsplit CD endpoints remain in their old child packets. Reading these
four bit strings supplies exactly the local demand argument of the six-party
matrix; an endpoint absent at the chosen party has width zero.


### `noncomputable local instance : DecidableEq X.Base`

 Classical equality of base vertices for identifying the old sites assigned to each demand
endpoint. 

### `Old`

 Independent old half-wire assignments for all sites placed at this motif party's resident
site in the chosen layout. 

### `endpoint`

 The length and bit string of the indicated demand endpoint at this party, extracted from
its placed old half-wire assignments. 

### `abHalf`

 Convert the two old network arguments to the AB copy program's input coordinates. 

### `abBit`

 The bit value produced by the AB column program at each of its two endpoints. 

### `ab_written`

 Native AB slice writes supply the staged word required by the local demand reader. 

### `cdBase`

 Directly addressed fields at parties C and D. 

### `placedPackets_frame`

 The original child packets survive a gather that changes only private
cells at or beyond the staging pivot. This applies to either unsplit CD end. 

### `Readback`

 Required AB output and the independent child packets selected at C and D. 

### `demandCells`

 Arbitrary, independently supplied old half-wires give the native demand
bits at every endpoint of the actual selected map. 

### `scratch_demandCells`

 Read all demand cells at the actual descriptor's field bases. Only A, B, C
and D have a nonempty demand endpoint. 
