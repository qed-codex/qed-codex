---
{
  "module": "OAI/Computability/VPVNP/PairRefreshResidentImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshResidentImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshResidentImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The diagonal, dispatch and motif rows of a refresh vertex

The two diagonal tests enter the grid/party loader on success and a local
reject instruction on failure. Every target of the ordinal chains is the
argument writer of the corresponding inlined map. All operands are evaluated
from the six registers selected by the enclosing role.


### `Plan`

 Fixed resident refresh plan giving the tie ordering, physical operand recipes, histogram
ordinals, and source register assignments. 

### `Plan.ties`

 Enumeration of the graph's refresh ties used by the operand and handler tables. 

### `Plan.stride`

 Stride supplied to the refresh term and route address recipes. 

### `Plan.input`

 Runtime address expressions for the old and new refresh argument packets and published
  level tables. 

### `Plan.directory`

 Recipe expression locating the private map-call directory. 

### `Plan.histogram`

 Recipe expression locating the persistent private histogram counters. 

### `Plan.ordinal`

 Map each refresh parameter entry to its counter ordinal in the common histogram. 

### `Plan.source`

 Identify the six recipe inputs among the DFS, saved, and shared registers. 

### `heads`

 Compute the planned map-call field heads from the tie geometry, argument inputs, directory,
and histogram. 

### `family`

 Assemble the refresh map handler for each demand and party, with inline table layout,
operand recipes, and global histogram ordinals. 

### `diagonal`

 Register expressions for checking the diagonal tie at the designated external refresh slot. 

### `route`

 Register expressions that select the demand profile and party of the refresh map call. 

### `Address`

 Instruction addresses for diagonal setup, the comparisons, route setup and dispatch, the
map handler, and the rejection exit. 

### `Local`

 Local register banks reserved for diagonal setup and scanning, route evaluation, and the
selected map handler. 

### `inputs`

 Resolve each recipe input to its host register using its designated DFS, saved, or shared
source. 

### `diagVM`

 Register embedding for the compiled diagonal-setup expressions. 

### `diagReg`

 Select the ten registers for the two diagonal bit scans from the setup outputs and the
additional scratch registers. 

### `routeVM`

 Register embedding for the compiled route-setup expressions. 

### `handlerReg`

 Place the refresh handler family's private registers in the resident plan's local bank. 

### `comparePC`

 Program counter of the chosen control or bit-scan instruction in the diagonal comparison
block. 

### `routePC`

 Program counter of a refresh grid or party dispatch instruction. 

### `handlerPC`

 Translate a local map-family instruction address into its resident program counter. 

### `bad`

 Rejection address reached when the resident refresh selection fails. 

### `diagSetup`

 Program counter for a diagonal setup line, with fallthrough to the first comparison once
all operands are evaluated. 

### `routeSetup`

 Program counter for a route setup line, with fallthrough to the dispatch entry after its
last line. 

### `dispatcher`

 The installed grid-and-party dispatcher using the evaluated route registers and the
family's handler entries. 

### `text`

 The host rows. The caller supplies the already loaded common registers and
the continuation for a successful motif. The diagonal and map failures halt. 

### `locations`

 Finite numbering of all addresses in the resident refresh instruction image. 

### `registers`

 Finite numbering of the shared and local registers used to install the resident image. 

### `segment`

 The vertex segment obtained by numbering the plan's instructions and registers, entered at
the first diagonal-setup instruction. 

### `Installed`

 Each physical instruction at a plan address is the plan's instruction resized to the
machine word width. 
