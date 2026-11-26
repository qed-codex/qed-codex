---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Window radius for the compiled evaluator

An absolute bound on both head positions bounds every tape write. The
nonblank support of the initial input is retained as well. Translating
these absolute positions to the current head yields a time-independent
window bound at every cut, including prefixes of malformed choice strings.


### `SupportedAt`

 All nonblank symbols lie in a fixed physical interval centered at the
initial head. `pos` is the position of the current head. 

### `history_fits`

 Any evaluator whose heads remain within radius `R` has canonical bounded
cut configurations on every branch, for every clock. 

### `history_fits_labeled`

 On the literal machine compiled from a finite stack evaluator, a bound on
the total stack storage supplies the cut window independently of its time. 
