---
{
  "module": "OAI/Computability/VPVNP/PairNativeOperandVector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandVector.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeOperandVector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native evaluation of a fixed vector from the eleven pair-stage operands

Register twelve retains the caller's private cache base. Results start at
register thirteen, in vector order. The final two instructions set the cache
write pointer and unit register for the consecutive private stores.


### `need`

 Number of extra temporary slots above an operand's result slot. A geometry expression uses
its compiler's space bound and a prefix field uses zero. 

### `fieldCost`

 Tick allowance for one vector entry, using the expression cost for a geometry operand and
one copy for either prefix operand. 

### `field`

 Produce one vector field in temporary slot `base` by compiling a geometry expression or
copying the selected prefix word or length. 

### `FieldFits`

 For a geometry operand, all bounds required by the public-expression evaluator hold at
modulus `2^g.w`. The two prefix operands are already word-valued. 

### `capacity`

 Largest temporary index reserved for the vector, allowing one result slot per entry and
enough extra slots for its most demanding expression. 

### `src`

 Register `13+i` holds vector entry `i` for the subsequent private cache store. 

### `saved`

 Temporary slot zero, register 12, holds the caller's cache base throughout geometry and
field evaluation. 

### `cursor`

 Fixed register 10 carries the write pointer for the sequence of private cache stores. 

### `unit`

 Fixed register 11 holds the unit increment used to advance from one cache entry to the
next. 

### `vector`

 Load the geometry, compute the vector fields in index order, and initialize the cache write
pointer and its unit increment. 

### `work`

 Tick bound for evaluating the entire operand vector, combining geometry setup with a
uniform per-entry bound and three bookkeeping instructions. 

### `Result`

 Postcondition for native vector evaluation. Each source register holds its encoded operand,
the cursor holds the supplied base and the increment register holds one. 
