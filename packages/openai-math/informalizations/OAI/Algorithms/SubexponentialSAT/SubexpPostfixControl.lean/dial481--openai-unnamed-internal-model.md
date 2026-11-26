---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPostfixControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPostfixControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPostfixControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete postfix instruction dispatch and literal push

The fixed prefix tags are push `0`, add `10`, and multiply `11`.
A push tag is followed by an `Encoding.frame` coefficient payload. End of
the code stack ends the instruction stream. The base dispatcher exposes
explicit service exits. The linked program implements literal push through
the actual frame parser and a Boolean-stack encoding loop; scalar arithmetic
remains at explicit service boundaries.

Registers: 0 last bit, 1 successful-pop flag, 2 binary-operation flag.
Stacks: 0 serialized code, 1 unary operand depth, 2 framed operand data.
The operand data stack is preserved throughout dispatch. On a successful
dispatch the depth stack has already been adjusted for the pending service.
The linked literal service uses stack 3 as initially empty scratch and returns
to dispatch with that scratch empty and the framed operand list updated.


### `pushService`

 Entry to a payload parser followed by a framed operand push. 

### `addService`

 Entry to the scalar addition service on the top two framed operands. 

### `mulService`

 Entry to the scalar multiplication service on the top two framed operands. 

### `program`

 Twenty labels, three one-bit registers, and three Boolean stacks. 

### `prepare_push_trace`

 Five actual transitions decode push and reserve one new operand slot. 

### `prepare_binary_trace`

 Thirteen actual transitions prepare either binary operation and check depth two. 

### `binary_prefix_trace`

 The common six-step tag decoder ends before accessing the operand-depth stack. 

### `eof_trace`

 Empty code is a completed instruction stream, not a malformed tag. 

### `truncated_tag_trace`

 A leading one must be followed by an operation bit. 

### `empty_depth_trace`

 Binary instructions reject an empty operand stack in eight measured steps. 

### `singleton_depth_trace`

 The second explicit pop rejects depth one before any arithmetic service. 

### `step_preserves_operands`

 Dispatch never treats a scalar operation as a primitive write to operand data. 

 ## Serialization of the existing postfix instruction type 

### `serialized_push_trace`

 At the push boundary the parser sees exactly one coefficient frame and the code suffix. 

### `serialized_add_trace`

 Arithmetic remains pending: only its tag and the two-operand guard have executed. 

 ## Literal-push service with the framed-list operand ABI 

### `literalService`

 The first seven labels are the actual relocated frame parser. The remaining
labels rebuild the escaped payload from its reverse and add the list cons tag. 

### `literalService_parse_trace`

 Reuse the measured parser trace through actual instruction-table relocation. 

### `escapeBits`

 Escaped data without the final false delimiter. 

### `literalService_trace`

 Complete literal service: consume one frame and push a framed list item. 

### `controlLabel`

 The control program retains its label range; the literal service follows it. 

### `pushLoopProgram`

 Concrete linkage: only push calls the literal service, whose halt is replaced
by a return to dispatch. Add/multiply remain explicit service boundaries. 

### `pushLoop_prepare_trace`

 The five dispatcher instructions and the actual service-call jump. 

### `pushLoop_service_trace`

 The source service's halt is the linked program's actual return jump. 

### `pushLoop_literal_trace`

 Full measured push instruction: consumes its tag and complete payload,
updates the framed operand list and depth, clears scratch, and returns to dispatch. 

### `serialized_push_complete_trace`

 A genuine implementation of a source postfix push under the framed-list ABI. 
