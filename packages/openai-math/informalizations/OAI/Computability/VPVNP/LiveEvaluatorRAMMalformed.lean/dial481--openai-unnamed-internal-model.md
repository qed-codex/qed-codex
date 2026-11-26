---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMMalformed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMMalformed.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMMalformed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native evaluator-group counts on arbitrary configuration words

If a complete native path accepts, the preparing call checks both state
words and the two scans check every symbol. Thus malformed words admit no
accepting path. The cost-capped path count agrees with the decoded local
tail factor even when a configuration fails to decode.


### `native_forces_configAt`

 Native success forces the original raw memory of each boundary to
represent an evaluator configuration, including canonical halt padding. 

### `tailCount_eq_capped`

 The native count under the actual global and per-call transcript caps
equals the local tail factor for every cut field. The endpoint memory
hypotheses identify the gathered words with their checked decoder, so the
two invalid-decoder cases give zero on both sides. 
