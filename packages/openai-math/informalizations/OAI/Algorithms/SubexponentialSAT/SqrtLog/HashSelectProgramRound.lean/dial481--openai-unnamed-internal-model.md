---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramRound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramRound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramRound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One concrete greedy round copies the saved family, evaluates every row,
selects a binary minimum, and prepends the winner to the current matrix. 

### `round`

 Genuine fixed code: no input-dependent unrolling and no semantic atom. 

### `round_eval`

 The only unimplemented computation in this composition is exactly the
explicitly supplied and traced `mass` command. `shape` is an ABI equality
about the copied queue, not a computation or an oracle assumption. 

### `state_eq_self`

 Characterization of the work-bank ABI inside an arbitrary outer state. 

### `copied_shape`

 The queue-copy shape obligation follows from ordinary empty work banks. 

### `round_eval_ready`

 Ready-to-run round with no abstract ABI equality assumption. 
