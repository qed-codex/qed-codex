---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/FieldLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/FieldLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/FieldLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing and matching one dyadic group

Represent a colony by its host and dyadic interval. Each unit wire keeps
its block index, while its two hosts determine its two colonies.


### `bin_charge`

 Pay for all core bins out of the total load and one allowance per host. 

### `pack_subround`

 A packing together with a compatible matching that internalizes at least
a quarter of the core width, less the tether and host allowances. 


# Charging the incidences of replacement wires

Each gadget has fewer than `4*b` wires. Both ends of every wire are
charged to one of its four original endpoints. The matched pairs use
disjoint sets of original wires.


### `contact_load`

 Each new wire has width `u / b`. Both endpoints count toward the load,
including two incidences at a common site when the wire is a loop. 


# Choosing the cheaper contraction before identifying any endpoints

The profile alone gives two complementary upper bounds on the number
of crossings. Their comparison does not inspect the actual diagram.
Additional coincidences of endpoints can only reduce the chosen cost.



# Simultaneous replacement of matched bundles

Each matched pair uses the same six-site identity, with its own
selector. Unmatched bundles pass through unchanged. The choices of
row or column contractions can be made after expanding this identity.


### `wireRule`

 A profile of each selector counts sub-bundles of width `z`. 


# Contracting a matched subround

On the core diagram, tether ends are named exterior wires. The selector
determines which layout to contract. Every surviving bundle still has
exactly `z` bits and the sum of the diagrams is the unmodified tensor.


### `Gadget`

 Fixed independently of the subdivision width. 

### `width_contract`

 The saving counts individual wire bits, even though matching was
performed on whole bundles. 


# Contracting on a projected host

Surviving core bundles have both ends in one group. Reassign tether
ends and frozen charges by the same layout, keeping their names intact.



# Simultaneous contraction of dyadic groups

Treat the group prefix as an extra host coordinate while packing.
Projection then returns that prefix to the block index. The resulting
host bounds are independent of the number of groups.


 # Transporting a contraction and a reset to a larger field 

### `map_packet`

 Extend the local factors of a packet along a field homomorphism.
The supply graph and selector set are unchanged. 
