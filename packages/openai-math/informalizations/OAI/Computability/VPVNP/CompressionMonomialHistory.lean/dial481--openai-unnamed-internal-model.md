---
{
  "module": "OAI/Computability/VPVNP/CompressionMonomialHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionMonomialHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionMonomialHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parameter labels through a compressor execution

All substeps of Section 7.4 use the same two sets of template labels. A
shrinking entry uses the first alphabet and a refresh entry the second.
The actual branch-dependent composition of passes preserves the witnesses
of every kernel, including through all repetitions of the fixed block.


### `left`

 Include the labels of a shrinking map in the common template alphabet. 

### `right`

 Include the labels of a refresh map in the common template alphabet. 

### `StatePass.MapWitnesses`

 Local entry witnesses for every kernel of a pass. 

### `MapWitnesses`

 Witnesses along exactly the nodes reached by the chosen terms. 

### `historyWitnesses`

 Use the pass witnesses in the actual kernel history, respecting the
pass's equality of its selected output with the next state. 

### `bindWitnesses`

 Branch-dependent continuation uses the witnesses of both component
executions, without adding choices at their join. 

### `MapWitnesses`

 A choice of local map witnesses for every input to a fixed procedure. 

### `id`

 The empty collection of local map-entry witnesses for the identity procedure, whose
execution ends at its input state. 

### `ofPass`

 Lift witnesses for every local map entry of a pass to the one-step procedure built from
that pass. 

### `seq`

 Combine the first procedure's map-entry witnesses with those of the second procedure at the
final state of each first-stage branch. 

### `reindex`

 Transport local map-entry witnesses along equalities of the procedure's degree, lane,
packing and energy parameters. 

### `repeatWitnesses`

 Repeating the block uses the original two label sets at every iteration. 

### `assembleBlockWitnesses`

 Preserve the concrete per-pass witnesses in the complete scheduled block. 
