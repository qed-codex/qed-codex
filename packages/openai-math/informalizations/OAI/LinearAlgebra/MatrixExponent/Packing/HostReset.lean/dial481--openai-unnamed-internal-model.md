---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/HostReset.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/HostReset.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/HostReset.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The result of resetting a host

Group-prefixed endpoints keep distinct blocks independent. The common
host contains both core links and possible tethers. Width is measured
in the same unit before and after the reset.


### `ResetResult.unscale`

 Undo the normalization by a single base's capacity. 


# The reset as an exact wire packet

Good contacts use the fixed reserved links. Exceptional ones have their
own paths in the contact trees. All sites project to a group and a slot
in the common trivalent host.


 # Incidence budget on the permutation hardware 

### `path_degree`

 A path visits each vertex at most once, hence contributes at most
two incidences there. 

### `incidence`

 Bound both endpoints of all supply wires on each absolute host site.
This includes repeated incidences and both ends of a loop. 

 # Per-site bounds on loads and wires in the reset packet 

### `active`

 No core wiring is introduced at a frozen host position. 

 # Total core width after the degree reset 

### `total_cost`

 Width is measured relative to the capacity of one base. 


# Resetting the core degree

The rotor and the core degree determine the depth, load and position
overheads. The full degree, which counts tethers, enters only the bound
on the new full degree. Every core demand is transmitted exactly.


### `reset_exists`

 A trivalent rotor of width `w` resets arbitrarily many independent
graphs on a common host. The cutoff for the group length is independent
of the number of frozen neighbors. 


# Applying a reset to a core diagram

All exterior ports, including tether ends, remain separately named.
Only crossing supplies survive, still bundled in the original unit.


 # Degree reset on a common host with frozen tensors 

### `reset`

 Reset all groups using one choice of common links and a single rotor. 
