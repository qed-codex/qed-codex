---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpAlgorithm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpAlgorithm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpAlgorithm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable separation into a growing number of groups

Each outer block contains a list of independent inner lists. The program first
sums each inner list, then multiplies the resulting sums. It never enumerates
the Cartesian product of those inner lists. All operation formulas display the
number of colors; no fixed-color constant is hidden in them.


### `Block`

 Explicit data for one choice of the outer coordinates and all cosets. 

### `expression`

 The r-fold product of independent sums in equation (4.6). 

### `expression_size`

 Every group computation is charged, and inner lengths occur only as a sum. 

### `ofFibers`

 Construct a block from an actual Fin r family of inner enumeration lists. 

### `momentExpression_size_le`

 A uniform bound in the number of colors, outer blocks and inner terms.
The group-program bound S is not permitted to hide a dependence on r. 

### `momentExpression_trace`

 An actual arithmetic-machine execution of the complete r-group moment. 

### `executeJet`

 A finite r-group coefficient-list algorithm. The same monomial enumeration,
bounded postfix execution, and post-extraction U summation work for every r. 
