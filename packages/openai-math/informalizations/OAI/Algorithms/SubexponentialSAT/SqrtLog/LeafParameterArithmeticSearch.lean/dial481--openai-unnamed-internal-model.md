---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParameterArithmeticSearch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParameterArithmeticSearch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParameterArithmeticSearch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Generic correctness for the actual tested square-times-coefficient search.
The command is exactly `Setup.Search.command`; there is no arithmetic oracle. 

### `command_eval`

 Fully concrete arithmetic search: input 1 is a positive coefficient,
input 2 the bound, 13 the counted fuel. Every tested candidate is charged. 
