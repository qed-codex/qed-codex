---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshArgumentAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshArgumentAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshArgumentAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiled addresses of a node's independent slot arguments

An argument buffer stores all outgoing fields followed by all incoming
fields. At an incoming port, the inverse incidence record identifies the
outgoing arc whose width must be counted. Static and runtime slot numbers
use the same ordering and the same width columns.


### `Input`

 Dynamic bases, node and site operands of the address calculation. 

### `Input.arenaBase`

 Expression for the first address of the private node argument arena. 

### `Input.stride`

 Expression for the number of words reserved for each node's argument frame. 

### `Input.node`

 Expression for the node index selecting an argument frame. 

### `Input.siteOrd`

 Expression for the physical site ordinal used to index the incidence columns. 

### `Input.actualIn`

 Expression for the base of the inverse actual-incidence column. 

### `Input.width`

 Expression for the base of the widths indexed by outgoing actual slots. 

### `Input.nodeBase`

 Compute a node's frame address from the arena base, node index, and frame stride. 

### `Input.port`

 Pack the runtime site ordinal and a fixed local slot number into an actual-slot index. 

### `Input.half`

 Load one slot's width, looking up its outgoing mate first when the slot is incoming. 

### `before`

 When the dynamic slot is `j`, the factor is one for `i < j` and zero
otherwise. The first division detects whether `j` reaches `i + 1`. 

### `sum`

 Sum a list of word-valued address expressions, using zero for the empty list. 

### `outgoing`

 Skip the outgoing fields when addressing the incoming half of a frame by summing all
outgoing widths. 

### `field`

 Dynamic slot address. The loop bound is the fixed graph degree. 

### `fieldStatic`

 Static-slot version, reading just the preceding fields on the selected side. 

### `siteOrdinal`

 Number a site by its base vertex and binary lane, with the lane as the low-order field. 

### `Represents`

 The published values and the node's own runtime ordinals. 

### `halfLoads`

 Reads needed for one slot width, counting any computed pointer operands. 

### `field_reads`

 Actual reads in the compiled dynamic expression, independent of machine
width, network size and field widths. Dynamic pointer loads are counted on
every occurrence. 

### `fieldStatic_reads`

 Compiling a static address reads only its preceding slots, with a single
additional inverse lookup for each incoming width. 
