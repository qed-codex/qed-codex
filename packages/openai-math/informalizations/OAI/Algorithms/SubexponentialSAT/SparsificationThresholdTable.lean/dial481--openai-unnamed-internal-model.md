---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SparsificationThresholdTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationThresholdTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationThresholdTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Statically compiled threshold banks

Every arithmetic expression and output port is fixed before the input M is
read. The common arithmetic workspace is reused, while completed outputs are
stored in a disjoint fixed bank.


### `sequence`

 This recursion builds finite syntax before the input word is supplied. 

### `expressions`

 There is one saved threshold per width 2,...,k. 
