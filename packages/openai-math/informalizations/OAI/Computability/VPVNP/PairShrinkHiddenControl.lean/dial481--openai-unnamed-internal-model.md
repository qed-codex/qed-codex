---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the shrinking hidden-array row control

One count probe initializes the row. The guard uses the remaining number of
entries, and the back edge advances the dense-ID pointer by one word.


### `setupEvents`

 The six events before the first loop test. They include one external read of the selected
owner's count and five local steps. 

### `setup_run`

 Load the count and the start of this owner's row, and establish the two
constant registers used by the guard and back edge. 

### `test_run`

 One local branch tests the remaining count, including a zero-length row. 

### `advance_run`

 The two local back-edge instructions consume one row entry and advance
the ID pointer, preserving the field buffers and the loop's stable registers. 
