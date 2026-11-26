---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanAddLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanAddLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanAddLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The vector length is a unary input, never a generated list of instructions. 

### `addScan_eval`

 Full vector addition scan. The input counter has one arbitrary bit per
coefficient. Both flat vector suffixes are currently empty; the lower-level
step already permits arbitrary suffixes for embedding in record interpreters. 

### `addVector_eval`

 A complete native flat-vector addition, with forward-order output on
stack zero and empty input/counter/scratch stacks. The width and modulus remain. 
