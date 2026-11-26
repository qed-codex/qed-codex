---
{
  "module": "OAI/Computability/VPVNP/EvaluatorTallyLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorTallyLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorTallyLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Enumerating the labels in an evaluator column

The remaining labels are counted in unary. The body sees the index of the
current label, starting at zero. Each normal return increments the index
before the next iteration. At the end of the column the loop clears the
index for reuse on the next column.


### `State`

 Control states for the unary label loop, including the callback, index advancement, final
index clearing and rejection. 

### `tallyLoop`

 A zero bit in the unary count rejects. The body is invoked once per mark. 

### `loop_count_succ`

 Reading one mark costs one instruction. Each path through the body spends
one further instruction to push the index mark if it returns normally. 

### `loop_count_zero`

 The empty test, one pop per used index mark, and the last empty index
test return to the caller, preserving every stack other than the index. 
