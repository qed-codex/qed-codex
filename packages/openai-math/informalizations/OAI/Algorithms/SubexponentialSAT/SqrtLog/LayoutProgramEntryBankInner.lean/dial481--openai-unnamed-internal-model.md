---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankInner.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankInner.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankInner.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual cached universal-entry call, including all physical staging,
export and cleanup. The caller's private fiber-loop bank is unrestricted. 

### `inner_eval`

 This theorem has no value-producing callback: it calls the fixed
`IntegerEntry.command`, and charges staging, export and complete cleanup. 
