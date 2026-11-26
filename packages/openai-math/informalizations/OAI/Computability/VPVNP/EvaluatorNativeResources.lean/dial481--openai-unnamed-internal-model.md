---
{
  "module": "OAI/Computability/VPVNP/EvaluatorNativeResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorNativeResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorNativeResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Resource bounds for the native finite-algebra evaluator

The streaming coordinate routines supply independent time and peak bounds.
The arithmetic, digit loops and radix converter run with fixed control. The
bounds below apply to all their paths for every input exponent width.


### `native_from_readers`

 The reachable-path and stopping contract for the entire converter and
scheduler, from the two concrete streamed-entry contracts. 

### `adviceCap`

 A uniform bit bound for the actual advice fields over every possible
path endpoint. The bound is independent of the exponent array. 

### `localTicks_polynomial`

 The deterministic preparation and field multiplication add a polynomial
term to each matrix query's clock. 
