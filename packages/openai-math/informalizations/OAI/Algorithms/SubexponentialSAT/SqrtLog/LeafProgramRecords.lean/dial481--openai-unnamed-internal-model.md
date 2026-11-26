---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measured physical folds over sparse-hash records

This module specializes the audited framed-record iterator to an accumulator
fold which visits every record. The callback is an actual finite `Cmd`; its
local execution contract remains explicit. `foldProgram_run` concerns primitive
Boolean-register/stack transitions, not an operation counter or semantic oracle.
The same program shape handles clause-literal products, sparse weighted sums,
coefficient-array maps, and support-key dictionary scans.


### `FoldContract`

 Local callbacks are required to operate on encoded records only. The
machine must consume the parsed reversed payload and preserve the unread tail.
The accumulator's semantic decoder is used only in the specification. 

### `foldProgram_run`

 The program has a fixed finite instruction table. Its actual trace bound
includes parsing and the final halt; the callback bounds remain explicit. 

### `accumulator_stack`

 An accumulator stored on a separate physical stack is unchanged by the
iterator's bookkeeping wrapper, so the preceding value statement refers to
the actual final machine state as well as its abstract base state. 
