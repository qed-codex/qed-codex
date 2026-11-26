---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Valued/StarWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Valued/StarWeights.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Valued/StarWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Evaluating tensor prices on coordinate arrays 

### `forget`

 Forgetting integrality makes every permitted restriction an ordinary one. 


# Interpolation at integral nodes

Pairwise unit differences keep the interpolation weights integral.
The linear overhead in degree disappears on taking tensor powers.


### `Family.bound_scalar`

 The price at an integral parameter cannot exceed a uniform bound
on an infinite set of nodes having pairwise unit differences. 


# Extracting base-field coefficients

Linear functionals on the ambient field commute with restrictions over
the base. They give additive evaluations, prior to imposing valuation
cutoffs on the functionals.


 # Changing coefficients and extending base-field tensors 


# Filtered linear measurements

Take a supremum over any subspace of the base-field dual. The
resulting functional remains additive on block sums. Indeed along
a line through two witnesses, power interpolation shows that all
but finitely many parameters nearly achieve both bounds.


 # Linear forms killing entries above a valuation cutoff 


# Interpolation of assisted costs

The one-copy envelope is additive. This permits bounding closures
of powers without asking a single extension to minimize at different
interpolation nodes.


 Interpolation nodes on the arms of a valuation star. 


# Choosing the numbers of interpolation nodes

An inner arm contributes only when its end rate is below the mean.
Its nodes absorb that difference. Their combined multiplicity supplies
the required vanishing order for the outer arm.

