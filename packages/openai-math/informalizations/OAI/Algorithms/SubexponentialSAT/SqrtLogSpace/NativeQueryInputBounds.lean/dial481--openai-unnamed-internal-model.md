---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQueryInputBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQueryInputBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeQueryInputBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed input-length bounds for the literal trial and accepted query
preparations. The common bound is produced before the greedy loop; none of
these caps contains a suspended caller word or a repeated-node scratch cap. 

### `sourceCap`

 One source allowance covers the actual marked entry and both canonical
numeric and physical parameter words. All coefficients are fixed first. 

### `frontendCap`

 Both literal frontends fit this source-only cost. 

### `preparedCap`

 This is the actual Setup.localBound after the frontend and preparation,
with its fixed preparation coefficient and degree. 

### `canonical_lengths_cubic`

 Canonical padding comes from the real frontend inputLengths definition;
the checked FrontState.canonicalLengths identifies these same words later. 

### `scalar_le_common`

 The common physical selector cap dominates its own scalar sum. 

### `cap_polynomial`

 Substitution uses a fixed polynomial for the genuinely produced common
bound. The degree is independent of all later states, candidates and nodes. 

### `trial_inputs`

 Literal losing or winning trial queries have one source cap before the
candidate, mark, retained collector and physical padding are chosen. 

### `accepted_inputs`

 The history-only final query uses the same kind of concrete source cap;
there is no candidate product and no unrestricted caller-word contribution. 

### `chosen_cap_polynomial`

 Substitute the actual startup and metadata output into the same common
bound used by every staged round and the final accepted history. 

### `setup_local_bound_le`

 Actual Setup uses a smaller frontend cost than the uniform literal-query
allowance, so its retained local bound fits the same preparedCap. 

### `setup_prefix_bound_le`

 The actual source-prefix bound is a maximum with the carried frame;
its local polynomial has no hidden-word or repeated-node scratch term. 

### `setup_time_le`

 The measured frontend/preparation/seed cost uses the same actual
local bound; it never uses the collector's physical length. 
