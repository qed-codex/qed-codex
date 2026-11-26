---
{
  "module": "OAI/Computability/VPVNP/RAMTapeAddressLogControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite bit-stack control for a private RAM write log

Parallel streams store the newest-first addresses, values, and one occupancy
bit per entry. The query stack itself sets the word width. Even width zero
therefore permits distinct entries. Bits visited during lookup are saved and
restored before return.


### `Port`

 Stack labels for a private write-log lookup, including the address, result, three log
streams, and five restoration stacks. 

### `Bank`

 Contents of the lookup stacks, with parallel streams for addresses, written values, and
entry marks. 

### `Bank.q`

 Bits of the query address. Its length determines how many bits to read per log word. 

### `Bank.o`

 Output stack onto which the lookup restores the selected value. 

### `Bank.ks`

 Address words of the private write log in newest-first order. 

### `Bank.vs`

 Written values in the same entry order as the address stream. 

### `Bank.marks`

 One occupancy mark per log entry, including entries with zero-width words. 

### `Bank.sk`

 Address bits saved in reverse order during the lookup. 

### `Bank.sv`

 Written-value bits saved for restoration after the scan. 

### `Bank.sq`

 Query bits temporarily removed while comparing an address. 

### `Bank.sm`

 Occupancy marks removed from entries already visited. 

### `Bank.so`

 Bits of the selected value staged for transfer to the output. 

### `Bank.stacks`

 Select the bit stack of a lookup bank by its port. 

### `Bank.set`

 Replace the bit stack at one lookup port. 

### `keys`

 Store every key in increasing order of bit significance. 

### `values`

 Concatenate the bit encodings of the written values in log order. 

### `bank`

 Initialize lookup with the query, output tail, encoded write log, one mark per entry, and
empty restoration stacks. 

### `Rewind`

 The common rewind loop specializes to each saved stream. 

### `State`

 Finite lookup control for comparing keys, selecting a value or zero, and restoring the
scanned stacks. 

### `Rewind.src`

 Scratch port holding the reversed bits for the current restoration pass. 

### `Rewind.dst`

 Port that receives the bits restored in the current pass. 

### `Rewind.next`

 Advance through restoration of the query, keys, values, occupancy marks, and result, then
finish. 

### `loadCode`

 A load stops at the first matching full word. The key and value scans
both have width determined by the query, independently of its numeric value. 

### `stepPush`

 Elementary instruction proofs can be stated directly in terms of a bank. 
