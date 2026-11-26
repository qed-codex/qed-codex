---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackPower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackPower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackPower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing power-entry queries on a scalar stack

Each product in a nontrivial power has one intermediate matrix index and
one degree split. The machine obtains both from its single loop counter by
division and remainder. Exponents and degrees in a saved query are bounded
by their initial limits.


### `Node`

 The two recursive requests at each valid product index of a composite node. 

### `Node.box`

 The matrix-index and degree loops share a single mixed-radix counter. 

### `value`

 Evaluate a leaf as its scalar and a branch as the sum of the products of its paired child
values. 

### `describe`

 Describe a node by returning its scalar if it is a leaf or its number of product terms if
it branches. 

### `children`

 Retrieve the two children of a product term, returning the fallback pair for a leaf or an
out-of-range index. 

### `program`

 Turn a family of query nodes into a stack program with descriptor, left-child, and
right-child operations. 

### `PowerKey`

 The bounded integer registers of one power request. 

### `PowerKey.exponent`

 Exponent of the matrix power, bounded by `H`. 

### `PowerKey.row`

 Row index of the matrix-power entry whose coefficient is requested. 

### `PowerKey.col`

 Column index of the matrix-power entry whose coefficient is requested. 

### `PowerKey.degree`

 Degree of the requested polynomial coefficient, bounded by `Z`. 

### `depth`

 Number of balanced exponent splits needed for this power query, bounded by the ceiling of
its base-two logarithm. 

### `value`

 Requested coefficient of the specified row and column of the matrix power. 

### `split`

 Each child holds the lower or upper half of the exponent. 

### `node`

 Describe a power query using the identity matrix at exponent zero, an entry read at
exponent one, and paired subqueries at larger exponents. 

### `program`

 Stack program for extracting coefficients of bounded matrix powers by balanced exponent
splitting. 

### `run`

 Every intermediate continuation has at most `⌈log₂ h⌉` frames. The run
returns the actual scalar coefficient of the polynomial matrix power. 
