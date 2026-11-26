---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectral/Rank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Rank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Rank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adding trivial sites and closing them with local covectors


### `pad`

 The new sites have one trivial coordinate. 

### `scalar`

 Scalar from closing the extra sites, evaluated separately on each term. 

### `close`

 Closing a term multiplies one of its remaining factors by the scalar. 

### `restricts_pad_iff`

 A restriction to a padded tensor uses one covector per extra site. 


# Adjoining unit legs

Padding preserves zero, one and products up to mutual restriction.
For sums, one can erase the summand label at every new site.



# Arrays and diagonal tensors


### `diag`

 One copy of the scalar unit for each possible value of a common label. 


# A diagonal restriction cannot increase the number of labels

Assign one label to a single site and a second label to all remaining
sites. This slice of the target diagonal is the identity matrix. The
restriction factors the slice through the source label space.



# Closing sums and products

On a direct sum the covector is restricted to each summand. In a
product with a padded tensor only the other tensor is contracted.



# Natural units and rank bounds

A decomposition with `n` terms is a restriction from the `n`-fold diagonal.
Reflection of the natural order requires at least two sites.


### `le_dimension`

 The coordinate expansion bounds rank by the product of the leg dimensions. 


# Orders after adjoining trivial tensor legs

