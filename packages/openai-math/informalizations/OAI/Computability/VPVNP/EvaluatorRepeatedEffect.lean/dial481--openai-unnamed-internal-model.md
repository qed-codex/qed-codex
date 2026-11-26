---
{
  "module": "OAI/Computability/VPVNP/EvaluatorRepeatedEffect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRepeatedEffect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorRepeatedEffect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Summing the traces of repeated evaluator transitions 

### `stepEffect`

 Sum the continuation over the choices of one linear step. 

### `repeatEffect`

 Sum over the choice traces of all repetitions of the same linear step. 

### `repeatEffect_eq_foldr`

 Folding the step effects in chronological order counts each trace once. 
