---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading a descriptor frame into native registers

The compressor's component templates have finite parameter banks. At call
entry a fixed prelude reads the bank from consecutive external words. The
relocated body executes each original public-word instruction as a register
copy, so repeated accesses to a parameter inside a long private computation
require no additional probes. The bank is a snapshot taken before the body.


### `PCs`

 Program-counter count for the frame-loading prelude and relocated body, with four
instructions per parameter. 

### `Regs`

 Register count for the framed body, its parameter cache, and the temporary frame-address
register. 

### `labels`

 Four prelude labels per frame word and one label for each original instruction. 

### `prePC`

 Program counter for a specified parameter and one of its four loading instructions. 

### `bodyPC`

 Relocated program counter of an original body instruction, following the frame-loading
prelude. 

### `ordinary`

 Embed a body register into the leading bank of the framed machine. 

### `cacheReg`

 Cache register holding the selected public parameter throughout the body execution. 

### `addressReg`

 Temporary register used to address external parameter words during frame loading. 

### `bodyCode`

 Public-word instructions are the only instructions whose operation
changes. Component destinations never address a cached parameter. 

### `bodyCode_wordWork`

 Reading a cached parameter costs the same private word work as the
original public-word access; all other body instructions keep their charge. 

### `nextPC`

 Enter the next parameter's loading sequence, or the body entry once the entire frame is
cached. 

### `compile`

 A single fixed compiled template whose sole public word is the
address of the descriptor frame. An empty bank needs no prelude. 

### `machine`

 Instantiate the compiled framed template with the external frame base as its public
operand. 

### `load_wordWork`

 The private dispatch charges of the four prelude instructions total
seventeen elementary word operations per parameter. 

### `execute_body`

 Within the relocated body, every finite-fuel execution is exactly the
original execution with its cached public data. This includes arbitrary
external writes (even to the frame), adaptive reads, and all choices. 

### `data`

 The source machine's public bank is the external frame at call entry. 

### `loadEvents`

 Chronological trace of the descriptor-frame loads starting at offset j. 

### `frame_cost`

 Each frame parameter adds one probe and three private ticks. The
continuation's report retains every branch bit and memory update. 

### `execute_frame`

 Exact native execution from fresh call entry for every component fuel
and branch stream. The original persistent input is passed through the
prelude. Subsequent calls take a new snapshot of their current frame. 

### `execute_cap`

 At every caller fuel cap, including a cap too small to finish the
prelude, the original component has exactly the remaining fuel. 

### `segment`

 The source execution for a sequence of calls fetches the public bank
from the current external memory at each boundary. Only the original
component's writes change the bank for later calls. 

### `runSegment_frame`

 Pathwise equality through successive calls, including frames overwritten
by earlier calls and streams that propose extra choices after a halt. 
