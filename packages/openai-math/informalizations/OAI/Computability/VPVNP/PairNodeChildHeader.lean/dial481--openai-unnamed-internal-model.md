---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading a placement row and the old layer's parameter directory

The popped descriptor supplies a child-list pointer and count. A seven-word
directory supplies the geometry of the old descriptors, the private argument
arena, and the inverse-incidence and width columns. These words are read
once before the child scan enters its loop.


### `Fields`

 The directory words, in their stored order. 

### `Fields.olderBase`

 External address of the first descriptor row in the older layer. The child scan subtracts
  this address from the child's row address to recover its offset. 

### `Fields.stride`

 Distance in words between successive older-layer descriptor rows. Dividing a row offset
  by this stride gives the child's site ordinal. 

### `Fields.degree`

 Number of outgoing slots per older-layer site. Multiplying the site ordinal by this
  degree gives the index of its first port. 

### `Fields.argumentStart`

 Base address of the private arena where the child scan stores guessed half-wire
  arguments. 

### `Fields.argumentStride`

 Distance in private words between argument buffers indexed by consecutive node addresses.
  A child at address `node` uses the buffer at `argumentStart + node * argumentStride`. 

### `Fields.actualIn`

 Base address of the inverse-incidence table. At an incoming port, this table gives the
  source port whose wire width the scan needs. 

### `Fields.width`

 Base address of the wire-width table indexed by actual outgoing ports. Each width tells
  the scan how many argument bits to guess for that wire. 

### `Fields.words`

 Seven words in the order read by the child scan. They contain the descriptor base and
stride, degree, private argument base and stride, inverse-incidence base, and width-table
base. 

### `Fields.Stored`

 The seven directory words occupy consecutive external memory cells beginning at `base`,
using word-address arithmetic. 

### `instruction`

 The 17 instructions that load the child-list pointer and count from the popped row, read
the seven older-layer directory words, and pass control to `done`. 

### `Linked`

 The machine contains the header's 17 instructions at the specified program counters, with
the supplied register assignment and continuation. 

### `events`

 Trace of the header load. The machine reads the child-list pointer and count at `node` and
`node + 1`, then reads the seven directory words beginning at `base`. 

### `Preserved`

 The header writes only the child scan's input registers. 

### `Ready`

 State at the header continuation. The scan registers hold one, the child-list pointer and
count, and the seven directory words. All other registers, private memory, and persistent
state retain their entry values. 

### `native`

 Load the child scan's actual source, count and layer parameters. The prefix
preserves the bit stream and reaches the linked loop on the same external memory. 
