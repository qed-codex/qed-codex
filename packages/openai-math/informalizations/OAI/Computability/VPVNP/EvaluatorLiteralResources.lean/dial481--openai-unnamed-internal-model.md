---
{
  "module": "OAI/Computability/VPVNP/EvaluatorLiteralResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorLiteralResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorLiteralResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counts, time and space of the literal evaluator from streamed coordinate queries

The program table is fixed by its two coordinate readers. Its correctness and
resources hold simultaneously for all binary exponent arrays. The same bounded
query executions justify both the field-valued path count and all-path storage.


### `stack_from_bounded_matrices`

 The all-path resource proof uses only the two deterministic read contracts
and positivity of the radix. It applies to any two matrices in the field. 

### `stack_from_bounded_readers`

 All paths of the linked bit-stack routine meet their clock and the same
height bound, even when a guessed ordinal is rejected. 

### `literal_from_bounded_readers`

 Equation (8.2) and the two literal head bounds for the same fixed binary
table. The clock may be enlarged arbitrarily without changing the path count. 
