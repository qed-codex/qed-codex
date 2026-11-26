---
{
  "module": "OAI/Computability/VPVNP/CompressorOrdinalProgress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOrdinalProgress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOrdinalProgress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Guard progress and work of a native packet

An ordered list of successful cursor returns determines the guard
progress needed to replay that packet in the online dispatcher. The
same report list also determines its calls-plus-probes charge.

