---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkGatherBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relocatable gather code before each shrinking map writer

Each grid, party and layout has a finite instruction range. The range copies
all of the party's AB and surviving fields into its own staging slots and
then jumps to the descriptor writer for that same grid and party.


### `Key`

 Select a shrinking gather by its demand grid point, one of the six motif parties, and the
surviving layout bit. 

### `Family`

 One fixed shrinking stage uses old and new degree exponents chosen in the schedule. 

### `Family.a`

 Exponent of the old degree for this shrinking stage. Its degree and color count determine
  the thick-wire frame count. 

### `Family.b`

 Exponent of the new degree used to determine the number of subdivisions of each surviving
  role. 

### `Family.operands`

 Call-header expressions for each grid point and party, supplying the level, motif,
  argument and hidden-slot geometry, and histogram address. 

### `Family.node`

 Expression for the parent node whose packet supplies the surviving half-wire bits for a
  grid-point and party handler. 

### `profile`

 The four role subdivision counts computed from the stage's old degree, color count, and new
degree. 

### `thickCount`

 Number of thick-wire frames in an AB column, equal to one quarter of the old degree times
the number of color patterns. 

### `Visits`

 Positions in the ordered list of AB and surviving frames incident to the selected party in
the given layout. 

### `setup`

 Register-setup and frame-copy recipe for each visit, using the selected party's header
operands and parent node expression. 

### `Address`

 Instruction address consisting of a grid, party, and layout key and a label in that key's
resident column gather. 

### `PrivateReg`

 Private evaluator register identified by its gather key, frame visit, and operand-compiler
register index. 

### `rowPC`

 Place an instruction of the selected resident column gather at its assigned machine program
counter. 

### `vm`

 Embed one frame visit's operand-compiler registers into the gather family's private
register allocation. 

### `entry`

 A party with no frames goes directly to its writer. 

### `text`

 Five-bit template instructions for insertion at arbitrary program locations. 

### `linked`

 Installation gives the precise code equation required by the linked native party theorem. 

### `Apart`

 The gather's private register bank is disjoint from the DFS, saved bootstrap, and shared
registers that provide its inputs. 

### `safe`

 No scratch operand can clobber one of the six input registers. 

### `preserved`

 A returning gather preserves the loop, DFS and saved bootstrap registers for its writer. 

### `execute`

 Enter the installed gather for the selected stage, grid point, party and layout.
Its returning configuration is already at that grid point's descriptor writer. 

### `execute_exact`

 The successful trace and upper scratch are fixed functions of the selected job and inputs.
The gather has no reads outside the stated region and keeps the lower private stack. 
