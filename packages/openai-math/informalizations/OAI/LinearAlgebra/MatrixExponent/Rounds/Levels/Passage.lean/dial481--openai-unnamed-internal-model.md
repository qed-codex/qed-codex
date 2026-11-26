---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rounds/Levels/Passage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Levels/Passage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Levels/Passage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A short record at each station in an initial board 

 # Seating product stations by their local span ordinals 

 # A directed presentation of the replicated board 


# Initial layer

Normalize the input diagram and use a common local device for
equal tables. Isolated station values move into one scalar before
the rounds begin. This also covers an empty exterior or zero scalar.


### `start`

 The initial layer represents independent copies of the whole input
tensor. Host and dictionary addresses have independent length bounds. 


# Cost of installing the initial stack

Long identifiers are counted per host. The shorter table labels are
counted per host and block. The exposed bit cost scales with the full
tensor power.


 # Sizes of the initial stack addresses 


# The invariant at the boundaries of complete rounds

Consuming group bits can increase the number of addresses. We bound
the product of the number of addresses and the number of blocks.
The full record length can grow by a constant factor per round.


 # Passing through the one-group concentration before the contractions 

### `Passage`

 The excess over the consumed block coordinates is constant. 

 # Instantiating the initial stack at the chosen levels 

 # The initialization budget of the realized stack 
