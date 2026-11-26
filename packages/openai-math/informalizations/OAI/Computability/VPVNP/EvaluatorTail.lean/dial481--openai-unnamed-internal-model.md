---
{
  "module": "OAI/Computability/VPVNP/EvaluatorTail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorTail.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorTail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One evaluator transition per tail group

In Section 14.1 each live tail group executes one transition, preserving the
two choices of a branching transition even if their successor configurations
are equal. An accepting halt is serialized by one canonical configuration.
For any fixed clocked machine, the sequence of matching cut configurations
is uniquely determined by the branch choices, and the successful sequences
count exactly its accepting paths.


### `State`

 Accepted computations propagate a single canonical halted state down the tail. 

### `canonical`

 Forget the tape contents on a halt. 

### `step`

 A padded choice zero propagates an accepting halt exactly once.
Invalid choices, including a one at an accepting halt, enter rejection. 

### `history`

 The initial configuration and one output configuration per tail group. 

### `eq_history`

 Local tail checks fix every cut configuration, starting from the advised
initial configuration and executing one step per group. 

### `Traces`

 Accepted tail choices and their matching configurations, including the
initial and final boundary values. 

### `tracesEquiv`

 Bijection used by the last `L/2` groups of Section 14.1. It includes an
initially accepting evaluator and every early halt. 

### `card_traces`

 The integer count of valid local tail transcripts equals the machine's
clocked accepting path count. 

### `encoded_cut_unique`

 For a fixed encoding of the reached configuration, checking the tail
layout and zero padding leaves exactly one possible cut string. 
