---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowInputTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowInputTypes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowInputTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Typed joins for the actual row-input setup.  The setup output is exactly
the correction-vector input; its first 29 stacks are exactly the type reader's
input.  These identities do not impose any initial Boolean-register values. 

### `command_eval_typed`

 The physical setup directly produces both typed views.  The master
relations are byte encodings of scalar inputs, types and the supplied row;
no computed matrix entry or correction coefficient is a premise. 
