---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerRunReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerRunReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerRunReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read footprint of a complete traversal-controller execution

At each active ordinal the wrapper reads only its operand bank and the
words read by the corresponding reference report. The resets and the
final acceptance read only their operand banks.


### `Segment.reads`

 Transfer the read footprint of the reference body and every live
register setup to the unique accepting native execution. 
