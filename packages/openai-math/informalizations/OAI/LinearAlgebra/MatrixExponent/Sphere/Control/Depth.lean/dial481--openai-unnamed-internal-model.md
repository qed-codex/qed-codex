---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Control/Depth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Control/Depth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Control/Depth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounding the depth of local table descriptions

A merger consumes a station. A crossing charges the receiving cell
one visit, and advances the moving clock. The collector has priority
over all moving clocks and keeps its local budget across arrivals.



# Local station labels

A label depends only on two local exterior strings, a list of selector
values and residual states, and the two sphere indices. Global station
and wire names occur in the layout and never in this interface.



# A finite menu of station tables

One operation fuses two labels, leaves a residue, or moves an
insertion. Its description includes input energies and the number
of ordinary keys to read for the first operand. No field elements
or absolute cell, edge, or wire names are needed by the operation.


 # Descriptions of the elementary station operations 


# An intrinsic record of a region

Station and seam identifiers are local. Ordinary keys and named
exterior interfaces may be renamed. No part of a station table
outside its label occurs in this record.


### `Outside`

 Unrelated cells keep their tables and ignore newly allocated wires.
The fresh keys and their levels are listed in order of creation. 

 # Effects of local edits outside the affected cells 


# Composition of local rewrites

Beyond the edited vertices and seam labels, the only effect of a
rewrite is to project away its newly allocated ordinary keys.


### `Matches.outside`

 A disjoint region keeps its entire record. 

 # Region records for individual station operations 

 # Updating a region without using global identifiers 


# Locality of keys

A crossing always leaves a fresh key at both endpoints, and
footprints never shrink. Thus any operation preserving footprints
outside a region can only move previously available keys within it.

