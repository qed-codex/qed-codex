---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading an old site's descriptor address for a child visit

The next word in a placement row names an old descriptor. Its ordinal within the
old layer identifies the first outgoing port. Its absolute address identifies
the private interval for this child's half-wire guesses. The seven instructions
read one external word and preserve the unconsumed choice bits.


### `instruction`

 Seven instructions that read the next child descriptor, advance the placement-row pointer,
and compute both the child's first outgoing port and its private argument base. 

### `Linked`

 The seven supplied machine labels contain the child-address instructions with the specified
register embedding and continuation. 

### `events`

 Trace of a child-address lookup, consisting of the external read of the descriptor at `ptr`
followed by six arithmetic ticks. 

### `native`

 The child setup preserves the parent's count, the incidence tables, the other
configuration registers, all private words, and the external memory. 

### `firstPort_eq`

 Dividing the descriptor offset by its positive stride recovers the old site
ordinal. Multiplying by the old degree gives the port used by the incidence reader. 
