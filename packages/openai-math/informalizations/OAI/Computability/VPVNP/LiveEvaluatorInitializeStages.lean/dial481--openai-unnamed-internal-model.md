---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorInitializeStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInitializeStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInitializeStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linkable stages for the evaluator endpoints

The control-word write accepts immediately. The tape-copy stage returns its
cursor on an intermediate bit and accepts on the last bit. If the public
active length is zero, one call accepts without reading or writing memory.


### `putStage`

 The control-word write is a complete native stage. 

### `execute_putStage`

 Exact result and branch string for the one-call stage. 

### `finalStage`

 The endpoint stage that writes the accepting control word and finishes in one call. 

### `finalStage_stores`

 One native stage prepares the accepting endpoint in its scratch bank. 

### `copyStage`

 The fifth public word is the active bit length. The entry guard bypasses
the packed input for a zero-length sweep. The exit test hands off the stage
on the call that actually wrote the last input symbol. 

### `copyPublic`

 Place the active bit count after the four existing evaluator operands. 

### `execute_copyStage_skip`

 When the cursor is already at the public capacity, the guard accepts
with three local ticks and leaves memory intact. 

### `execute_copyStage_active_replay`

 Execute one active bit at any sufficient instruction cap. Only the
empty branch string succeeds. Every such call performs the packed source
read, the destination write, and four extra control ticks. 

### `copy_pair`

 The bounded and unbounded copies differ only in control events and their
return state. They read and write the same actual memory. 

### `copyStage_sweep`

 Starting at cursor zero, the copy stage uses exactly one call per active
bit, or one empty skip for a zero-length input. Its last call accepts, and its
memory contains the same initialized symbols as the unbounded copy sweep. 

### `prepareStages`

 The two accepting stages, with a fresh cursor at the handoff, prepare the
actual evaluator's initial bank from the packed input words. 
