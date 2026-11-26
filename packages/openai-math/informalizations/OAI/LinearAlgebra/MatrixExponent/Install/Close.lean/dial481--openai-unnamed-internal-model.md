---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Install/Close.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/Close.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/Close.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing a mask into batches

A marked slot's zero-based rank determines both its batch and its
position within the batch. Hence each batch has at most `2^q` slots
and the total capacity of the used batches wastes at most one batch.



# A six-choice graph for sparse routing

Count all functions assigning six neighbors per source, allowing repetitions.
For r sources and 4r candidate destinations the fraction trapped in those
destinations is (4r/n)^(6r). Summing over both sets and then over r leaves
a graph with the required expansion.


### `split_links`

 Split each target into groups of at most 24 links. At most one
partially filled group per old target is charged in addition to the
total number of links divided by 24. 

 # Implementing the peeling rounds by bounded local updates 

### `depends_step`

 Six lists of at most 24 incident links suffice to compute the current
degrees. The previous value of the output and its activity bit are also read. 


# Sparse compaction into a fixed dyadic capacity

The costs of successive halvings sum to a geometric series. In
particular there is no logarithmic factor multiplying the payload.


### `compact`

 Compact the marked records from `2^(h+k)` candidate slots to `2^h` slots. 


# Pooling queries to the same scalar table

Only marked arguments contribute. Compact them into the smaller bank of
table calls and fill unused positions with an argument of weight one.



# Dividing one group of transports into batches

Each marked endpoint identifies the physical slot of its source. Both
endpoints consult the same source slot to determine their batch.



# Dividing a group preserves oriented pairing

Both orientations consult the same identifier. Injectivity of
(identifier, orientation) bounds the selected endpoints by twice the
number of identifiers in the batch.



# A layer of shorter permutation calls

A candidate module lists oriented ends of chunk transports. Its closure
tests that opposite ends have matching identifiers and payloads. Both
the set of modules in use and the set of endpoints within each module
may depend on the selector and the input.


### `Layer.l`

 Height of a shorter call. 

### `Layer.u`

 Width of a shorter call. 

### `Layer.o`

 The installation reserves `2^o` physical modules. 

### `Layer.c`

 Excess log count of candidate modules. 

### `Layer.d`

 Excess log count of candidate endpoints per module. 

### `Layer.r`

 Endpoint width including the orientation bit. 

### `work`

 The cost of handling candidate endpoints and the module masks. 

### `Open`

 The network up to the point where the chunk transports must be wired.
Invalid configurations have coefficient zero before any transports are checked. 

### `OpenProtocol`

 Protocol construction before installing the recursive calls. 


# Installing the transport modules

First compact endpoints inside a candidate module, then compact the
selected modules as whole records. Only physical module slots invoke
the smaller tagged permutation verifier.


### `protocol_of_open`

 Uniformly bounded installed width suffices for the inductive
protocol. Control, switching and padding cost subpolynomial overhead. 


# A fixed partition of the available transport slots

The local circuits supply endpoints in groups. Which slots are used,
their matching, and their payload may depend on the input and selector.
A group needs only a bound on total capacity. The circuit itself finds
the active batches within each group.


### `Plan.g`

 Number of groups, in log scale. 

### `Plan.t`

 Number of batches per group, in log scale. 

### `Plan.q`

 Number of identifiers in a batch, in log scale. 

 # Distributing groups of endpoint pairs among the candidate modules 
