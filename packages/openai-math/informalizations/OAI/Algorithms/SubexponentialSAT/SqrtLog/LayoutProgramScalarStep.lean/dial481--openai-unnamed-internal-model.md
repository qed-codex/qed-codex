---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramScalarStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramScalarStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramScalarStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A single cached scalar term: three parsed operands, three real signed
multiplications, and one real signed addition. 

 Polynomial source-step bounds for the concrete cached scalar arithmetic.
The stream has three actual binary signed operands per summand, not a stream
of precomputed products or an assumed arithmetic callback. 

### `Encodes`

 A signed triple consists of the cached coefficient, the clearing power,
and the cached binomial weight. The arithmetic loop itself multiplies them. 

### `scalarProgram_encodes_runsIn`

 Exact arithmetic conclusion for the cached scalar; parity is a separate
swap of the two output words. All three factors are multiplied by the program. 

 Exact unsigned component totals for the same concrete scalar program.
The extra invariant controls cancellation without changing any instruction. 
