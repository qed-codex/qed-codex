---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Classification of all actual old arcs in a shrinking pass

The complete native scan assigns every absolute outgoing slot to its thick-wire
or CD bundle and writes its relative sorting key. Distinct parallel wires retain
their original array indices. The combined bucket column can serve immediately
as the owner array of the bounded-append pass.


### `bothThick`

 Test whether both endpoints of an old arc are thick under the shrinking placement, making
the arc a thick payload wire. 

### `Classified`

 Numerical bucket and key columns indexed by the original absolute arc number. 

### `Classified.thick_key`

 The typed key is the bounded mask/slot key on the entire thick fiber. 

### `Classified.motif_key`

 All motif keys are indexed using the zero-residual-lane representative of the CD arc. 
