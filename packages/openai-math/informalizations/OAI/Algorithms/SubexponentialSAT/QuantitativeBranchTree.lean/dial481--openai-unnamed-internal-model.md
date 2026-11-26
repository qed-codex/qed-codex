---
{
  "module": "OAI/Algorithms/SubexponentialSAT/QuantitativeBranchTree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/QuantitativeBranchTree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/QuantitativeBranchTree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quantitative binary-tree counting with a variable exponential budget

Appendix A.2 of the subexponential manuscript. All constants remain visible:
M, C, and the exponential budget σ may vary between inputs. The finite encoding
and real-cutoff binomial estimate are imported from the frozen BranchTree module.


### `card_paths_le_exponential`

 A variable exponential budget, with the complete finite prefactor exposed.
The budget itself suffices; positivity of σ need not be a separate premise. 

### `natural_log_budget_of_logb`

 Conversion of the manuscript's base-two logarithmic budget. 

### `nodeCount_le_exponential`

 Node-count form for an actual inductive finite tree. 

### `nodeCount_le_quadratic`

 Explicit quadratic dependence on input size, retaining the C and k factors. 

### `nodeCount_le_coefficient`

 This version accepts an explicit bound on the coefficient, enabling later
substitution of polynomial bounds in M or in the inverse budget. 

### `decomposition_nodeCount_le`

 The actual sunflower decomposition has the required path budgets. Only
its externally chosen quantitative parameter inequalities are inputs here. 

### `treeFor_nodeCount_le`

 The bound applies to the actual deterministic tree for every input formula.
There are no path-budget or antichain assumptions on the caller. 

### `coefficient_le_polynomial`

 Explicit polynomial control of the node-count coefficient from C ≤ a*M^b. 

### `exists_coefficient_polynomial`

 The polynomial's coefficient and degree depend only on k; M remains quantified. 

### `coefficient_le_of_parameter_bound`

 Substituting a parameter bound M ≤ A*X^d does not conceal any dependence on X. 

### `nodeCount_le_parameter_bound`

 A complete node estimate exposing both the parameter polynomial and the
variable exponential rate. X can later be instantiated as 1/σ+2. 

### `treeFor_nodeCount_le_parameter_bound`

 The parameter-polynomial estimate for the tree computed from a formula. 

### `exists_treeFor_node_polynomial_M`

 The coefficient and degree are fixed before M, σ, n, and F vary. 

### `treeFor_leaves_length_le`

 The explicitly returned family is no larger than the tree that computes it. 

### `selected_nodeCount_le`

 The reciprocal-budget selector discharges all numerical budget assumptions
for the actual formula-dependent tree. 

### `exists_selected_node_polynomial`

 A single polynomial works for every inverse budget s and every input.
The existential constants are quantified before s, n, and F. 

### `exists_selected_leaves_polynomial`

 The explicit returned family obeys the same uniformly quantified polynomial. 

### `exists_rational_selected_node_polynomial`

 Rational budget lift. The coefficient A and degree d depend only on k, and
are fixed before numerator a, denominator b, input size n, and formula F vary. 

### `exists_rational_selected_leaves_polynomial`

 The actual output family has the same rational-budget size bound. 

### `exists_sigma_selected_node_polynomial`

 Direct rational-budget statement of the node bound in Lemma 2.1.
All selected parameters are concrete and the polynomial is uniform in σ and n. 

### `exists_sigma_selected_leaves_polynomial`

 Direct rational-budget bound for the explicit returned leaf list. 
