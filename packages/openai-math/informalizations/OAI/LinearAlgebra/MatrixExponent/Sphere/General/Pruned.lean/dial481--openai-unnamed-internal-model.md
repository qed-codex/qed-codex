---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/General/Pruned.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/General/Pruned.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/General/Pruned.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Endpoints retained by loop removal 


# The local order of a station's ports

Each side begins with its exterior bits. Named internal bundles follow
in the chosen order, with ascending offsets inside each bundle.


 Incidence bijections with independently prescribed local orders. 


# Ordered bundles presented to local concentration

The table label includes any local permutation of its arguments.
The decoder reads only this label, the lengths and directions of
the bundles, and their bits in order. It never reads a remote
vertex name or an exterior wire name.


 # Identifying entire bundles that close at their own station 

 # A source-side bit for every local self-loop 

### `loopBits`

 Index each bit summed by loop contraction by its outgoing lane and offset. 

 # Placement of the wire ends surviving local loop contraction 

### `keepWidth`

 Removing loops either retains an entire bundle or empties it. 

### `keep`

 Surviving ends retain their entire position, including the bit offset. 

 # Local table values after contracting self-loops 

### `loopTable`

 Values on ports at other stations are immaterial. The two ends of
each removed loop share one summation bit. 

 # Restricting an ordered bundle presentation to positive-arity stations 

### `prunePosition`

 An inhabited bundle already has a positive-arity owner. 

### `prune`

 Scalar stations have no wire ends. All remaining labels, lanes and offsets stay fixed. 
