---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMTranscript.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMTranscript.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMTranscript.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native reports of scheduled live evaluator calls

A scheduled call starts with zeroed registers and private memory, executes
the fixed evaluator body, then compares the successor cursor with the call
count. The comparison contributes one final tick to the report. The two
footer instructions fit in a uniform allowance independent of the tape
radius and word width.


### `nativeProgram`

 The concrete finite program specialized only by the word width and its four public words. 

### `callFuel`

 Enough fuel for every route through the acyclic body and both footer opcodes. 

### `nextState`

 The terminal cursor comparison at the end of an actual call. 

### `nextState_at`

 The allocated cursor sequence halts on its last call, even when the total
number of calls is exactly the word modulus. 

### `nativeStep_iff`

 Exact native success at the reset entry point. Report replay obtains precisely
the external memory produced by the body; the footer consumes no choice bit. 

### `nativeStep_of_exec`

 Compute the actual report from a successful scheduled body execution. 

### `nativeStep_exists_iff`

 Existential report form for composing calls on a specified post-call memory. 

### `nativeCell_report`

 Every actual cell call leaves external memory intact, has an empty branch stream,
and makes exactly six external reads. 

### `nativePrepare_report`

 Native cost of the cursor-zero call. Its initial source-state read is the
only extra probe beyond preparing the five scratch words. 

### `nativeStep_report_length`

 Every returned report uses less than the fixed allowance, including its final tick. 
