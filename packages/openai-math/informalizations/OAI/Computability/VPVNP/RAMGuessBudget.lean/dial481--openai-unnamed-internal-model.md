---
{
  "module": "OAI/Computability/VPVNP/RAMGuessBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMGuessBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMGuessBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A uniform bound on the private bit string of a successful site

Every local binary choice uses one bit, and each admitted read guesses one
full word. These bounds give the finite range for a tape program that chooses
the complete private string, with a single stop at its selected length.


### `PrivateRAM.Machine.incident_guesses_le`

 This single public length bound works for every incident string arising
from the shared-bit layout, independently of its acceptance or rejection by
other sites. 
