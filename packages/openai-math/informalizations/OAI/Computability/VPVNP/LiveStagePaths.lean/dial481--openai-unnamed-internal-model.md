---
{
  "module": "OAI/Computability/VPVNP/LiveStagePaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStagePaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStagePaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Factoring native live-program paths at component completion

A stage may take a different number of calls on each branch. The first
accepting exit of its original opcode table still gives a unique split
of the linked machine's private choices. The stage tag is preserved on
continuing calls, and its accepting exit either writes a successor tag
or halts. Fuel accounts for the dispatcher and the final transfer.


### `sourceProgram`

 Burst-RAM program of a single source stage, obtained by instantiating that stage's
instruction template with the given public words. 

### `outerProgram`

 Linked burst-RAM program that reads the stage tag at the given address and follows the
successor map on component completion. 

### `transferState`

 The continuation starts from a fresh zero state after transfer. 

### `room`

 Each successful ordinary call leaves room for its linked exit. 

### `TagFrame`

 The component may use scratch memory while preserving its outer stage
tag throughout all calls which continue this component. 

### `Completion`

 The exact first source-component completion with its final source memory.
This relation includes every private choice and native report in its order. 

### `Completion.splice`

 An ordinary completed stage splices into any continuation without adding
branch choices. Every native report of that stage gains its linker events. 

### `split_halted`

 A halted linked path starting in this component must reach its first
ordinary accepting exit. The suffix has exactly the reset word and memory
specified by the transfer and can include any number of later stages. 

### `Completion.uniqueSplit`

 Determinism of native execution fixes the first completed component
inside a given complete sequence of choices. The source memory and reports
are fixed along with the position of the split. 

### `Parts`

 A full native branch of the component followed by a native branch of
the linked remainder. The cap is imposed on the actual concatenated reports. 

### `Parts.first`

 Per-call choice tapes used through the current source stage's first accepting exit,
  including the tape for its final call. 

### `Parts.rest`

 Choice tapes for the linked continuation starting with the state and memory produced by
  transfer out of the completed stage. 

### `Parts.reports`

 Source reports produced by the calls in the first part, in execution order before the
  linker's dispatcher and transfer events are added. 

### `Parts.lastMem`

 Source-stage memory after the final call and before transfer to the successor stage. 

### `Parts.tailReports`

 Linked reports produced by running the remaining tapes from the transferred state and
  memory until the outer program halts. 

### `Parts.join`

 Concatenate the two native choice streams. 

### `partsEquiv`

 Native accepting paths at the selected tag are bijective to the ordered
choice of the first completed component and the accepted continuation. The
bijection remains valid for variable component lengths and resource caps
depending on the entire joined report sequence. 

### `Ordinary`

 Ordinary complete paths satisfying the linked stage's per-call clock. 

### `ordinaryReports`

 The report list of a completed ordinary source path, recovered from its successful run on
the path's own choice tapes. 

### `Remainder`

 Suffix choices carry the *joined* report cap. Their start memory is the
actual memory after the selected ordinary path and its transfer. 

### `ordinaryEquiv`

 Factorization in ordinary stage-path types. Replaying the first path fixes
its source reports, final memory, and every argument to the continuation. 

### `count_stage_remainders`

 The exact finite sum used when successive live phases are counted. 
