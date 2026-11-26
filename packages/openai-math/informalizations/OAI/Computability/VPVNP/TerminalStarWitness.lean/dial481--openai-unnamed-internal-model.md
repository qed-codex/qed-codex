---
{
  "module": "OAI/Computability/VPVNP/TerminalStarWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TerminalStarWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TerminalStarWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extracting a tensor witness on equally wide terminals

In (4.4), the height and the old tensor are chosen before the circuit
lengths. The star width is the number of terminal legs at each party.
Reindexing the profile witness gives one coefficient table on the
terminals, with dimension `2 ^ b` at each of them and no other legs.


### `terminalMultiplicity`

 The number of terminal legs grouped at the given party. 

### `starWitness_eq_placed`

 Reindex the coordinates of a width-profile witness as one equal-sized
leg per terminal. At a party with no terminal there is one coordinate. 

### `exists_terminalStar_witness`

 A strict lower bound valid for every extending center selects a concrete
height and terminal coefficient table over the original field. 

### `exists_cubeStar_witness_of_embeddings`

 Equation (4.4) from CAT(0) embeddings of the extending spectral points.
The selected tensor has one explicit equal-sized basis at each marked
singleton corner. The height and the table are independent of later powers. 

### `exists_cubeStar_witness`

 Equation (4.4) for a cube realized by a spectral wire metric. The
CAT(0) completion of the attaining extension supplies the star bound. 
