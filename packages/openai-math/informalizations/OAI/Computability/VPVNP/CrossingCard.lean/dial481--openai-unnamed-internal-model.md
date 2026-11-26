---
{
  "module": "OAI/Computability/VPVNP/CrossingCard.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CrossingCard.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CrossingCard.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dimensions of the two wires in the shifted crossing

The operator indices in Appendix B range over nonvacuum occupation states.
The sigma type used for the integral pairing separates these states by their
positive particle number. Counting that type removes exactly the vacuum.


### `crossingState_card`

 The positive particle-number sectors together index exactly the cutoff count
minus the unique empty occupation state. This includes the zero-energy cutoff. 

### `modeCutoff_card_le`

 Upper bound for the number of finite-mode matrix indices below an integer cutoff. 

### `modeCutoff_card_eq`

 A finite-mode matrix with at least `E` modes realizes every state at energy at most `E`. 
