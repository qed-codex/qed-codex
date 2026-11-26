---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordGreedyInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordGreedyInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Emitting greedy operand rows from the level's slot tables

Outgoing and incoming mate arrays are indexed by `vertex * degree + port`.
Each cell contains the packed vertex and port at the opposite incidence.
Displacements use the outgoing slot index. Labels use the vertex index.
The row initializer reads exactly one mate, obtains the neighbor by division,
and writes the one or four operand addresses used by the greedy visitor.

Registers 0–7 carry the vertex index, destination cursor, degree, outgoing
and incoming table bases, displacement base, assignment base and zero cell.
The finite public table holds the local slot numbers and is common to all
vertices and all compression levels of the same degree.


### `PortTables`

 The degree and external table addresses used to initialize greedy operand rows from a
level's directed slots. 

### `PortTables.degree`

 The vertex degree, used to pack and unpack a vertex and local port as one word. 

### `PortTables.outgoing`

 Base address of the array mapping outgoing ports to their incoming mates. 

### `PortTables.incoming`

 Base address of the inverse array mapping incoming ports to their outgoing mates. 

### `PortTables.displacements`

 Base address of the displacement array indexed by outgoing ports. 

### `PortTables.labels`

 Base address of the greedy assignment cells, one per vertex. 

### `PortTables.zero`

 Address of the cell supplying zero to a padded tag comparison. 

### `vertexNumber`

 Encode a vertex's ordinal in the supplied vertex order as a machine word. 

### `portNumber`

 Encode a vertex and port as the vertex ordinal times the degree plus the local port number. 

### `PortTables.Represents`

 The level's two directed incidence arrays, including inverse slot numbers. 

### `PortTables.addresses`

 The same address convention in the operand-record reader. 

### `slotNumbers`

 The public constant at index `i` is the word encoding its ordinal, from zero through the
degree. 

### `Operand`

 Operand address formulas sharing the single mate lookup in one row. 

### `tagOperands`

 List the four operands for a tag exclusion, padding a local test with two zero operands or
including the neighbor's label for a two-end test. 

### `loadMate`

 Compile the shared endpoint and directed displacement index. 

### `emitOperand`

 Emit the computed operand address at the row cursor and advance the cursor by one word. 

### `initRow`

 Initialize one operand row by reading the selected port's mate and emitting the requested
operand addresses in order. 

### `RowInput`

 Register contract for starting a row, specifying its vertex, destination cursor, degree,
and five table addresses. 

### `arcOf`

 Recover the outgoing arc of an incidence, using the inverse slot matching when the
incidence is incoming. 

### `operandAddress`

 Resolve a symbolic greedy operand to its address in the zero, displacement, or label table. 

### `writeRow`

 External writes of the packed output words, starting at the supplied cursor. 

### `initRow_trace`

 The machine reads one directed mate and writes exactly the specified operand
row. No later lookup in this row depends on the overwritten external cells. 

### `writeRow_outside`

 Sequential writes preserve the complete external memory outside the row. 

### `initRow_native`

 Execution at the normal entry of the compiled word program with the level's
register arguments. Its event log installs the reader's operand words in external
memory and leaves every word outside their address interval unchanged. 

### `PortTables.Free`

 One output interval is disjoint from both directed mate arrays. 

### `OperandRows`

 The ordered incidence and operand lists used to initialize one vertex's greedy record. 

### `rowWords`

 Flatten the resolved operand addresses of all rows for a vertex in their emission order. 

### `initRows`

 Concatenate the native row initializers in the order of the supplied incidence rows. 

### `initRows_native`

 A single fixed instruction table emits every forbidden pointer for a vertex,
retaining the current external memory between rows. 

### `colorOperandRows`

 The two vertex programs use the exact exclusion order of the greedy reader. 

### `tagOperandRows`

 Enumerate the four-operand rows for all tag exclusions of a degree-`d` vertex. 
