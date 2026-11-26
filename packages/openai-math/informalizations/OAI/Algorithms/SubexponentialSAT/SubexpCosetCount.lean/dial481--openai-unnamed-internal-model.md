---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCosetCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCosetCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCosetCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact multi-color coset counts and their exponent bound

This file proves the cardinality calculation in (1.1) and (4.7) of the
subexponential manuscript. Every color count and field size remains a parameter.
The count concerns actual finite quotient classes and points in their cosets;
it is not a theorem about the bit cost of constructing or enumerating them.


### `alpha`

 The exponent coefficient in the manuscript. 

### `iterationCount`

 Outer choices times the total number of inner-sum terms per outer choice. 

### `iterationCount_eq_sum`

 Distribution over colors gives one power per color. 

### `exponent_le_alpha`

 The total-dimension and maximum-dimension hypotheses bound each exponent.
No rounding of `D/r` or `(1-τ)^2 D` is implicit: these are real inequalities. 

### `iterationCount_le_real`

 The exact integer count satisfies the claimed real-exponent bound.
This even holds when `r=0` (both counts are zero); applications use `r ≥ 2`. 

### `OuterData`

 One complement vector and a quotient class for each color. 

### `InnerData`

 Choosing a color and a point in that color's actual coset describes one
term to be accumulated among the separate inner sums. 

### `IterationData`

 All actual inner-sum terms for all actual outer choices. 

### `outerMap`

 The complement vector and all quotient classes of a split assignment. 

### `outerMapFiberEquiv`

 The fiber of `outerMap` consists precisely of one point in each given coset. 

### `familyCosetEquiv`

 The exact multi-color quotient/coset decomposition of all split assignments.
Compose this with the disjoint-coordinate linear equivalence to obtain the
decomposition of the original full coordinate space. 

### `ambientDimension`

 The complement dimension plus all coordinate-block dimensions. 

### `sum_dimensions_le`

 The sum of the inner dimensions cannot exceed the ambient dimension. 

### `ambientDimension_eq_finrank`

 Any linear splitting of the ambient space identifies its dimension with
the complement-plus-block dimension used in the cardinality formulas. 

### `ambientDimension_eq_card_coordinates`

 Specialization for an actual finite coordinate space. It lets the
disjoint-support splitting module supply `D` without an extra dimension axiom. 

### `card_outer`

 Exact number of quotient-class choices, with the complement included. 

### `card_inner`

 Every color contributes exactly a field-size power to the inner term count. 

### `card_iteration`

 Exact cardinality of the actual dependent iteration type. 

### `card_iteration_le_real`

 The manuscript's bound for actual coset enumeration, with all parameters
visible. Disjoint-support applications supply the two dimension estimates. 

### `CoordinateOuterData`

 Outer data for the literal disjoint coordinate supports of the layout. 

### `coordinateCosetEquiv`

 Restrict coordinates and then record one quotient class and coset point
for every color. This partitions the original full assignment space exactly. 

### `coordinateReconstruct`

 Reconstruction of an original assignment from all its coset data. 

### `coordinateReconstruct_eq`

 The concrete reconstruction is the complement extension plus the sum of
the zero extensions of the selected color vectors. 

### `coordinate_ambientDimension`

 The coordinate splitting supplies the ambient-dimension equality. 

### `card_coordinate_iteration_le_real`

 The complete exact-coset-to-real-bound statement on the original
coordinate supports. Both dimension estimates are explicit hypotheses. 
