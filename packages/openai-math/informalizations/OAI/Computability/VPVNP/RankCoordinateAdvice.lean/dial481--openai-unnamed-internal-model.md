---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Static advice for the Cramer coordinate reader

Each slice supplies the two determinant roots, the greedy selector, the equation
rank and row count, and one scale for each operation. Live basis indices and
the label are supplied by the caller. All private work stacks start empty.


### `advice`

 The persistent image shared by the label and Frobenius readers. 

### `extra`

 Advice and initially empty work stacks, mounted on the evaluator's extra ports. 

### `portBound`

 Width of the largest advised stack, including the two nested readers and
the selector's side bank. 

### `fit`

 The bounds consumed by the preparation routine. Only the live unary label
can exceed the maximum advised word length. 

### `extra_total_length`

 Empty work ports add no bits to the total advice length. 
