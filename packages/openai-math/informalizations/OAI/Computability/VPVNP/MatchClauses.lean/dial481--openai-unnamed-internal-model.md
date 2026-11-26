---
{
  "module": "OAI/Computability/VPVNP/MatchClauses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MatchClauses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MatchClauses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Boolean flags for matching finite words

Each match flag is equivalent to a conjunction of prescribed bit values.
There is one binary implication per bit and one clause for the converse.


### `meetCNF`

 Conjunction over a finite index type. 

### `matchClauses`

 A flag is set exactly when the payload bits match the specified word. 
