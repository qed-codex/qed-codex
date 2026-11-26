---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Copy/Overlay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Copy/Overlay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Copy/Overlay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing physical codes for dictionary addresses

A code is a bijection. Its length equals the logical address width,
so changing codes costs no additional bits. A visible bit is a
constant or one projection, uniformly over a family of inputs.



# Synchronous forwarding of requested bits

Each request receives its own register. Round zero initializes it
locally. At each subsequent tick it either stays or moves through
one host link, without changing blocks or reading another register.


### `register`

 A register is initialized once, then copied at every clock tick.
The fixed route determines both the sending and receiving host. 

 # Counting copies and transmissions in a local schedule 

### `Event`

 Each initialization or copy occupies one slot. We charge stays
including those used for padding the shorter paths. 

### `congestion`

 At most one requested bit of each kind per destination. Charge
all registers visiting a site, even those forwarded elsewhere. 

 # A window code consists entirely of nearby old bits 

 # Appending a literal slot number to a window of copied labels 

 # Copying dictionary bits through a movement history 

 # Revised labels copy an old address, a printed address and an outline 

 # Bootstrapping the dictionary from one neighborhood 

 # Selector projections and fixed padding away from occupied positions 

 # Fixed wiring for the local labels of a complete concentration 

 # Distributing all child labels of all occupied occurrences 

 # Sending schedule messages along the original host contacts 

 # Synchronous schedules for raw and revised output labels 
