---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transcript/Route/Packets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Route/Packets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transcript/Route/Packets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matching uniquely addressed messages

The active and direction bits precede the payload and identifier.
Only the two flags and the identifier are sent through the ordinary
sorting network. Reversing active directions must permute the full
records, so both ends carry identical data.



# Equality links implemented by packets

Select the headers and their pairing before reading payloads. Once
those headers are checked, the global permutation test imposes exactly
the indicated bit equalities between opposite ends of each active key.

