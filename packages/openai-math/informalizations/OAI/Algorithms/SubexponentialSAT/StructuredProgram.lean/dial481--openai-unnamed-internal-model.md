---
{
  "module": "OAI/Algorithms/SubexponentialSAT/StructuredProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StructuredProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/StructuredProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Structured programs compiled to finite bit instruction tables

The syntax has no unbounded natural-number registers or semantic-function
instructions. All data operations are the concrete Boolean-register and stack
instructions of BitProgram. Loops inspect a Boolean register, and changing data
never changes the finite generated instruction table.


### `State`

 Data separate from the finite program counter. 

### `Atom`

 Every atom is a single existing instruction with its continuation omitted. 

### `eval`

 Atom evaluation uses the existing instruction evaluator itself. 

### `Eval`

 Finite executions count exactly the atom and Boolean-test instructions. 

### `Site`

 One static site per atom or guard; sequencing introduces no instruction. 

### `entry`

 Entry address when the command's continuation is a given address. 

### `code`

 Actual instruction at each static site. While bodies return to their guard. 

### `eval_trace`

 The compiler correctness statement is about the actual BitProgram step.
The local table-agreement premise is discharged by the whole-program compiler. 

### `size`

 Syntactic control size, independent of all runtime stack lengths. 

### `siteEquiv`

 An explicit computable enumeration of control sites; no finite-choice
oracle is used to construct the generated instruction table. 

### `labelEquiv`

 The extra address is the common final halt instruction. 

### `compiled`

 A concrete, computably generated finite bit program. 

### `compiled_trace`

 Whole-program correctness: n structured steps become n actual bit-program
steps to the exit address, with no unresolved compiler-certificate premise. 

### `compiled_halt_trace`

 Executing the generated final halt costs one additional instruction. 

### `ioState`

 Canonical stack input/output data, including all cleared work registers. 

### `primitive_execution`

 The generated structured program executes on the actual primitive tape
machine, at its proved program-fixed overhead times the source step count. 

### `primitive_outputs`

 Canonical input and one-bit output connect directly to the strict primitive
machine output convention; all work storage must be cleared in the source proof. 
