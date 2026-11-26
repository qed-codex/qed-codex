---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairHandoff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairHandoff.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairHandoff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Factoring native compressed-pair paths into online and terminal stages

After the eight deterministic initialization calls, the online calendar and
the terminal evaluator can both use nondeterminism. Their actual choice tapes
are concatenated. At the boundary the first stage's accepting exit writes
the terminal tag and resets the cursor. The cap examines the reports from
both stages, including their exact tag reads, writes and private entry ticks.


### `innerProgram`

 The inner program linking all compressed-pair components through the pair tag and stage
successor function. 

### `clockAt`

 The fuel available to the selected source stage after the five entry ticks and its tag
dispatch. 

### `StagePaths`

 The ordinary accepted paths of one component stage, beginning at cursor zero on the given
memory and stage fuel. 

### `Protected`

 The reachable invariant protects the pair-level tag at every continuing
source call. It may depend on the actual state and memory. 

### `Protected.invariant`

 The predicate on the current cursor and memory used to preserve the stage tag across
  continuing calls. 

### `fuelEquiv`

 Rewriting a fuel bound preserves the native private choice sequence. 

### `terminalEquiv`

 Exact terminal-stage path equivalence before the pure address prelude is
added. Since this stage accepts the entire pair, a successful continuation
has no remaining calls. 

### `onlinePost`

 The memory passed to the terminal stage after replaying an online path and writing the
successor stage tag. 

### `onlineReports`

 The online path's ordinary reports wrapped with the physical pair's dispatch and transfer
events. 

### `onlineTerminalEquiv`

 The complete pair body from its online tag. The branch stream is a
unique online path followed by a terminal path in its actual post-memory.
The latter runs the original terminal evaluator's finite instruction table. 

### `fullEquiv`

 Include all eight native setup calls in the path bijection. The tag,
memory and cap at the join use their actual reports. 

### `full_run`

 Replay the exact native boot, online and terminal report streams. The
same witness gives both the path classification and its physical memory. 
