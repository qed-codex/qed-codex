---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private bit-stack storage of the virtual validator

Each finite port has a disjoint private interval. Its empty pointer is
the interval base and its top pointer is the exclusive end of the occupied
cells. The top-first bit list occupies those cells in reverse order.


### `Layout`

 Private memory layout for named bit stacks, with a base for each stack and a common
capacity whose disjoint intervals and exclusive ends fit the machine address space. 

### `Layout.base`

 Natural address of the first private bit cell reserved for each named stack. 

### `Layout.capacity`

 Number of private bit cells reserved for each stack. 

### `Layout.address`

 Machine-word address of the cell at offset `i` from the base of stack `a`. 

### `Layout.Contents`

 Cell at offset equal to the length of the suffix after this bit. 

### `Represents`

 The RAM configuration realizes the logical stack bank by holding zero and one, the base and
exclusive top pointers, and the occupied cells in bottom-to-top order. 
