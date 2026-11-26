---
{
  "module": "OAI/Computability/VPVNP/EvaluatorMonomialSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMonomialSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMonomialSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The exponent scheduler's all-branch time and space bounds

The largest intermediate digit counter has the bit width of the field
cardinality, regardless of how many times the label callback is invoked.
The fixed control therefore preserves a polynomial storage cap even on
branches that reject inside a matrix-entry query.


### `machine_bounded`

 For callbacks with the indicated all-path contracts, the complete
monomial traversal uses the same clock as its count computation and keeps
every stack within the polynomial scheduler allowance. 

### `machine_space_clock`

 The bounded contract implies a physical stopping statement and the peak
bound on all reachable stack states, even if an intermediate branch rejects. 
