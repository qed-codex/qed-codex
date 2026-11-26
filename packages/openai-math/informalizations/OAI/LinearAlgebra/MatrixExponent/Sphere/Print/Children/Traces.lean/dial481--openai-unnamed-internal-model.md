---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Print/Children/Traces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Print/Children/Traces.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Print/Children/Traces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Recover adjacency from the two node addresses and data local to their roots. 

### `traceAdj`

 Endpoints either lie on the same tree or join two fully addressed leaves. 

### `cases_possible`

 A one-way candidate ending at another leaf always has the target
address. Its source may have been an unused address. 


# Short intrinsic names for bundles

A key alias can be reused in distant footprints. Seam and station
names need only distinguish the contacts of a single cell.


 Both endpoints of a logical bundle are encoded in its short name. 


# Terminal cell data

One cell's station and seam lists are in their original order. The
only extra variable information from outside that cell is membership
of key aliases in the footprints of neighboring cells.


 # Exact coverage of the incident logical wires by the cell data 

 # Printing equality constraints on all the hub's ordinary wires 


# Shape ownership

Store the two station shapes at the station's cell. A seam shape
belongs to its source cell and is indexed by its destination color.
The other end reads this same value.


 # Matching the printed pattern to an ordered physical table 

 # Capacity and energy bounds for indexed station tables 
