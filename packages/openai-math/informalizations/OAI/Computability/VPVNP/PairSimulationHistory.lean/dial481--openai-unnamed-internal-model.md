---
{
  "module": "OAI/Computability/VPVNP/PairSimulationHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary paths through a local compression history

Section 13 reads the old half-indices of each child once, then uses the same
arguments in the local map tests and the child's expansion. An absorbed
supply field is owned by one site and has just one code even if several map
arguments read it. These readers operate on a shared suffix of a binary
stream, so the encoding of a site can be followed immediately by its siblings.


### `Order`

 An ordered descriptor list with each of its entries present once. 

### `Order.length`

 Number of positions in the descriptor's enumeration. 

### `Order.entries`

 Bijection from descriptor positions to entries, used to visit each entry once in that
  order. 

### `Order.reader`

 Read a list of dependent fields or child vertices in descriptor order. 

### `pair`

 Read the first factor and then the second, with no separator or tag. 

### `fiberEquiv`

 The arguments of a placement kernel only mention fields owned here. 

### `fiber`

 Only fields in the stored preimage list are consumed. 

### `half`

 Outgoing and incoming indices are independent, also for a self-loop. 

### `bitField`

 An actual arc carries its declared number of bits, including the empty word. 

### `statePayload`

 The old and final payloads in a lifted compressor state have explicit bit readers. 

### `reject`

 Reader for an impossible local choice. Every input stream fails to decode. 

### `accept`

 Reader for a successful deterministic local check. It returns the unique choice and
consumes zero bits. 

### `entryReader`

 Test the map arguments before recursing. Successful entries use no bits
and the indicated parameter occurrences retain their own multiplicities. 

### `layoutReader`

 A layout sums over one word per absorbed wire. Each map entry sees the
entire resulting local assignment, including a shared field at both ends. 

### `LocalOrder`

 Per-site field and child orders from the descriptor of a selected term. 

### `LocalOrder.children`

 Traversal order of the input sites placed at each output site of the term. 

### `LocalOrder.outgoing`

 Order in which to read the outgoing half-wire payloads at each input site. 

### `LocalOrder.incoming`

 Order in which to read the incoming half-wire payloads at each input site, after its
  outgoing payloads. 

### `pushReader`

 Read the old half-bits, the local kernel choices, and then each child.
Kernel checks see the same arguments passed to the child readers. 

### `Readers`

 At the terminal level, the same arc assignment is passed to every site.
At a branch, the descriptor phase supplies the choice and the local field
and vertex orders of that choice. 

### `historyReader`

 One binary parser for the semantic occurrence type of (12.2).
All branch selectors precede the shared arc assignment. The final-site
readers descend through the stored preimage lists, including on branches
whose term selections change the network topology. 

### `successful`

 Every successful complete binary stream gives precisely one occurrence,
even if several streams accumulate the same exponent vector. 

### `weightedStreams`

 Weighted enumeration of binary transcripts. The exponent vector on an
accepted transcript is computed on its decoded occurrence. 

### `incidentPrefix`

 Execute the original site loop once. The unused suffix is kept for the
following child. The final status, successor, sort and memory tests are
performed on the reports of this same loop. 

### `incidentPrefix_iff`

 On every incident bit vector, even one incompatible with the remote
vertices, this parser takes exactly the accepting validator's private bits. 

### `incidentReader`

 The raw reader returns an accepting string as its own representation. 

### `incidentReader_length_le`

 The successful raw prefix bound holds for independent half-wires as
well as for a globally consistent assignment. 

### `bufferReader`

 Route and clamp checks precede any private validator choice. The
transit case keeps the incoming suffix intact, including when it is nonempty. 

### `initialReader`

 The actual cursor factor, on any supplied half-wire assignment. 

### `pushLeafReaders`

 Transport actual leaf readers, including their individual accepting
branch strings, into the dyadic-degree compressor's site coordinates. 

### `cursorReader`

 Read the terms, shared arc bits and all local subtrees of a compression
of the paper's RAM network, preserving the multiplicity of (12.2). 

### `cursor_weightedStreams`

 Equation (13.1)'s weighted equality with the original capped RAM path
count, for the supplied kernel descriptors of the compressed history. 
