---
{
  "module": "OAI/Computability/VPVNP/EvaluatorStreamCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorStreamCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorStreamCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting a streamed sequence of linear steps

After an index guess, the evaluator retains only that index and its running
product. Different branches may take different times to query their matrix
entries. A common bound per step suffices for the modular count: after every
permitted choice the remaining clock still covers the remaining steps.


### `Continuation`

 The continuation count as a function of the remaining instruction budget and the current
evaluator stack bank. 

### `actionCount`

 Continuation semantics of the chronological actions, independently of the
finite control that emits the schedule. 

### `actionCount_mod`

 After all streamed queries, reducing the integer count modulo the prime
gives the first coordinate of the accumulated weighted matrix product. 

### `monomial_actionCount_mod`

 Apply the chronological count identity to the actual Frobenius and label
matrices in their monomial basis. The functional is applied after all digits. 
