---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutDenominatorProgramQueryReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutDenominatorProgramQueryReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutDenominatorProgramQueryReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact-time replay of the complete denominator call. The three opaque
outer accumulators are never inspected, including by storage subroutines. 

### `command_avoids`

 This is a syntactic no-read/no-write certificate for the actual fixed
40-register denominator program, not just a final-state preservation fact. 

### `command_rebase`

 Arbitrary replacement of outer accumulators preserves the exact number
of executed instructions, the registers, and every visible output tape. 
