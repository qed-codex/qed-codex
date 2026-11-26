---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Footprint/Load.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Footprint/Load.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Footprint/Load.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Connectivity of the ordinary information carried by moving stations

Selectors are indexed by their cell, and the fresh wire created by a
crossing is indexed by the current stack length. Carrying information
to the neighboring cell extends each footprint along a seam.


 # Cells of a network and their nonempty oriented seams 

 # Counting port incidences in a grid of stations 

### `carries_le_uses`

 Each crossing wire along a port charges its unique endpoint in this cell. 

### `ports_bound`

 Each neighboring cell contributes at most two oriented ports. 

 # Numbering a finite set by a local key 

### `number`

 Use increasing key order where the keys distinguish the elements.
Unordered inputs still admit the same contraction proofs. 

### `number_keys`

 Absolute element names disappear after numbering. The ordered
list of keys depends only on the unordered set of keys. 

 # Transporting stationwise properties through a scene update 

 # Information that a station may read 

### `Observe`

 Agreement on one ordinary key. Natural-number keys are introduced
sequentially and their values are homogeneous states. 


# Propagation of ordinary information

Merging takes the union of the reads. A crossing transfers those reads
and creates one independent key for the mover's former private state.
The near-side residue needs only that new key.



# Bounding the number of ordinary keys at a cell

A fresh private state becomes local to the departure cell. The only
non-collector allowed to carry keys from elsewhere is the current
mover. Its number of nonlocal keys grows linearly in its crossing
count, independently of the number of untouched auxiliary marks.



# Station names stay in their original cells

Only collectors carry names. Moving a station can therefore neither
displace a name nor duplicate one.

