---
{
  "module": "OAI/Computability/VPVNP/PairTreeFrontier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeFrontier.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeFrontier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prepared packets and the unvisited descriptor subtrees

Distinct current addresses alone would allow a pending sibling to occupy
a child's address. The frontier therefore records the numerical preorders
of the entire remaining subtrees. Popping a row and exposing its children
removes precisely one address from this list, regardless of the guessed
half-wire values and regardless of whether a later visit accepts.


### `subtreeAddresses`

 Preorder address list of a packet's subtree, beginning with its node followed by the
recorded descendant addresses. 

### `Frontier`

 The whole private state outside live argument packets is constrained
only by the supplied stability predicate, for instance the resident geometry
and operand cache. The typed format accepts arbitrary old half-wire values. 

### `frontier_headDomain`

 The actual typed role domain only needs the first prepared packet,
its numerical address and its physical scratch. 

### `Frontier.pop`

 A leaf may change its own private workspace. No old pending packet is
lost if its fitted interval remains stored and the common frame persists. 

### `Frontier.push`

 The children are precisely the next packets in the row's stored
placement order. Their regions cannot collide with any older pending
sibling, because all these subtrees already belonged to a disjoint forest. 
