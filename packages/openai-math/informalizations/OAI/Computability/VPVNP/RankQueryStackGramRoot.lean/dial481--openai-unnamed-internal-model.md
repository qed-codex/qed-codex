---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackGramRoot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramRoot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackGramRoot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# End-to-end determinant coefficient query on a streamed relation matrix

The independent height bound of the matrix-entry reader is reused through
every recursive call. The entry reader's running time only enters the clock.
The answer is the bivariate coefficient of the reverse characteristic
polynomial of the weighted Gram matrix over the native extension-field ring.


### `descriptorSpace`

 Stack-height bound while decoding a Schur query, including its suspended frames and the
Gram entry reader. 

### `queryTime`

 Bit-stack step bound for a Schur coefficient query, using the recursion depth, branching
bound, and entry-reader clock `B`. 

### `querySpace`

 Maximum stack height during a Gram coefficient query, including its recursive frames and
the entry reader's workspace. 

### `root_query`

 The physical root subroutine performs its own Schur recursion and scalar
arithmetic. Its caller supplies a bounded entry routine for the original
matrix. The query's two coefficient indices may vary between calls. 
