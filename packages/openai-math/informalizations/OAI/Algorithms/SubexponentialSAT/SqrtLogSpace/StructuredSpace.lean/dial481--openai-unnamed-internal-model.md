---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/StructuredSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/StructuredSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/StructuredSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Prefix resource preservation for the actual finite instruction linker.
The source bound concerns every intermediate configuration. Unassigned caller
stacks retain their original contents. Local runtime bounds may be used for
polynomial subroutines, but no accumulated outer-loop time appears here. 

### `relocate_trace_prefix`

 Every prefix of a relocated source execution is exactly the relocation of
the same-length source prefix, including a halt changed to a return jump. 

### `relocate_trace_stack_bound`

 Port embedding preserves a uniform local stack bound and the caller's
off-port bound separately. It never charges the caller's frame repeatedly. 

### `call_stack_bound`

 A structured call retains its callee's every-prefix stack bound in the
actual caller table. The table premise is the same one used by eval_trace. 

### `command_stack_bound`

 A bound proved for one compiled structured block transfers to every
installation of that same block in a finite caller table. No bound on the
caller's total runtime is used. 

### `sequence_stack_bound`

 Sequential command blocks share one uniform space bound. 

### `while_true_stack_bound`

 A loop induction combines its current body and remaining iterations by
maximum space; the number of completed iterations never multiplies the bound. 

### `loop_stack_bound`

 A boundary invariant and a uniform actual-body prefix bound establish the
same space bound through any finite number of loop iterations. 

### `compiled_halt_stack_bound`

 The final concrete halt instruction changes no stack and preserves the
bound already established through the command's exit boundary. 

### `local_stack_bound`

 The local runtime estimate applies to one concrete routine invocation.
Reusing it in an outer loop requires its boundary input bound on every call. 
