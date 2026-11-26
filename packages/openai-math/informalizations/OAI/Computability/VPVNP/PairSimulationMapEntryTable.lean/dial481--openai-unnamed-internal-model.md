---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapEntryTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntryTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntryTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete private instruction table for a grouped motif entry

The selector scan, row driver, full-width comparison and histogram loop share
one program counter space and one fixed public-word bank. The decoder and the
row dispatcher share selector ordinals. The expected widths and histogram
registers occupy distinct positions throughout both earlier phases.


### `Register`

 Logical registers of the grouped map interpreter, comprising selector registers, row-bank
registers, one expected width per supply edge, and six histogram registers. 

### `PublicPort`

 Public-word indices for the selector codes and the row bank's selector ordinals, widths,
matrix keys, and parameter ordinals. 

### `Allocation`

 The allocation can be embedded in a larger vertex program. 

### `Allocation.reg`

 Inject the grouped interpreter's logical register slots into the machine register file. 

### `Allocation.pub`

 Inject the selector-code and matrix-table ports into the enclosing machine's public-word
  bank. 

### `Allocation.edgeOrder`

 Fixed enumeration of the supply edges used for the port directory and the final width
  checks. 

### `allocation`

 One concrete finite allocation before the number of copies, word width, or input. 

### `selectors`

 Selector scanner and decoder allocation within the entry table. The decoder's output-name
ports are shared with the row bank's dispatch ordinals. 

### `bank`

 Restrict the entry table's registers and public ports to the selected-row driver and matrix
bank. 

### `expected`

 Assign one separate physical register per supply edge for its expected total payload width. 

### `histReg`

 Place the six private histogram-loop registers in the grouped interpreter's register file. 

### `guardTemp`

 Use the row bank's temporary register as the scratch word for the final width guard. 

### `guard`

 Compiled checks comparing each supply edge's accumulated offset with its expected payload
width, in the allocation's edge order. 

### `SelectorBody`

 Addresses of the selector scan and decoder instructions installed in the entry table, with
their exits supplied by the enclosing interpreter. 

### `BankBody`

 Addresses of the row driver and matrix lookup bodies installed in the entry table, with the
driver continuations supplied by the enclosing interpreter. 

### `Address`

 Addresses of the selector phase, row bank, width checks, seven histogram instructions, and
the success and rejection exits. 

### `exitPC`

 Address of the grouped map's normal continuation when `bad` is false or its common
rejecting exit when `bad` is true. 

### `histPC`

 Address in the complete entry table of histogram instruction `i`. 

### `guardPC`

 Relocate a width-guard label to its numbered instruction in the complete entry table. 

### `bankPlace`

 Redirect the row driver's successful exit into the first guard instruction. 

### `selectorPlace`

 Redirect a successful selector scan into the driver's first test. 

### `selector`

 The relocated selector program whose successful decoder enters row dispatch and whose
failure reaches the entry table's common rejecting exit. 

### `program`

 The concrete four phases in the same address space. 

### `text`

 The complete code, including a common reject instruction and a normal exit. 

### `installed`

 Only the successful continuation can be replaced by an enclosing procedure. 

### `linked`

 The actual instructions discharge the common evaluator's control hypotheses. 

### `separate`

 Width targets and histogram registers survive both earlier stages. 

### `words`

 The public selector codes precede the public row bank. Every decoded ordinal
uses exactly the port tested by row dispatch. 

### `install`

 Install public values at their fixed addresses inside an enclosing bank. 

### `locations`

 Bijection numbering every symbolic instruction address of the complete grouped map entry. 

### `template`

 Numerical fixed finite table; all relative and absolute targets above are its own PCs. 

### `template_exits`

 Both final exits are genuine terminal instructions of the standalone template. 

### `machine`

 The fixed template instantiated with its actual selector, width and matrix words. 
