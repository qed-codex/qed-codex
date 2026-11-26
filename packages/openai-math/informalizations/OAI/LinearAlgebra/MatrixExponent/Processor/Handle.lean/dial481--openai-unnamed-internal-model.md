---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/Handle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Handle.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Handle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A worker as a sum over local bits and independent class kernels 

### `site_eq`

 After the relay check, sum over just the incident bit symbols. The
packet batch includes the private sums for all incident class symbols. 


# Fixed station data cells

Every potential cell has the same address at all workers. At the end
of the array, reserve the full exterior color-slice capacity, so a
worker with fewer exterior ports simply leaves more cells unused.


### `read`

 Resolve a template address before applying the activation mask. 

 # Decoding template addresses into the common cell format 

### `lookup`

 Unused bank addresses have no corresponding input cell. 

 # Resolving the three kinds of bank input cells 

 # Reading the fixed array of packet inputs at a selected class 

 # Wiring the entire batch of packet-class kernels 

 # Space for padded template addresses 

 # Bounds shared by the worker circuits 

### `Window`

 The workspace has `2^W` lanes, each containing a `W`-bit register. 

 # Testing activation and fetching a slot in the worker template 

 # Computing every input bit of the station bank 

 # Cost of the packet contribution at a processor 

 # An exact scalar network for the programmed station bank 


# Assembling one fixed-cut worker

The sum over the fixed tape of guesses is exact. The private check
forces inactive cells to zero and enforces the delivered bits. The
public relay check needs only the processor inputs.


### `handles`

 One scalar circuit suffices for every worker, script and feasible
report at the prescribed cut. 
