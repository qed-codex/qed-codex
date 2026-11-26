---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramPair.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native arbitrary-width coefficient multiply-and-accumulate. The high
workspace computes the ring product; the low workspace updates one encoded
array cell. Its runtime index scans and all transfers are explicitly paid. 

### `command_run`

 This is the concrete bit-command execution for one pair; all coefficient
arithmetic calls are the native programs, never abstract ring operations. 
