---
{
  "module": "OAI/Algorithms/SubexponentialSAT/FixedParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FixedParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FixedParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed finite programs and measured expansion of TM2 statements

This module expands TM2's finite statement blocks into actual one-constructor
stack transitions.  The execution theorem counts those transitions.  It does
not identify a stack operation with a primitive binary tape operation; that
additional encoding is a separate compiler layer.


### `statementSize`

 The number of constructor nodes in a finite statement. 

### `MicroCfg`

 A configuration during expansion of a source statement. 

### `embed`

 Source block boundaries are represented by their next statement. 

### `microStep`

 One transition executes one constructor, and at most one stack operation. 

### `statement_micro_execution`

 Every source statement has a measured, finite expansion into microsteps. 

### `blockOverhead`

 The largest source block is fixed by the machine, not by its input. 

### `micro_simulation`

 The local compiler theorem is proved from the transition definitions. 

### `micro_execution`

 A source run of t blocks expands to at most C_tm * t actual microsteps. 

### `codeSet`

 All microcode comes from a finite set of substatements of source blocks. 

### `microStep_code_mem`

 Executing one constructor cannot introduce code outside the fixed program. 

### `microTrace_code_mem`

 Every state in an actual micro-execution retains fixed finite code. 

### `Control`

 The complete set of instruction pointers is finite for each fixed source. 

### `FiniteMicroCfg`

 A micro-configuration with its finite-code invariant built into the type. 

### `finiteControl`

 The finite portion of the compiled control: instruction and local variables. 

### `finiteMicroStep`

 Restricting the transition function requires no additional runtime operation. 

### `finiteEmbed`

 The compiled initial and block-boundary configurations. 

### `finiteMicroStep_forget`

 Erasing invariant proofs recovers exactly one stack microtransition. 

### `finiteTrace_of_microTrace`

 Restriction to finite code preserves the exact number of actual steps. 

### `finite_micro_execution`

 A concrete finite-control stack implementation of every measured macro-run. 

### `outputs_finite_micro_execution`

 A successful finite TM2 output has an actual finite-control stack execution. 

### `fixed_multiplier_bound`

 Multiplying an established running time by a fixed constant preserves the exponent. 

### `fixed_startup_bound`

 A fixed startup and fixed per-step overhead are absorbed by a fixed coefficient.
The execution bound being transformed must be supplied separately. 

### `fixed_table_primrec`

 Fixing any finite table yields a genuinely primitive-recursive lookup.
This is a computability statement, not a constant-time bit-machine assertion. 

### `hardcoded_parameter_computable`

 Hardcoded parameters remain computable without an input-dependent oracle. 

### `selected_parameter_hardcoded`

 Any selected parameter can be hardcoded once its width is fixed. This alone
does not assert computability of the entire width-indexed family. 

### `uniform_parameter_preprocessing`

 Effective parameter tests give actual computable preprocessing of a
width/input pair; its output ignores the variable input word. 

### `wordWriter`

 A two-tape primitive program which writes a fixed word on work tape 1. 

### `writerCfg`

 Configuration before writing symbol i, or at the end when i=length. 

### `writeIndex`

 One indexed symbol is written, and the work head advances one cell. 

### `writeIndices`

 Iterated physical work-tape updates performed by the fixed writer. 

### `wordWriter_execution`

 Initialization by a fixed word has a proven input-independent primitive runtime. 

### `writeBits`

 Direct physical writing of the listed bits, with the head advancing right. 

### `wordWriter_correct`

 The hardcoded word is physically present on the work tape after a constant
number of primitive steps, and the input tape is unchanged. 

### `Scanner`

 A finite deterministic scanner over the binary input alphabet. 

### `smallAcceptedWords`

 A finite, explicitly exhaustive precomputation for a fixed variable threshold. 

### `smallSolver`

 A real primitive machine for the bounded-variable branch. All truth-table
work is finite preprocessing, using the explicit exhaustive SAT evaluator. 

### `smallSolver_bound`

 The finite-threshold branch has a proved bit-machine runtime within the
candidate envelope. The machine depends on B, never on the varying formula. 
