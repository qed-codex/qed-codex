---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankCache.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankCache.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntryBankCache.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `CacheWords`

 The persistent cache fields. There is deliberately no condition on the
caller's private accumulator and queue ports212..251. 

### `covered_attach`

 Reattach the two covered-case branches around an actual inner trace. 

### `selected_attach`

 Reattach the row-covered flag after either concrete branch has run. 
