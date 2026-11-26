---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SparsificationBudgetProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationBudgetProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SparsificationBudgetProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A directly computed dyadic sparsification budget

For each fixed width k, a fixed control constant T suffices.  The selected
parameter is a power of two whose binary length is an affine function of the
binary length of the inverse budget.  This is the explicit witness from
SparsificationBudget.dyadic_witness, rather than the least passing candidate.

The control constant is chosen before the input word.  Program definitions
below manipulate bits only; their specifications use the corresponding
natural-number values.


### `Control`

 A fixed control constant, with the polynomial bound used to certify it. 

### `outputWord`

 The exact binary word produced by the finite program. 

### `outputWord_from_trim`

 High zero padding in the input does not affect the selected parameter. 

 ## The actual fixed finite program 

### `program`

 The first stage strips high zero padding and the leading one.  The second
stage writes the fixed T+2 zeroes and two zeroes per remaining input cell. 

### `primitive_linear`

 The multiplicative constant depends on the fixed control table, before
the unbounded input word is chosen. 

### `canonical_primitive_linear`

 On canonical binary input, the actual primitive cost is in particular
polynomial in the numerical inverse budget. 

### `exists_linear_primitive_selector`

 The program works for zero and padded inputs as well.  Zero is normalized
to the harmless reciprocal budget one in the specification only. 

 ## The input-size to inverse-budget to M pipeline 

### `fromSizeProgram`

 The growing inverse budget s(n) is also computed by a fixed bit program. 
