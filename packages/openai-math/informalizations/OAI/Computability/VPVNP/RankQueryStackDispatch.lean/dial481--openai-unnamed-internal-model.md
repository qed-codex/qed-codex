---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed arithmetic code for Schur node dispatch

The same decision trees serve every matrix size and every bidegree. Input
registers zero through five hold the query, register six is the product-loop
counter, and register seven is the matrix height. The child routine selects a
side and returns the six registers of that child. The description routine
returns a scalar, a scalar-entry request, or the arity of the product sum.


### `Arith`

 Natural-number arithmetic operations available in Schur dispatch expressions. 

### `Arith.eval`

 Interpret a dispatch arithmetic operation using natural addition, subtraction,
multiplication, division or remainder. 

### `Expr`

 Arithmetic expression over literals and the eight immutable dispatch inputs. 

### `Expr.eval`

 Evaluate a dispatch expression in the supplied bank of eight natural numbers. 

### `Code`

 Decision tree that tests expression equality and emits six expressions at the selected
leaf. 

### `Code.eval`

 Follow equality tests on the input words and evaluate the six fields of the reached leaf. 

### `absolute`

 Absolute row of an index in the trailing matrix. 

### `child`

 Dispatch on the Schur key tag to construct the selected left or right child query. 

### `describe`

 Dispatch on the Schur key tag to describe its product scan or its scalar result. 

### `inputs`

 Assemble the six encoded query words, child index and matrix dimension into the dispatch
input bank. 

### `decode`

 Interpret an emitted descriptor using only a query for a scalar entry. 

### `simplifyDispatch`

 Evaluate the rank-query dispatcher and its selected child description
using the branch and cursor equations in the local context. 

### `child_eq`

 At a valid product-loop index the fixed code supplies precisely the
query saved by the typed stack interpreter. 
