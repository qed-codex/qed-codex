---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing a live evaluator transition

The first scheduled call checks the old state, reads the two heads of a
running configuration, chooses a row slot, and checks the proposed output
state. It writes the selected target, first write and move, and second write
and move to five consecutive scratch words. An accepting source carries
state one and four zeros without a choice.


### `Code`

 The transition-preparation flow with 32 registers and four public configuration operands. 

### `firstAddress`

 The head of the first tape follows the state word and the left half-window. 

### `secondAddress`

 The second tape starts one complete window after the first. 

### `firstHead`

 Read the symbol under the old first-tape head from its external configuration address. 

### `secondHead`

 Read the symbol under the old second-tape head from its external configuration address. 

### `rowNumber`

 The zero-based row number computed in machine-word arithmetic. 

### `rowRegs`

 The register bank after reading both heads and computing the instruction row indexed by the
old state and the two symbols. 

### `rowTrace`

 The two external head reads and arithmetic ticks used to locate the running configuration's
dispatch row. 

### `carryRegs`

 Set the instruction registers to the accepting carry transition, with target one and zero
tape writes and motions. 

### `scratchAddress`

 The physical scratch addresses visited in order; all increments are native word additions. 

### `scratchMemory`

 The exact external memory after the five consecutive writes. 

### `publishRegs`

 The register bank at the end of publishing an instruction, with the address cursor on its
fifth scratch word. 

### `publishTrace`

 The destination state read and five scratch writes that publish the checked target, tape
symbols, and motions. 

### `boundsRegs`

 Install the highest permitted control-state number in the register used for the state bound
check. 

### `prepare`

 Register 16 is the source state, 11 the window radius, 22 the window length,
23 and 24 the input and output state-word addresses, and 25 the scratch base.
Registers 0 through 3 carry their respective constants. 

### `prepare_loopFree`

 Only fixed straight-line blocks and the machine's finite dispatch occur. 

### `tableRow`

 The fixed program row addressed by the two actual head reads. 

### `selectedRegs`

 The register bank after locating the row and installing the chosen instruction's five
fields. 

### `Selected`

 The two successful possibilities before checking and publishing the proposed target. 

### `prepareTrace`

 The complete event stream for a successful preparing call. 

### `prepare_exec_iff`

 Characterization for *all* raw source words, proposed outputs and choice streams.
A successful run validates the source-state range, the chosen slot, the nonzero target
and the matching output word before performing precisely the five scratch writes. 

### `prepare_accept_exec`

 A previously accepting state is carried deterministically after checking its proposed successor. 

### `prepare_running_exec`

 An occupied slot of a running source executes with its actual head reads and exact target. 

### `prepare_slot_bits`

 The exact bit stream for a successful running slot, including the genuine bit
distinguishing the two slots even when both instructions are identical. 

### `prepare_cost`

 All successful preparing calls make six probes for a carried accepting state
and eight probes for a running source. Only an occupied two-slot row consumes a bit. 

### `firstAddress_val`

 If the first head address fits, its machine word is the ordinary
input base plus the state-word offset and the window radius. 

### `secondAddress_val`

 When the second address fits, the second head lies exactly one window
length after the first head. 

### `rowNumber_val`

 The machine computes the natural row index whenever the source state is
a running state and the final index fits. Intermediate products may wrap. 

### `scratchAddress_val`

 Unit increments give the ordinary consecutive scratch address whenever it fits. 

### `scratchMemory_at`

 At each allocated scratch offset the caller reads the corresponding instruction register. 

### `scratchMemory_outside`

 Publishing leaves every address outside the five-word scratch interval intact. 

### `Selected.frame`

 Selecting a transition preserves the four constants, window coordinates, source state,
and the registers above the row-calculation workspace. 

### `publishRegs_other`

 Publication uses only register 10 as its scratch-address cursor. 
