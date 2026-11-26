---
{
  "module": "OAI/Computability/VPVNP/RankPrefixTemplate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPrefixTemplate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPrefixTemplate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Supplying a variable row prefix to the determinant interpreter

The outer rank cursor and the Schur interpreter read the same dimension
from three places. All other startup stacks come from one reusable
matrix, field and reader template.


### `PrefixPort`

 Ports for a row-prefix rank scan whose Schur engine obtains Gram entries from the
underlying matrix reader. 

### `prefixDynamic`

 Select the three ports that receive the variable row-prefix length, namely the row-count
stack, cursor input one, and Gram-engine register seven. 

### `prefixRawBank`

 Initial stacks for the rank of an n-row prefix with m columns, with the loop flag set, the
Gram engine idle, and the product-depth stack empty. 

### `prefixRawBank_eq`

 Substitution of the physical prefix-length word into the template gives
the complete initial bank, including the empty balanced-depth stack. 
