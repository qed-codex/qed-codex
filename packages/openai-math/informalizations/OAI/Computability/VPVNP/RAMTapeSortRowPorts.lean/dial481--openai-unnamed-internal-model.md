---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fetching comparison operands at one physical sorting row

The row traversal retains its unary row offset. A local stride additionally
fetches its XOR partner from the same materialized block. At a cross-site
stride the two remote fields are instead consumed as record streams.


### `Port`

 Stacks for a sorting row, including the current and next blocks, remote streams, row
offsets, comparator orientation, and validity flags. 

### `Operand`

 Which locally fetched record to stage, the current row's record or its partner's. 

### `Operand.index`

 Select the unary row offset or partner offset used to fetch this operand. 

### `Operand.destination`

 Select the left or right staging stack for the fetched operand. 

### `fetchPorts`

 Connect the block reader to the current block, scratch stacks, and this operand's
destination. 

### `fetch`

 Fetch the indexed record from the current block while preserving the operand's offset. 

### `FetchReady`

 Scratch and the word-width register required by a materialized array lookup. 

### `clearPartner`

 The computed partner offset is private to one row. Discard it when
returning control to the outer traversal. 
