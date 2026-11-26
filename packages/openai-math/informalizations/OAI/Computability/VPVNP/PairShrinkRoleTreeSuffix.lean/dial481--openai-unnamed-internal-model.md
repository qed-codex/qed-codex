---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleTreeSuffix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleTreeSuffix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleTreeSuffix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparing a shrinking visit with its typed kernel reader

At a vertex the first guesses describe the placed old half-wires, and the
next guesses describe the hidden assignments. The native scratch after both
writes supplies the resident map checks. Matching those deterministic checks
to the chosen kernel gives equality of the suffix on every input tape.


### `hiddenInputScratch`

 The private cells used by the hidden scan, after storing the old
arguments and running the hidden-stage setup. 

### `treeSuffix_of_maps`

 The child and hidden decoders give their exact typed prefixes. Only the
deterministic test on the resulting resident fields depends on the kernel. 
