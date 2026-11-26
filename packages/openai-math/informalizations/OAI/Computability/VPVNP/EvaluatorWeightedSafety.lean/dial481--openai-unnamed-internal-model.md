---
{
  "module": "OAI/Computability/VPVNP/EvaluatorWeightedSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorWeightedSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorWeightedSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Independent time and space bounds for a weighted matrix step

The index choice, field multiplication and ordinal commit use short clocks.
The entry query supplies its own space-bounded execution. Consequently the
query's potentially exponential running time never enters the stack capacity.


### `bankSpace`

 At call boundaries the largest field stream occupies one working word
per extension coefficient. 

### `localTicks`

 Space reserved for the short subroutines. 

### `callback_bounded`

 From a space-bounded scalar reader, the whole callback returns a legal
weighted payload on every nonrejecting branch within its stated clock. 
