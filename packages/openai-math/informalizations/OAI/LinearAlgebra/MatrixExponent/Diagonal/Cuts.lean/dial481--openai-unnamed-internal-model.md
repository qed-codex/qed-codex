---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagonal/Cuts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Cuts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Cuts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Balancing finitely many weight classes

The squared discrepancies are summed over every color and class.
At each vertex some color makes the total cross term nonpositive.


### `color`

 Every class and color has squared discrepancy at most the sum of
squared weights across all classes. Weights may have either sign. 


# Coloring one side of a bipartite graph

Group edges by the prescribed color of their far endpoint. The load of
a vertex in any class is at most its degree, so the sum of squared
loads is at most the maximum degree times the number of edges.


### `bipartite`

 Color the free endpoints, controlling both the number of vertices
in each color and the number of edges of each ordered color pair. 

 # Distributing wires among finitely many labels 

### `multiplicity`

 Count sites carrying the specified label. 


# Packing directed wires into binary cubes

Use every ordered pair of labels as a template, allowing coincidences
in individual coordinates. The corners are labelled by choosing one
symbol or the other in each coordinate. For a fixed corner, the
map from templates to opposite pairs of labels is an involution.
Consequently every demand occurs equally often, even if some of the
corner labels coincide.


### `endpoints`

 The ordered pair served by a particular wire in a packet. 

### `rounds`

 Repetition count fixed from the capacity before laying out any diagram. 

### `pack`

 A uniform supply of cube packets suffices. The rounding error
costs at most one full packet for every ordered pair of labels. 


# Assigning labels to a subdivided batch

Exterior slots may have prescribed labels. Place the remaining junctions
first, then simultaneously balance all incidence counts at the stations.
This avoids any independence assumption about repeated edges or loops.


### `label_diagram`

 Orient each subdivided edge from its junction to its original station.
Every ordered pair of labels has bounded edge multiplicity. 

 # A bounded cube layout for every network of small maximum arity 

### `Layout`

 Each wire of the normalized diagram occupies its own directed
position. The orientation convention is independent of the local tables. 

 # Exact wire identities with a cut along every cube coordinate 

### `Expansion`

 Each corner sends a word to the opposite corner. Index both words
by the sending corner. At any cut the sending and receiving positions
belong to opposite sides. 


# Expanding an exact contraction by packets

Unoccupied positions are pinned to zero on both sides. Summing freely
over them instead could change the scalar in positive characteristic.


### `Layout.eval`

 A network with independent slot bits on the two sides of every edge.
The full sum over packet selectors restores all the wire equalities. 

 # Locality and cost of a coordinate cut 

### `group`

 A template meets at most two groups at a fixed coordinate. 

### `Layout.side_local`

 A side table needs no slot bits from other groups. 

### `Expansion.coordinate`

 The cut may depend on the complete selector tuple. The cost is
bounded uniformly over all such tuples. 

 # Choosing which packets to cut after their selectors are known 

### `sum_value`

 An uncut packet has exactly one assignment of zero bits, avoiding
an extra multiplicity in the field. 

### `adaptive`

 Both the coordinate and the subset of packets to split may depend
on the entire selector tuple. 
