---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagonal/Replay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Replay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Replay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Substitution in a closed network of processors

Each processor sees its own literals, the same broadcast and its
incident link bits. Pad incomplete batches with a fixed input of weight
one before substituting a diagram that realizes a batch exactly.


### `substitute`

 Replacing each complete batch preserves the scalar for all literal
settings, including literal settings depending on the replacement diagram. 

 # The unit branch in the diagonal computation 

### `branch`

 A broadcast code chooses a report or the extra unit. Unused
codes reject. The unit branch pins all physical links. 

 # Independent restrictions on classes of variables 

### `sum_classes`

 An independent constraint on each class can be tested on the
corresponding restriction of a single global assignment. 


# Evaluation on padded slot assignments

Unoccupied positions are pinned on the station side. On the junction
side equality in the sum over all selectors forces the same padding.



# Independent selector alphabets after fixing the public report

Every assignment occurs with multiplicity one. In particular,
reports for which a class has no possible selector contribute zero.



# Local factors of a reported contraction

Light classes contribute one factor at each home. For a heavy class
the packet worker alone evaluates the entire packet weight. If two
homes coincide their factors are multiplied at the same worker.


### `factor`

 Product of the packet factors assigned to this worker. 

 # Assigning original station weights and padding pins to workers 


# A distributed contraction on the virtual links

For a fixed report all communication is along a fixed graph. The
local factors depend only on their incident symbols and exterior bits.
Any additional filter accepting every honest report preserves the sum.


### `virtual`

 The public information is summed once, including any reports with
impossible histograms. Those reports have no symbol assignments. 


# Additional links for literal pins and exterior values

A reported contraction uses at most half of each worker's virtual
bandwidth. The other half can carry arbitrary additional bits.


 # Every processor sees shared bits at the same tape position 

### `input_local`

 The old literals, broadcasts, and links are visible wherever the same
position is requested, including when the last batch uses padding. 


# Distributing a substituted block

The processor count is fixed before the number of copies in a batch
is known. Extra copies may be fed an accepting constant input.


### `joint`

 The supplied literal at a site is used only there. Other literal
bits are transmitted as part of the virtual assignment. 


# Scalar equality for the physical simulation

The literal strings may depend on the entire replacement graph.
At run time each processor sees only its own string.


### `replay`

 All sums in the simulation are over assignments with multiplicity
one. The width of a physical processor's view is only `N / 4`. 
