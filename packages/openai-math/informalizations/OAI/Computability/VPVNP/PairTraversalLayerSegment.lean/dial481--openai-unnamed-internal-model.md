---
{
  "module": "OAI/Computability/VPVNP/PairTraversalLayerSegment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalLayerSegment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalLayerSegment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Consecutive reset-entry calls for one traversal layer

The persistent word counts the sites already translated. Every call starts
with fresh private registers and memory and reads the raw rows that remain
below the descriptor arena. The sequence constructs the exact descriptor
image used by the traversal.


### `SiteWorkerRun`

 The native site worker reads one row from its directory, publishes its
descriptor, and returns the successor cursor. 

### `run_numbered_layer`

 Run one call for every site from cursor zero. Each report's instruction and
probe counts are tied to that site's actual number of children. 

### `workerData`

 The first three words address the raw counts and preimage array. The
remaining words address the old and new descriptor layers at their common stride. 

### `directory_worker`

 The same six-parameter instruction table realizes every site in a directory. 

### `run_step_layer`

 The fixed site worker runs from cursor zero through a selected term's entire
output layer, with one reset-entry call per new site. 
