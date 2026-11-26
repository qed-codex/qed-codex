---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairAreas.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairAreas.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairAreas.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Disjoint physical arrays for preparing the auxiliary pair counter 

### `headerBase`

 Natural base address of the live header workspace at the group geometry. 

### `tableBase`

 Natural base address of the auxiliary descriptor table at the group geometry. 

### `counterBase`

 Natural base address of the label-counter array at the group geometry. 

### `shadowBase`

 Natural base address of the virtual RAM shadow at the group geometry. 

### `histLength`

 Length of the nominated histogram, one word per grammar production. 

### `counter_end_le_shadow`

 Motif counters follow the grammar counters in the same live array. 

### `address_values`

 The untruncated public addresses used by all three preparation stages. 

### `source_interval`

 An occupied source lies in the header output area or in the nominated
counter array. It is above the stage tag and below the virtual shadow. 

### `GeometryAreas`

 Address conditions for the selected auxiliary pair and histogram length. The sparse
descriptor, source, and shadow areas satisfy the copy routine’s separation conditions and
avoid the stage tag. 

### `geometry`

 A single bound on the occupied prefix of the virtual shadow discharges
all source, descriptor, stage-tag and destination separation conditions. 

### `headerSpan`

 The fixed expression for the reserved virtual header size has no group
dependence. Only the populated subset varies with the exterior cuts. 

### `eventually_geometry`

 The threshold for disjoint word addresses is uniform over all first-half
groups, the evaluator and the actual contents of the external arrays. 

### `nominationFits`

 The same address fit discharges the histogram region conditions of the
preceding nomination stage. 
