---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateNativeReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateNativeReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateNativeReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Returning a Cramer quotient to the native evaluator

Both determinant programs and the quotient arithmetic run inside a finite
workspace. After the quotient has been copied into the evaluator's scalar
operand, one pass clears every workspace stack, including the two determinant
results and any registers left by the coefficient readers.


### `Bus`

 The scalar reader's public ports with separate auxiliary banks for advice and writable
workspace. 

### `Workspace`

 The denominator, numerator, and quotient working banks of the paired Schur query. 

### `port`

 Embed one stack of the Schur-pair workspace in the writable portion of the scalar-reader
bus. 

### `quotient`

 The multiplication accumulator containing the final numerator divided by the denominator. 

### `state`

 Combine the label, live basis ordinals, scalar result, immutable advice, and writable
workspace into one reader state. 

### `finish`

 Copy the completed quotient to the public scalar result and reclaim the reader's working
stacks. 

### `returnClock`

 Bound the final result copy and cleanup scan using the workspace's port count and peak
stack height. 

### `core`

 Prepare the live arguments, evaluate the Schur pair on its mounted workspace, then return
the quotient and clean up. 

### `core_bounded`

 Execute a prepared physical determinant pair and return with precisely
the same label, basis indices and persistent advice. 
