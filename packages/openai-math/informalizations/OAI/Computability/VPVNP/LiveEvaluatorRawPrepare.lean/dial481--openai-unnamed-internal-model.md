---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRawPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRawPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRawPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing a transition from raw configuration words

A successful first call bounds the source state, verifies the proposed target
and publishes its instruction. Every word of both configuration blocks can
still be read at the same address after the call.


### `Prepared.raw_facts`

 Consequences of native preparation before either tape block has been decoded. 
