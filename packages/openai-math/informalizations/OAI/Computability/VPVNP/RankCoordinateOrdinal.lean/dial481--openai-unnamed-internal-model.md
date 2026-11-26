---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateOrdinal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateOrdinal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateOrdinal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Calling convention for a streamed greedy index

The input is a dense basis ordinal. A physical selector returns its original
index in a fresh binary result word. Its auxiliary ports can be reused by a
subsequent scalar query as soon as they satisfy the ready predicate again.


### `Port`

 An ordinal reader receives a binary input index and writes the selected original index on
its result stack. 

### `bank`

 Initialize the ordinal reader with a fixed-width input index, a result stack, and its
auxiliary stacks. 

### `CorrectSpace`

 For every valid ordinal and ready auxiliary bank, preserve the input word and return the
selected index in a width-w word within the step and per-stack height bounds. The final
auxiliary bank is ready for another call. 
