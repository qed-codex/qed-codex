---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRowInterpolation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowInterpolation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRowInterpolation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit mismatch interpolation for the multi-color layout

Section 3.3 of `subexponential-sat.txt`. All inverse data are supplied as
units. The polynomials are finite sums and products, not chosen witnesses.
Their scalar evaluation functions are executable from the supplied ring
operations and units; the semantic polynomial definitions use mathlib's
noncomputable polynomial representation.


### `NodeUnits`

 Actual invertible elements for every denominator used in interpolation. 

### `nodeInverse`

 The supplied inverse of a nonzero interpolation node. 

### `differenceInverse`

 The diagonal branch is unused by products over `erase i`. 

### `NodeUnits.ofField`

 Construct the unit data directly from field inversion and its laws. 

### `basisDivisor`

 A normalized linear factor vanishing at node `j` and equal to one at `i`. 

### `basis`

 The source's `T / λ_i` times the Lagrange product. 

### `correctionPolynomial`

 Explicit correction polynomial, including the empty-constraint case. 

### `correctionEval`

 Direct finite evaluation of the source's displayed interpolation formula. 

### `columnCorrection`

 One correction for each selected column, and the zero polynomial elsewhere. 

### `columnEval`

 Scalar execution of the column correction formula. 

### `rowPath`

 The initial selector is retained even when its own column gets a correction. 

### `mismatchPositions`

 A column needs a prescribed value exactly when its head differs from the factor color. 

### `correctionColumns`

 The actual `Y` in Section 3.3, defined by a mismatch-count bound. 

### `mismatchCorrection`

 Simultaneous correction values: one polynomial is reused for every other color. 

### `mismatchCorrection_eval_other_color`

 Each other-color side uses the same polynomial and its unique prescription at `t`. 

### `mismatchRowPath`

 The actual polynomial row formed from all mismatch corrections. 

### `mismatchRowEval`

 Execute an evaluation of a row from ring operations and the supplied units. 

 ## Executable finite expression codes

The following constructors produce polynomial expression data using only
finite `List.ofFn` traversals. Their denotations are the proved polynomials
above. This supplies a concrete path representation in addition to the
executable scalar evaluator.


### `PolynomialCode`

 Finite arithmetic expression data for a univariate polynomial. 

### `denote`

 Mathematical meaning of the finite expression. 

### `eval`

 Direct execution using the supplied coefficient ring operations. 

### `basisCode`

 Executable expression for a Lagrange basis with zero constant term. 

### `correctionCode`

 Executable constructor for the actual correction polynomial. 

### `mismatchRowCode`

 A fully finite, executable expression constructor for the multi-color row. 
