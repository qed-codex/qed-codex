---
{
  "module": "OAI/Computability/VPVNP/PairVertexImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite native image of a final-vertex call

The site bootstrap and final-wire loader enter a common nine-row DFS.
Its role router and histogram flush obtain their branch-dependent bases
from a private geometry table. The three native role bodies return to the
same child-list header. All labels and registers of the table are finite
and independent of the input length.


### `Saved`

 Stable bootstrap registers, in the terminal caller's order. 

### `roleOffset`

 Saved register holding the displacement from DFS node addresses to their role words. 

### `histBase`

 Saved register for the base address of the private histogram counters. 

### `ordinal`

 Saved register for the ordinal of the final site being processed. 

### `root`

 Saved register for the selected final site's root DFS node address. 

### `header`

 Saved register holding the external terminal header address. 

### `finalSites`

 Saved register holding the number of final sites from the terminal header. 

### `slots`

 Saved register holding the count of numbered final arc slots. 

### `widths`

 Saved register pointing to the final arc-width column. 

### `incoming`

 Saved register pointing to the final incoming incidence column. 

### `prefixBase`

 Saved register pointing to the terminal width-prefix column. 

### `wires`

 Saved register pointing to the shared final wire-bit interval. 

### `Segment`

 A relocated block has its own labels and private registers. The common
DFS and bootstrap registers are explicit arguments. Five literal bits cover
the constants of the full cursor-leaf program. 

### `Segment.count`

 Number of instructions owned by this linked vertex segment. 

### `Segment.privateRegs`

 Number of local registers required by the segment in addition to the DFS and saved banks. 

### `Segment.entry`

 Local instruction ordinal at which control enters the segment. 

### `Segment.row`

 Instruction generator for this segment under the given program-counter and register
  placements and continuation. 

### `Part`

 The installed components of a terminal vertex computation, from bootstrap and geometry to
the three role handlers and the final return. 

### `rolePart`

 Choose the leaf, shrink, or refresh instruction segment for a decoded node role. 

### `CorePC`

 Labels of the shared vertex control code, including DFS, packet copying, role dispatch, and
histogram flushing. 

### `PC`

 A vertex instruction address is either a shared control label or an instruction ordinal
inside one named segment. 

### `Reg`

 The vertex register space combines the DFS, saved, and counter banks with a separate local
bank for each segment. 

### `Placement`

 An enclosing program can install the image among its other opcodes. 

### `Placement.pc`

 Inject the shared and per-segment instruction addresses into the enclosing machine's
  program counters. 

### `Placement.reg`

 Inject the vertex's named register banks into the enclosing machine's registers. 

### `core`

 Place a shared vertex control label at its host program counter. 

### `stage`

 Place a local instruction ordinal of a named segment at its host program counter. 

### `entry`

 The host program counter of a named segment's designated entry instruction. 

### `dfs`

 Embedding of the nine DFS registers into the host machine. 

### `saved`

 Embedding of the vertex operands that remain available across segment calls. 

### `counter`

 Embedding of the six registers used by the vertex counter and flush operations. 

### `localRegs`

 Embed one named segment's private register bank in the enclosing vertex register space. 

### `dfsPC`

 Host program counter of one instruction in the common DFS controller. 

### `copyPC`

 Host program counter of one instruction in the packet-copy control block. 

### `rolePC`

 Host program counter of one instruction in the node-role dispatcher. 

### `flushPC`

 Host program counter of one instruction in the histogram flush loop. 

### `flushStartPC`

 Host program counter of one instruction that prepares the histogram flush. 

### `copyRegs`

 Use the first five DFS registers as the register bank of the private copy loop. 

### `returns`

 Continuation address after each vertex segment, linking bootstrap to geometry, geometry to
root fields, and the role handlers back to DFS. 

### `geometryRows`

 Read the private geometry pointer from the word at the DFS stack's
exclusive end, then form the address of a fixed geometry field. 

### `dispatchRows`

 The role offset is a private word in the terminal header. The rest of
the router is the common six-row role decoder. 

### `flushStartRows`

 Public words 4, 5 and 9 give the external counter base, production
count and template count. Register 2 initially addresses the private
geometry slot containing the histogram base. 

### `rows`

 All parts share one opcode array and one physical register space. 

### `Contains`

 The host machine contains every placed vertex instruction at its width-resized encoding. 

### `core_linked`

 The exact rows used by the DFS and both physical copy/flush loops. 

### `placement`

 Canonical numerical labels of the assembled width-independent table. 

### `template`

 Assemble the numbered vertex instructions into a five-bit template entered at the bootstrap
segment. 
