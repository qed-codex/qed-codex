---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapHandlerImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vertex image of the grid-point and party map handlers

Every fixed handler first evaluates its argument recipes and writes the raw
call descriptor. The descriptor pointer goes directly into the lowered map's
pointer register. All successful calls enter the common continuation, while
failed calls reach a rejecting instruction local to the selected handler.


### `Source`

 The writer's six incoming values can be selected from DFS, saved bootstrap,
or the enclosing role's own shared header and cursor registers. 

### `Index`

 A demand grid point paired with the party whose local map table handles that demand. 

### `Family`

 Fixed code and data recipes for one whole role. 

### `Family.regCount`

 Number of source registers allocated to each grid-point and party map table. Lowering the
  table adds two scratch registers. 

### `Family.portCount`

 Number of public ports in each source map table, used to index the constants that will be
  inlined. 

### `Family.layout`

 Register, port and argument allocations used to assemble the map call table for each
  demand grid point and party. 

### `Family.ordinal`

 Assigns each motif parameter entry its histogram index, shared by the lookup tables of
  every handler in the family. 

### `Family.base`

 Expression whose value is the first private word of the call descriptor for the selected
  handler. 

### `Family.field`

 Expression that computes the word to publish for each named descriptor argument of the
  selected handler. 

### `Family.source`

 Chooses a DFS, saved bootstrap or role-shared register for each of the descriptor
  writer's five public operands and its state operand. 

### `fields`

 Descriptor field expressions in physical slot order. The layout's inverse argument
numbering recovers the named argument stored at each offset. 

### `image`

 Vertex code segment for one lowered map call table, with the family's parameter ordinals
embedded among its lookup constants. 

### `WriterPC`

 Local instruction addresses for evaluating one handler's field and base expressions,
installing its descriptor pointer and storing the fields. 

### `Address`

 Instruction addresses of the whole family. Each selects a grid point and party, then either
a descriptor writer instruction or a row of the lowered map. 

### `VMCount`

 Size of the register bank needed to evaluate all descriptor field expressions and the base
expression for one handler. 

### `Local`

 Registers private to one handler, grouped into the expression evaluator, two
descriptor-writing temporaries, and the map's source registers plus two lowering
temporaries. 

### `PrivateReg`

 A private register identified by its grid-point and party handler and its slot in that
handler's local bank. 

### `inputs`

 Resolves one of the writer's six input operands to the physical DFS, saved or shared
register chosen by the handler's source assignment. 

### `localReg`

 Embeds the selected handler's local register slots into the host machine through the
allocation of the family's private registers. 

### `vm`

 Physical registers used by the selected handler's expression evaluator to compute the
descriptor fields and pointer. 

### `mapReg`

 Physical register embedding for one lowered map, including its source map registers and the
two scratch registers used to materialize constants. 

### `aux`

 The descriptor publisher returns the pointer in exactly the source map's pointer
register. Its two other temporaries belong to the writer. 

### `writerPC`

 Host program counter of an instruction in the selected handler's descriptor writer. 

### `mapPC`

 Host program counter of a row in the selected handler's lowered map segment. 

### `placement`

 Installs one lowered map at its assigned instruction and register locations, routing
success to the shared continuation and rejection to its local reject instruction. 

### `target`

 The dynamically selected target starts with the actual descriptor writer. 

### `text`

 The first part of each grid/party bank is the raw argument writer, followed
by the actual inlined eleven-port map code. 

### `Apart`

 The role's shared inputs and the caller's saved registers lie outside the bank
in which the handlers publish and evaluate their descriptors. 

### `vm_aux`

 All writer scratch slots are disjoint from the map pointer and writer cursors. 

### `links`

 Per-handler links extracted from the actual rows of the complete image. 

### `locations`

 Finite numbering of all descriptor writer instructions and lowered map rows, used to
address the family as one vertex segment. 

### `registers`

 Numbers the role's shared registers together with every handler's private slots for
allocation in the vertex segment's register bank. 

### `segment`

 A native vertex subsegment with a designated grid/party entry. In a larger
role, the caller can use the other targets of the same installed table. 

### `segment_rows`

 The surrounding role can recover every installed handler row from the
ordinary vertex segment interface at its finite program-counter numbering. 

### `different_registers`

 All registers of a different grid/party handler survive the selected handler. 
