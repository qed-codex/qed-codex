---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEvaluationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEvaluationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEvaluationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete evaluation-result extraction

The extractor removes the singleton operand-list framing, parses the result
payload into a reversed scratch stack, and transfers it to physical stack 15.
It clears the operand/depth/scratch stacks and preserves every other stack.


### `extract_trace`

 Actual singleton decoding, including clearing the old destination. 

### `snapshot`

 The interpreter's final stack contents before the framing is removed. 

### `evaluation_runsIn`

 A concrete evaluation/extraction service for the shared moment machine.
The final payload is forward on stack 15, and stacks 27, 28, 29 are empty. 

### `evaluation_preserves_caller`

 All twenty-eight caller-persistent stacks are unchanged. 

 ## Entry from arbitrary caller registers 

### `contextOf`

 Recover the persistent context from an arbitrary shared-machine frame. 

### `readyEvaluationProgram`

 This ready-to-call service first clears all sixteen registers by concrete
instructions, so caller loop flags need no special precondition. 

### `ready_evaluation_state_runsIn`

 State-level entry contract: only the source bytes and three empty work
stacks are prescribed; the rest of the shared frame is recovered explicitly. 
