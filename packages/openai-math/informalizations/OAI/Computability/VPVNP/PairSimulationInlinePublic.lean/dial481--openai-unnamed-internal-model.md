---
{
  "module": "OAI/Computability/VPVNP/PairSimulationInlinePublic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationInlinePublic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationInlinePublic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lowering a static public bank to a fixed native instruction table

The enclosing machine supplies only code labels and register positions. Its public
words are available to other routines. Each source instruction occupies an equally long
block consisting of a local constant synthesis followed by the relocated operation.
The final operation has the source's branches, probes and halt behavior.


### `capacity`

 A fixed bound covering every source immediate and every fixed public word. 

### `Placement`

 Native locations of the relocated code, source registers, and the two scratch words. 

### `Placement.pc`

 Host code address for each source instruction and offset in its block of `C + 3`
  instructions. 

### `Placement.reg`

 Embed the source registers into the host register file for the relocated instruction. 

### `Placement.unit`

 Scratch register initialized to one for the increments used to synthesize a fixed
  operand. 

### `Placement.acc`

 Scratch register that accumulates the fixed operand before the relocated instruction
  runs. 

### `entry`

 Host address at offset zero of the block for a given source instruction. 

### `privateReg`

 A host register reserved for the enclosing program, distinct from both scratch registers
and all relocated source registers. 

### `operand`

 The word prepared by this source row. 

### `body`

 Only the two instructions with immediate data are replaced by a copy from the
accumulator. All other operands and control transfers are directly relocated. 

### `row`

 Code for one uniform block in a host with any public-word ABI. 

### `canonical`

 Consecutive code blocks and a trailing scratch register pair. 

### `compiled`

 Closed width-two template. Neither its labels nor its code depends on the word width. 

### `ContainsAt`

 The complete block is present at this source label. 

### `Agrees`

 Observable configuration data. The enclosing code can reserve unrelated registers. 

### `Related`

 The host is at the entry of the current source instruction's block, agrees on source
registers, private memory and persistent state, and matches the given frame on enclosing
registers. 

### `ActionsMatch`

 A matching native action has the same observable event and relates all continuations. 

### `simulate_row`

 Exact one-row simulation, from an arbitrary source and host configuration. 

### `padded`

 Nonterminal traces insert the constant block's local ticks before each source event. 
