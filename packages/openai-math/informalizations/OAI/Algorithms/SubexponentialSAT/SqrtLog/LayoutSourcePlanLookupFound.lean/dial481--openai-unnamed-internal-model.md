---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourcePlanLookupFound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourcePlanLookupFound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourcePlanLookupFound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The same frozen pair-lookup program exposes its native found bit in register4.
No extra scan, metadata value, or runtime instruction is introduced. 

### `pair_command_eval_found`

 Register4 is the actual full-pair membership result, including the miss case.
This strengthens the frozen native command without adding an instruction. 
