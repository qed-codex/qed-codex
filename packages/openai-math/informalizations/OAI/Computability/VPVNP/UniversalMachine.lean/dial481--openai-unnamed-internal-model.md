---
{
  "module": "OAI/Computability/VPVNP/UniversalMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/UniversalMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The coefficient machine of “VP and VNP differ over every field”, §1.1

We fix two two-way tapes over the alphabet blank, zero, one (codes 0, 1, 2). States 0 and 1
halt with rejection and acceptance. The running states start at 2. Every transition writes
one symbol on each tape, moves each head by at most one cell and enters its target state.

The prefix is the table's bit length in unary (`1^k 0`) followed by exactly `k` bits. Inside
that table each natural-number field is also unary. The empty table has no running states and
starts in the accepting state. Otherwise the first field is the number of running states minus
one. The remaining fields give all nine rows for each running state, ordered by state, first
head and second head. Each row is a branch count (0, 1 or 2) followed by that many records.
A record lists target, first symbol, first move, second symbol, second move. Moves 0, 1 and 2
mean stay, left and right. All fields are literal. Both tapes start with the head at cell 0,
and the first tape carries the complete input, including the program prefix.


### `Symbol`

 The tape alphabet encodes blank, binary zero and binary one as 0, 1 and 2. 

### `Word`

 A finite binary input, including its literal program prefix. 

### `Instruction`

 `target = 0` rejects, `target = 1` accepts, and `target = 2 + i` enters running state `i`. 

### `Instruction.target`

 The state entered after the writes and head movements. 

### `Instruction.firstSymbol`

 Symbol written under the first head. 

### `Instruction.firstMove`

 First-head movement, in the order stay, left, right. 

### `Instruction.secondSymbol`

 Symbol written under the second head. 

### `Instruction.secondMove`

 Second-head movement, in the order stay, left, right. 

### `Branches`

 Each branch occupies its own slot, even if two transitions are identical. 

### `Program`

 A finite nondeterministic table with a row for each running state and symbol pair. 

### `Program.extra`

 Number of states besides the two halting states. 

### `Program.rows`

 Transition lists ordered by state, first-head symbol, then second-head symbol. 

### `Config`

 The state and both head-centered tapes at one instant of a computation. 

### `Config.state`

 The current running or halting state. 

### `Config.firstTape`

 The tape that initially holds the input word. 

### `Config.secondTape`

 The initially blank work tape. 

### `emptyProgram`

 The empty table is the machine that starts already halted in acceptance. 

### `initial`

 Start at the first running state with the complete input on the first tape.
The empty table starts in the accepting state. 

### `branches`

 Look up the transition slots for the current running state and the two scanned symbols. 

### `updateTape`

 Write at the head and then carry out its specified movement. 

### `advance`

 Apply one chosen transition to both tapes and enter its target state. 

### `paths`

 Accepting leaves within `fuel` transitions of the encoded machine, including time zero. 

### `unary`

 The unary field for a number, including the terminating zero. 

### `readFields`

 Read all unary fields in the table. A last field with no terminator fails. 

### `decode`

 Decode just the program prefix. The payload is unrestricted. 

### `instructionFields`

 The five integer fields that encode a single instruction. 

### `branchFields`

 Encode the number of branches followed by their instructions in slot order. 

### `tableBits`

 Serialize the table with no implicit rows or unbounded instructions. 

### `programPrefix`

 A literal prefix, independent of the subsequent payload. 

### `decode_programPrefix`

 Decoding the self-delimiting prefix recovers the exact machine, on every payload. 

### `clockExponent`

 The exponent `K_*` from §1.1. 

### `acceptingCount`

 The integer coefficient `U_n(x)` of equation (1.1), prior to casting to a field. 
