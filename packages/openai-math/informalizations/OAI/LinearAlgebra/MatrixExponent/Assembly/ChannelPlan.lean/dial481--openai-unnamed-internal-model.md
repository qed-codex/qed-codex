---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/ChannelPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/ChannelPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/ChannelPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A controlled payload transfer

Local pointers gather bits from a bank into packets. A permutation
of packets at each scale pairs their ends, and the mask pins unused
output bits to zero. Only the packet indices are global addresses.


### `copy`

 Read the named input bit, or zero for padding. Repetition of an
input name is allowed. 

### `Covers`

 Check the controls independently of the data values. Unused
destinations are pinned, and every other destination has a source. 


# Channel slots at variable capacities

A slot of depth `s` participates at every packet width `2^i`
with `i ≤ s`. Each endpoint reserves at most twice its capacity at
each scale, regardless of the number of neighbors. The extra local
address bit allows padding.


### `Plan`

 Pointers and peers are control data, independent of the bit values. 


# Packing disjoint contacts of one size

The length class and ordinal determine the physical lane. Disjoint
use of bits bounds the number of occupied lanes of each size.


### `lane_end`

 The exclusive end of any active lane fits in the address word. 


# Reserving a packet for a pair of ports

Round the actual transmission length up to a power of two. The unused packet
positions read zero. Ports outside the pairing match themselves.



# Assigning active channel lanes

Unlike payload hosts, empty channels do not take a seat.
The largest address is never a positive length's level, so it can
serve as the bucket for every inactive or padded channel.



# Local gathers and global checks

The addresses of a gather refer only to the local bank. A single
hidden bit is shared by all constant-zero taps. Every other hidden
bit is the output of exactly one deterministic gather.


### `realize`

 One tagged permutation per packet scale suffices. 


# Total cost of reserving all the smaller channels

Global addresses are paid per endpoint. The bit volume, including
dummy packets in the dyadic lists, is bounded by the total capacity
times the number of levels and ports.

