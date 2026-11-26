---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortLayerRowsPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRowsPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRowsPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stack assignments inside a sorting layer

The address routine reads the binary index, and the record lookup reads
its unary copy. The partner count and two decision bits go directly from
the address routine to the record routine. Both routines preserve the
site identifier and the stage counters throughout the traversal.


### `Extra`

 Site address, stage counters, observed wire bits and scratch stacks used when computing the
comparator's partner and orientation. 

### `Data`

 Combine the record-operation ports with the additional ports for computing a row's address
and partner. 

### `Port`

 The layer's data stacks together with the row iterator's binary and unary counters. 

### `rowPorts`

 Connect the record routine's row offset to the iterator's unary counter and its other
operands to the layer data. 

### `addressPorts`

 Route the address computation to the iterator's binary row index, preserved site and stage
parameters, and its decision and scratch stacks. 

### `bank`

 The site and stage data shared by consecutive visits. Only the accumulated
output, the two exchange streams, and the list of flags change during a layer. 

### `keepMin`

 This wire keeps the smaller record precisely when the stride bit and phase bit of its
global wire index agree. 

### `peerIndex`

 For an in-site stride, toggle its bit in the row index to find the partner. A cross-site
comparator uses the same row at the peer site. 

### `prepared`

 The prepared row has its three address outputs installed in the record
routine's input ports, with every other port equal to the callback's entry. 

### `address_run`

 Running the installed address machine leaves all pending tape streams
available to the record operation on that row. 
