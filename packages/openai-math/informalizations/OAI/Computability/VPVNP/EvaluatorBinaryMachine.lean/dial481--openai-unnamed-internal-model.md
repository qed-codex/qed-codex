---
{
  "module": "OAI/Computability/VPVNP/EvaluatorBinaryMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorBinaryMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorBinaryMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary machine for matrix-index evaluation

The input reader, radix converter, digit scheduler and terminal residue test
are linked in finite control. Only the two matrix callbacks vary when the
program is constructed. The tape table itself is independent of the advice
and the exponent width. Its two callbacks implement the scalar coordinate
queries and multiplication in the advised field.


### `MachinePort`

 The binary evaluator's stack ports. The extra port holds the raw input, and the remaining
ports belong to the input converter and scheduler. 

### `outputPorts`

 Embed the three terminal registers into the scheduler's work bank. 

### `evaluator`

 Run the raw binary monomial program, then test its final endpoint and
branch directly on the low limb of the accumulated product. 

### `program`

 The literal table of a fixed evaluator. Every input starts on its designated
raw input tape. 

### `program_paths_eq`

 A bound for every stack path transfers the integer count to the fixed
literal table. The overhead is quadratic in the bit-stack time and input size. 

### `program_head_space`

 A reachable bank size bound limits each literal tape head throughout
the evaluator computation, independently of the number of transitions. 

### `stackCount_mod`

 The actual stack-path count modulo the advised prime, given the two
matrix-step specifications. Output data are the binary current ordinal,
unary working limb width, and the packed field product beginning with its
prime-field coordinate. 
