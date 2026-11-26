---
{
  "module": "OAI/Computability/VPVNP/CompressorPrefixWorkerFit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPrefixWorkerFit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPrefixWorkerFit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Motif selector word and clock bounds at reachable boundaries

The shrinking and refresh selectors use different native tables. Both accept
a fixed clock determined by the input length and the templates. The refresh
bound also covers the width cells emitted by the chosen continuation.


### `refreshConstant`

 Fixed word-width contribution of the refresh selector for the schedule's expander and motif
tie order. 

### `eventually_refresh`

 Uniform width and clock arithmetic used in the selected refresh run. 

### `eventually_shrink`

 Apply the actual shrinking prefix bounds directly to a partial semantic
execution at its current graph. 
