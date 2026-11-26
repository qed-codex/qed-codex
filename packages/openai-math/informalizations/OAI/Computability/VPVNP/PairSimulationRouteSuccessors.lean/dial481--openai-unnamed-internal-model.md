---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteSuccessors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSuccessors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteSuccessors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking the successor fields in cursor-bit order

The counted range starts at offset zero. For each cursor bit it calls the
native routing checker on the corresponding successor field and then advances
the common offset by eight guest words. Its mismatch mask records exactly
the failed successor checks on the four resident half-wire buffers.

