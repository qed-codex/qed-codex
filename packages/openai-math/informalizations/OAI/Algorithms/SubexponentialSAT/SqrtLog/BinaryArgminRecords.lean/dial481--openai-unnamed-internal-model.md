---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminRecords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminRecords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/BinaryArgminRecords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A concrete paid loader for explicitly supplied binary-score records.
The representation stores the bits reversed inside each self-delimiting frame,
so the existing parser places each little-endian word directly on its stack.
The input supplies the scores; computing them is not part of this parser. 

### `records_eval`

 The parser, initialization, all comparisons, all copies, and the terminal
load are included. Scores are supplied in binary and may be exponentially
large as numbers while the bound remains linear in their bit width. 
