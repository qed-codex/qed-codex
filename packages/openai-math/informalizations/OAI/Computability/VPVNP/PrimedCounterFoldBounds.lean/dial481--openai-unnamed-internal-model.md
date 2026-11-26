---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterFoldBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterFoldBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterFoldBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds on every executed prefix of node calls

The remaining node count drops by one at each successful visit. This makes
the terminal stack test redundant after exactly the prescribed number of calls.
Every histogram component can increase by at most the prefix length, including
prefixes of tapes that fail a later check.


### `nodePrefix`

 Run the chosen prefix without testing for end of traversal. 

### `nodePrefix_visits`

 A full row has exactly as many node calls as pending nodes at its root. 
