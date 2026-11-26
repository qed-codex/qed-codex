---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSetupStorageCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupStorageCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupStorageCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of the concrete setup storage instructions

Copying and cleanup are charged by the lengths of the words physically read.
The final stage bound is linear in a common word bound; its coefficients depend
only on the statically allocated ports and copy lists.


### `storageOverhead`

 The allocation and copy-list lengths are fixed when the setup program is
fixed, so this overhead is linear in the runtime word bound. 
