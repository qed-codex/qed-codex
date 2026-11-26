---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourceRowsProgramConcrete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourceRowsProgramConcrete.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSourceRowsProgramConcrete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual finite source-row controller. This is a fixed composition of
native plan lookup, source dispatch, polynomial execution and row emission. 

### `sourceRows`

 The lookup's retained register4 reports actual pair membership. Missing
factor incidences produce a complete ambient zero-row table. Caller parks the
four target-cutoff caches before entry and restores them after exit; the full
source cutoff is always read from210. 
