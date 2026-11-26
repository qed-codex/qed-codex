---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Prices/Motion/Rigidity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/Rigidity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Prices/Motion/Rigidity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Submean tests on a valuation disk 


# From leaves to points of the disk tree

The leaf metric alone does not locate midpoints in the ambient space.
A three-arm test with a moving midpoint supplies the missing estimate.


### `inner`

 Points in the unit disk of the midpoint comparison. 

### `outer`

 Any distant leaf lies on an arm through the same midpoint. 

 # Distances between the chosen disk midpoints 

### `ordered`

 Two ordered points on a common segment have distance equal to
the difference of their distances from the initial endpoint. 


# Submean comparison on the branches of the disk tree

For each moving leaf choose a distant endpoint whose distance
from that leaf is constant throughout the star. Harmonic depths
then give harmonic distances to both endpoints of the segment.



# Submean tests on the geodesic hull

First allow a different orbit mark at every slot. Simultaneous
geodesic interpolation then gives the tests for terms. A countable
intersection and continuity in placement pass them to the closure.


 # Restricting the submean comparison to a single wire 


# Submean estimates survive the zoom

Dilation of the coefficients multiplies the lengths of all arms by
the same positive number. A single residue outside countably many
exceptions works throughout the sequence of zooms.



# Rigidity of analytic motion

A nonconstant action with the disk tests and continuity at the origin
produces a configuration of leaves on the disk tree. Excluding
that configuration forces the action to fix the chosen mark.


### `Moving.constant`

 Continuity need only hold at the chosen mark. 
