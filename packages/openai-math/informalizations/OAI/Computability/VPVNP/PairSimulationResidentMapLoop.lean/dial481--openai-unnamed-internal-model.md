---
{
  "module": "OAI/Computability/VPVNP/PairSimulationResidentMapLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentMapLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentMapLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Visiting a selected node's resident map entries

The loop tests the private row cursor against its exclusive end, enters the
resident entry routine, and advances the cursor only on success. Histograms
retain the increments of all earlier successful entries when a later map is
syntactically zero. Neither the directory order nor repeated names are deduplicated.


### `Job`

 The value of one occurrence may be zero. The two bounds include directory
reads, operand preparation, matrix dispatch, and the private parameter scan. 

### `Job.names`

 Parameter labels emitted by the map, or `none` if it rejects. 

### `Job.work`

 Bound on events in the descriptor read and map execution. 

### `Job.probes`

 Bound on probes in the descriptor read and map execution. 

### `labels`

 Concatenate the labels of successive jobs up to the first failure, retaining multiplicities. 

### `passed`

 Whether every job returned a list of labels. 

### `work`

 Event bound charging a test and an advance per job, plus the final test. 

### `probes`

 Sum of the probe bounds for the individual jobs. 

### `Program`

 The item starts at its genuine descriptor-reader entry. The returning
map takes the increment row; unsuccessful map images enter their rejecting halt. 

### `Program.test`

 Address of the test for the end of the directory slice. 

### `Program.advance`

 Address of the cursor increment after a successful item. 

### `Program.item`

 Entry address of the current item's descriptor reader. 

### `Program.done`

 Continuation reached when the cursor equals the exclusive end. 

### `Program.cursor`

 Register holding the current directory row. 

### `Program.stop`

 Register holding the exclusive end of the directory slice. 

### `Program.one`

 Register supplying one for cursor increments. 

### `control`

 Test the cursor against its exclusive end (`false`) or advance it and retest (`true`). 

### `Linked`

 The machine contains the cursor test and advance instructions at the loop addresses. 

### `Stable`

 Scratch facts for the remaining operands survive the two loop rows. 

### `Item`

 An item reader and map body at its real directory position. The accepted
result and all future operand buffers can depend on the supplied half-wires. 

### `Items`

 Every source position receives its own callback; a repeated local matrix
and a repeated output label retain their separate occurrences. 

### `native`

 Run the actual loop, retaining the exact prefix of successful parameter
labels on every rejecting branch. The bounds also hold when the first entry fails. 
