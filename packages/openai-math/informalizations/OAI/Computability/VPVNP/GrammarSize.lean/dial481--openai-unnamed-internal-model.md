---
{
  "module": "OAI/Computability/VPVNP/GrammarSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarSize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Size bounds for the ordered circuit grammar

A tree at layer `d` has `d` binary productions and `d + 1` terminals. There
are Catalan many ordered shapes, two state choices at each binary production,
and one variable choice at each terminal. The labels are shared among all parses.


### `card_orderedParse`

 Number of ordered parses with fixed root state. 

### `catalan_le_four_pow`

 The shape count at layer `d` is at most `4 ^ d`. 

### `card_orderedParse_le`

 A bound on the number of parses prior to imposing a coefficient query. 

### `card_grammarLabel_le`

 The grammar has polynomially many scalar labels in the variable count, the
state count and the degree cutoff. 
