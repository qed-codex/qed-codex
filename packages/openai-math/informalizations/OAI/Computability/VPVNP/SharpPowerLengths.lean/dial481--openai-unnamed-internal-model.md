---
{
  "module": "OAI/Computability/VPVNP/SharpPowerLengths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SharpPowerLengths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SharpPowerLengths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Selecting a tensor power with polynomial overhead in its length

For a projection requiring `A (h+1)^D B^h` input bits, choose the largest power
which fits at an available small-circuit length. The next power's requirement is
an upper bound on that length. Its polynomial factor stays separate from `B^h`.


### `exists_last_fitting_index`

 At a length admitting the requested starting index, select a maximal fitting
index and compare with its successor. 

### `arbitrarily_large_powers_of_sharp_projections`

 Unboundedly many small circuits for `P` give arbitrarily high powers with the
same exponential rate in their circuit-size bound. 
