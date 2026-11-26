---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutMatrixProgramSource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutMatrixProgramSource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutMatrixProgramSource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Relocatable finite-bank contract for integer incidence entries, and the
fixed physical storage layout used by the direct all-row matrix builder. 

### `EntryContract`

 This is a native command contract, not an entry-value oracle. Instantiation
requires an actual Eval of the fixed finite instruction program. Cache and
workspace contents are restored exactly; only the four entry ports vary. 
