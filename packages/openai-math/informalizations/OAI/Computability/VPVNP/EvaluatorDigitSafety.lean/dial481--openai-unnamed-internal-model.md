---
{
  "module": "OAI/Computability/VPVNP/EvaluatorDigitSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorDigitSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clock and storage along every branch of a digit countdown

A decremented digit can cause many nondeterministic matrix queries. Across
these queries the two counter stacks hold at most the original width, even
on a path that eventually rejects. The callback must itself supply a clock
and storage guarantee for every branch, and preserve the counters whenever
it returns normally.


### `repeat_safe`

 A safety condition checked at every callback instruction and at every
countdown instruction holds throughout the full repetition. All normal
returns present empty counter stacks and reserve at least `extra` more
instructions. Abnormally terminating branches satisfy the same time and
storage checks up to their halt. 

### `frame_length_le`

 The countdown's local storage allowance is the width of one digit. 

### `repeat_space_clock`

 On the closed binary-choice machine, all branches halt within the clock
and every reachable configuration fits the peak bound. The final instruction
closes a normal return with the selected halt outcome. 
