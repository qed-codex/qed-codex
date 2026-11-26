---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/BadBases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/BadBases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/BadBases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Propagating dyadic splits across a host

An edge with delay `d` moves a split up `2*d` levels. To bound all
propagated marks we sum a geometric majorant over neighbours. This
counts paths with multiplicity and needs no choice of shortest paths.


### `spread_bound`

 A column-sum bound on the delay weights gives an absolute constant,
independent of the number of neighbours and the number of levels. 


# Propagation through fixed bases

Weight the count of splits by the depth below each vertex's base. Moving
a mark across an edge of length `16 * d` costs at least `8 * d` levels
relative to the respective bases, and thus a factor of at least `2 ^ d`.


### `choose_bases`

 Choose base depths from the total normalized loads, before mixing.
In a minimal feasible choice each depth is tight either locally or
along an edge. The incoming weight bound pays for all tight edges. 

### `base_splits`

 Bound the number of base cells forced to split by the weighted initial
marks within all bases. The constant is independent of the host degree. 


# Initial marks in the dyadic tree

A heavy cell carries more than one unit of normalized load. Since no
block carries more than half a unit, at least half a unit of ordered
cross products lies in this cell. Only pairwise collisions are needed
to bound the mean number of initial marks.


### `heavy`

 Load is normalized by the capacity of a colony. 

### `heavy.depth`

 If each block occupies at most a reciprocal power of two units, the
finest levels need no splits. 


# A fixed menu of mixers for every block length

The number of candidates is at most the block count. Repetitions and
unused entries are harmless because the election minimizes a score.



# Bad bases in a degree reset

Index contacts by a family and a binary cell within it. Only their two
endpoints are charged on overflow. All positions and contacts use the
same permutation of the blocks.


### `BadBase`

 A split propagated from a cell of load greater than two, or an
endpoint of a contact with load exceeding its mean by more than `1/g`. 

### `score`

 This quadratic upper bound on the exceptional load can be minimized
using aggregated difference counts. 

### `bad_bases`

 A single linear mixer bounds the total load of all bad bases.
The estimate is independent of the number of tether neighbors. 


# Balanced dyadic partitions

The vertices share a single linear permutation of the block indices.
Loads are normalized by the capacity of one part. In the paper's
notation the minimum length is `A = 2 ^ k` and the edge delay is `2 * d`.


### `balanced_partition`

 The count is bounded across all vertices. Each label has exactly the
indicated prefix as its fiber, with bounded load and length at least `2 ^ k`.
The depth comparison applies in both directions on an undirected edge. 
