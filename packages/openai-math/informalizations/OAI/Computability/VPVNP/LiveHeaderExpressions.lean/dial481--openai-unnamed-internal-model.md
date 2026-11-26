---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderExpressions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderExpressions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderExpressions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arithmetic expressions for the complete live header operand bank

Only the four inputs of the physical site reader and fixed constants appear
in these expressions. Their values include the nested stage tag address,
all source and destination buffer addresses, and the public scan limits.


### `Lengths`

 The five public size expressions used to allocate and parameterize live-header storage for
any processor geometry. 

### `Lengths.h`

 The public expression for the chain-height parameter used in group and cut numbering. 

### `Lengths.delta`

 The public expression for the basic cut width used in the exterior and padding
  capacities. 

### `Lengths.advice`

 The public expression for the number of distributed advice bits. 

### `Lengths.e`

 The public expression for the serialized exponent field length. 

### `Lengths.config`

 The public expression for the serialized evaluator configuration length. 

### `Lengths.eval`

 Evaluate the five public header dimensions at the supplied geometry. 

### `capacity`

 The maximum scan length allocated to the requested incident field. 

### `width`

 The workspace address holding the computed cut width for one of the five live or primed
slots. 

### `flag`

 The workspace address holding the selected group-phase flag. 

### `firstTail`

 The workspace cell marking the first evaluator group. 

### `mode`

 The workspace cell holding the selected unit, pair, or tail mode. 

### `offset`

 The shared descriptor cell holding the next incident field's source offset. 

### `count`

 The shared descriptor cell holding the next incident field's live length. 

### `borrow`

 The workspace cell carrying the borrow while constructing primed group indices. 

### `index`

 The base address of the unpacked one-based group index. 

### `high`

 The cell after the group-index array storing the position of its highest set bit. 

### `population`

 The cell storing the number of set bits in the group index. 

### `leftIndex`

 The base of the unpacked left primed group index. 

### `rightIndex`

 The base of the unpacked right primed group index, following the left index array. 

### `advice`

 The distributed advice array's base following both primed index arrays. 

### `exterior`

 The base of the selected side's exterior payload, with a full reserved interval per side. 

### `exponent`

 The base of the selected side's exponent buffer following both exterior reservations. 

### `config`

 The base of the selected side's evaluator configuration buffer following the exponent
buffers. 

### `limit`

 The exclusive end of the live-header workspace, immediately after the right configuration
buffer. 

### `dest`

 The destination base for a side's payload field, using zero as the unused operand of a
padding check. 

### `row`

 Assemble the selected header stage's public operand expressions from the size parameters
and workspace layout. 

### `operands`

 Flatten the fixed 31 rows, appending the address of the header-stage tag. 

### `operands_eq`

 The expression bank instantiates precisely the native header's ABI. 
