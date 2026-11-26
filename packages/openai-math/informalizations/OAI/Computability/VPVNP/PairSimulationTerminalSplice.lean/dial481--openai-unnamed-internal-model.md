---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalSplice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSplice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSplice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splicing ordinary worker stages into the terminal table

A closed stage can be run from a physical memory that differs from its source
memory on the two terminal control cells. Source reads avoid those cells.
Worker writes propagate to both memories, and the terminal controller updates
the stage and saved word between calls. The final accepting call either starts
the next worker at zero or halts the terminal table.


### `workerCell`

 An external address outside the two terminal-controller cells. 

### `handoff`

 Entry state selected by the final accepting call of a worker. 

### `stageReports`

 Attach each call's entry and exit events, restoring the cursor returned
by the preceding call. A closed source stage has one accepting call at its end. 

### `StageRun`

 The native reports, persistent handoff and the memory conditions needed to
splice the next stage at the end of this particular closed stage. 

### `closed_stage_run`

 Replay the worker's own choices in the terminal machine. Correctness of
each source read is transported through memory agreement before executing that
call, and agreement is re-established after its physical exit. 

### `StageRun.append`

 Continuing a linked execution consumes the stage's entire branch prefix
and resumes from its exact physical memory and marker. 
