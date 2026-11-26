---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BlockSearchLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete nested control of the universal-block basis search

The matrix-product command is a fixed finite subroutine supplied by
`MatrixPairProgram`. All tuple arrays and split positions are runtime data.
The three loops scan tables, splits, and coefficients, respectively.


### `zeroFrom`

 Copying preserves the vector used by the second matrix product. 

### `tailZero`

 Skip the saved split number of complete coefficient frames, then test
the remaining scalar words. Both the split and full coefficients survive. 

### `coefficientCallback`

 The supplied matrix command computes y=Cx and z=My on fixed work ports.
The rest of this callback uses only concrete copying and Boolean programs. 

### `dimensionCallback`

 The current split is copied into persistent output metadata before its
universal coefficient scan. It remains there when the scan succeeds. 

### `tableCallback`

 The current table is installed in forward frame order and retained while
the complete split enumeration is scanned. 

### `program`

 A finite instruction table whose only parameter is another fixed finite
instruction table. It has no dimension- or prime-dependent control labels. 

### `Context`

 Persistent physical inputs of the two matrix-product calls. 

### `WorkReady`

 All work stacks needed by one coefficient test are empty at its boundary. 

### `CoefficientContract`

 The arithmetic callback must frame both parent iterators. This contract
is an actual execution obligation for the concrete coefficient code above. 

### `coefficientScan_eval`

 A complete coefficient scan frames both enclosing loops, including their
unread serialized tails. The copied working enumeration is empty on exit. 
