---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorLogged.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLogged.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLogged.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The logged interpreter computes the same metered local calls

The physical processor represents private memory by a finite write log.
These equations transfer the native instruction and probe cutoff, including
rejection on a short guess stream, to that representation.

