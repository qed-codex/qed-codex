---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rounds/Sweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Sweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rounds/Sweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Joining stages with their own arity and table budgets 

 # Local concentration with arbitrary integral scales and bundles 

### `LocalLaw.with_padding`

 Apply concentration after zero-padding the actual ordered bundles.
The caller supplies a positive loopless diagram and its host, with no
condition on the divisibility of the old bundle widths. 

 # Fitting the charged stations into the terminal evaluator 


# Accounting for a sequence of encoded rounds

Each round carries its own finite dictionary. Their union suffices for
the entire sequence, and the network cost is the sum of the round costs.
The initialization and terminal contraction are paid separately.


### `sequence`

 Compose a nonempty sequence, with one arity ceiling for the whole
sequence. No copy of the intermediate wires is charged at composition. 

### `Layer.install_sequence`

 Install the rounds between initialization and the terminal evaluator,
keeping the original exact tensor power and accounting for every label. 


# Iteration of bounded round constructions

Each step may choose the next representation and its tables from the
current representation. This packages those choices into one
installation, with the cost and vocabulary bounded by the given sums.



# Separating the cost of addresses, controls and payloads

The long-address cost is charged per host. Retaining enough blocks at
the end pays for this cost from the occurrence budget. Short records
may use a fixed power of the grouping size, with a polylogarithmic
factor. The exponent on the terminal payload and the exterior can be
arbitrarily small.


### `Levels.expense`

 Raw cost before absorbing fixed constants and logarithmic factors. 


# Absorbing the implementation overhead

The logarithmic slack pays for fixed factors and powers of the logarithm
of the height. The vocabulary budget accommodates any fixed polynomial
in the height.


 # The overhead of summing the rounds 

### `Levels.installed_of_round_budget`

 The total cost allows one estimate per round and two more for the
initial and terminal stages. The vocabulary counts include the terminal
evaluator. All eventual bounds are uniform in the working field. 

 # Charging phase operations to the shared compression budget 

### `Levels.host_budget`

 Keeping at least the prescribed number of blocks pays for long
addresses out of a budget on occurrences. 

### `Levels.phase_expense`

 A phase may use a separate layout for long addresses, for short
records at each occurrence, and for the full exposed payload. 

### `Levels.terminal_expense`

 The terminal evaluator uses the final charge of the live graph and
the exposed bits. Control and wiring costs can also use the phase budget. 

 # Installing a sequence with a uniform per-stage cost 

 # Removing scalar-only entries from presented boards 

### `singleton`

 Presentation of a single board, with a separate initial scalar. 

 # A terminal circuit for a ready layer 


# Uniform termination of a layer

One choice of the three labels serves every summand of the layer.
All hidden assignments are summed inside the same network.

