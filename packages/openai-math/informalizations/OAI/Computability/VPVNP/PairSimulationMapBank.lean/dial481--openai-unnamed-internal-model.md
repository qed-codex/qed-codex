---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing the row driver and every selector's matrix in one finite table

For a fixed block, grid point and party, all selectors share the query, cursor,
and result registers. Each selector has its own width and matrix ports. The
row returns to the driver's label store, and all failed paths use the common
rejecting exit. The enclosing program can supply the final width-check address.


### `Register`

 Register slots shared across all selector rows of one map bank. Six belong to the outer
driver, and the endpoint and group slots include the label register returned to that
driver. 

### `PublicPort`

 The selector's dispatch ordinal and the width and matrix words for that row. 

### `Allocation`

 Shared register and public-port positions inside an enclosing machine. 

### `Allocation.register`

 Inject the row bank's driver and field slots into the enclosing machine's register file. 

### `Allocation.port`

 Assign distinct public-word positions to the selector ordinals and the widths, keys, and
  parameter names of each selector's matrix. 

### `allocation`

 These finite counts always suffice for this fixed motif. 

### `rowReg`

 Place the endpoint, group, and scratch registers used by the selected matrix row in the
machine register file. 

### `driverReg`

 The driver's last register is precisely the shared row result. 

### `selectorPort`

 Public port holding the ordinal against which the driver compares the loaded selector. 

### `widthPort`

 Public port for the selected base demand width or supply payload width of group `g`. 

### `keyPort`

 Public port holding the expected digit of field `f` in matrix row `y` for selector `s`. 

### `namePort`

 Public port holding the parameter ordinal returned when the lookup matches row `y` for
selector `s`. 

### `words`

 Local public values can be installed without constraining any other public ports. 

### `install`

 Install the complete fixed public table while preserving enclosing ports. 

### `public_spec`

 Code and public words determine the exact comparison and row ordinal at each selector. 

### `RowBody`

 Only body labels are allocated for a row. Its exit belongs to the driver. 

### `Address`

 The two exits designate the following width comparison and rejection. 

### `rowPlace`

 Place a selector's row instructions in the bank, redirect its successful return to the
driver's label store, and send its failed lookup to the shared rejecting exit. 

### `sites`

 Program counters for field reads, matrix lookup, and offset advancement of one selector's
row in the combined bank. 

### `driver`

 Assemble the driver that walks the private selector array, dispatches to the chosen row,
stores its returned label, and enters the width check after the last copy. 

### `registerLayout`

 The row result register coincides with the driver's label register, while
all six controller operands occupy separate locations. 

### `text`

 Fixed text relocated to the encompassing address space. Only the body instructions
are used when linking it into a larger evaluation pipeline. 

### `inBody`

 Test whether an address belongs to the driver or a selected row body. The two exits have
separate addresses for use by an enclosing program. 

### `linked`

 Every selector returns to the shared label store. All its rejecting paths target
the driver's common bad exit. 

### `locations`

 A fixed numbering of the combined address set. 

### `template`

 Standalone finite implementation for all selected rows together with their driver. 

### `template_linked`

 All code links of the entire driver and every decoded row hold in the same machine
for every word width and public input. 

### `machine`

 Install all row widths, all selector ordinals and all fixed matrix words in
the same standalone instruction table. 

### `native`

 The actual finite driver and row machine writes the ordered parameter ordinals
of every copy and reaches the final-width checker with the full offset vector. 
