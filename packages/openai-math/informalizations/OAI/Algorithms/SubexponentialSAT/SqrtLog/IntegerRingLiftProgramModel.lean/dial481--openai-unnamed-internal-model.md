---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IntegerRingLiftProgramModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IntegerRingLiftProgramModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IntegerRingLiftProgramModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete, fixed native programs lifting a pair of arbitrary little-endian
binary words to the actual RingModel. There is no integer-lifting callback.
The only runtime constants are explicit represented ring caches. 

### `modelScaledBudget_polynomial`

 Explicit polynomial bound in input bit length, extension degree and scalar
word width. No dependence on the integers' magnitudes occurs. 
