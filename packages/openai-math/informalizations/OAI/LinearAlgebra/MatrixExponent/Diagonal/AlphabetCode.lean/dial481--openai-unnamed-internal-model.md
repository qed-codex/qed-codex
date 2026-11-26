---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagonal/AlphabetCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/AlphabetCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/AlphabetCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Uniformity of the two group names of a packet 

### `uniform`

 A product parametrization makes the number of points per label exact. 

### `Key`

 Each of the two labels has one independently variable symbol per coordinate. 


# Two coordinate assignments for overloaded groups

Keep light work at its group. Assign heavy work by a different
coordinate of its label. The bound below applies both to the reassigned
work and to each light group's contacts with heavy groups.


### `contact`

 The packet touches a heavy group at the cut and a given group
at the worker coordinate. 


# Bounding communication with two fixed pools of workers

A light home can afford the crossing bits of its light pairs. Packets
touching a heavy group are evaluated whole, assigning workers by a
second coordinate. Each such packet costs at most two full blocks of
slots at any one worker.


### `charge`

 Count both incidences, even if they belong to the same group. 

### `workload`

 Bound the entire workload of each reassigned worker (`i ≠ j`)
or the work sent to heavy partners by any light home (`g ∉ H`). 


# Assigning each virtual bit to two processors

Two pools indexed by the auxiliary coordinate handle the heavy groups.
This makes the locations of the workers independent of the internal
wiring of the batch. Self-links may remain private.


### `Message`

 Heavy packets share both blocks of slots. Light packets share
the selector and the wire bits at the chosen cut. 

### `capacity`

 The endpoint budget for all packets, including every padded position. 

 # Adaptive packet expansion for independent copies of a diagram 

### `batchLoad`

 Keep the cube template and combine the batch and repetition indices. 

### `eval_batch`

 All copies may share a single coordinate choice based on all selectors.
Station and junction bits remain separate until the packet sum restores their
equality. 


# Cutting a packet across one cube coordinate

Partition the supply edges into crossing edges and two sets of internal
edges. Fixing the crossing bits leaves independent contractions on the
two sides. Each supply edge is charged at exactly one coordinate.


### `region`

 Charge each supply bit to the unique coordinate changed by its edge. 

### `expansion`

 A cube of arbitrarily large dimension with a packet expansion.
The average crossing cost and the selector length can both be made
arbitrarily small compared with the number of demanded bits. 

 # Uniform communication plans for exact packet expansions 

### `bounded_expansion`

 One exact cube identity works for every problem size and every tuple
of selectors. The packet links consume at most half of each worker's
virtual bit budget, leaving room for the literal pins. 


# A public report for the adaptive plan

Packets in one class have the same pair of homes and the same packet
worker. Report selector counts by class. A report gives the costs at
all candidate cuts, so one can check the minimizing rule even though
the partition into classes itself depends on the proposed cut.


### `Report`

 A class can report at most the total number of packets. 

### `checks_iff`

 Every selector assignment has exactly one valid report. 

### `report_size`

 The public report has polynomially many count fields, each of
logarithmic bit length, at fixed cube and coefficient field. 


# Encoding the choices of one packet class

Once the report is fixed the total crossing width is independent of the
assignment of selectors in a class. The selectors and their crossing
bits therefore fit in a single bit string of the reported length.


 # Packing one selector class in packet order 

### `pack`

 Concatenate blocks in packet order, padding with zero when necessary. 

### `alphabetCode`

 The fixed prefix determines the lengths of the crossing blocks. 
