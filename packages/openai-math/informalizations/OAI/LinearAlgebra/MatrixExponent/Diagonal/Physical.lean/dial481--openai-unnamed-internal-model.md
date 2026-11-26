---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagonal/Physical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Physical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Physical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Routing virtual bits over complete physical links

Bit number `i` of a pair passes through processor `i % R`. If that
processor is an endpoint, the path is direct. The two orientations of
each physical link use even and odd positions. At a given endpoint,
each other endpoint is allotted a disjoint interval of quotients `i/R`.


### `address`

 The sum of the two processor indices modulo R gives at most R
matchings. Both endpoints use the very same address for a shared bit. 

### `Leg`

 There is a leg from each endpoint to the intermediate processor,
except when they coincide. 

### `link`

 The actual unordered processor pair carrying a leg. 

### `at_endpoint`

 Both endpoints can read the bit, including on a direct path. 

### `encode`

 Fixing unused slots to zero makes the physical encoding unique. 

### `decode`

 When the two legs agree at their shared intermediate processor,
they determine a unique virtual bit assignment. 


# Contracting local tables over physical links

A processor sees the shared positions of its incident links. It tests
equality at every relay and pins unused positions to zero. Each virtual
assignment then contributes exactly once, in any characteristic.


### `view`

 Read the incident bits at synchronized addresses. Other positions
in the reserved link interval contain zero. 

### `site`

 A table whose input is only the processor's reserved interval. 


# Local contraction with arbitrary virtual links

Parallel edges may be numbered in any prescribed order. Loops are
summed privately so they consume no physical links.



# Routing finite alphabets

At each endpoint, privately sum over the incident symbols and require
their encodings to match the shared bits. An injective code forces the
same symbol at both ends. A loop needs no shared bits.


### `contract`

 The alphabet on each edge may be empty. Only edges joining distinct
processors contribute to the bandwidth condition. 


# Link usage under a valid report

A shared class transmits its selector and crossing bits. Other classes
transmit the individual packet positions. Loops consume no bandwidth.


 # Assignments of a reported network 

 # Physical links for a reported packet network 

### `Worker.index`

 Number homes first, then station workers and finally packet workers. 

### `budget`

 Only links between distinct workers use the communication budget. 

### `processor`

 The processor table acts on its own input interval. Simultaneous
numbering of the parallel wires is specified by the caller. 
