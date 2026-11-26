---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshMapOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Operand slices of the degree-refresh map

The two old half-wires are stored independently at the child node. The
two external payloads and the internal expander halves belong to its parent
node. Both ends of an external segment use the prefix offset in the original
outgoing bundle, even when port translation permutes the incoming slots.


### `NodeFields`

 The independent slot vectors in the private argument buffer of a node. 

### `oldSite`

 The original site whose lanes are promoted to this port. 

### `oldHalf`

 Pulls the incoming half-wire assignment back to the port-split coordinates of the selected
site. 

### `newState`

 The graph whose independent new halves the selected kernel receives. Taking
the selected block supply widths gives exactly the dyadic refresh output state. 

### `newIso`

 Identifies the promoted network with its refreshed wire coordinates, including the binary
encoding of each internal payload. 

### `newHalf`

 Pulls the output half-wire assignment at a promoted site back along the promotion
isomorphism. 

### `externalOut`

 The outgoing external bundle of the promoted site's half-wire assignment. 

### `externalIn`

 The incoming external bundle indexed by the inverse bundle target at the promoted site. 

### `segments`

 Splits the incoming and outgoing external bundles into the incident old-port segments of
this site. 

### `supplyArg`

 Extracts the selected port's expander supply half from the refreshed half-wire assignment. 

### `demandArg`

 Builds the selected port's demand input from the incoming half-wire assignment and the
external segments of the refreshed assignment. 

### `externalOffset`

 The offset of port j's segment in the site's incoming or outgoing external bundle,
according to the direction bit. 

### `operandBase`

 Every endpoint has its own physical operand pointer. The old half of a
tie uses its destination slot. The new external half uses its source port as
the segment index. Incoming expander halves use the reverse edge's port. 

### `entryInput`

 The exact input of the single motif map at the refreshed port, from the
independent old and new node halves. 

### `buffers`

 The resident row buffer of the selected refresh invocation. Its supply
ranges stop at the payload ends while the full words (including their tag
suffixes) are separately available at the same bases. 

### `operandData`

 Each present demand and supply bit in the actual interpreter is recovered
from its physical node address. A nonincident endpoint has no readable bit. 

### `supplyPortBase`

 Full supply fields include selector bits above the payload. The pointers
used by the agreement scan refer to the same two physical halves used by
the map row, including different slot ordinals at opposite endpoints. 
