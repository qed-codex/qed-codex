---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgramCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-port binary argmin calls and a parser for unevaluated candidate
payloads. The scores are absent from the input encoding. All supplied commands
are actual finite programs; semantic scores are never atomic instructions. 

### `candidateEncoding`

 Only payloads are serialized. In particular no uncomputed score is supplied
as input data to this parser. A final false list marker is consumed. 
