---
{
  "module": "OAI/Computability/VPVNP/PairSimulationVertexJobs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationVertexJobs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationVertexJobs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local choices and exponent increments in DFS visit order

For a fixed final vertex and a choice in its expansion, each descriptor
visit consumes the old half-wire choices and the local kernel choices
once. Its children then use those very half-wires. Splitting the binary
stream this way aligns the row addresses with native depth-first traversal
and the local parameter increments with the final vertex's monomial.


### `VertexJob`

 One depth-first descriptor visit, carrying its row address, the local witness tape it
consumes, and its contribution to each parameter exponent. 

### `VertexJob.address`

 Address of the descriptor row visited by this job. 

### `VertexJob.bits`

 The segment of the vertex choice stream consumed at this descriptor visit. 

### `VertexJob.increment`

 The contribution of this visit's local witness to the exponent of each parameter label. 

### `JobsFor`

 Per-site jobs indexed by the incoming half-wires and the selected
local monomial occurrence. 

### `TermParsers.nodeBits`

 The old halves of every child and the local kernel assignment in the
same order in which the push reader consumes them. 

### `leafJobs`

 Each input vertex makes one visit. Its job carries precisely the
factor witness supplied by that input parser. 

### `pushJobs`

 Build the pushed site's jobs by emitting its own descriptor visit first, then the chosen
child jobs in the term parser's child order. 

### `JobsSpec`

 Agreement of a site's jobs with its tree and parser. The addresses follow preorder, the
concatenated tapes encode the witness, and the increments sum to its exponents. 

### `chainJobs`

 Follow the selected terms, retaining the local split into descriptor
visits at every stage. 

### `vertexJobs`

 Jobs for each final site of a selected term chain, obtained by starting with one visit per
input leaf and applying the successive term parsers. 

### `cursor_leafJobs`

 The selected cursor leaves consume their validator strings and add zero
to every parameter count. 

### `selectedCursor_jobs`

 The visit lists for the original machine specialize all three
identities to the compressor's actual records and branch choice. 

### `RealizesJob`

 The observable obligations for the native path of a single visit.
The extracted histogram may depend on the private scratch layout. 

### `execute_vertexJobs`

 Link a native path at each listed job to one complete final-site
expansion. The resulting burst reads exactly that witness's binary code
and increments each histogram component by that witness's exponent. 
