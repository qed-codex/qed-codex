---
{
  "module": "OAI/Computability/VPVNP/ShiftedBlockCuts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedBlockCuts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedBlockCuts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From shifted Fock modes to the two crossing factorizations

The tensor in a fixed source block is its integral vacuum pairing times the
Kronecker delta on the exterior-state indices. Its two summands factor through
energy cutoffs differing by twice the coefficient shift in doubled-energy units.


### `ShiftedBlockCuts`

 An integral four-index tensor written as the sum of two cut factorizations,
with the source block's binomial index included in each coordinate set. 

### `homogeneous_energyMode`

 A matrix entry in its energy-difference diagonal has exactly the specified
change of energy, including for negative shifts. 

### `shiftedBlockCuts_of_modes`

 Apply the two finite cut bounds to an energy-mode residue identity. 

### `fock_block_cuts`

 The integral block tensor from the finite exterior-algebra operators in Appendix B.
All terminal states in the energy cutoff are included. 
