---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/MovingForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/MovingForms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/MovingForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A center for prescribed widths

Minimize a smoothed transport cost over ordinary one-site extensions.
Pointwise compactness gives a minimizer. The tangent inequality for
square root makes the same extension minimize a weighted variance.


### `choose_weights`

 A common positive compact range of weights works for every
ordinary spectral point. 


# Weighted quadratic budgets

A transport bound implies coercivity, hence a maximizing nonzero form at
every positive scale. The normalized deficit dominates the sum of squared
distances of the rescaled widths from their targets.



# Distance tests from a synchronized extension and wire recovery

Use the same extended price for all site probes. A cubic energy cutoff
absorbs the bounded quadratic optimizer budgets. The logarithm of the
polynomial overhead in the recovered wire is then logarithmic in the
optimizer scale.


### `WeightedExtension`

 A price extension with a separate energy penalty at each site. 


# Uniform distance tests for weighted budgets

Penalties are squared rescaling factors. The new site pays the largest
allowed penalty. Since its probe energy is at most the optimizer scale,
this adds only a bounded term to the logarithmic error.



# Uniform prescribed widths

A smoothed minimizing extension sets the weights of the quadratic
optimization. Its strict slack absorbs the uniform error in the
optimizing widths. The price and width bounds use natural logarithms.


### `profile`

 Uniformity in both the price and a compact range of penalties. 

### `prescribed_widths`

 At all sufficiently large scales, every spectral point admits a
sphere within the prescribed caps whose log price approaches the
transport cost of the caps at a single extended site. 

 Simultaneous price bounds for one moving sphere insertion. 
