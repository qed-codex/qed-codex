---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPlanAlphabetEmit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPlanAlphabetEmit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPlanAlphabetEmit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical double framing for one vertex-plan alphabet entry. 

### `command_eval`

 Consume a plan word and prepend a record whose payload is its frame.
Consequently two such payloads concatenate to a pair of framed plans. 
