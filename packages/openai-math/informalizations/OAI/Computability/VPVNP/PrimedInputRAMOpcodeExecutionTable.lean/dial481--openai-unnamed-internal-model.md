---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite table for the two-pass input RAM

Four private instructions compare the persistent cursor with twice the public rectangle
size. At the terminal cursor they jump to accept. At each data cursor they jump into the
compiled input block, whose return instruction supplies the next cursor from register 29.


### `body`

 Code for one data call. It loads parameters, decodes the cursor, resolves the incident port
when needed, and performs the scheduled action. 

### `pcCount`

 Number of instruction addresses in the input table, including its seven front instructions
and the data-call body. 

### `bodyLabel`

 Translate a data-call instruction label into its table address after the seven front
instructions. 

### `returnPC`

 Instruction address that returns register 29 as the next persistent cursor. 

### `badPC`

 Address of the input table's rejection instruction. 

### `inputTable`

 The same opcode table works for all parameter lengths and word widths. 

### `prefixEvents`

 The four private ticks spent comparing the persistent cursor with the end of the two
passes. 

### `prefixRegs`

 Registers after the four entry instructions. Registers 4, 5 and 30 hold the cursor, the
rectangle size and twice that size. 

### `execute_prologue`

 Execute the four private prologue opcodes, preserving memory and branch choices. 

### `execute_terminal`

 At the terminal cursor the physical RAM accepts after four private ticks. 

### `execute_data`

 The linked body may start with the prologue's live registers. It returns register 29
after exactly the structured trace, with the four control ticks included in the report. 
