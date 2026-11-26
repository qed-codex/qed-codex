---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/Skip.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Skip.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Skip.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Numbering a pair's virtual bits by whole channels 

### `Channels`

 The bits with any one key have identical endpoints. 

 # Arithmetic form of the physical address at either end of a link 

### `wireAddress`

 The parity bit identifies the endpoint and the position modulo
the processor count identifies the relay. 


# Inverting the physical link schedule

Parity recovers the sending endpoint. Prefix intervals identify its
partner. The quotient inside the interval and the relay identify the
virtual bit. Unused positions, including holes at interval boundaries,
are rejected by the final index check.


### `active_iff`

 An arithmetic decoder recognizes exactly the occupied slots. 

### `peer`

 At a relay the peer leg has the same bit index and reversed endpoints. 

### `relayCheck`

 The tape may be extended arbitrarily outside its valid addresses.
Only an active relay with a second leg reads the peer address. 

 # Batched binary search on prefix intervals 

### `evolve`

 Each step gets the unchanged input and the current vector. Track
actual gate counts to avoid raising the cost exponent at every step. 

### `search`

 Find the last prefix offset not exceeding each query. The circuit
tests one candidate per lane per bit of the partner index. 

 # Reading a link when a worker is itself the intermediate processor 

 # Simultaneous decoding of occupied positions on physical links 

### `sub`

 Subtract ordered operands by modular addition. 

### `decode_slot`

 Compute the partner, index, length and peer address for each lane.
A peer address is used only when the partner leg exists. 

 # Enumerating the incident links of one processor in parallel 

### `fan`

 Repeated lanes are harmless in a conjunction. Assign the diagonal
of the processor-pair matrix to any existing link at the processor. 

### `relay_lanes`

 The fixed lane index specifies a peer and a byte. A small matrix
indexed by the worker and peer supplies link-specific metadata. 

 # Reading the incident bits of numbered channels 

 # Prefix offsets in the physical relay schedule 
