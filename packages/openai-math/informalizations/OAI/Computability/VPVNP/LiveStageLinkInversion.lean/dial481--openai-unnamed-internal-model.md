---
{
  "module": "OAI/Computability/VPVNP/LiveStageLinkInversion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLinkInversion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLinkInversion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Recovering an accepting source segment from an accepting linked run 

### `recover_call`

 Every successful call at a valid stage tag arises from its actual source
table on the same bit string. This direction uses exactly the remaining fuel. 

### `recover_accepting_stage`

 An accepting run beginning at a known tag contains a complete accepting
source segment for that tag before any later component can execute. 
