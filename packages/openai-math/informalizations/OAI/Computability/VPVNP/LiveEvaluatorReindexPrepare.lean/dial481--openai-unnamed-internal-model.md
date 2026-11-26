---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorReindexPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Joining the physical prefix and runtime initialization writes

The prefix copy stops at the true length of the advised evaluator input.
The runtime skeleton starts at that address. Together these prepare the
state bank used by the exponent scatter phase.


### `Copied.append`

 Adjacent completed native copies agree with a single copy of the
concatenated stream, including the case of an empty first or second piece. 

### `prefix_runtime_stores`

 Native control, exact advice-prefix and runtime-skeleton writes prepare
the zero-exponent bank. The addresses here use the actual prefix length. 
