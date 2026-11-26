---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpIncidencePlanScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidencePlanScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidencePlanScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed finite scan of encoded scopes. No slot map is supplied as input:
the local slot order is the encounter order of incident factors. 

### `scanBudget_le`

 The actual scan cost is polynomial in the encoded pattern and unary query. 
