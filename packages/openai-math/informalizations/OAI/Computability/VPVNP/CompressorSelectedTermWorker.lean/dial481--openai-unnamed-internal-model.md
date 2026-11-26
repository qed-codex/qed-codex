---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedTermWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedTermWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedTermWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform costs for the selected ordinal-native motif passes

Only the shrink and refresh grids enter the constants. They are independent
of the width data, branch choices, compression level and number of levels.
Every reset uses the same private-work cap. Calls and probes are charged
against the original physical slots of their level.


### `siteFit`

 Grid-dependent contribution to the word width needed for the scan's bound on each motif
visit. 

### `gridFit`

 Common word-width allowance for the grid's term worker, individual visits, and write frame. 

### `fitConstant`

 Word-width allowance sufficient for both the shrinking and refresh term workers. 

### `clock`

 Private instruction budget shared by the selected motif visits at word width `w`. 

### `input`

 The fields provided by the physical level directory suffice to construct
the reindexed worker input using the same instruction cap on every level. 

### `run`

 The selected real-level execution charges one call per motif. The final
memory preserves every field, and the uniform bound applies at each report
and to the complete event log. 

### `executeLevels_cost`

 Along a selected execution, summing the real calls and probes requires
only a fixed multiple of the descriptor units. The clock is uniform over
the entire branch. 
