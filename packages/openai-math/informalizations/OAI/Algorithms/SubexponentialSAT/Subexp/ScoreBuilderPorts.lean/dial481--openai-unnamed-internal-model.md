---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed global scorer stack layout

The preparation and candidate routines use the controller's 48 stacks through
explicit injective maps. The finalizer moves ordered score records to port 0
and clears the temporary selected-pair table, restoring the higher-stack
environment expected by the sequential controller.


### `call_lifted_update`

 A lifted actual subroutine that changes one local stack changes exactly
the corresponding caller stack. This proof does not execute an abstract map;
the premise is the concrete subroutine's instruction trace. 

### `environment`

 Runtime tables are data on six fixed stack ports. All other high ports are
empty at a complete scorer-call boundary. 

### `finish_eval`

 Two transfers restore the original byte order of the score records. The
selected-pair table is then cleared by actual pop instructions. 
