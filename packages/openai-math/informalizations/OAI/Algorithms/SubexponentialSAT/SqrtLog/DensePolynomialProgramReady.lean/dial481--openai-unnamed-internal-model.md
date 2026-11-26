---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramReady.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramReady.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/DensePolynomialProgramReady.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Static native arithmetic readiness, independent of the final service
composition. The two polynomial caches do not participate in readiness. 

### `BaseReady.frame_except_caches`

 Readiness only inspects native arithmetic ports; the two protected
polynomial caches may vary while the native arithmetic frame is retained. 
