---
{
  "module": "OAI/Computability/VPVNP/MacaulayReadArms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadArms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadArms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native exponent scans in the matrix reader

The source and column ordinals are the third and fourth words returned by the
row decoder. The equation and powered-row scans use separate advised radix
bounds. Each scan preserves the decoded words, returning its flag and exponent
buffer to the selected coefficient routine.


### `Extra`

 Auxiliary ports for the encodings of zero and one, a temporary copy stack and the
coefficient routine's payload. 

### `Leaf`

 Private ports of the matrix reader. Each of its two monomial scans has a pair-call bank
alongside the shared auxiliary ports. 

### `Ports`

 The matrix reader's row, column and result ports together with its decoder, monomial scans
and coefficient payload. 

### `slot`

 Locate a pair-call stack in the private bank for the ordinary scan or the powered-row scan. 

### `extra`

 Locate a shared auxiliary stack of the coefficient routines on the matrix reader's bus. 

### `ordinalField`

 Output-field index for a decoded monomial ordinal. The source uses field 2 and the column
uses field 3. 

### `pairPorts`

 Alias the two ordinal inputs to the decoded words on the physical bus. 

### `storage`

 Storage owned by the matrix reader. Aliased ordinal stacks have no
private copy. The other bank remains intact when a scan updates its buffer. 

### `addressed`

 Fill the pair scan's source and column ordinals from the row decoder's output registers. 

### `scan_bounded`

 Run either physical pair scan in the full reader. Only its own output
buffer and flag change. All other scratch is restored at the call boundary. 
