---
{
  "module": "OAI/Computability/VPVNP/ParseTreeBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseTreeBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseTreeBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Parsimonious Boolean encoding of an ordered parse

The flags selected by a satisfying assignment are precisely the occurrences of
one tree. Conversely, the characteristic function of a tree's occurrences
satisfies every incidence clause. Thus summation over accepted Boolean witnesses
counts each ordered tree exactly once.


### `treeBits`

 The finite Boolean word recording exactly the occurrences of the parse. 

### `satisfyingEquiv`

 For a fixed root degree and state, the accepting words are in bijection
with the ordered parse trees. 
