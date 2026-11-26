---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPairReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPairReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPairReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical input and output exponent words of a nominated pair

The first-half count uses the counter arrays on the two adjacent cuts of
the live chain. In the first group the preceding array is all zero. The
header's output memory supplies both arrays to the native exponent checker,
also after the auxiliary computation has modified its own scratch.


### `Output.pairExponentWords`

 All outgoing counters and the immediately preceding incoming counters
from the mathematical contraction are present in the real scratch banks. 

### `Output.pairBufferValues`

 Exactly the buffer hypothesis consumed by the native first-half
exponent-stage count. The two public operands address the decoded banks. 

### `Output.pairBufferValues_after`

 The nomination and pair phases may change scratch outside the two
read-only banks. The same native checker then sees the original counters. 

### `Output.pairExteriorWords`

 The two exterior fields are the actual physical sources of the
auxiliary RAM at the adjacent primed even cuts. Empty fields at either
primed endpoint have no read addresses. 
