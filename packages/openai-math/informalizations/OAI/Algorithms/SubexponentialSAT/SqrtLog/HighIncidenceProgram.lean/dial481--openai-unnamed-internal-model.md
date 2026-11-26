---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical high-incidence selection from supplied explicit scopes

The input is a framed list of scopes with original natural-number identifiers.
Every query invokes the audited source-preserving record/membership scan. The
cutoff is a supplied unary integer in this module; no arithmetic or translation
from clauses to scopes is silently performed. The fixed program appends the
strict comparison bit and advances the original-coordinate counter.

