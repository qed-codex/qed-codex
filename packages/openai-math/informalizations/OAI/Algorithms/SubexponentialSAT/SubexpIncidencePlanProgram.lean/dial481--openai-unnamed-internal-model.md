---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpIncidencePlanProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidencePlanProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidencePlanProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Encoded scopes to a concrete incidence read plan

This is one fixed finite program. Runtime stacks supply the encoded scope list,
the vertex token, and unary D and Delta. No slot assignment is supplied to the
machine. Incident slots are allocated in outer-list encounter order.


### `command_eval`

 An actual execution computes the entire reversed unary read plan from
encoded scopes. The sole structural premise is the degree bound for padding. 

### `produced_records_eq_readPlan`

 The bytes produced by the machine are exactly the typed read-plan bytes
for the explicit occurrence-rank slot assignment. 
