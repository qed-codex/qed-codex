---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A native instruction table for the shrinking hidden-field pass

Four public operands identify the packed owner, private slot base and stride,
and old-level header. The finite table first loads these operands, reads the
live published header, scans the owner's fields and enters an accepting halt.
Only the binary compiler for the two stage constants depends on the stage.


### `lines`

 The compiled register-setup rows for the hidden scan's header recipe at selector width `s`
and owner row stride `t`. 

### `aux`

 Register count of the compiled header recipe, including its ten output registers and its
expression-evaluation workspace. 

### `Label`

 Labels for the four public operand loads, the compiled header rows, the field-scan stages,
and the accepting halt. 

### `Reg`

 Physical register indices for the scan's 22 registers, the header compiler's auxiliary
bank, and the six source registers. 

### `P`

 Number of program counters in the reset-entry hidden-field instruction table. 

### `R`

 Number of physical registers allocated to the reset-entry hidden-field program. 

### `label`

 Encode a symbolic instruction label as a program counter using the finite enumeration of
table labels. 

### `boot`

 Program counter for the initial load of the indexed public operand. 

### `loop`

 Program counter of a field-scan stage inside the reset-entry table. 

### `done`

 Program counter of the accepting instruction reached when the owner's remaining field count
is zero. 

### `setup`

 Program counter for header instruction number `i`. An index past the last header
instruction enters the first scan control. 

### `regs`

 Embed the scan's 22 logical registers in the physical register bank of the table. 

### `inputs`

 Physical register for each of the header recipe's six protected source positions. 

### `vm`

 Embed the header compiler's registers so its ten outputs land in their designated scan
registers and its other registers use the auxiliary bank. 

### `source`

 Assign the four public operand loads to source positions 0, 1, 2, and 5, with the old-level
header address in position 5. 

### `afterBoot`

 Successor of a public operand load. The first three loads advance to the next load, and the
fourth enters header setup. 

### `template`

 Reset-entry instruction template that loads four public operands, executes the compiled
header recipe, scans the owner's fields, and accepts at the end. 
