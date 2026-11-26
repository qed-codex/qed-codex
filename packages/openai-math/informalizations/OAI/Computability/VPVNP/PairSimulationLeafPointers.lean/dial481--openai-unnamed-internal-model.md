---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafPointers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPointers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafPointers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Allocating the auxiliary validator's private stack ports

The loop is unrolled only over the fixed set of machine ports. Each port
receives two equal pointers at its empty interval. Existing cells may hold
arbitrary values. The capacity and first address come from the enclosing
call's registers, so the instruction table is independent of the input length.


### `Reg`

 The validator's stack registers together with the allocation cursor and per-stack address
stride. 

### `stack`

 Physical embedding of the stack registers inside the pointer allocator's register bank. 

### `finish`

 The final two rows initialize the permanent zero and unit operands. 

### `allocate`

 Three instructions set a port's base and top to the current cursor, then advance the cursor
by one stack stride. 

### `next`

 Continue at the first allocation instruction of the next port, or at the end label once the
list is empty. 

### `Rows`

 The host code allocates each port in the given order and links the last allocation to the
specified end label. 

### `initialize_pointers`

 From the caller's base address and stride, install the actual pointer registers
and represent an empty bank even when this is a later leaf reusing the same region. 
