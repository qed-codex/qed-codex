---
{
  "module": "OAI/Computability/VPVNP/RankQueryGramRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reading a weighted Gram coefficient on the determinant machine

A nonzero Gram descriptor specifies two rows and a shared column. The first
entry read writes directly to the multiplier's query stack and the second to
its accumulator. Both reads see the same persistent Macaulay description.


### `Port`

 Stack addresses for reading one matrix entry, comprising its row and column words, the
packed scalar result and the reader's auxiliary storage. 

### `bank`

 Encode row `i` and column `j` as `w`-bit words alongside the supplied result stack and
auxiliary state of the entry reader. 

### `Correct`

 Calling convention for a single coefficient of the advised relation matrix. 

### `Port`

 Ports for reading two entries in a common column, with separate row words, one column word,
a field multiplier and shared reader storage. 

### `readPorts`

 Route an entry read through the chosen row and common column. The first result goes to the
multiplier's query stack and the second to its accumulator. 

### `machine`

 Read `M i k` and `M j k` from the shared column `k`, then multiply the two packed entries
in the field accumulator. 

### `bank`

 Pack row indices `i` and `j` and their shared column `k` into `w`-bit words alongside the
multiplier stacks and the reader's auxiliary bank. 

### `arithmeticBank`

 Prepare the multiplier with packed modulus coefficients `c` at limb width `v`, the supplied
query and accumulator stacks, and clean internal work stacks. 

### `machine_runs`

 Two physical reads followed by the fixed polynomial-basis multiplier. 
