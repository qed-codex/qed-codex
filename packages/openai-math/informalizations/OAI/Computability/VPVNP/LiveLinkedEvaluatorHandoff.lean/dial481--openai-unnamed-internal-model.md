---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorHandoff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorHandoff.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorHandoff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Handoff of a deterministic evaluator stage in the complete live program

A successful standalone scan has one empty choice string per call. If its
returning reports preserve the stage tag, the outer dispatcher adds its
exact reports, retags the final memory and starts the next stage at zero.
The inverse direction removes this forced prefix from every accepted path.


### `linkedLogs`

 Add the group dispatch and handoff events to each source report of the selected stage. 

### `deterministicHandoff`

 Each accepted continuation corresponds to exactly one complete choice
stream with the verified empty-choice prefix. The cap includes every
dispatch, return and final stage transfer in that prefix. 
