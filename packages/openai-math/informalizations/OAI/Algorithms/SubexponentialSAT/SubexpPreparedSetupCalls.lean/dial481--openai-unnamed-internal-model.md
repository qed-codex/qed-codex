---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPreparedSetupCalls.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPreparedSetupCalls.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPreparedSetupCalls.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed storage for prepared-quartic setup

Twenty-four work stacks are reused by the concrete arithmetic routines. Nine
cache stacks occupy ports 24 through 32; port 33 is the physical copy temporary.
This module only supplies the copying, cleanup, and frame rules. A call is
justified by an actual trace of its finite instruction table.

