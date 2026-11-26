---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Multi/Radial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Multi/Radial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Multi/Radial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing independent cubes into a degree simplex

Index the cubes by nonnegative translation vectors with sum at most
`q`. Summing the one-variable grading over the coordinates keeps
only terms whose input and output translation vectors all agree.



# Packing ordered simplices into a cube

Cumulative degrees with strictly increasing offsets give one copy for
each coordinate ordering. The variation grading removes mixed orders.


### `simplex_le`

 Each of the `m!` orderings contributes a disjoint simplex at grade zero. 

 # Independent groups of polynomial variables 


# Degree energy and its upper bound at small costs

Use total-degree budgets in `m` variables. A common slack variable
homogenizes each input and the output without changing the tensor.
The ordering degeneration gives the upper bound directly, uniformly
in the number of variables.



# The continuum limit of degree energy

Fix a cube shape in the univariate supremum, then pack translated
copies inside a multivariate simplex. The strict slack in each
width pays for rounding the number of translates.


 # Degree and width energy at a fixed finite placement 


# Increasing returns from substitution in two groups of variables

Tensor the two test products up to the same number of variables. The
sector expansion loses only a logarithmic cost, which disappears under
further joint powering.


### `Sectors`

 Log-price comparison with a polynomial number of degree sectors. 

 # The cost of a polynomial number of bidegree sectors 


# Radial comparison of degree-energy differences

In the mixed placement one test uses only inner inputs and one uses
only outer inputs. Increasing returns compares these two tests to an
unrestricted test and a shifted inner test. The former contracts onto
the outer sites. The latter discards zero-degree inputs.


 # Radial contraction of width energy at finite placements 
