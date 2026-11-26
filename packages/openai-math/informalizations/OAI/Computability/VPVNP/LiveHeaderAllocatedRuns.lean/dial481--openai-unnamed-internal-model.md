---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderAllocatedRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAllocatedRuns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAllocatedRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-capacity native live-cut scans

Each stage performs exactly its public number of calls. The runtime count
occupies a prefix, followed by idle calls that only read the count. Every
successful report preserves the reserved tag under arbitrary replay. A final
bounded call accepts and transfers control to the next stage.


### `program`

 Instantiate the allocated-field worker on the selected slot, copy or padding mode, and
public operands. 

### `Outside`

 An address precedes the field array or lies at or beyond its exclusive end. 

### `Loaded`

 Runtime offset and count were written by the descriptor stage. 

### `Sizes`

 Public scan capacity and bounds needed to read the occupied source sites. 

### `CopyLayout`

 The occupied destination is disjoint from its sources, count and offset. 

### `copy_sweep`

 All active and idle calls, before the bounded wrapper's accepting call.
The final copy has exactly the runtime length and every report, even under
arbitrary replay, preserves any designated address outside its destination. 

### `ZeroPad`

 The occupied padding positions are zero in the original processor words. 

### `padding_sweep_sound`

 Any successful sequence of padding calls covering the whole public
allocation forces each occupied original site to be zero. 

### `boundedProgram`

 The instantiated allocated-field worker wrapped in a public capacity check. 

### `copy_bounded`

 The source stage in the native linker. Its accepting path includes one
closing call after the public capacity, and has the exact occupied copy. 

### `padding_bounded`

 The complete bounded padding stage succeeds on a zero padding field.
Neither its active nor its idle calls write any memory. 

### `padding_bounded_sound`

 On arbitrary choice strings and for every allocated fuel, an accepting
bounded scan has checked every occupied original padding bit. Early stopping
leaves a live cursor and cannot skip a failing padding position. 

### `physical_copy_bounded`

 Runtime descriptors and the preserved headers identify the actual
incident cut in the completed fixed-capacity copy, with a full scratch
frame and the per-report linker frame. 

### `physical_padding_bounded_iff`

 Among all possible paths through the bounded table, an accepting
path exists exactly for canonical zero padding in the actual cut field. 
