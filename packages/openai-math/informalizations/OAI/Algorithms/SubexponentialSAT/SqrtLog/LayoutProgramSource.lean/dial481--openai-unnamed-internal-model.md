---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramSource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramSource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramSource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The physical Lagrange row-source emitter instantiated with integer-derived
ring scalars. Its inputs are scalar arrays, not a preassembled polynomial or
instruction stream. Upstream proofs must supply the scalar arrays and their
individual decode laws; the concrete emitter itself is fully traced. 

### `emitSource_runsIn`

 Real source construction plus its exact ring-valued polynomial meaning.
The scalar-table producer is deliberately not hidden inside this theorem. 
