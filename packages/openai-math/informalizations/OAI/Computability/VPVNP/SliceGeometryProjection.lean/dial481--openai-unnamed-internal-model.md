---
{
  "module": "OAI/Computability/VPVNP/SliceGeometryProjection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometryProjection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceGeometryProjection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coordinate projections through a Macaulay matrix pencil

Adjoin the equation `X_i - c = 0` to a finite polynomial system, first with
an indeterminate in place of `c`. The resulting Macaulay matrix has entries
of degree at most one in the parameter. Under the uniform weak Nullstellensatz
bound, the coordinate image of the common zero set consists precisely of the
parameters where adjoining the coefficient row of one increases rank.


### `coordinateEquations`

 Adjoin the equation fixing the selected coordinate to the parameter. 

### `coordinatePencil`

 The Macaulay matrix over the univariate parameter ring. 

### `augmentedCoordinatePencil`

 Augment the matrix pencil by the constant coefficient row of one. 

### `coordinatePencil_eval`

 Specialization at `c` gives exactly the bounded coefficient matrix of the
original equations and the fiber equation `X_i - c`. 

### `coordinatePencil_degree_le`

 The indeterminate enters the coordinate fiber equation linearly. 

### `coordinateImage_iff_row_notMem`

 The coordinate image is detected by failure of the bounded certificate
row test. The forward direction holds for any multiplier bound. 

### `coordinateImage_iff_rank_lt`

 Appending the coefficient row of one turns the fiber test into a strict
inequality between the ranks of the two specialized matrix pencils. 

### `pinnedEquations`

 Present the partially pinned set using the original equations and one
potential linear equation per variable. An unused pin contributes zero. 

### `geometricPinnedEquations`

 Extend the system of partial pins to the geometric field. 

### `mem_pinnedPoints_iff`

 The fixed-size pinned equation list cuts out precisely the partially pinned
geometric point set. 

### `mem_pinnedCoordinateImage_iff_rank_lt`

 Rank criterion for each coordinate of each partial pin, with the same
certificate bound and index types at every stage of the slicing procedure. 
