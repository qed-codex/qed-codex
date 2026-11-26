---
{
  "module": "OAI/Computability/VPVNP/LiveModes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveModes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveModes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First-half and tail paths in the live chain

For fixed primed exterior bits, nominations, and pair paths, each first-half
group checks its incoming and outgoing counters. The middle cut initializes
the evaluator. Each tail group checks a single transition and the uniquely
encoded outgoing configuration. Forgetting these forced fields leaves just
one accepting path of the evaluator on the full sum of the exponents.


### `TailBits`

 There are `2^h - 1` cuts strictly after the midpoint and before the final
endpoint. On each of these the tail sends an evaluator configuration. 

### `TailValid`

 Every outgoing tail cut encodes the configuration reached after the
corresponding transition and contains only zero padding. 

### `LocalRun`

 One set of local paths with their constrained first-half bit fields,
their branch-distinguished tail history, and their serialized tail cuts. 

### `localRunEquiv`

 A fixed collection of pair choices has one canonically filled first half,
then exactly as many completions as the evaluator has accepting paths. 

### `liveModesEquiv`

 Applying the local path bijection at every nomination gives the exact
two-mode path type of Proposition 9.1. 
