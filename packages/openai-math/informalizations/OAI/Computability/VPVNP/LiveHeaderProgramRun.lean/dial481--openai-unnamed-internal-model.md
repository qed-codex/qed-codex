---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderProgramRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProgramRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProgramRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composing native live-header stages on shared external memory

The source executions use their own seventeen-word parameter rows. At every
accepting boundary the native linker updates the reserved tag word and resets
the cursor. The combined report records each dispatch read and each handoff
write, with an exact cost in calls and external probes.


### `run_component`

 Row relocation preserves the native segment of the small stage table. 

### `run_entry`

 Embed a complete native stage segment in the fixed header register file. 

### `StageTrace`

 Reports and branch choices of a complete source stage. 

### `StageTrace.id`

 The header stage whose source reports this trace records. 

### `StageTrace.fuel`

 The source-stage clock used to execute the recorded calls. 

### `StageTrace.paths`

 The private choice tape supplied to each successive source-stage call. 

### `StageTrace.reports`

 The ordered source reports returned by the recorded calls before linker dispatch and
  handoff events. 

### `StageTrace.output`

 The source reports wrapped with the header linker's dispatch and stage-transfer events. 

### `StageTrace.cost`

 The source cost plus a dispatch probe per report and a transfer probe when the stage has a
successor. 

### `StageTrace.finalMem`

 The memory after the source reports and the linker's transfer to the next header stage. 

### `StageRuns`

 Source runs in the prescribed order, each with its fresh cursor and the
memory actually passed from its predecessor. 

### `finalMemory`

 Replay a list of header stages in order, including the transfer writes between stages. 

### `calls_output`

 Every linked call corresponds to one source call; there are no extra
handoff calls between stages. 

### `run_of_stages`

 Execute a complete suffix of the scheduled native header program with
the original branch inputs. The accepted output and its cost are exact. 

### `remainingStages`

 The suffix of the header schedule starting at the given stage, empty after completion. 

### `StageRuns.schedule`

 Accepted execution traverses precisely the suffix prescribed by the
header's sequential successor, even when a scan has zero active entries. 

### `complete_budget`

 Bounds for the full program at the prescribed entry. The second inequality
also budgets two enclosing-dispatch probes per header call. 
