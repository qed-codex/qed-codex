---
{
  "module": "OAI/Computability/VPVNP/EvaluatorBinarySafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorBinarySafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorBinarySafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stopping time and space for the complete binary evaluator

The raw input reader, radix converter, matrix callbacks and final residue
comparison execute as one finite stack routine. Both bounds cover rejected
paths as well as accepted paths. The terminal clock charges only the endpoint
and low-limb scans and adds no term involving the earlier running time to
the space estimate.


### `SafeFrom.weaken_space`

 The same execution certifies every weaker pointwise storage condition. 

### `terminalTicks`

 Time spent after the final matrix step. 

### `fullTicks`

 Instruction bound for the raw input reader, radix conversion, matrix schedule and final
endpoint and residue test together. 

### `fullSpace`

 Stack bound for all branches of the binary evaluator, including the storage used in its
final endpoint and residue scan. 

### `fullTicks_le_exp_poly`

 The terminal scan preserves the separation between the singly exponential
input-length factor and the polynomial exponent-width factor of Theorem 8.1. 

### `fullSpace_le_power`

 The space bound on the full machine is quartic in the numerical widths,
the label count, advice size and the space occupied by its callbacks. 

### `full_space_clock`

 All binary branches of the complete evaluator halt by the full clock.
Every reachable stack on that same program satisfies the polynomial height bound. 
