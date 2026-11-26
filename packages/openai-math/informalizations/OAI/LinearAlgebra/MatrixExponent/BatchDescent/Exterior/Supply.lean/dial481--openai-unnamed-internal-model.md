---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Exterior/Supply.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Exterior/Supply.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Exterior/Supply.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matching active rows with multiplicity

An inactive row contributes no condition. Active rows can have
repeated identifiers, so compare the complete records as multisets.


### `RowTap`

 Each row has one activity bit followed by an arbitrary set of
named data bits. Taps may specify constants. 

### `match_rows`

 Two sorts check equality of multisets without any promise that the
active addresses provide a permutation. 


# Canonical allocation to bands

A band has a fixed number of rows for one exterior name. Sort the
active data together with empty rows. The multiset fixes the entire
sorted band, so guessing it adds no multiplicity.


### `Match.all`

 Match transfers any condition on the active records. 

### `bands`

 Padding and monotonicity remove any selector multiplicity. 

 # Canonical Boolean encoding of a band and the adjacent-row check 

### `check_store`

 Verify canonical order and inactive padding by overlapping pairs of
rows. The dictionary needs no name bits. 

 # Soundness of checking an exterior band against its original stacks 

### `flatten`

 Expand active records into their active slots. 

### `compare`

 Input locations are known only through the descriptors on the
active internal rows. No addresses of padding stacks are required. 


# Supplying exterior addresses from ordinary port headers

Only an active exterior row needs its original name. Its stack
addresses live inside its short descriptor, in the same order as
the payloads. A long sort puts all such descriptors in fixed bands.


 # Checking the contents of each exterior band by short sorts 

### `short_sort`

 Each short sort uses only a stack identifier and one stack. It
does not carry a host address or the name of the exterior bit. 


# Exterior supply without a prescribed permutation of the blocks

Use one long sort to identify the assigned bands, a dictionary to
make their ordering and padding unique, and one short sort per
exterior name to compare each complete stack.


### `supply`

 On any valid assignment of row names and local stack addresses,
the test compares exactly the required exterior bits. It receives no
inverse permutation or addresses for empty slots. 
