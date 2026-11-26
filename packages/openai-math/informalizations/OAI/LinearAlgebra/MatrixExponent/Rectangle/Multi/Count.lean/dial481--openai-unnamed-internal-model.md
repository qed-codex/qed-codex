---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Multi/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Multi/Count.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Multi/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The volume correction per variable 

 The sum of all positive pair differences is subadditive.
For vectors with distinct entries equality forces a common ordering. 

 Multivariate polynomial multiplication with total-degree budgets. 


# Homogeneous coordinates on a simplex

A slack variable gives each monomial a prescribed total degree.
A pair of multiplications has one term for each pair of input tuples.


 # Number of available cube translations in a degree simplex 


# Bihomogeneous substitution

Expand `X^u (X+Y)^v` in powers of `X+Y` and `Y`. Its component of
highest Y-degree is `X^u Y^v`. Terms already containing too many Y's
cannot contribute to the chosen component.


### `mix`

 The monomial `X^u Y^v (X+Y)^w` in a formal polynomial ring. 

### `expand_mix`

 The new right degree can be at most the old left degree. 


# Redistributing degree budgets

At each input expand in the variables `X+Y,Y`. At the output extract
the coefficient with the original Y-degree. Sectors above that degree
vanish. Each remaining sector is a pair of ordinary multiplications.


### `sector`

 The number of bidegree sectors is polynomial in the total degree. 

 # Natural-log simplex prices at finite placements 


# Merging polynomial inputs at each site

Inputs grouped at a site multiply locally. Those reaching the output
site multiply into the answer there. The local coefficient maps use
total degrees, so the new budgets are the sums at the input sites.


 # Zero-degree inputs are dummy sites 


# Moving inputs toward the output

Convexity rounds each intermediate placement to one endpoint of its
segment without decreasing the price minus the assigned costs. Merging
inputs then gives a degree budget on the original set of sites.


### `contract`

 Every budget for the mixed placement is dominated, after costs, by
some budget at the outer placement. 
