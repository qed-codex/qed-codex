---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorCallRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Correctness of the physical call loop

Strong induction on unspent private instruction fuel follows every sequence
of adaptive reads and writes. At each callback the proof uses the actual
site table, the three remaining allowances, and the single physical record
emitted for the probe. It covers malformed guesses and every cap rejection.

