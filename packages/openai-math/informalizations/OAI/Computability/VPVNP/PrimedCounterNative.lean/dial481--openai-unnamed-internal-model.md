---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The exact native path count of the auxiliary RAM

Section 11 realizes the coefficient of the primed pair polynomial on one
fixed private-RAM instruction table. Each accepting path consists of the
actual binary choices made at the designated internal endpoints and at the
ordered parser visits. The full native history satisfies the probe caps
and ends in an accepting halt.


### `accepts_iff`

 The native run on one complete chronological tape accepts precisely
when the assembled input bits and the joint production counts pass (9.4).
The transcript caps admit every such path. 

### `pathEquiv`

 Parsimony from complete accepted native paths to the chronological
tapes recognized by the coefficient counter. 

### `native_count`

 The actual native machine realizes the integer coefficient `f` of
the primed pair in equation (9.4), with no restrictions on internal bits. 
