---
{
  "module": "OAI/Computability/VPVNP/GrammarAssignment.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarAssignment.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrammarAssignment.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The coefficient equations at a small-circuit length

At a length where the universal polynomial has a circuit of the stipulated size, the
positive-degree grammar of Section 8.1 admits one assignment of all labels satisfying
every paired coefficient equation simultaneously. The width and start slot below are
those of the paper. The start slot numbered one there is zero in Lean.


### `parseSlots_le`

 The width from Section 8.1 accommodates all variables, gates and the designated output. 

### `exists_pathCount_parseGrammar`

 A small circuit for the universal polynomial gives an assignment in its own
coefficient ring whose output entries are exactly the machine path counts. 

### `pathCount_labelEquations`

 Equation (8.1): one assignment to the universal integer parameter polynomials
works for all queried words. The assignment is obtained from the actual circuit. 
