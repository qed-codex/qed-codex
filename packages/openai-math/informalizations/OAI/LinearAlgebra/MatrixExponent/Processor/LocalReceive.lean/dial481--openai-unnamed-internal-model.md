---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/LocalReceive.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/LocalReceive.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/LocalReceive.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact semantics of the worker's packet kernel 

### `kernel_eq`

 Each private code string represents at most one class symbol.
Ill-formed code strings contribute zero. 


# Summing the private records of a packet class

The external positions supply the packet data, the reported counts,
and the compacted stream. Each contributing symbol has exactly one
fixed-width encoding in the private positions.



# The packet contribution at one worker

Only data delivered to the worker can affect its factor. In particular
the remaining rows of the fixed layout may be filled with zeros.


### `product_eq`

 Private summation in the class kernels computes exactly the worker's
sum over incident symbols, constrained by the received physical bits.
Slots whose destination is another worker are unrestricted. 

 # Network cost of checking the physical link schedule 

### `valid`

 A single circuit checks all unused-slot pins and relay equalities.
The pair counts, skip offsets and current processor may vary with the
input. The link tape is selected by a fixed list of bit names. 


# Pair lengths and processor offsets for accepted reports

The register bound need only hold at the guaranteed input reports.
All circuit statements still involve a single computation independent
of the report.


### `Limits`

 Bounds with slack so all addresses in the table fit in a register. 

 # Inspecting arbitrary endpoint metadata in parallel 

 # Checking relay consistency directly from the public input bits 

### `relay_net`

 One circuit works for all feasible reports, processor identifiers
and scripts at this cut. It pins unused slots and checks every relay. 


# Separating bit and class symbols at one worker

A shared bit has exactly one specified physical address. Private
bits and class symbols remain independent summation variables.



# A fixed-size table of potentially incident slot keys

A home or station worker uses just its coordinate slice of the
possible endpoints. A packet worker instead uses the auxiliary
coordinate of the first template label. The size is the same for
all three roles, regardless of the heavy set.


 # Separating the bit and class checks in the physical input 

### `extendLocal`

 This is the extension in the localization of a vertex table. 
