---
{
  "module": "OAI/Computability/VPVNP/SlotIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Directed incidences at the thin endpoint

Appendix C assigns each non-thick–thick wire to the bundle of its thin
endpoint C. The original direction breaks ties on thin–thin wires. Incoming
wires can be enumerated at their target through the inverse slot permutation.


### `cdIncidenceEquiv`

 Partition the actual CD wires by their old direction relative to C.
The predicate may inspect either old position. This allows the same
enumeration to count demands by bundle or by the new position of D. 
