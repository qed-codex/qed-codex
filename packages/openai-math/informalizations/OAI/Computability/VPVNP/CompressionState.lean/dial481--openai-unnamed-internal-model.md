---
{
  "module": "OAI/Computability/VPVNP/CompressionState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degree and lane states of the compressor

A state retains the actual slots, their binary displacements and the width
of every individual wire. A substep specifies one such output per admitted
term of its local tensor identity. These types let Section 7.4 compose the
shrinking and degree-refresh identities even when the next topology depends
on all term choices made so far.


### `State`

 Degree exponent and available binary lane coordinates index a network. 

### `State.Base`

 Finite type of base vertices whose lifts by the lane bits give the sites of this
  compression state. 

### `State.baseIndex`

 Number the base vertices by consecutive finite ordinals for use in the descriptor tables. 

### `State.slots`

 Directed slots and lane displacements describing the network lifted from the base
  vertices. 

### `State.width`

 Number of bits carried by an individual outgoing wire, indexed by base vertex, port, and
  lane. 

### `productIndex`

 The indexed order on a product base. The first component is the
old base address and the second is the promoted tag or port coordinate. 

### `network`

 The wire tensor uses the finite binary word alphabet on each actual arc. 

### `positions`

 Number of processor positions, including all lanes at each base vertex. 

### `energy`

 Energy at the normalized mass of a single directed arc. 

### `totalWidth`

 Sum of the widths of all shared fields. 

### `StatePass`

 A local tensor identity whose output at each choice has the indicated
degree and lane count. 

### `StatePass.step`

 The network step expressing each input wire-tensor coefficient as the sum of the term
  values at the same half-wire assignment. 

### `StatePass.next`

 Output compression state for the network of each chosen term. 

### `StateExecution`

 An exact computation with the same final degree and remaining lane
count for every sequence of admitted choices. 

### `Choices`

 Only the motif choices are part of the path. The kernel contractions
sum over their hidden wire coordinates separately. 

### `finalState`

 Output topology and widths determined by the choices. 

### `history`

 The coefficient identity is iterated over exactly these substeps. 

### `bind`

 Continue each admitted term independently. 

### `forall_final_bind`

 Every final state of a continuation is reached by a path of the initial
execution followed by a path of the chosen continuation. 
