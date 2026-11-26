---
{
  "module": "OAI/Computability/VPVNP/PairRefreshTraversalQuiet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshTraversalQuiet.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshTraversalQuiet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Choice and external-memory frames of the canonical refresh action

Only the preceding child reader consumes the guessed half-wire bits. The
selected local action consumes no further choices and only reads external RAM.


### `canonicalAction_report`

 Every successful complete report factors at the certified local prefix, including
reports obtained at an arbitrary fuel bound. All its external updates occur in the suffix. 
