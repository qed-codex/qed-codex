---
{
  "module": "OAI/Computability/VPVNP/HCGadgetSpanning.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCGadgetSpanning.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCGadgetSpanning.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Connectivity of the directed Hamiltonian-cycle gadget

If each pair of ports and each buffer belongs to the same permutation cycle as its
neighbors, the whole variable track lies in one cycle. The separators join the tracks
in cyclic order, and a single incident port suffices to attach each clause.


### `isCycleOn_of_track_connections`

 The local connectivity conditions for variable tracks, separators and clause
vertices suffice to make the permutation a Hamiltonian cycle. 
