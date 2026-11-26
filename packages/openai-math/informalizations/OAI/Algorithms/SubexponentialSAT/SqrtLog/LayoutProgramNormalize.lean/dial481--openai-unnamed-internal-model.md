---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramNormalize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramNormalize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramNormalize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Runtime-width normalization for signed-component matrix words. This uses
only the existing padding, clear and transfer bit programs. In particular,
normalizing a component never invokes modular integer arithmetic. 

### `normalizeAt`

 Local normalization ports: input/output 0, consumed unary width 7;
port 5 is preserved data. Ports 1,2,3,4,6 are empty work stacks. 

### `normalizeAt_eval`

 Even a long input with redundant zero bits is normalized by an actual
finite program. Both its source length and its requested width are paid. 
