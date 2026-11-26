---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteSizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteSizes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteSizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the word width and sorting block length after parsing

The validator retains the public address count `d` and bucket size `H`. The
following fixed pass gives the successor reader its word width and the sorter
its block length. The input and the two output counts occupy distinct stacks.


### `siteSizeProgram`

 Write the word width and the number of five-word sorting slots. 

### `siteSizes`

 Prepared site-size tallies with word width `(d + 10)^4` and sorting block length `4*H`. 
