---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorSuccessor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorSuccessor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorSuccessor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading both successor fields at a site

The two eight-word fields occupy the first `16*w` incident bits in Lemma 10.1.
On an internal edge the site parses and checks the candidate successor. On a
missing edge it checks the zero clamp. The initial site supplies its own start
state, and the terminal site has no target cut. The same fields supply the
two records used in the predecessor check after sorting.


### `successorField`

 Read the contiguous field at base address `8*w*dir`. 

### `readEdge`

 Computing the base costs two multiplications. Each decoder bit read adds
the base to its within-field offset. In the zero test this addition is already
included in the six operations per iteration (test, decrement, address, load,
branch on bit, loop branch). The four fixed operations cover base setup,
dispatch and return. 

### `SiteSuccessors`

 The parts of the successor fields needed before and after the local sort. 

### `SiteSuccessors.input`

 Incoming cumulative cost and persistent state for the site, using the prescribed initial
  cut at the first site. 

### `SiteSuccessors.output`

 Outgoing successor cut when the site has a following processor in the chain. 

### `SiteSuccessors.received`

 Predecessor's final record recovered from the incoming successor field for the boundary
  check. 

### `SiteSuccessors.sent`

 Final record carried by the site's outgoing successor field and checked against its local
  record sequence. 

### `SiteSuccessors.valid`

 Whether both successor fields pass their decoding checks, including the zero clamp where
  an edge is absent. 

### `scanSuccessors`

 Check both fields even on malformed input. The fixed allowance covers
site endpoint tests, copies of the selected cut and record registers, and
combining the two success flags. 

### `scanSuccessors_cost`

 A uniform bound on raw incident arrays, including nonzero end fields
and unrecognized tags. 

### `SuccessorSendOK`

 The first conjunct of the outgoing encoding check. 

### `SuccessorReceiveOK`

 The first conjunct of the incoming encoding check. 

### `SiteSuccessors.Spec`

 Match both cut registers, both record registers and the validity flag
to the typed site validator on its incident shared-bit assignment. 
