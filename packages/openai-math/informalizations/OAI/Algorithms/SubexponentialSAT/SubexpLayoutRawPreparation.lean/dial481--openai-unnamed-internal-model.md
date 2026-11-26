---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLayoutRawPreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLayoutRawPreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLayoutRawPreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual entry preparation for the paired clause-family program

The five retained inputs are binary n, binary ell, the prime word, binary D,
and the forward encoded leaf. The fixed code constructs the unary-factor
prefix, saves both streams, builds the clause shape masters, and copies the
leaf. No scope list, factor table, or unary shape is supplied as an oracle.

