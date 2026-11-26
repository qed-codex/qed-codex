---
{
  "module": "OAI/Computability/VPVNP/LiveExponentRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native burst RAM digit calls for the live exponent update

The persistent word indexes the flattened exponent array. Public words
designate the incoming bit array, outgoing bit array, increment array,
digit width and total digit count, respectively. The increment array
initially holds the nominated grammar counts followed by the gadget
counts. Its entry for a label doubles as that label's carry. Each call
uses four external probes regardless of the length of an exponent.


### `DigitOp`

 A native digit-update operation over sixteen registers and five public operands. 

### `digitOps`

 Register zero is the digit cursor and register one receives its successor.
Registers 2, 3, 4 hold incoming, outgoing and carry addresses. Registers 5, 6, 7
hold their loaded values. Registers 8 and 9 hold the total and next carry.
The last bit of each label additionally requires the carry to vanish. 

### `incomingAddress`

 Address of the incoming cut bit at the flattened digit cursor. 

### `outgoingAddress`

 Address of the proposed outgoing cut bit at the flattened digit cursor. 

### `carryAddress`

 Address of the current label's increment word, used as the carry during its digit scan. 

### `digitEvents`

 Exact event stream of a successful digit block, including its three
memory reads and its single write. 

### `digitTemplate`

 The extra entry test ends the stage at cursor `t * Z`. Each prior call
executes one copy of the same digit block and returns cursor plus one. 

### `digitReport`

 Native report of one successful call, including its entry instructions. 

### `execute_done`

 The completed stage accepts with exactly four entry ticks and no choices. 

### `DigitTest`

 Ordinary integer addition, phrased using the natural values of the cells
read by one call. The final bit of each label also checks for overflow. 

### `execute_digit_iff`

 Every well-sized nonterminal call has exactly the branch stream and report
specified by the arithmetic test. The fuel bound counts the final return. 

### `data_result`

 Every successful nonterminal call consumes an empty choice stream and
returns the next cursor, including on arbitrary initial memory. 
