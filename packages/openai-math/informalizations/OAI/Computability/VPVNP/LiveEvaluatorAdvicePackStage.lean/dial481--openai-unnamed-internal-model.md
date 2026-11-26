---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdvicePackStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePackStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdvicePackStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Advice packing as a linkable stage

The wrapped table uses the ordinary sweep when rows are allocated. An empty
bank takes one accepting call with zero probes, so the stage linker advances
in both cases. The unique accepting stream has one empty list per call.


### `stageCalls`

 Allocated nonempty rows have one reset plus one call per column. The
empty bank has one accepting call at its zero cursor. 

### `stageStep`

 At an individual cursor the native stage produces one deterministic report
and advances the entire row-prefix memory, including the empty-bank handoff. 

### `packStageSweep`

 The linked-stage table prepares all word rows and has one exact native
stream, including when there are zero output rows. 

### `packStagePathCount`

 The wrapper has native path multiplicity one under Lemma 10.1's caps. 
