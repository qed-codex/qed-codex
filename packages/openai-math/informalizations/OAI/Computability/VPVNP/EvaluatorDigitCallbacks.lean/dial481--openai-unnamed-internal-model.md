---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitCallbacks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitCallbacks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitCallbacks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iterating a branching evaluator callback by a binary digit

Each positive counter value dispatches one copy of the same callback. Its
different outcomes can take different times and change the evaluator state.
The counter stays at the decremented value for all of these outcomes. At
zero the loop clears the counter and invokes the caller once per sequence
of callback outcomes, with the actual remaining fuel for that sequence.


### `repeatBudget`

 A per-trace upper bound. It covers the empty-counter pass at the end,
one scan and restoration per positive counter, and every callback. 

### `repeat_count_of_bound`

 The output on trace `z` is obtained by folding the callback transition
over exactly `d` outcomes. The single family of actual delays works for
every continuation, including continuations that inspect the fuel. 
