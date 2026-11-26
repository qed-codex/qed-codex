---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorTail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorTail.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorTail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting actual configuration strings on the live tail

For each of the `2^h` tail groups the input is either the initialized machine or
a decoded incoming cut. The output is either a decoded outgoing cut or the
mandatory accepting halt at the endpoint. Each interior cut checks the live
mode, the fixed-width word encoding of both tapes and the control, and zero
padding. The resulting count is the machine's accepting path count whenever
its accepting histories fit in the chosen tape window.


### `Layout`

 The fixed fields and bit-capacity proofs shared by all groups of the tail. 

### `writeCut`

 The bits emitted at the cut after tail group `j + 1`. 

### `readCut`

 Parse all three fields, rejecting malformed words, mode, or padding. 

### `boundary`

 The first tail group receives its initialized state from the middle
exponents. The last group compares its successor to the accepting halt. 

### `Valid`

 Each physical group checks its two endpoints and one literal branch
choice. A rejecting halt fails the group that reaches it. 

### `HistoriesFit`

 The accepted runs lie in the supplied tape-space bound at every group. 

### `Runs`

 The only data counted are branch bits and the actual interior cut bits.
No configuration string is placed at either endpoint. 

### `runsEquiv`

 On an accepting computation all cut fields are forced. Reading just the
bits at adjacent cuts conversely recovers a unique accepting computation. 

### `card_runs`

 The tail contributes exactly the clocked accepting path count, including
initial acceptance, early acceptance and coincident branching successors. 

### `initialCode`

 Initialize the bounded fields from the tape machine at the middle cut. 

### `card_of_head_bound`

 For a bounded-head tape program all running states reached on a choice
string fit into a common window. This specializes the bit-string count with
no remaining hypothesis about the validity of individual configurations. 

### `card_labeled`

 Specialization to the literal two-tape machine emitted by the finite
stack compiler. The storage bound is required only on reachable stack states. 

### `middleInput`

 Recover the evaluator input from the counter words on the physical middle
cut, with the input format, advice and length parameter supplied by `assemble`. 

### `card_middle`

 The middle cut supplies the actual initial input to the first tail
transition. The count for the entire tail is the evaluator's accepting count
on the sum of the nominated production and gadget exponents. 
