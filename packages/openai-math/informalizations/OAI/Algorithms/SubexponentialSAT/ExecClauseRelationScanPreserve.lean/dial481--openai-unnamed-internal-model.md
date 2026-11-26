---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecClauseRelationScanPreserve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseRelationScanPreserve.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecClauseRelationScanPreserve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A preserving wrapper for repeated clause-vs-formula scans. A real copy of
the full formula is scanned, and its residual copy is explicitly cleared. 

### `command_eval`

 Both the original formula and query survive the scan. Only the output
singleton must be consumed before invoking another preserving scan. 
