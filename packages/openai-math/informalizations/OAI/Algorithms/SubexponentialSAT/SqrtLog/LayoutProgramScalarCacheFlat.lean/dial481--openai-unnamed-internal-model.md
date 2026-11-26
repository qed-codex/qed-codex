---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramScalarCacheFlat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramScalarCacheFlat.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramScalarCacheFlat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The H cache builder followed by the shared physical fixed-width adapter.
Only the common width survives alongside the two flat output arrays. 

### `hWords_entry`

 Per-entry H cache contracts used by the numerator's `Cache.Values` and
`Cache.Totals` predicates. The negative array consists of actual zero words. 
