---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The live group's native header program

The same table parses every group and input length. The public-data function
uses the chain and field sizes and the scratch base. The group number, advice,
mode, cut lengths, field offsets and payloads come from word-memory probes.


### `StageTemplate`

 Uniform scratch-register and local public-operand capacities of a stage. 

### `includeFin`

 Embed a smaller register or operand index into a larger bank at the same numerical
position. 

### `entry`

 Widen a native component template to the common header stage interface of 50 registers and
17 public operands. 

### `widthSlots`

 The fixed public operand assignment for the scalar cut-width and flag calculations. 

### `descriptorSlots`

 The nine public slots assigned to the descriptor worker's width, flags, dimensions, and
output cells. 

### `scanSlots`

 The four public slots assigned to the field scan's first cursor, source offset,
destination, and runtime count. 

### `stageTemplate`

 Each stage either accepts after one microcall or is wrapped with a
public-capacity test. In particular, a zero-capacity scan makes one terminating call. 

### `publicRow`

 One row of public operands. The last operand of every bounded stage
holds the capacity at the position expected by its own wrapper. 

### `StageId`

 An index into the fixed list of native live-header stages. 

### `PublicIndex`

 An index in the flat bank containing seventeen public words per header stage. 

### `stage`

 Retrieve the scheduled header operation at a given stage index. 

### `rowEmbedding`

 Embed a local operand position in the seventeen-word public row of the selected stage. 

### `component`

 Relocate all public operands into their respective fixed rows. 

### `next`

 Advance to the following header stage, returning no successor at the end of the list. 

### `program`

 A standalone executable native template, which accepts only after the
last padding scan reaches its limit. Inner stage handoffs reset the cursor. 

### `publicData`

 Exact finite operand vector used by the linked header program. `base`
also serves as the inner linker's tag address, initially in zero memory. 

### `rowData`

 Public operands before relocation into the combined header table. 

### `bank`

 Read the flattened public operand by recovering its stage row and offset and evaluating the
corresponding row data. 

### `component_start`

 A call in a linked operand bank executes the original stage with its
own prescribed public row. The two relocations add no work or branch bits. 
