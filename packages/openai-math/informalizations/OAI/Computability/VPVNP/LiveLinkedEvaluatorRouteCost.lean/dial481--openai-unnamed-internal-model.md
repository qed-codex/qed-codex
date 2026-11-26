---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorRouteCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorRouteCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorRouteCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Costs of the incoming and outgoing routes to the evaluator

The zero-flag route makes one router jump followed by one gather call per
configuration word. The one-flag route makes a jump and a control-word
write. In both cases the charged reports include the stage dispatcher and
its transfer to the next row.


### `gatherLogs_calls`

 The gather reads the bits of one word and writes the reconstructed word.
The linked route adds at most two probes to each such report. 

### `putLogs_cost`

 Each endpoint path consists of two four-unit calls. 

### `logs_cost`

 Either kind of outgoing field fits the word-gather allowance. 
