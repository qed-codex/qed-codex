---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMarkedQueryAdapter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMarkedQueryAdapter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMarkedQueryAdapter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual per-mark staging and return adapters. Each reference is copied and
reversed into the frontend marker words. Each completed high-assignment count
is moved to the marked collector, with its temporary words reclaimed and parser
registers reset by real instructions. Fresh high-query setup remains mandatory. 

### `markInput_eval`

 This is the original reverse-aware marker staging on the shared leaf bank. 

### `cleanupPorts`

 These words are freshly created by the marker/high-query invocation and
must have been empty at its external entry. No shared-H assumption is used. 
