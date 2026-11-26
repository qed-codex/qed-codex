---
{
  "module": "OAI/Algorithms/SubexponentialSAT/UnaryForPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/UnaryForPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/UnaryForPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control unary-counted callbacks

The counter is a Boolean stack whose length is the iteration count. Its bits
are ignored. The controller pops before each callback and tests the presence
flag; callbacks preserve the remaining counter tail and may clobber all
registers. Every observation contains an actual callback evaluation.


### `Visits.bounds`

 Exact callback count and exact controller overhead, including the final
empty pop and false guard. 

### `for_correct_measured`

 Explicit observations of the actual callbacks, with a sum of their costs. 
