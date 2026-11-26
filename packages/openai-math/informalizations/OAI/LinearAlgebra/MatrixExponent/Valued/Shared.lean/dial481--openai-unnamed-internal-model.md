---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Valued/Shared.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Valued/Shared.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Valued/Shared.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Existence of a valued lift

From a price over an infinite field, construct a price on every
rationally valued field extension trivial on the base. The discount
fixes scalar values, and power interpolation gives integral monotonicity.


 # Simultaneous bounds over the open valuation disk 

### `DiskSync`

 Uniform strict slack in finitely many price bounds suffices. 


# From the open valuation disk to its boundary

At degree k use nodes of valuation at least 1/(k+1), with pairwise
differences of exactly that valuation. One factor t clears every
interpolation denominator. Its cost is independent of the power.


### `Family.bound_disk`

 Any monotone valued character bounded on the open disk is bounded by
the same constant on the closed valuation disk. 


# Recovering an ordinary simultaneous price

A valued extension controls all positive-valuation shifts at once.
Power interpolation recovers the bound at each constant. It suffices
to have strict slack and finitely many families because each ordinary
closure test uses only a finite list of indices.


### `finite_slack`

 Passing all finite tests with arbitrarily small slack suffices. 

### `uncountable_extension`

 An uncountable field of constant parameters over any base. 

 # The spectral pseudometric on the additive group of disk shifts 


# Synchronization from collapse of the pinned sites

Every finite tuple of shifts is realized by an assignment dominated
by its generic profile on ordinary tensors. If all its wire distances
vanish, integral transport identifies the sites even on valued inputs.



# Rigidity of the pinned disk

Compatibility gives an isometric action on the closed hull.
The submean comparison extends from orbit tests to the hull,
and continuity at the marked orbit point forces it to be fixed.



# Synchronization or contact

Nonconstant motion supplies three fixed branches on the disk tree.
One-sided private products give contact on their homogeneous tangent,
and the tripod comparison propagates contact to every shape.
Otherwise all pinned profiles collapse, giving simultaneous pricing.


### `contact_of_not_shared`

 Descend the square and rectangular conclusions from the countable
algebraic closure. The network estimates can stay over the finite field. 
