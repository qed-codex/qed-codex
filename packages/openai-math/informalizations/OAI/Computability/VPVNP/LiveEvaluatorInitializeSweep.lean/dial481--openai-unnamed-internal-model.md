---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorInitializeSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInitializeSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInitializeSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete native scan of the evaluator's initial tape

The initialized state bank occupies consecutive words for the control and
both tapes. A state write is followed by one native burst per input bit on a
running evaluator. An initially halted evaluator and the final accepting
endpoint each use a single state write.


### `activeLength`

 Number of input bits to copy into the initial tape, zero for an evaluator that starts
halted. 

### `controlTag`

 The initial control word, one for an initially accepting evaluator and two for its first
running state. 

### `Stores`

 A complete word image of the code in the contiguous memory region. 

### `field_cases`

 Each configuration word is the control field or one indexed tape symbol. 

### `firstData`

 The natural address of the head cell of the first tape, where copying the initial input
begins. 

### `Copied`

 Precisely the first `cursor` symbols have been written. 

### `copy_segment`

 The native run over every input bit, including the empty run when
the evaluator starts in its accepting state. The source words may be on
either side of the writable input interval. 

### `copied_stores`

 After the last burst the entire two-tape bank is the canonical initial
code. The untouched left side, second tape, and right padding use zero-default
memory. An empty program has only its state word. 

### `final_stores`

 At the last group the outgoing scratch bank is the accepting sentinel.
Only one control word is written. There is no outgoing physical cut. 

### `prepare_native`

 The control-write call and all input-bit calls together prepare the actual
initial evaluator bank. The packed input buffer must survive the control write
and lie outside the writable tape interval. 

### `final_native`

 The last tail group compares against a native-prepared canonical accept
bank without receiving an outgoing cut from a nonexistent neighbor. 
