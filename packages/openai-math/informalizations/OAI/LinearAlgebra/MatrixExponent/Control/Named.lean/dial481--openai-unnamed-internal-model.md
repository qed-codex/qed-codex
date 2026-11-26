---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Control/Named.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Control/Named.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Control/Named.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking agreement on repeated addresses

Sort by address and then by bit. Complement the bit on every row and
test whether the list is still sorted. This holds exactly when all
rows with the same address agree.



# Simultaneous reads from an array of bits

Pair each data bit with its fixed address and each proposed output bit
with its requested address. Consistency on the combined list uniquely
determines every output, even when the same address is requested often.


 # Reading an array in any exterior bit layout 
